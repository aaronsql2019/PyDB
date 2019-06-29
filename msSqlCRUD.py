from msSqlConnect import msSqlConnect
import pyodbc
import sys


# Connect MSSQL
cnxn = msSqlConnect()
# Create a cursor from the connection
cursor = cnxn.cursor()

# Create
# Create Table
# cursor.execute(
#     "CREATE TABLE Boxes(Name nvarchar(30) NOT NULL, Size nvarchar(30), Colored bit)")
# Insert many
params = [('Express box', '尺寸 (cm):長83x寬44x高39', 0),
          ('Express box 400', '尺寸 (cm):長68.5x寬51x高41', 1),
          ('Express box 360', '尺寸 (cm):長49.5x寬44.5x高36.5', None),
          ('Express box 300', '尺寸 (cm):長42x寬37x高31', 0),
          ('Express box 290', '尺寸 (cm):長46.5x寬33x高30', 0),
          ('Express box 250', '尺寸 (cm):長41x寬32x高26', 0),
          ('Express box 40', '長24x寬17.5x高5.5', 0)]
cursor.executemany(
    "INSERT INTO Boxes(Name, Size, Colored) VALUES (?, ?, ?)", params)
# Insert one
# cursor.execute("INSERT INTO Boxes(Name, Size, Colored) VALUES (?, ?, ?)",
#                'Express box', 'L83W44H39', 0)

# Update
# Add Column
# cursor.execute("ALTER TABLE Boxes ADD (_id tinyint);")
# Alter Column
# cursor.execute("ALTER TABLE Boxes ALTER COLUMN Size nvarchar(30);")

# Delete
# cursor.execute("DELETE FROM Boxes")
# print(cursor.rowcount, '種箱子被刪除')
# Drop Table
# cursor.execute("DROP TABLE Boxes")

cnxn.commit()

# Read
# Sample select query
# cursor.execute("SELECT @@version;")
# row = cursor.fetchone()
# while row:
#     print(row[0])
#     row = cursor.fetchone()

# Returns a list of all the remaining rows in the query.
# cursor.execute("SELECT * FROM Inventory")
# rows = cursor.fetchall()
# for row in rows:
#     print(row.Name, row.Quantity)

# Read the rows one at a time
for row in cursor.execute("SELECT * FROM Boxes"):
    print('%-17s %-28s %s' % (row.Name, row.Size, row.Colored))
