"""
Prepare and aggregate Figaro MRIO data

This script raw extracts Figaro MRIO data, maps emissions to sectors and aggregates regions based on predefined groupings.
The resulting aggregated MRIO data is saved to a NetCDF file.

@author: wirth 2025
"""

import os
import sys
import warnings
import yaml
import logging
from mrio_toolbox import MRIO, extract_MRIO, multi_scale_mapping
from mrio_toolbox.utils.savers._to_nc import save_to_nc 
# Suppress warnings about duplicate dimension names specific UserWarnings from xarray.namedarray
warnings.filterwarnings("ignore", category=UserWarning, module=r"xarray\.namedarray\.core")

logging.basicConfig(level=logging.INFO)

year = 2024
edition = 26
version = "eu27" 
#version = "eu27_ch_no" # all eu27 countries with switzerland and norway
#version = "eu27_ch_no_without_mt_si_lv_cy" # with switzerland and norway, without malta, slovenia, latvia, cyprus


filepath = os.path.abspath(f"data/figaro io/formatted io/figaro_year{year}.nc")
grouping_file_path = os.path.abspath(f"data/figaro io/figaro{edition}ed_grouping_{version}.yaml")
output_filepath = os.path.abspath(f"data/figaro io/formatted io/figaro_year{year}_aggregated_{version}.nc")

if not os.path.isfile(filepath): 
    figaro = extract_MRIO(source= "data/figaro io/raw io/",
                          table = "figaro",
                          year = year,
                          extraction_kwargs= {"edition": edition, "sut" :"supply"})
    save_to_nc(figaro, filepath)
else:
    figaro = MRIO(file = filepath)

    
groupings = yaml.safe_load(open(grouping_file_path))
figaro.set_groupings(groupings)
figaro.aggregate(on = "countries")

# map emissions to figaro
multi_scale_mapping (
    mrio = figaro,
    mapping_file = "mapping_crf_Figaro",
    year = 2024, 
    crf_version = "2026",
    hist_version = "2025",
    emissions_year= "same" ,
    mapping_extension= ".csv",
    table = "figaro2024",
    primap_path= "data/emission data", 
    mapping_path= "data/emission data",
    entities = ["CO2", "CH4", "N2O"], 
    kyoto_basket= False,
    crf_name = "CRT_emissions_processed",
    hist_name = "primap_hist_processed",
    categories_output =  "all"
    )


save_to_nc(figaro, output_filepath)
print("Aggregation complete. Data saved to netCD.")