pMultiQC
========

.. raw:: html

   <div style="background: linear-gradient(135deg, #10b981 0%, #059669 100%); padding: 25px; border-radius: 10px; color: white; text-align: center; margin: 20px 0;">
      <h2 style="margin: 0; font-size: 22px;">📊 pMultiQC: Comprehensive Proteomics QC</h2>
      <p style="margin: 10px 0;">Advanced quality control reporting for mass spectrometry-based proteomics</p>
   </div>

`pMultiQC <https://github.com/bigbio/pmultiqc/>`_ is a comprehensive python library for quality control (QC) of proteomics data, built as a `MultiQC <https://multiqc.info>`_ plugin. It provides interactive HTML reports with sophisticated visualizations for evaluating the quality of mass spectrometry-based proteomics experiments across multiple analysis workflows.

.. raw:: html

   <div style="background: #f0fdf4; padding: 20px; border-radius: 8px; border-left: 4px solid #10b981; margin: 20px 0;">
      <h4 style="margin: 0 0 15px 0; color: #10b981;">🌐 Try pMultiQC Online</h4>
      <p style="margin: 0 0 10px 0;">Experience pMultiQC without installation using the official EBI PRIDE service:</p>
      <a href="https://www.ebi.ac.uk/pride/services/pmultiqc/" style="color: #10b981; text-decoration: none; font-weight: bold;">→ https://www.ebi.ac.uk/pride/services/pmultiqc/</a>
   </div>

Key Features and Capabilities
-----------------------------

pMultiQC supports **four major proteomics analysis workflows** with comprehensive QC reporting:

- **quantms pipeline**: Complete integration with identification, quantification, and statistical analysis
- **MaxQuant**: Standard label-free and TMT proteomics workflows  
- **DIA-NN**: Data-independent acquisition analysis with library-free approaches
- **mzIdentML**: PRIDE Complete submissions supporting multiple search engines
- **ProteoBench**: Benchmarking results for standardized performance evaluation

The tool generates **metadata-aware reports** using SDRF-driven experimental design information, enabling sophisticated quality assessment strategies with actionable insights for experimental optimization.

Core Processing Framework
-------------------------

The pMultiQC processing framework consists of three main stages optimized for memory efficiency and scalability:

.. raw:: html

   <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; margin: 20px 0;">
      
      <div style="background: #dbeafe; padding: 20px; border-radius: 8px; text-align: center;">
         <div style="background: #3b82f6; color: white; width: 40px; height: 40px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 15px auto; font-weight: bold; font-size: 18px;">1</div>
         <h4 style="margin: 0 0 10px 0; color: #3b82f6;">Data Detection & Parsing</h4>
         <p style="margin: 0; font-size: 14px;">Automatic file type identification and format-specific parsing with memory-efficient processing</p>
      </div>
      
      <div style="background: #dcfce7; padding: 20px; border-radius: 8px; text-align: center;">
         <div style="background: #22c55e; color: white; width: 40px; height: 40px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 15px auto; font-weight: bold; font-size: 18px;">2</div>
         <h4 style="margin: 0 0 10px 0; color: #22c55e;">Data Integration & QC</h4>
         <p style="margin: 0; font-size: 14px;">Comprehensive QC metric computation and standardization for MultiQC visualization</p>
      </div>
      
      <div style="background: #fef3c7; padding: 20px; border-radius: 8px; text-align: center;">
         <div style="background: #f59e0b; color: white; width: 40px; height: 40px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 15px auto; font-weight: bold; font-size: 18px;">3</div>
         <h4 style="margin: 0 0 10px 0; color: #f59e0b;">HTML Report Generation</h4>
         <p style="margin: 0; font-size: 14px;">Self-contained interactive reports with embedded JavaScript for dynamic exploration</p>
      </div>
   </div>

Example Reports and Performance
-------------------------------

Experience pMultiQC capabilities through live example reports showcasing different workflows:

