#!/usr/bin/env python3
import csv
import MySQLdb
import sys

# Path to and name of a CSV output file
output_file = "D:/Kwonhee/OneDrive/Github/study_python/Kwonhee/파이썬 데이터 분석 입문/database/5output.csv"

# Connect to a MySQL database
con = MySQLdb.connect(host='localhost', port=3306, db='my_suppliers', user='idencosmos', passwd='password')
c = con.cursor()

# Create a file writer object and write the header row
filewriter = csv.writer(open(output_file, 'w', newline=''), delimiter=',')
header = ['Supplier Name','Invoice Number','Part Number','Cost','Purchase Date']
filewriter.writerow(header)

# Query the Suppliers table and write the output to a CSV file
c.execute("""SELECT *
		FROM Suppliers
		WHERE Cost > 500.0;""")
rows = c.fetchall()
for row in rows:
	filewriter.writerow(row)
