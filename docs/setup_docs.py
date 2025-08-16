import requests

OUTPUT_URL = (
    "https://raw.githubusercontent.com/bigbio/quantms/HEAD/docs/output.md"
)
SCHEMA_URL = (
    "https://raw.githubusercontent.com/bigbio/quantms/HEAD/nextflow_schema.json"
)


def download_file(url, save_path, timeout=20):
    """
    Download a file from a URL and save it to the specified path.

    Args:
        url (str): URL of the file to download
        save_path (str): Path where the downloaded file will be saved
        timeout (int): Timeout for the download request in seconds

    Returns:
        bool: True if download was successful, False otherwise
    """

    # Send GET request
    response = requests.get(url, stream=True, timeout=timeout)
    response.raise_for_status()  # Raise exception for HTTP errors

    # Write content to file
    with open(save_path, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)

    print(f"Successfully downloaded: {url} to {save_path}")
    return True


def _md_to_rst(md_text: str) -> str:
    """Best-effort Markdown (GitHub) to simple reStructuredText conversion for Sphinx.

    This handles basic headings, links, code blocks, and a few internal anchors used in quantms_output.md.
    It is not a general-purpose converter but good enough for our generated page.
    """
    import re

    lines = md_text.splitlines()
    rst_lines = []
    in_code = False
    code_buffer = []

    def flush_code():
        nonlocal code_buffer
        if code_buffer:
            rst_lines.append(".. code-block:: text")
            rst_lines.append("")
            rst_lines.extend(["    " + l for l in code_buffer])
            rst_lines.append("")
            code_buffer = []

    for line in lines:
        # code fences
        if line.strip().startswith("```"):
            if not in_code:
                in_code = True
                continue
            else:
                in_code = False
                flush_code()
                continue
        if in_code:
            code_buffer.append(line)
            continue

        # convert headings ###, ##, # to rst
        m = re.match(r"^(#{1,6})\s+(.*)$", line)
        if m:
            level = len(m.group(1))
            title = m.group(2).strip()
            rst_lines.append(title)
            underline = "=" if level == 1 else ("-" if level in (2, 3) else "~")
            rst_lines.append(underline * len(title))
            rst_lines.append("")
            continue

        # Convert [text](#anchor) → plain text (avoid :ref: when no titled target exists)
        line = re.sub(r"\[([^\]]+)\]\(#([^)]+)\)", r"\1", line)

        # Convert external links [text](http...) → anonymous RST link `text <url>`__
        line = re.sub(r"\[([^\]]+)\]\((https?://[^)]+)\)", r"`\1 <\2>`__", line)

        rst_lines.append(line)

    flush_code()
    # Ensure top title
    if rst_lines and not rst_lines[0].strip():
        rst_lines = rst_lines[1:]
    if rst_lines and not any(ch == "=" for ch in rst_lines[1:2]):
        title = "quantms outputs"
        rst_lines = [title, "=" * len(title), ""] + rst_lines
    return "\n".join(rst_lines)


def download_output(output_path="quantms_output.rst"):
    """
    Download the output file from the specified URL and save it locally to use
    for Sphinx documentation purposes.
    """
    # new folders would need to be created if necessary

    # Download the upstream Markdown file to a temporary location
    tmp_md = output_path if output_path.endswith(".md") else "quantms_output.md"
    assert download_file(OUTPUT_URL, tmp_md)  # prints success message

    with open(tmp_md, "r") as f:
        md_text = f.read()
    assert md_text.strip(), "Downloaded file is empty"

    # Convert to reStructuredText
    rst_text = _md_to_rst(md_text)

    # Write to .rst for Sphinx to pick up
    rst_path = output_path if output_path.endswith(".rst") else "quantms_output.rst"
    with open(rst_path, "w") as f:
        f.write(rst_text)

    # Remove temporary md file to avoid duplicate docnames
    try:
        if tmp_md != rst_path:
            import os
            os.remove(tmp_md)
    except OSError:
        pass


