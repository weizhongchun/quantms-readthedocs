import requests

OUTPUT_URL = (
    "https://github.com/bigbio/quantms/raw/refs/heads/README_links/docs/output.md"
)


def download_file(url, save_path):
    """
    Download a file from a URL and save it to the specified path.

    Args:
        url (str): URL of the file to download
        save_path (str): Path where the downloaded file will be saved

    Returns:
        bool: True if download was successful, False otherwise
    """

    # Send GET request
    response = requests.get(url, stream=True)
    response.raise_for_status()  # Raise exception for HTTP errors

    # Write content to file
    with open(save_path, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)

    print(f"Successfully downloaded: {url} to {save_path}")
    return True


def download_output(output_path="quantms_output.md"):
    """
    Download the output file from the specified URL and save it locally to use
    for Sphinx documentation purposes.
    """
    # new folders would need to be created if necessary

    if download_file(OUTPUT_URL, output_path):
        print(f"Output file saved to {output_path}")
    else:
        print(f"Failed to download the output format files from: {OUTPUT_URL}")
        
    with open(output_path, "r") as f:
        content = f.readlines()
    
    content[0] = '# quantms outputs\n'
    
    with open(output_path, "w") as f:
        f.writelines(content)


if __name__ == "__main__":
    download_output()

