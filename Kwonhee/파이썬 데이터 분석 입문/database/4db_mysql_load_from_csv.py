#!/usr/bin/env python3
import csv
import MySQLdb
import sys
from datetime import datetime, date

# Path to and name of a CSV input file
input_file = "D:/Kwonhee/OneDrive/Github/study_python/Kwonhee/파이썬 데이터 분석 입문/database/supplier_data.csv"

# Connect to a MySQL database
con = MySQLdb.connect(host='localhost', port=3306, db='my_suppliers', user='idencosmos', passwd='password')
c = con.cursor()

# Read the CSV file
# Insert the data into the Suppliers table
file_reader = csv.reader(open(input_file, 'r'), delimiter=',')
header = next(file_reader)
for row in file_reader:
	data = []
	for column_index in range(len(header)):
		if column_index < 4:
			data.append(str(row[column_index]).lstrip('$')\
			.replace(',', '').strip())
		else:
			print(row[column_index])
			a_date = datetime.date(datetime.strptime(\
			str(row[column_index]), '%m/%d/%y'))
			print('a_date:', a_date)
			# %Y: year is 2016; %y: year is 15
			a_date = a_date.strftime('%Y-%m-%d')
			# 윗줄은 무슨 변화를 줘도, db에는 날짜로 저장된다. datetime.date(2014, 1, 20)처럼
			data.append(a_date)
	print(data)
	c.execute("""INSERT INTO Suppliers VALUES (%s, %s, %s, %s, %s);""", data)
con.commit()

# Query the Suppliers table
c.execute("SELECT * FROM Suppliers")
rows = c.fetchall()
for row in rows:
	print('row:', row)
	row_list_output = []
	for column_index in range(len(row)):
		row_list_output.append(str(row[column_index]))
	print('row_list_output:', row_list_output)
