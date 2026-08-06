This folder contains four sub-folders:

- 'crf_2026' holds the processed dataframe of national emissions in the common reporting framework in the file 'CRT_emissions_processed.csv' These emissions are sourced from the 2026 release of the UNFCCC common reporting tables (CRTs). The format of the spreadsheet resembles that of PRIMAP-crf but it contains more recent years. We use this dataset in the multi-scale-mapping algorithm to map emissions disaggregated into IPCC categories to the different NACE sectors.
- 'hist_2025' holds the 2025 release of the PRIMAP_hist series once in the original version with ISO3 country codes and once in a modified version with ISO2 country codes. It is used together with the 'CRT_emissions_processed.csv' table in the multi-scale mapping algorithm. Due to the design of the MRIO toolbox, these first files need to be in separate folders.
- 'mapping documentation' has additional documents to detail the mapping between CRF categories and NACE2 sectors
- 'UNFCCC common reporting tables': a folder containing the common reporting tables for our countries of interest. We use those tables to extract detailed and timely information on emissions for different emission categories


This folder also contains several spreadsheets:

- 'CRT_codes.csv': A list with descriptions of the emission codes used in the common reporting tables (CRTs)
- 'Guetschow-et-al-2021-PRIMAP-crf_2021-v1.csv': The original primap.crf spreadsheet, used for comparison with overlapping years of our custom disaggregation, which we directly create from the common reporting tables.
- 'mapping_crf_Figaro.csv': A mapping of NACE Rev2 sectors in Figaro to IPCC2006 emission categories used in PRIMAP. The mapping largely follows the official correspondence table from the European union, which can be found in the 'Documentation' sub-folder. There also exists an .xlsx version of this mapping in the 'mapping documentation' folder, which contains comments about certain mapping choices, whenever we deviate from the correspondence table.
- 'primap_crf_processed.csv': A processed version of the PRIMAP-crf dataset with ISO2 instead of ISO3 codes. We use ISO2 codes, because the Figaro MRIO tables uses ISO2 for the countries. This modified

Furthermore, the folder contains the file 'emission_data.pkl' which is an intermediate file created by our CRT disaggregation process.
