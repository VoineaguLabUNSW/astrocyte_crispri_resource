# Gene Annotation Description

This document describes the columns contained in the [gene annotation table](./Gene_annot_FullTable.csv).

## Gene and Linked Enhancer information		

- **Gene**: Gene tested in the study (n = 3,125).
- **LinkedEnh**: Enhancer identified as significantly regulating the given gene.
- **Hit**: Boolean indicating whether one or more enhancers were identified as having a significant functional regulatory effect on the given gene.

## Functional annotation of all genes tested 
- **AstAgeing_CombinedStudies to AstActivation_Leng2022_ProtocolTCW**:  
  For each resource, **-1** and **+1** encode significant down- and up-regulation, respectively, while **0** represents non-significance or no data. For markers and housekeeping genes (binary calls without a sign), **+1** represents presence in the resource.  
  Descriptions of the resources, including criteria for significance, are included in the Methods. Categories of resources include:  
  - **Ageing**: Aged versus developmentally mature adult astrocytes.
  - **Maturation**: Foetal and early development versus adult mature astrocytes.
  - **Astrocyte markers**: Increased expression in astrocytes versus other brain cell types.
  - **Housekeeping**: Standard genes used as internal controls.
  - **Astrocyte activation**: Induced by IL-1α + TNF + C1q in vitro.  
  Resources labeled with "CombinedStudies" sum the values for all resources within the same category (note that "AstMarkers_Subtypes_Sadick2022" is not included in the combined astrocyte marker annotation).

## Astrocyte-specific DE of enhancer-regulated genes in various disease phenotypes		

- **AD_Morabito2021 to Peritumour_Krawczyk2022**:  
  Astrocyte-specific differential expression of enhancer-regulated genes in various disease phenotypes. Linked enhancers are only shown for hit genes. For each resource, **-1** and **+1** encode significant down- and up-regulation, respectively, while **0** represents non-significance or no data.  
  Descriptions of resources and criteria for significance are included in the Methods. Abbreviations include:  
  - **AD**: Alzheimer's disease  
  - **ASD**: Autism spectrum disorder  
  - **MS**: Multiple sclerosis  
  - **GBM**: Glioblastoma

## ROSMAP DE data for enhancer-regulated genes identified in the CRISPRi screen

- **Cluster to Variable: ROSMAP differential expression (DE) data for enhancer-regulated genes identified in the CRISPRi screen. Data from Mathys, H. et al. Cell 186, 4365–4385.e27 (2023).**
  - **Cluster**: The cell type cluster used for DE analysis.
  - **Variable**: The variable used for DE analysis.
