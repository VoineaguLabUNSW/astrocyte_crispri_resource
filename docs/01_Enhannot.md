# Enhancer Annotation Description

This document describes the columns contained in the [enhancer annotation table](./Enh_annot_FullTable.csv).

## Enhancer id

- **Enh**: Enhancer identifier.
- **ExpressedGene_500kb**: Boolean indicating whether at least one expressed gene is located within 500 kb of the enhancer midpoint.
- **Coord**: Genomic coordinates of the candidate enhancer (chromosome:start-end).
- **Tested**: Boolean indicating whether the enhancer was tested against at least one gene (TRUE for n=957 out of 979 candidates).
- **Hit**: Boolean indicating whether the enhancer was identified as functional by having a significant regulatory effect on at least one gene.

## Functional annotation of candidate enhancers											

- **LinkedGene**: The gene(s) identified as significantly regulated by the enhancer. This field is populated only for enhancers marked as "Hit".
- **ENCODEv3_Meuleman2020_UbiquitousConstant to NHA_Superenhancer_Hnisz2013**: Each column represents a functional annotation indicating whether the given candidate is annotated with that specific feature.

## Transcription at candidates											

- **TTseq_eRNA**: Classification of enhancer RNA (eRNA) transcription based on TT-seq data. Categories include:
  - `"eRNA-"`: Does not meet the TT-seq threshold on either strand.
  - `"unidirectional eRNA+"`: Meets the TT-seq threshold on one strand only.
  - `"bidirectional eRNA+"`: Meets the TT-seq threshold on both strands.
- **NascentEnriched**: Boolean indicator of whether the total TT-seq read count exceeds the ribo-depleted RNA-seq read count for the candidate region, indicating enrichment of nascent transcription.
- **Count_TTseq_PosStrand**: Raw TT-seq read count mapped to the positive strand of the candidate region.
- **Count_TTseq_NegStrand**: Raw TT-seq read count mapped to the negative strand of the candidate region.
- **Count_TTseq_Total**: Combined TT-seq read count from both strands (unstranded total).
- **CPM_TTseq_Total**: TT-seq read count normalized to counts per million (CPM), representing the total unstranded signal.
- **Count_RiboDepRNAseq_PosStrand**: Raw ribo-depleted RNA-seq read count mapped to the positive strand of the candidate region.
- **Count_RiboDepRNAseq_NegStrand**: Raw ribo-depleted RNA-seq read count mapped to the negative strand of the candidate region.
- **Count_RiboDepRNAseq_Total**: Combined ribo-depleted RNA-seq read count from both strands (unstranded total).
- **CPM_RiboDepRNAseq_Total**: Ribo-depleted RNA-seq read count normalized to counts per million (CPM), representing the total unstranded signal.
- **FANTOM5_AnySample_CAGE**: Boolean indicator of whether the candidate region overlaps a CAGE peak from any sample in the FANTOM5 dataset, representing evidence of transcription initiation.

## Transcription Factor (TF) Motif Counts

- **ARNT2 to ZSCAN31**: Number of bound transcription factor (TF) motifs for TFs that are expressed in astrocytes. TF binding was inferred via footprinting analyses using the TOBIAS algorithm. Counts are provided only for candidate enhancers with at least one tested gene (n=957).

## Co-accessibility Network (kME Data)

- **moduleLabel**: The module to which the candidate enhancer has been assigned, based on co-accessibility network clustering.
- **M0 to M6**: Module eigengene-based connectivity (kME) values for each candidate enhancer.

## SNPs

- **SNPs**: List of SNPs linked to functional enhancers.

##  Brain eQTLs linked to functional enhancers																							
- **Pair**: Functional enhancer-gene pairs identified in the CRISPRi screen (n=158).
- **Gene_SignBased_eQTL to OtherGenes_NotExpressed_AstrSpecific_eQTL**: Summary of brain eQTLs linked to functional enhancers. Summaries are provided separately for:
  - **Significance-based eQTLs** ("SignBased" columns; GTEx, mmQTL, Metabrain, and Bryois),
  - **Fine-mapping-based eQTLs** ("FinemappingBased" columns; GTEx and mmQTL), and
  - **Astrocyte-specific eQTLs** ("AstrSpecific" columns; Metabrain and Bryois).  
  
  For each functional enhancer-gene relationship identified in the CRISPRi screen (n=158), a call is given per eQTL dataset indicating whether the enhancer's assigned variants have no eQTLs, eQTLs to only different genes, or at least one eQTL to the same gene as identified in the screen. The number of eQTL datasets with the same gene called is summed in the "nRep" column. For each eQTL dataset with a "Different gene" call, those genes are listed (separated by "|"), categorized by whether they pass the expression threshold used in differential expression analyses (Methods), with numbers in parentheses indicating the number of eQTL datasets in which that gene was linked by a variant. An overall categorization across eQTL datasets is provided as follows:
  - `"Same gene"`: At least one "Same gene" classification.
  - `"Different gene"`: At least one "Different gene" but no "Same gene" classifications (subcategorized by whether at least one of those different genes was found in multiple eQTL datasets).
  - `"No eQTL`": All classifications are "no eQTL".
