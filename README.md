# geocode-addresses
:earth_americas: Locate addresses using data from US Census shapefiles

Python scripts to build geodatabase from US Census shapefiles, create address locators in ArcMap, and locate addresses

Build address locators
1.  Download and unzip US census shapefiles (1_get_census_data.py)
2.  Add fields for FIPS county code and FIPS state code to address features (2_add_fields.py)
3.  Create a geodatabase of merged address features (3_create_geodatabase.py)
4.  Create a dual ranges address locator in ArcMap (4_create_street_address_locator.py)
5.  Add places (i.e., cities) to geodatabase and merge (5_merge_place_shapefiles.py)
6.  Join counties to places (6_join_counties_to_places.py)
7.  Create city, state composite address locator in ArcMap (7_create_city_address_locator)

Geocode addresses
1.  Export addresses from SQL server to ArcMap geodatabase (1_export_addresses.py)
2.  Geocode addresses at street level (2_geocode_street.py)
3.  Geocode addresses at city, state level (3_geocode_city_state.py)
4.  Import geocode results from ArcMap geodatabase to SQL server