# Geocode street addresses
#
# Author: Nathaniel Price
# Date: May 22, 2018

# NOTE:
# Excute script from within ArcMap
# execfile('C://Users//nprice3//PycharmProjects//merge_shapefiles//5_geocode_street.py')

# Setup ---------------------------------------------------------------------------------------------------------------
# Import system modules
import csv
import glob
import os
import arcpy
from arcpy import env

# Overwrite existing files
arcpy.env.overwriteOutput = True

# Geocode streets
arcpy.GeocodeAddresses_geocoding(in_table="E:/QGIS/geocoding2018/geocoding.gdb/address",
                                 address_locator="C:/Users/nprice3/Documents/ArcGIS/Address_Locators/streets/national_streets",
                                 in_address_fields="Street Street VISIBLE NONE;ZIP ZIP VISIBLE NONE",
                                 out_feature_class="E:/QGIS/geocoding2018/geocoding.gdb/geocodeResultStreet",
                                 out_relationship_type="STATIC")
