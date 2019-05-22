# Join counties to places when they are completely within county boundaries
#
# Author: Nathaniel Price
# Date: June 16th, 2017

# execfile('C://Users//nprice3//PycharmProjects//merge_shapefiles//join_counties_to_places.py')
# Setup ---------------------------------------------------------------------------------------------------------------
# Import system modules
import csv
import glob
import os
import arcpy
from arcpy import env

# Overwrite existing files
arcpy.env.overwriteOutput = True

# Spatial join --------------------------------------------------------------------------------------------------------

# Add features to database
arcpy.FeatureClassToGeodatabase_conversion('E://QGIS//tl_2016_us_county//tl_2016_us_county.shp', 'E://QGIS//cb_2016_place_500k//cb_2016_place_500k.gdb')

# Set environment
env.workspace = 'E://QGIS//cb_2016_place_500k//cb_2016_place_500k.gdb'

# Create a new fieldmappings and add the two input feature classes.
fieldmappings = arcpy.FieldMappings()
fieldmappings.addTable('CB_PLACE')
fieldmappings.addTable('tl_2016_us_county')

# Delete unused county fields
x = fieldmappings.findFieldMapIndex("COUNTYNS")
fieldmappings.removeFieldMap(x)
x = fieldmappings.findFieldMapIndex("PLACENS")
fieldmappings.removeFieldMap(x)
x = fieldmappings.findFieldMapIndex("NAMELSAD")
fieldmappings.removeFieldMap(x)
x = fieldmappings.findFieldMapIndex("LSAD")
fieldmappings.removeFieldMap(x)
x = fieldmappings.findFieldMapIndex("CLASSFP")
fieldmappings.removeFieldMap(x)
x = fieldmappings.findFieldMapIndex("MTFCC")
fieldmappings.removeFieldMap(x)
x = fieldmappings.findFieldMapIndex("CSAFP")
fieldmappings.removeFieldMap(x)
x = fieldmappings.findFieldMapIndex("CBSAFP")
fieldmappings.removeFieldMap(x)
x = fieldmappings.findFieldMapIndex("METDIVFP")
fieldmappings.removeFieldMap(x)
x = fieldmappings.findFieldMapIndex("FUNCSTAT")
fieldmappings.removeFieldMap(x)
x = fieldmappings.findFieldMapIndex("ALAND")
fieldmappings.removeFieldMap(x)
x = fieldmappings.findFieldMapIndex("AWATER")
fieldmappings.removeFieldMap(x)
x = fieldmappings.findFieldMapIndex("INTPTLAT")
fieldmappings.removeFieldMap(x)
x = fieldmappings.findFieldMapIndex("INTPTLON")
fieldmappings.removeFieldMap(x)
x = fieldmappings.findFieldMapIndex("AFFGEOID")
fieldmappings.removeFieldMap(x)
x = fieldmappings.findFieldMapIndex("GEOID")
fieldmappings.removeFieldMap(x)


arcpy.SpatialJoin_analysis(target_features = 'CB_PLACE',
                           join_features = 'tl_2016_us_county',
                           out_feature_class = 'place_join_county',
                           join_operation = 'JOIN_ONE_TO_MANY',
                           join_type = 'KEEP_ALL',
                           # field_mapping = fieldmappings,
                           match_option = 'COMPLETELY_WITHIN')