# Create national address locator for street addresses
#
# Author: Nathaniel Price
# Date: June 16th, 2017

# Setup ---------------------------------------------------------------------------------------------------------------
# Import system modules
import os
import arcpy
from arcpy import env

# Set working directory
os.chdir('E://QGIS//cb_2016_place_500k//')

# Define output path
OutputPath = 'C://Users//nprice3//Documents//ArcGIS//Address_Locators//'

# Create address locator ----------------------------------------------------------------------------------------------
# Set environment
env.workspace = "E:/QGIS/2016_ADDRFEAT/2016_ADDRFEAT.gdb"

# Create national streets address locator
output = OutputPath + "streets//national_streets"
arcpy.CreateAddressLocator_geocoding(in_address_locator_style = "US Address - Dual Ranges",
                                     in_reference_data = "ADDRFEAT 'Primary Table'",
                                     in_field_map = "'Feature ID' OBJECTID VISIBLE NONE;'*From Left' LFROMHN VISIBLE NONE;'*To Left' LTOHN VISIBLE NONE;'*From Right' RFROMHN VISIBLE NONE;'*To Right' RTOHN VISIBLE NONE;'Prefix Direction' <None> VISIBLE NONE;'Prefix Type' <None> VISIBLE NONE;'*Street Name' FULLNAME VISIBLE NONE;'Suffix Type' <None> VISIBLE NONE;'Suffix Direction' <None> VISIBLE NONE;'Left City or Place' <None> VISIBLE NONE;'Right City or Place' <None> VISIBLE NONE;'Left ZIP Code' ZIPL VISIBLE NONE;'Right ZIP Code' ZIPR VISIBLE NONE;'Left State' <None> VISIBLE NONE;'Right State' <None> VISIBLE NONE",
                                     out_address_locator = output,
                                     config_keyword = "",
                                     enable_suggestions = "DISABLED")
