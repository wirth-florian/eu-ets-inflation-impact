This folder contains raw MRIO and supply tables from the figaro project in the subfolder 'raw'.
Those are formatted as netCDF objects for use with the mrio-toolbox python package in the subfolder 'formatted'

The .yaml files contain aggregation codes for aggregating different sets of countries. E.g. we include Norway and Switzerland in the carbon model, as they have linked their ETS to Europe's ETS, but Switzerland is later exclude in the impact analysis of the HICP as there is no CPA -> COICOP mapping published for Switzerland. Furthermore, Malta, Slovenia, Latvia and Cyprus were excluded, as their supply tables were internally imbalanced.


