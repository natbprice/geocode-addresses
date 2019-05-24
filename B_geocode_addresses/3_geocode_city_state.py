# Geocode city state addresses
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
filePath = 'E://QGIS//geocoding//cityState//'
os.chdir(filePath)
fileList = glob.glob('*.csv')

# # Create geodatabase
# arcpy.CreateFileGDB_management("E://QGIS//geocoding", "geocoding.gdb")

# Set workspace
env.workspace = 'E://QGIS//geocoding//geocoding.gdb'

# Don't add outputs to map
arcpy.env.addOutputsToMap = 0

# # Loop over files adding to geodatabase and geocoding
# for i in range(30, len(fileList)):
#
#     # Current file
#     print fileList[i]
#
#     # Variable names
#     fnameIn = filePath + fileList[i]
#     pathOut = 'E://QGIS//geocoding//geocoding.gdb'
#     fnameOut = 'addressCityState' + fileList[i][9:-4]
#     resultOut = 'geocodeResultCityState' + fileList[i][9:-4]
#
#     # Import addresses to geodatabase
#     arcpy.TableToTable_conversion (in_rows = fnameIn,
#                                    out_path = pathOut,
#                                    out_name = fnameOut)
#
#     # Geocode cities
#     address_table = fnameOut
#     address_locator = 'C://Users//nprice3//Documents//ArcGIS//Address_Locators//places_composite//places_by_state'
#     address_fields = "'City' city;'State' state"
#     geocode_result = resultOut
#
#     arcpy.GeocodeAddresses_geocoding(in_table = address_table,
#                                      address_locator = address_locator,
#                                      in_address_fields = address_fields,
#                                      out_feature_class = geocode_result)
#
#
# # Get list of all results
# features = arcpy.ListFeatureClasses('geocodeResultCityState*','All')
#
# # Merge all results
# arcpy.Merge_management(features, 'geocodeResultCityStateMerged')

# Split match address into city state
arcpy.AddField_management(in_table = 'geocodeResultCityStateMerged',
                          field_name = 'matchCity',
                          field_type = 'TEXT',
                          field_length = 120)
arcpy.AddField_management(in_table = 'geocodeResultCityStateMerged',
                          field_name = 'matchState',
                          field_type = 'TEXT',
                          field_length = 2)
arcpy.CalculateField_management('geocodeResultCityStateMerged',
                                'matchCity',
                                expression = '!Match_addr!.split(", ")[0]',
                                expression_type = 'PYTHON_9.3')
arcpy.CalculateField_management('geocodeResultCityStateMerged',
                                'matchState',
                                expression = '!Match_addr!.split(", ")[-1] if ("," in !Match_addr!) else ""',
                                expression_type = 'PYTHON_9.3')

# Join county
