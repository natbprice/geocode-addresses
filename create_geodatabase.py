# Merge 2016 US Census addrfeat shapefiles into a geodatabase
#
# Author: Nathaniel Price
# Date: June 14, 2017

# Setup ---------------------------------------------------------------------------------------------------------------
# Import modules
import arcpy
from arcpy import env
import glob
import os

# Set working directory
os.chdir("E:\\QGIS\\tl_2016_addrfeat\\")

# Create geodatabase --------------------------------------------------------------------------------------------------
# Get list of shapefiles
fileList = glob.glob("*.shp")

# Create geodatabase
arcpy.CreateFileGDB_management("E:/QGIS/2016_ADDRFEAT", "2016_ADDRFEAT.gdb")

# Add shapefiles to geodatabase
arcpy.FeatureClassToGeodatabase_conversion(fileList, "E:/QGIS/2016_ADDRFEAT/2016_ADDRFEAT.gdb")

# Set environment to geodatabase
arcpy.env.workspace = r"E:/QGIS/2016_ADDRFEAT/2016_ADDRFEAT.gdb"

# Get list of all feature classes
features = arcpy.ListFeatureClasses('*','All')

# Merge all features
arcpy.Merge_management(features, 'ADDRFEAT')