def _collect_params(node, prefix=None):
    """Traverse a JSON schema-like tree and collect leaf parameters.

    Returns a list of dicts with keys: path, name, type, default, description, group.
    """
    prefix = prefix or []
    results = []

    # If this node defines nested properties, traverse them
    props = node.get("properties") if isinstance(node, dict) else None
    if isinstance(props, dict):
        for key, child in props.items():
            results.extend(_collect_params(child, prefix + [key]))
        return results

    # Leaf-like node: try to read attributes
    if isinstance(node, dict):
        name = ".".join(prefix) if prefix else ""
        ptype = node.get("type")
        default = node.get("default")
        desc = node.get("description") or ""
        # Determine top-level group as first segment
        group = prefix[0] if prefix else "general"

        # Heuristic: accept as parameter only if we have a name and some metadata
        if name and (ptype or desc or default is not None):
            results.append(
                {
                    "path": name,
                    "name": name,
                    "type": ptype if isinstance(ptype, str) else None,
                    "default": default,
                    "description": desc.strip(),
                    "group": group,
                }
            )
    return results


def _schema_to_rst(schema_obj):
    """Render a simple, grouped list-table RST from an nf-core nextflow_schema.json."""
    import re
    lines = []
    lines.append("Parameters")
    lines.append("===========")
    lines.append("")
    lines.append("This page lists pipeline parameters extracted from the Nextflow schema.")
    lines.append("")

    # Collect all params from top-level properties or definitions
    root_candidates = []
    if isinstance(schema_obj, dict):
        if "properties" in schema_obj:
            root_candidates.append(schema_obj)
        # Some schemas embed under definitions → iterate all dicts looking for properties
        defs = schema_obj.get("definitions") or schema_obj.get("$defs")
        if isinstance(defs, dict):
            for d in defs.values():
                if isinstance(d, dict) and "properties" in d:
                    root_candidates.append(d)

    params = []
    for root in root_candidates or [schema_obj]:
        params.extend(_collect_params(root))

    if not params:
        lines.append(".. note:: No parameters found in the schema or schema unavailable.")
        return "\n".join(lines)

    # Group by top-level key
    from collections import defaultdict

    group_to_params = defaultdict(list)
    for p in params:
        group_to_params[p["group"]].append(p)

    # Stable ordering: general first, then alphabetical
    groups = sorted(group_to_params.keys())
    if "general" in groups:
        groups.remove("general")
        groups = ["general"] + groups

    for group in groups:
        section_title = f"{group}"
        lines.append(section_title)
        lines.append("-" * len(section_title))
        lines.append("")
        lines.append(".. list-table::")
        lines.append("   :header-rows: 1")
        lines.append("   :widths: 28 12 20 40")
        lines.append("")
        lines.append("   * - Name")
        lines.append("     - Type")
        lines.append("     - Default")
        lines.append("     - Description")

        for p in sorted(group_to_params[group], key=lambda x: x["name"]):
            ptype = p.get("type") or ""
            default = p.get("default")
            if isinstance(default, bool):
                default_str = "true" if default else "false"
            elif default is None:
                default_str = ""
            else:
                default_str = str(default)
                # Wrap string defaults to avoid interpreted text like 'DECOY_' being seen as a reference
                if isinstance(default, str):
                    default_str = f"``{default_str}``"

            desc = p.get("description") or ""
            # Sanitize markdown / anchors inside schema help_text
            desc = re.sub(r"\[[^\]]+\]\((?:#|https?://)[^)]+\)", lambda m: re.sub(r"^\[|\]\(.*\)$", "", m.group(0)), desc)
            desc = re.sub(r"\(#([^)]+)\)", "", desc)  # strip raw (#anchor)
            # Escape newlines in desc for list-table row
            desc = " ".join(desc.splitlines()).strip()

            lines.append(f"   * - ``{p['name']}``")
            lines.append(f"     - {ptype}")
            lines.append(f"     - {default_str}")
            lines.append(f"     - {desc}")
        lines.append("")

    return "\n".join(lines)


def generate_parameters(parameters_path="parameters.rst"):
    """Download nextflow_schema.json and render parameters.rst."""
    import json
    try:
        # Download schema
        schema_tmp = "nextflow_schema.json"
        downloaded = download_file(SCHEMA_URL, schema_tmp)
        if not downloaded:
            raise RuntimeError("Schema download failed")
        with open(schema_tmp, "r") as f:
            schema_obj = json.load(f)
    except Exception as exc:
        print(f"Warning: could not obtain or parse schema: {exc}")
        raise RuntimeError("Failed to obtain or parse schema, cannot generate parameters.rst")

    rst = _schema_to_rst(schema_obj)
    with open(parameters_path, "w") as f:
        f.write(rst)
    print(f"Wrote parameters to {parameters_path}")


if __name__ == "__main__":
    download_output()
    generate_parameters()
