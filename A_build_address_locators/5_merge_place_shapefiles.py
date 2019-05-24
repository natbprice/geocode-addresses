# Merge 2016 US Census place shapefiles
#
# Author: Nathaniel Price
# Date: June 14, 2017

# Import modules
import arcpy
from arcpy import env
import glob
import os

# Overwrite existing files
arcpy.env.overwriteOutput = True

# Set working directory
os.chdir('E://QGIS//cb_2016_place_500k//')

# Get list of shapefiles
fileList = glob.glob("*.shp")

# Create geodatabase
arcpy.CreateFileGDB_management('E://QGIS//cb_2016_place_500k', "cb_2016_place_500k.gdb")

# Add shapefiles to geodatabase
arcpy.FeatureClassToGeodatabase_conversion(fileList, 'E://QGIS//cb_2016_place_500k//cb_2016_place_500k.gdb')

# Set environment to geodatabase
arcpy.env.workspace = 'E://QGIS//cb_2016_place_500k//cb_2016_place_500k.gdb'

# Get list of all feature classes
features = arcpy.ListFeatureClasses('*','All')

# Merge all features
arcpy.Merge_management(features, 'CB_PLACE')