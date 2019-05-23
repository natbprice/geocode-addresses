import pyodbc
import csv
import pandas as pd

conn = pyodbc.connect('DSN=PermitDatabase;'
                      'Database=NGPCPermits201904;'
                      'Trusted_Connection=yes;')

df = pd.read_sql('SELECT * FROM Address', conn, chunksize = 1000)
for chunk in df:
    chunk.to_csv("address.csv", encoding="utf-8", mode = "a")

# cursor = conn.cursor()
# cursor.execute('SELECT * FROM Address')
#
# with open("address.csv", "wb") as csv_file:
#     csv_writer = csv.writer(csv_file)
#     csv_writer.writerow([i[0] for i in cursor.description]) # write headers
#     csv_writer.writerows(cursor)