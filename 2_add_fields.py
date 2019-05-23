# Add fields for FIPS county and state codes to each address feature shapefile
#
# Author: Nathaniel Price
# Date: May 22, 2018

# Import modules
import arcpy
import glob
import os

# Set working directory
os.chdir("E:\\QGIS\\tl_2016_addrfeat\\")

# Get list of shapefiles
fileList = glob.glob("*.shp")

# Loop over address feature shapefiles
for i in range(0, len(fileList)):

    # Current shape file
    point_shp = fileList[i]

    # FIPS county code
    fips_co = "\"" + point_shp[8:13] + "\""

    # FIPS state code
    fips_st = "\"" + point_shp[8:10] + "\""

    print i, point_shp, fips_co, fips_st

    # Add FIPS county field
    arcpy.AddField_management(point_shp, "FIPS_CO", "TEXT", "", "", "5", "", "NON_NULLABLE", "NON_REQUIRED", "")
    arcpy.CalculateField_management(point_shp, "FIPS_CO", fips_co, "PYTHON_9.3")

    # Add FIPS state field
    arcpy.AddField_management(point_shp, "FIPS_ST", "TEXT", "", "", "2", "", "NON_NULLABLE", "NON_REQUIRED", "")
    arcpy.CalculateField_management(point_shp, "FIPS_ST", fips_st, "PYTHON_9.3")

