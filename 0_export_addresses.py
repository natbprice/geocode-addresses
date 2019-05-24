# Load modules
from collections import namedtuple
from itertools import imap
import os.path
import arcpy
from arcpy.da import InsertCursor
from arcpy.conversion import TableToTable
from arcpy.management import CreateTable, AddField, GetCount, Delete
import pyodbc

# Create empty geodatabase
exists = os.path.isdir('E://QGIS//geocoding2018//geocoding.gdb')
if not exists:
    arcpy.CreateFileGDB_management("E://QGIS//geocoding2018", "geocoding.gdb")

# Connect to SQL database
cnxn = pyodbc.connect('DSN=PermitDatabase;'
                      'Database=NGPCPermits201904;'
                      'Trusted_Connection=yes;')
in_cursor = cnxn.cursor()
in_cursor.execute("SELECT * FROM Address")

# pyodbc cursor description object
FieldDesc = namedtuple("FieldDesc", ("name", "type_code", "display_size", "internal_size",
                                     "precision", "scale", "null_ok"))
# Create temporary table
temp_table = r"in_memory\temp"
CreateTable(*os.path.split(temp_table))

# Add fields to temporary table
for fielddesc in imap(FieldDesc._make, in_cursor.description):
    typename = fielddesc.type_code.__name__

    if typename == "int":
        fieldtype = "LONG"
    elif typename == "datetime":
        fieldtype = "DATE"
    elif typename == "float":
        fieldtype = "FLOAT"
    elif typename == "Decimal" and fielddesc.precision < 7:
        fieldtype = "FLOAT"
    elif typename == "Decimal":
        fieldtype = "DOUBLE"
    elif typename == "str":
        fieldtype = "TEXT"
    elif typename == "bool":
        fieldtype = "SHORT"
    else:
        raise ValueError("Unsupported field type: %s" % typename)

    nullable = "NULLABLE" if fielddesc.null_ok else "NON_NULLABLE"

    AddField(temp_table, fielddesc.name, fieldtype, fielddesc.precision, fielddesc.scale,
             fielddesc.internal_size, None, nullable)

# Get field names for temp_table, which may differ from in_table
fieldnames = [field.name for field in arcpy.Describe(temp_table).fields \
              if field.type != "OID"]

# Copy rows into temporary table
with InsertCursor(temp_table, fieldnames) as out_cursor:
    for in_row in in_cursor:
        out_cursor.insertRow(in_row)

# Convert temporary table to table in geodatabase
TableToTable(in_rows=temp_table,
             out_path='E://QGIS//geocoding2018//geocoding.gdb',
             out_name='address')

# Delete temporary table
if arcpy.Exists(temp_table):
            Delete(temp_table)
