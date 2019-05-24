# Create address locators for cities in each state. Create composite address locator for all states.
#
# Author: Nathaniel Price
# Date: May 22, 2018

# Setup ---------------------------------------------------------------------------------------------------------------
# Import system modules
import csv
import glob
import os
import arcpy
from arcpy import env

# Set working directory
os.chdir('E://QGIS//tl_2018_place//')

# Overwrite existing files
arcpy.env.overwriteOutput = True

# Define output path
OutputPath = 'C://Users//nprice3//Documents//ArcGIS//Address_Locators//'

# Create geodatabase --------------------------------------------------------------------------------------------------
arcpy.CreateFileGDB_management("E://QGIS//geocoding", "geocoding.gdb")

# Create a city address locator for each state ------------------------------------------------------------------------
# Get list of shapefiles
fileList = glob.glob('tl_2018*.shp')

# # Create table from state FIPS excel file
# env.workspace = r'E:/QGIS/geocoding/geocoding.gdb'
# arcpy.ExcelToTable_conversion ( "E:/QGIS/stateFIPS.xls", "stateFIPS", "state")
#
# # Loop over place shapefiles
# fname = [0] * len(fileList)
# for i in range(0, len(fileList)):
#     # Define path for locator
#     fname[i] = fileList[i][0:-4]
#
#     # Join state name table to city table
#     arcpy.JoinField_management(fileList[i], "STATEFP", "stateFIPS", "STATE")
#
#     # Create city address locator
#     arcpy.CreateAddressLocator_geocoding("US Address - City State", fileList[i] + " 'Primary Table'",
#                                          "'Feature ID' FID VISIBLE NONE;'*City' NAME VISIBLE NONE;'State' STUSAB VISIBLE NONE;",
#                                          OutputPath + "places/" + fname[i], "", "DISABLED")

# Create composite address locator from state locators ----------------------------------------------------------------
# Redfine workspace
arcpy.env.workspace = OutputPath + 'places//'

# Get list of shapefiles
os.chdir(OutputPath + 'places//')
locList = glob.glob('*.loc')

# Define string of address locators with names
locators = ""
locName = [0] * len(locList)
for i in range(0, len(locList)):
    locName[i] = locList[i][8:16]
    locators = locators + locList[i] + ' ' + locName[i] + ';'
locators = locators[0:-1]

# Define field map
fm = """City "City Names" true true false 100 Text 0 0 ,First,#,"""
for file in locList:
    fm = fm + file + ",City,0,0,"

fm = fm[0:-1] + """;State "State" true true false 40 Text 0 0 ,First,#,"""
for file in locList:
    fm = fm + file + ",State,0,0,"

fm = fm[0:-1]

# Parse CSV file of state FIPS codes to state abbreviations
with open('E://QGIS//stateFIPS.csv', 'rU') as infile:
  # read the file as a dictionary for each row ({header : value})
  reader = csv.DictReader(infile)
  data = {}
  for row in reader:
    for header, value in row.items():
      try:
        data[header].append(value)
      except KeyError:
        data[header] = [value]

stateFP = data['STATE']
stateABB = data['STUSAB']

# Define selection criteria
sc = ""
for name in locName:
    ind = stateFP.index(name[0:2])
    criteria = """State='{0}'""".format(stateABB[ind])
    sc = sc + name + ' ' + criteria + ";"

sc = sc[0:-1]

# Create composite locator
arcpy.geocoding.CreateCompositeAddressLocator(in_address_locators = locators,
                                              in_field_map = fm,
                                              in_selection_criteria = sc,
                                              out_composite_address_locator = OutputPath + 'places_composite//' + 'places_by_state')