.. raw:: html

   <div style="background: #f8fafc; padding: 20px; border-radius: 8px; margin: 20px 0;">
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 15px;">
         
         <div style="background: white; padding: 15px; border-radius: 6px; border: 1px solid #e2e8f0;">
            <h5 style="margin: 0 0 8px 0; color: #3b82f6;">📊 quantms LFQ</h5>
            <p style="margin: 0 0 10px 0; font-size: 13px; color: #64748b;">PXD007683 | Time: 989s | Memory: 2.8GB</p>
            <a href="https://pmultiqc.quantms.org/LFQ_PXD007683/multiqc_report.html" style="color: #3b82f6; text-decoration: none; font-weight: bold;">→ View LFQ Report</a>
         </div>
         
         <div style="background: white; padding: 15px; border-radius: 6px; border: 1px solid #e2e8f0;">
            <h5 style="margin: 0 0 8px 0; color: #22c55e;">🏷️ quantms TMT</h5>
            <p style="margin: 0 0 10px 0; font-size: 13px; color: #64748b;">PXD007683 | Time: 779s | Memory: 5.8GB</p>
            <a href="https://pmultiqc.quantms.org/TMT_PXD007683/multiqc_report.html" style="color: #22c55e; text-decoration: none; font-weight: bold;">→ View TMT Report</a>
         </div>
         
         <div style="background: white; padding: 15px; border-radius: 6px; border: 1px solid #e2e8f0;">
            <h5 style="margin: 0 0 8px 0; color: #f59e0b;">📈 DIA-NN Results</h5>
            <p style="margin: 0 0 10px 0; font-size: 13px; color: #64748b;">PXD063291 | Time: 49s | Memory: 891MB</p>
            <a href="https://pmultiqc.quantms.org/DIANN/multiqc_report.html" style="color: #f59e0b; text-decoration: none; font-weight: bold;">→ View DIA-NN Report</a>
         </div>
         
         <div style="background: white; padding: 15px; border-radius: 6px; border: 1px solid #e2e8f0;">
            <h5 style="margin: 0 0 8px 0; color: #8b5cf6;">🔬 MaxQuant Results</h5>
            <p style="margin: 0 0 10px 0; font-size: 13px; color: #64748b;">PXD003133 | Time: 15s | Memory: 718MB</p>
            <a href="https://pmultiqc.quantms.org/PXD003133/multiqc_report.html" style="color: #8b5cf6; text-decoration: none; font-weight: bold;">→ View MaxQuant Report</a>
         </div>
         
         <div style="background: white; padding: 15px; border-radius: 6px; border: 1px solid #e2e8f0;">
            <h5 style="margin: 0 0 8px 0; color: #ec4899;">📋 mzIdentML + mzML</h5>
            <p style="margin: 0 0 10px 0; font-size: 13px; color: #64748b;">PXD051187 | Time: 362s | Memory: 2.5GB</p>
            <a href="https://pmultiqc.quantms.org/PXD051187/multiqc_report.html" style="color: #ec4899; text-decoration: none; font-weight: bold;">→ View mzIdentML Report</a>
         </div>
         
         <div style="background: white; padding: 15px; border-radius: 6px; border: 1px solid #e2e8f0;">
            <h5 style="margin: 0 0 8px 0; color: #059669;">🏆 ProteoBench</h5>
            <p style="margin: 0 0 10px 0; font-size: 13px; color: #64748b;">Benchmarking evaluation results</p>
            <a href="https://pmultiqc.quantms.org/ProteoBench/multiqc_report.html" style="color: #059669; text-decoration: none; font-weight: bold;">→ View ProteoBench Report</a>
         </div>
      </div>
   </div>

Advanced Features
-----------------

.. raw:: html

   <div style="background: #ecfdf5; padding: 20px; border-radius: 8px; border-left: 4px solid #10b981; margin: 20px 0;">
      <h4 style="margin: 0 0 15px 0; color: #10b981;">🌐 PRIDE Integration</h4>
      <p style="margin: 0 0 10px 0;">Access and analyze PRIDE datasets directly using ProteomeXchange accession numbers. Perfect for evaluating public datasets before download or reuse.</p>
      <code style="background: #1e293b; color: #f1f5f9; padding: 8px 12px; border-radius: 4px;">https://www.ebi.ac.uk/pride/services/pmultiqc/submit?accession=PXD003133</code>
   </div>

