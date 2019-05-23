# geocode-addresses
:earth_americas: Locate addresses using data from US Census shapefiles

Python scripts to build geodatabase from US Census shapefiles, create address locators in ArcMap, and locate addresses

1. Download and unpack US census shapefiles (ftp2.census.gov/geo/tiger/TIGER2018)
   * Places (/PLACE/*)
   * Address features (/ADDRFEAT/*)
   * Counties (/COUNTY/*)
   * Zip-code Tabulation Areas (/ZCTA5/*)
2. Add fields for FIPS county code (5 digits) and FIPS state code (2 digits) to address features using script 1_add_fields.py
3. Convert address feature shapefiles to feature classes in a geodatabase and then merged into a single feature using script
2_create_geodatabase.py
4. Create a dual ranges address locator using script 3_create_street_address_locator.py
