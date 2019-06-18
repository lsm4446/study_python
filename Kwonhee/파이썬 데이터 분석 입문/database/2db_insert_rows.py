#!/usr/bin/env python3
import csv
import sqlite3
import sys

# Path to and name of a CSV input file
input_file = "D:\Kwonhee\OneDrive\Github\study_python\Kwonhee\파이썬 데이터 분석 입문\database\supplier_data.csv"
# Create an in-memory SQLite3 database
# Create a table called Suppliers with five attributes
con = sqlite3.connect('Suppliers.db')
c = con.cursor()
create_table = """CREATE TABLE IF NOT EXISTS Suppliers
				(Supplier_Name VARCHAR(20),
				Invoice_Number VARCHAR(20),
				Part_Number VARCHAR(20),
				Cost FLOAT,
				Purchase_Date DATE);"""
con.execute(create_table)
con.commit()

# Read the CSV file
# Insert the data into the Suppliers table
file_reader = csv.reader(open(input_file, 'r'), delimiter=',')
header = next(file_reader, None)
for row in file_reader:
	data = []
	for column_index in range(len(header)):
		data.append(row[column_index])
	print(data)
	c.execute("INSERT INTO Suppliers VALUES (?, ?, ?, ?, ?);", data)
con.commit()

# Query the Suppliers table
output = c.execute("SELECT * FROM Suppliers")
rows = output.fetchall()
for row in rows:
	output = []
	for column_index in range(len(row)):
		output.append(str(row[column_index]))
	print('output:', output)
