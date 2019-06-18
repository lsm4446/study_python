#!/usr/bin/env python3
import csv
import glob
import os
import string
import sys

input_path = "D:\OneDrive\Github\study_python\Kwonhee\파이썬 데이터 분석 입문\csv"
output_file = "D:\OneDrive\Github\study_python\Kwonhee\파이썬 데이터 분석 입문\csv\output_10.csv"

output_header_list = ['file_name', 'total_sales', 'average_sales']

csv_out_file = open(output_file, 'a', newline='')
filewriter = csv.writer(csv_out_file)
filewriter.writerow(output_header_list)

for input_file in glob.glob(os.path.join(input_path,'sales_*')):
	with open(input_file, 'r', newline='') as csv_in_file:
		filereader = csv.reader(csv_in_file)
		output_list = [ ]
		output_list.append(os.path.basename(input_file))
		header = next(filereader)
		total_sales = 0.0
		number_of_sales = 0.0
		for row in filereader:
			sale_amount = row[3]
			total_sales += float(str(sale_amount).strip('$').replace(',',''))
			number_of_sales += 1.0
		average_sales = '{0:.2f}'.format(total_sales / number_of_sales)
		output_list.append(total_sales)
		output_list.append(average_sales)
		filewriter.writerow(output_list)
csv_out_file.close()
