## Astrocyte CRISPRi Resource

![pipeline](./docs/Website_Fig.jpg)

Launch [site](https://voineagulabunsw.github.io/astrocyte_crispri_resource/).

This website allows the exploration of CRISPR interference (CRISPRi) data on enhancers in normal human astrocytes (NHAs), from Green et al. 2024.
For each enhancer-gene pair tested in the screen, the following data is available:

- **Statistical significance and effect size (Hit, log2FC, P, FDR)**, displayed in a searchable table and displayed on the corresponding Volcano plot.
    - search the table by gene name or hg38 genome coordinates.
    - to download the filtered data click on the CSV button.
- **ATAC-seq, TT-seq, and Deep-learning-based functional variant annotation**, displayed as a UCSC genome browser track collection.
    - select an enhancer-gene pair in the table OR plot and click the UCSC button to navigate to the enhancer position.
    - select an enhancer-gene pair and click the prediction button to navigate to the enhancer's DeepSEA (beluga) heatmap viewer.

 Code for the heatmap viewer can be found  [here](https://github.com/VoineaguLabUNSW/deepsea_viewer).
