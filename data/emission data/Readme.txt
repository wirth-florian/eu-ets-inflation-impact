This folder contains two sub-folders:

- 'Documentation': a folder containing additional information and documentation for the emission mapping procedure
- 'UNFCCC Common reporting tables': a folder containing the common reporting tables for our countries of interest. We use those tables to extract detailed and timely information on emissions for different emission categories


This folder also contains seven spreadsheets:

- 'CRT_codes.csv': A list with descriptions of the emission codes used in the common reporting tables (CRTs)
- 'CRT_emissions_processed.csv': A spreadsheet with emissions sourced from the CRTs. The format of the spreadsheet resembles that of PRIMAP-crf but it contains more recent years. We use this dataset in the multi-scale-mapping algorithm to map emissions disaggregated into IPCC categories to the different NACE sectors.
- 'Guetschow_et_al_2025a-PRIMAP-hist_v2.7_final_22-Aug-2025.csv': The PRIMAP-hist spreadsheet
- 'Guetschow-et-al-2021-PRIMAP-crf_2021-v1.csv': The primap.crf spreadsheet
- 'mapping_crf_Figaro.csv': A mapping of NACE Rev2 sectors in Figaro to IPCC2006 emission categories used in PRIMAP. The mapping largely follows the official correspondence table from the European union, which can be found in the 'Documentation' sub-folder. There also exists an .xlsx version of this mapping, which contains comments about certain mapping choices, whenever we deviate from the correspondence table.
- 'primap_crf_processed.csv': A processed version of the PRIMAP-crf dataset with ISO2 instead of ISO3 codes. We use ISO2 codes, becase the Figaro MRIO tables uses ISO2 for the countries. This modified version of primap-crf is only used for comparison with our own dataset which we source from the CRTs
- 'primap_hist_processed': A processed version of the PRIMAP-hist dataset with ISO2 instead of ISO3 codes. We use it in the multi-scale-mapping algorithm.
