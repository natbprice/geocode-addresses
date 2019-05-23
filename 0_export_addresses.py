# Load modules
import pyodbc
import csv
import pandas as pd

# Connect to SQL database
conn = pyodbc.connect('DSN=PermitDatabase;'
                      'Database=NGPCPermits201904;'
                      'Trusted_Connection=yes;')

# Save addresses to CSV in chunks
df = pd.read_sql('SELECT * FROM Address', conn, chunksize = 1000)
for chunk in df:
    chunk.to_csv("address.csv", encoding="utf-8", mode = "a")