.. raw:: html

   <div style="background: #ede9fe; padding: 20px; border-radius: 8px; border-left: 4px solid #8b5cf6; margin: 20px 0;">
      <h4 style="margin: 0 0 15px 0; color: #8b5cf6;">🔧 ProteoBench Integration</h4>
      <p style="margin: 0 0 10px 0;">Integrated support for ProteoBench benchmarking results enables standardized performance evaluation across different tools and configurations.</p>
      <code style="background: #1e293b; color: #f1f5f9; padding: 8px 12px; border-radius: 4px;">multiqc --parse_proteobench /path/to/proteobench/files -o ./report</code>
   </div>

Installation and Usage
----------------------

.. raw:: html

   <div style="background: #1e293b; color: #f1f5f9; padding: 20px; border-radius: 8px; margin: 20px 0;">
      <h4 style="margin: 0 0 15px 0;">📦 Quick Installation & Usage</h4>
      <div style="background: #374151; padding: 15px; border-radius: 6px; font-family: monospace; margin: 10px 0; font-size: 13px;">
         # Install from PyPI<br>
         pip install pmultiqc<br><br>
         # quantms results<br>
         multiqc /path/to/quantms/results -o ./report<br><br>
         # MaxQuant results<br>
         multiqc --parse_maxquant /path/to/maxquant/results -o ./report<br><br>
         # DIA-NN results<br>
         multiqc /path/to/diann/results -o ./report<br><br>
         # ProteoBench results<br>
         multiqc --parse_proteobench /path/to/proteobench/files -o ./report
      </div>
   </div>

Report Sections and QC Metrics
-------------------------------

pMultiQC organizes comprehensive QC metrics into **nine main sections** addressing different aspects of mass spectrometry data analysis:

Acquisition performance heatmap
----------------------------------

The Acquisition performance heatmap allows users to compare the performance of different metrics for the different MS runs in the dataset. Each row of the heatmap correspond to a MS run while a column is a QC metric:

.. image:: images/pmultiqc-heatmap.png
   :width: 600
   :align: center

- **Contaminants**: It measures the number of contaminants proteins quantified.
- **Peptide Intensity**: Measures the total peptide intensity of the quantified peptides. Low peptide intensity usually goes hand in hand with low MS/MS identification rates and unfavourable signal/noise ratios, which makes signal detection harder. Also instrument acquisition time increases for trapping instruments.
- **Charge**: Measures the distribution of the charge states of all quantified peptides.
- **Missed cleavages**: This metrics capture the number of missed cleavages in the identified peptides.
- **ID rate over RT**: Judge column occupancy over retention time. Ideally, the LC gradient is chosen such that the number of identifications (here, after FDR filtering) is uniform over time, to ensure consistent instrument duty cycles. Sharp peaks and uneven distribution of identifications over time indicate potential for LC gradient optimization [MORUZ2014]_ .
- **MS2 oversampling**: An oversampled 3D-peak is defined as a peak whose peptide ion (same sequence and same charge state) was identified by at least two distinct MS2 spectra in the same Raw file. For high complexity samples, oversampling of individual 3D-peaks automatically leads to under sampling or even omission of other 3D-peaks, reducing the number of identified peptides. Oversampling occurs in low-complexity samples or long LC gradients, as well as undersized dynamic exclusion windows for data independent acquisitions.
- **Missing values**: Missing peptide intensities per MS run. This metric shows the fraction of missing peptides compared to all peptides seen in the whole experiment. The more Raw files you have, the higher this fraction is going to be If all Raw files are (technical) replicates, i.e. we can expect that missing peptides are indeed present and have an intensity similar to the peptides we do see, then the median is a good estimator. Peptides obtained via **Match-between-run (MBR)** are accounted for (i.e. are considered as present = non-missing).

