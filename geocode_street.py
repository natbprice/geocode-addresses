# Geocode street addresses
#
# Author: Nathaniel Price
# Date: June 16th, 2017

# NOTE:
# Excute script from within ArcMap
# execfile('C://Users//nprice3//PycharmProjects//merge_shapefiles//geocode_city_state.py')

# Setup ---------------------------------------------------------------------------------------------------------------
# Import system modules
import csv
import glob
import os
import arcpy
from arcpy import env

# Overwrite existing files
arcpy.env.overwriteOutput = True

# Geocoding -----------------------------------------------------------------------------------------------------------
# List of files
filePath = 'E://QGIS//geocoding//street//'
os.chdir(filePath)
fileList = glob.glob('*.csv')

# # Create geodatabase
# arcpy.CreateFileGDB_management("E://QGIS//geocoding", "geocoding.gdb")

# Set workspace
env.workspace = 'E://QGIS//geocoding//geocoding.gdb'

# Don't add outputs to map
arcpy.env.addOutputsToMap = 0

# Variable names
fnameIn = fileList[0]
pathOut = 'E://QGIS//geocoding//geocoding.gdb'
fnameOut = 'addressStreet'
resultOut = 'geocodeResultStreet'

# Import addresses to geodatabase
arcpy.TableToTable_conversion(in_rows=fnameIn,
                              out_path=pathOut,
                              out_name=fnameOut,
                              field_mapping = """uid "uid" true true false 4 Long 0 0 ,First,#,E:\QGIS\geocoding\street\addressStreet.csv,uid,-1,-1;street "street" true true false 8000 Text 0 0 ,First,#,E:\QGIS\geocoding\street\addressStreet.csv,street,-1,-1;zip "zip" true true false 8000 Text 0 0 ,First,#,E:\QGIS\geocoding\street\addressStreet.csv,zip,-1,-1;validStreet "validStreet" true true false 8 Double 0 0 ,First,#,E:\QGIS\geocoding\street\addressStreet.csv,validStreet,-1,-1""")

# Geocode streets
arcpy.GeocodeAddresses_geocoding(in_table="E:/QGIS/geocoding/geocoding.gdb/addressStreet",
                                 address_locator="C:/Users/nprice3/Documents/ArcGIS/Address_Locators/streets/national_streets",
                                 in_address_fields="Street Street VISIBLE NONE;ZIP ZIP VISIBLE NONE",
                                 out_feature_class="E:/QGIS/geocoding/geocoding.gdb/geocodeResultStreet",
                                 out_relationship_type="STATIC")
