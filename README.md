# geocode-addresses
:earth_americas: Locate addresses using data from US Census shapefiles

Python scripts to build geodatabase from US Census shapefiles, create address locators in ArcMap, and locate addresses

0. Export addresses from SQL server to CSV file (0_export_addresses.py)
1. Download and unzip US census shapefiles (1_get_census_data.py)
2. Add fields for FIPS county code (5 digits) and FIPS state code (2 digits) to address features (2_add_fields.py)
3. Convert address feature shapefiles to feature classes in a geodatabase and then merged (3_create_geodatabase.py)
4. Create a dual ranges address locator in ArcMap (4_create_street_address_locator.py)
5. Geocode addresses at street level (5_geocode_street.py)