Experimental design
--------------------------
The experimental design table shows the design of the proteomics experiments including: the name of the spectra file, fraction group, fraction, label, Sample accession, MSstats condition (condition), MSstats_Bioreplicate.

.. image:: images/pmultiqc-ed.png
   :width: 800
   :align: center

Summary Tables
---------------------------

The Summary Table and Pipeline Results Statistics describe the identification results of the analysis. The Summary Table summarize the total of MS/MS spectra, the number of identified MS/MS, the ratio of identified MS/MS, total number of proteins and peptides identified. The Pipeline Results Statistics represents the identification results by Ms runs including number of peptides, number of modified peptides and total number of identified proteins.

.. image:: images/pmultiqc-summary-table.png
   :width: 800
   :align: center

The MS1 subsection displays the total ion chromatograms curve, base peak chromatograms curve, distribution of peaks and general stats.

.. image:: images/pmultiqc-ms1-tic.png
   :width: 800
   :align: center

.. image:: images/pmultiqc-ms1-general_stats.png
   :width: 800
   :align: center

In addition, the **Spectra-Tracking** table reports the number of identified peptides and proteins by search engines comet (:doc:`comet`) or msgf (:doc:`msgf`).

.. image:: images/pmultiqc-track.png
   :width: 800
   :align: center

Number of peptides per protein
---------------------------------

The Number of peptides per protein, displays the distribution of peptides per protein in the experiment. Proteins supported by more peptide identifications can constitute more confident results.

.. image:: images/pmultiqc-pep-prot.png
   :width: 800
   :align: center

Summary of search engines scores
---------------------------------

These plots contain search scores and PEPs counts for different search engines in different files, and they also contain a summary of the consensus PSMs if two or more search engines are used.

.. image:: images/pmultiqc-search_scores_summary.png
   :width: 800
   :align: center

.. image:: images/pmultiqc-consensus_summary.png
   :width: 800
   :align: center

Distribution of precursor charges
---------------------------------

This is a plot representing the distribution of the precursor ion charges for a given experiment. This information can be used to identify potential ionization problems including many 1+ charges from an ESI ionization source or an unexpected distribution of charges. An unexpected charge distribution may furthermore be caused by specific search engine parameter settings such as limiting the search to specific ion charges.

.. image:: images/pmultiqc-charges.png
   :width: 800
   :align: center

Peaks Intensity Distribution
-----------------------------

This is a plot representing the ion intensity vs. the frequency for all MS2 spectra in a whole given experiment. It shows the information for identified and unidentified spectra. This plot can give a general estimation of the noise level of the spectra. Generally, one should expect to have a high number of low intensity noise peaks with a low number of high intensity signal peaks. A disproportionate number of high signal peaks may indicate heavy spectrum pre-filtering or potential experimental problems.

.. image:: images/pmultiqc-peaks.png
   :width: 800
   :align: center

Delta Mass distribution
-----------------------

This chart represents the distribution of the relative frequency of experimental precursor ion mass (m/z) - theoretical precursor ion mass (m/z).

.. image:: images/pmultiqc-delta.png
   :width: 800
   :align: center

Results exploration
-----------------------

pmultiqc uses two tables **Quantification Result** and **Peptide-Spectrum Matches** to enable the users to browse over quantified peptides and reported PSMs in the mzTab (:doc:`formats`).

.. image:: images/pmultiqc-qr.png
   :width: 800
   :align: center

.. tip:: Both tables allows the users to sort the results by columns and also **search** for the peptides of interest.

.. image:: images/pmultiqc-psms.png
   :width: 800
   :align: center

References
--------------------------

.. [MORUZ2014] Moruz L, Käll L. GradientOptimizer: an open-source graphical environment for calculating optimized gradients in reversed-phase liquid chromatography. Proteomics. 2014 Jun;14(12):1464-6. doi: 10.1002/pmic.201400036. Epub 2014 May 15. PMID: 24700534.
