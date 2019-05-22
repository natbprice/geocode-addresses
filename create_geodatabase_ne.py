# Import modules
import arcpy
from arcpy import env
import glob
import os

# Set working directory
os.chdir("E:\\QGIS\\tl_2016_addrfeat\\")

# # Get list of shapefiles
# fileList = glob.glob("tl_2016_31*.shp")
#
# # Create geodatabase
# arcpy.CreateFileGDB_management("E:/QGIS/nebraska_addrfeat", "nebraska_addrfeat.gdb")
#
# # Merge shapefiles
# arcpy.Merge_management(fileList, "E:/QGIS/nebraska_addrfeat/addrfeat.shp")

# # Add merged shapefile to geodatabase
# arcpy.FeatureClassToGeodatabase_conversion("E:/QGIS/nebraska_addrfeat/addrfeat.shp", "E:/QGIS/nebraska_addrfeat/nebraska_addrfeat.gdb")
#
# # Get list of shapefiles
# fileList = glob.glob("tl_2016_31*.shp")
#
# # Create geodatabase
# arcpy.CreateFileGDB_management("E:/QGIS/nebraska_addrfeat_2", "nebraska_addrfeat_2.gdb")
#
# # Add merged shapefile to geodatabase
# arcpy.FeatureClassToGeodatabase_conversion(fileList, "E:/QGIS/nebraska_addrfeat_2/nebraska_addrfeat_2.gdb")

arcpy.env.workspace = r"E:/QGIS/nebraska_addrfeat_2/nebraska_addrfeat_2.gdb"

features = arcpy.ListFeatureClasses('*','All')

arcpy.Merge_management(features, 'ADDRFEAT')