How quantms compares to other tools
===================================

The following table highlights key differences between quantms and commonly used proteomics tools. This is a high-level, opinionated comparison; each tool evolves quickly, so always consult upstream documentation for the latest details.

.. list-table:: Feature comparison
   :header-rows: 1
   :widths: 26 12 12 12 16 22

   * - Feature
     - quantms
     - MaxQuant
     - DIA-NN
     - FragPipe
     - ProteomeDiscoverer
   * - Workflow type
     - Nextflow pipeline (cloud/on-prem)
     - Desktop/CLI app
     - Desktop/CLI app
     - Orchestrated CLI (Philosopher + tools)
     - Commercial GUI
   * - Acquisition support (DDA/DIA/Isobaric)
     - Yes/Yes/Yes
     - Yes/No/Yes (TMT)
     - No/Yes/Partial (channels via DIA)
     - Yes/Partial/Yes (TMT)
     - Yes/Partial/Yes (TMT)
   * - Multiple search engines
     - Yes (MSGF+, Comet, SAGE)
     - Primarily Andromeda
     - DIA-focused scoring
     - Yes (MSFragger + extras)
     - Yes (via nodes, licensed add-ons)
   * - Rescoring with ML (DeepLC/MS2PIP)
     - Integrated (quantms-rescoring)
     - Limited
     - Built-in DIA rescoring
     - Optional (Percolator/others)
     - Optional (nodes)
   * - Reproducibility (containers)
     - First-class (Docker/Singularity/Podman)
     - Not container-native
     - Not container-native
     - Can be containerized
     - Not container-native
   * - Standard outputs (mzTab/MSstats/Triqler)
     - Yes
     - mzTab (via converters), limited MSstats
     - MSstats ready (DIA)
     - Yes (via export)
     - Via nodes
   * - Scalability (HPC/cloud)
     - Built-in via Nextflow
     - Limited
     - Limited
     - Moderate (parallelizable steps)
     - Limited
   * - License
     - Open source
     - Free for acad., source-available parts
     - Free for acad.
     - Open source (core components)
     - Commercial

.. note:: This comparison focuses on workflow orchestration, reproducibility, and standardized outputs. It does not capture every feature (e.g., PTM localization, library building specifics, GUI convenience).


