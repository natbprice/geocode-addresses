# Merge 2018 US Census addrfeat shapefiles into a geodatabase
#
# Author: Nathaniel Price
# Date: May 22, 2018
#
# NOTE:
# Excute script from within ArcMap
# execfile('C://Users//nprice3//PycharmProjects//merge_shapefiles//create_geodatabase.py')
#
# Setup ---------------------------------------------------------------------------------------------------------------
# Import modules
import arcpy
from arcpy import env
import glob
import os

# Set working directory
os.chdir("E:\\QGIS\\tl_2018_addrfeat\\")

# Create geodatabase --------------------------------------------------------------------------------------------------
# Get list of shapefiles
fileList = glob.glob("*.shp")

# Create geodatabase
arcpy.CreateFileGDB_management("E:/QGIS/2018_ADDRFEAT", "2018_ADDRFEAT.gdb")

# Add shapefiles to geodatabase
arcpy.FeatureClassToGeodatabase_conversion(fileList, "E:/QGIS/2018_ADDRFEAT/2018_ADDRFEAT.gdb")

# Set environment to geodatabase
arcpy.env.workspace = r"E:/QGIS/2018_ADDRFEAT/2018_ADDRFEAT.gdb"

# Get list of all feature classes
features = arcpy.ListFeatureClasses('*','All')

# Merge all features
arcpy.Merge_management(features, 'ADDRFEAT')


