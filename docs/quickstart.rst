Quickstart
==========

.. raw:: html

   <div style="background: linear-gradient(135deg, #059669 0%, #10b981 100%); padding: 25px; border-radius: 10px; color: white; text-align: center; margin: 20px 0;">
      <h2 style="margin: 0; font-size: 22px;">⚡ 5-minute quickstart</h2>
      <p style="margin: 10px 0;">Test quantms with Docker in one command</p>
   </div>

.. raw:: html

   <div style="background: #1f2937; color: #f9fafb; padding: 20px; border-radius: 8px; margin: 20px 0;">
      <div style="display: flex; align-items: center; margin-bottom: 15px;">
         <span style="background: #22c55e; color: white; width: 30px; height: 30px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold; margin-right: 15px;">1</span>
         <span style="font-size: 18px; font-weight: bold;">Install Nextflow (one-time setup)</span>
      </div>
      <div style="background: #374151; padding: 15px; border-radius: 6px; font-family: monospace; font-size: 14px; margin: 10px 0;">
         curl -s https://get.nextflow.io | bash<br>
         mv nextflow ~/.local/bin/
      </div>
   </div>

.. raw:: html

   <div style="background: #1f2937; color: #f9fafb; padding: 20px; border-radius: 8px; margin: 20px 0;">
      <div style="display: flex; align-items: center; margin-bottom: 15px;">
         <span style="background: #3b82f6; color: white; width: 30px; height: 30px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold; margin-right: 15px;">2</span>
         <span style="font-size: 18px; font-weight: bold;">Run the test</span>
      </div>
      <div style="background: #374151; padding: 15px; border-radius: 6px; font-family: monospace; font-size: 14px; margin: 10px 0;">
         nextflow run bigbio/quantms -r 1.6.0 -profile test_lfq,docker
      </div>
      <div style="background: #065f46; padding: 10px; border-radius: 4px; margin-top: 10px;">
         <strong>✅ Success:</strong> You should see "Pipeline completed successfully!" after 5-10 minutes
      </div>
   </div>

.. note::
   **Prerequisites**: Make sure you have Java 11+ and Docker installed.

What just happened?
-------------------

.. raw:: html

   <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 15px; margin: 20px 0;">
      
      <div style="background: #f0f9ff; padding: 15px; border-radius: 6px; border-left: 3px solid #3b82f6;">
         <strong style="color: #3b82f6;">📥 Downloaded</strong><br>
         <small>Test mzML files and FASTA database</small>
      </div>
      
      <div style="background: #f0fdf4; padding: 15px; border-radius: 6px; border-left: 3px solid #22c55e;">
         <strong style="color: #22c55e;">🔍 Processed</strong><br>
         <small>Peptide identification and quantification</small>
      </div>
      
      <div style="background: #fef3c7; padding: 15px; border-radius: 6px; border-left: 3px solid #f59e0b;">
         <strong style="color: #f59e0b;">📊 Generated</strong><br>
         <small>Results tables and QC reports</small>
      </div>
   </div>

Key outputs to explore
----------------------

.. raw:: html

   <div style="background: #f8fafc; padding: 20px; border-radius: 8px; margin: 20px 0;">
      <h4 style="margin: 0 0 15px 0; color: #475569;">📂 Check these files in your results directory:</h4>
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 15px;">
         
         <div style="background: white; padding: 15px; border-radius: 6px; border: 1px solid #e2e8f0;">
            <strong style="color: #3b82f6;">📊 Results Tables</strong><br>
            <code style="background: #f1f5f9; padding: 2px 4px; border-radius: 2px;">*_mztab.tsv</code><br>
            <small>Peptide and protein quantification</small><br>
            <a href="quantms_output.html" style="color: #3b82f6;">→ Understanding outputs</a>
         </div>
         
         <div style="background: white; padding: 15px; border-radius: 6px; border: 1px solid #e2e8f0;">
            <strong style="color: #22c55e;">📈 QC Report</strong><br>
            <code style="background: #f1f5f9; padding: 2px 4px; border-radius: 2px;">multiqc_report.html</code><br>
            <small>Quality control metrics</small><br>
            <a href="pmultiqc.html" style="color: #22c55e;">→ QC guide</a>
         </div>
      </div>
   </div>

Try with your data
------------------

.. raw:: html

   <div style="background: #ede9fe; padding: 20px; border-radius: 8px; border-left: 4px solid #8b5cf6; margin: 20px 0;">
      <h4 style="margin: 0 0 10px 0; color: #8b5cf6;">🎯 Ready for your own data?</h4>
      <p style="margin: 0 0 15px 0;">Replace the test files with your own:</p>
      <div style="background: #1f2937; color: #f9fafb; padding: 15px; border-radius: 6px; font-family: monospace; font-size: 12px; margin: 10px 0;">
         nextflow run bigbio/quantms -r 1.6.0 \<br>
         &nbsp;&nbsp;--input YOUR_EXPERIMENT.sdrf.tsv \<br>
         &nbsp;&nbsp;--database YOUR_PROTEOME.fasta \<br>
         &nbsp;&nbsp;-profile docker
      </div>
      <a href="getting_started.html" style="color: #8b5cf6; text-decoration: none; font-weight: bold;">→ Full setup guide</a>
   </div>

Next steps
----------

.. raw:: html

   <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 15px; margin: 20px 0;">
      
      <div style="background: #f0f9ff; padding: 15px; border-radius: 6px; text-align: center; border: 2px solid #3b82f6;">
         <div style="font-size: 24px; margin-bottom: 10px;">📖</div>
         <strong style="color: #3b82f6;">Learn the Basics</strong><br>
         <a href="getting_started.html" style="color: #3b82f6;">Getting Started</a>
      </div>
      
      <div style="background: #f0fdf4; padding: 15px; border-radius: 6px; text-align: center; border: 2px solid #22c55e;">
         <div style="font-size: 24px; margin-bottom: 10px;">🎯</div>
         <strong style="color: #22c55e;">Follow Tutorials</strong><br>
         <a href="tutorials.html" style="color: #22c55e;">Step-by-step guides</a>
      </div>
      
      <div style="background: #fef3c7; padding: 15px; border-radius: 6px; text-align: center; border: 2px solid #f59e0b;">
         <div style="font-size: 24px; margin-bottom: 10px;">⚙️</div>
         <strong style="color: #f59e0b;">Configure</strong><br>
         <a href="parameters.html" style="color: #f59e0b;">Parameter Reference</a>
      </div>
      
      <div style="background: #fdf2f8; padding: 15px; border-radius: 6px; text-align: center; border: 2px solid #ec4899;">
         <div style="font-size: 24px; margin-bottom: 10px;">🔬</div>
         <strong style="color: #ec4899;">Choose Analysis</strong><br>
         <a href="dda.html" style="color: #ec4899;">DDA</a> | <a href="dia.html" style="color: #ec4899;">DIA</a> | <a href="iso.html" style="color: #ec4899;">TMT</a>
      </div>
   </div>


