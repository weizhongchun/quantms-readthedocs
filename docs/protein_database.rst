Creating the protein database (DDA and DIA)
===========================================

This page explains how to prepare the protein sequence database used by quantms for both DDA and DIA analyses, how to include contaminants, how to add decoys (inside the workflow and externally), and how to use entrapment proteins for additional FDR assessment.

Download proteomes from UniProt
--------------------------------

- We recommend downloading a reference proteome FASTA from `UniProt <https://www.uniprot.org/>`__ (Proteomes section).
- Include isoforms if appropriate for your study; otherwise use canonical-only.
- Make sure to include common contaminants (see below) and remove stop codons `*` if present.

Contaminants
------------

- Include a contaminants FASTA (e.g., common laboratory proteins). Prefix contaminant accessions with ``CONTAM_`` to simplify downstream filtering.
- You can append contaminants to your organism FASTA to create a combined database. quantms will pass the combined FASTA to the search engines.

Curated contaminants FASTA (recommended)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- We provide a curated contaminants database with the ``CONTAM`` prefix that works out-of-the-box with pMultiQC, iBAQpy, DIA-NN and related tools.
- Download the file from `quantms-test-datasets (contaminants-202105-uniprot-description.fasta) <https://github.com/bigbio/quantms-test-datasets/blob/quantms/databases/contaminants-202105-uniprot-description.fasta>`__ and append it to your target UniProt FASTA.
- Example concatenation:

  .. code-block:: bash

     cat uniprot_proteome.fasta contaminants-202105-uniprot-description.fasta > proteome_with_contaminants.fasta

.. note:: For DIA (DIA-NN) pipelines, contaminants with UniProt descriptions (containing gene names) are recommended so that DIA-NN can form gene groups correctly. See repository listing: `quantms-test-datasets/databases <https://github.com/bigbio/quantms-test-datasets/tree/quantms/databases>`__.

Decoys inside the workflow
--------------------------

- For DDA analyses, quantms can generate and append decoys to the given protein FASTA automatically.
  - Enable with ``--add_decoys``; adjust marker and method with ``--decoy_string``, ``--decoy_string_position``, and ``--decoy_method`` (reverse/shuffle). See `Database search parameters <parameters.html#protein-database>`_.
- For DIA analyses with DIA-NN, decoys are not required in the input FASTA because DIA-NN handles decoy generation internally. The workflow will skip decoy creation for DIA.

Generating decoys outside the workflow (py-pgatk)
-------------------------------------------------

You can also generate decoys beforehand using the `py-pgatk <https://github.com/bigbio/py-pgatk>`__ toolkit. It supports multiple strategies including DecoyPYrat.

Example (conceptual) workflow using py-pgatk:

.. code-block:: bash

   # Install pypgatk (choose one)
   pip install pypgatk
   # or: conda install pypgatk

   # Generate a decoy-augmented database using DecoyPYrat strategy
   pypgatk_cli generate-decoy \
     --input proteome_with_contaminants.fasta \
     --method decoypyrat \
     --output proteome_with_contaminants_and_decoys.fasta

See the command implementation and options in the repository: Decoy generation command (``proteindb_decoy.py``) `link <https://github.com/bigbio/py-pgatk/blob/master/pypgatk/commands/proteindb_decoy.py>`__ and project homepage `link <https://github.com/bigbio/py-pgatk>`__.

Entrapment proteins for additional FDR assessment
-------------------------------------------------

Beyond target-decoy, an additional strategy is to include entrapment proteins (from a species or simulated species not present in the sample) to empirically assess false positives and refine DIA results.

- Concatenate a set of entrapment protein sequences (e.g., from an unrelated organism) to your target database. Keep them distinguishable (e.g., prefix ``ENTRAPMENT_``).
- For DIA analyses (e.g., DIA-NN 1.8.*), entrapment can help evaluate FDR control, especially in multi-dataset integration scenarios.
- See the assessment with entrapment in Nature Methods (2025) and the FDRBench resources:
  - Nature Methods article: `Assessment of false discovery rate control using entrapment <https://www.nature.com/articles/s41592-025-02719-x>`__
  - FDRBench repository: `Noble-Lab/FDRBench <https://github.com/Noble-Lab/FDRBench>`__

FDRBench-based decoy and entrapment generation
----------------------------------------------

For comprehensive decoy and entrapment construction you can use `FDRBench <https://github.com/Noble-Lab/FDRBench>`__ to create augmented FASTA files:

- DDA database generation (adds two decoys and one entrapment per target):

  .. code-block:: bash

     java -jar fdrbench-0.0.2/fdrbench-0.0.2.jar \
       -level protein \
       -db {database_name}.fasta \
       -o {database_name_output}.fasta \
       -I2L -fix_nc c -check \
       -decoy -decoy_label DECOY_ -decoy_pos 0 \
       -entrapment_label ENTRAP_ -entrapment_pos 0

  This produces entries prefixed with ``DECOY_`` and ``ENTRAP_`` alongside each target.

- DIA database generation (entrainment only; decoys handled by DIA-NN):

  .. code-block:: bash

     java -jar fdrbench-0.0.2/fdrbench-0.0.2.jar \
       -level protein \
       -db {database_name}.fasta \
       -o {database_name_output}.fasta \
       -I2L -diann -uniprot -fix_nc c -check \
       -entrapment_label ENTRAP_ -entrapment_pos 0

Post-processing tip: ensure all headers clearly encode the role in the accession itself (e.g., ``DECOY_``, ``ENTRAP_``, ``CONTAM_``). If needed, run a small header-fixing script to standardize names across tools before use.

Standardizing headers after FDRBench
------------------------------------

After generating augmented FASTA files with FDRBench, standardize headers so that the role is encoded both in the accession and the protein name. Use the helper script referenced in the datasets repository:

.. code-block:: bash

   python fdrbench_accessions.py

This enforces prefixes like ``DECOY_``, ``ENTRAP_`` and ``CONTAM_`` consistently, improving downstream filtering and reporting. See the README for context: `quantms-test-datasets/databases/README.md <https://github.com/bigbio/quantms-test-datasets/blob/quantms/databases/README.md>`__.

Recommended final FASTA naming
------------------------------

Adopt a descriptive name including organism, source, and build date, for example:

``Homo-sapiens-uniprot-reviewed-contam-entrap-decoy-20241105.fasta``

Tips and best practices
-----------------------

- Keep decoys and contaminants clearly labeled (prefixes) for easy filtering and reporting.
- For DIA, avoid decoys in FASTA input; let DIA-NN create decoys internally. If desired, include entrapment proteins with an ``ENTRAP_`` prefix to monitor empirical FDR in integrative analyses.
- For reproducibility, store the exact FASTA (with contaminants/decoys/entrapment) alongside results.


