#!/usr/bin/env python3
import glob
import os
import sys
from datetime import date
from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook

input_folder = "D:/kwonhee/OneDrive/Github/study_python/Kwonhee/파이썬 데이터 분석 입문/excel"
output_file = "D:/kwonhee/OneDrive/Github/study_python/Kwonhee/파이썬 데이터 분석 입문/excel/14output.xls"

output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('sums_and_averages')

all_data = []
sales_column_index = 3

header = ['workbook', 'worksheet', 'worksheet_total', 'worksheet_average',\
 					'workbook_total', 'workbook_average']
all_data.append(header)

for input_file in glob.glob(os.path.join(input_folder, '*.xlsx')):
	with open_workbook(input_file) as workbook:
		list_of_totals = []
		list_of_numbers = []
		workbook_output = []
		for worksheet in workbook.sheets():
			total_sales = 0
			number_of_sales = 0
			worksheet_list = []
			worksheet_list.append(os.path.basename(input_file))
			print(worksheet_list)
			worksheet_list.append(worksheet.name)
			print(worksheet_list)
			for row_index in range(1,worksheet.nrows):
				try:
					total_sales += float(str(worksheet.cell_value(row_index,sales_column_index)).strip('$').replace(',',''))
					number_of_sales += 1.
				except:
					total_sales += 0.
					number_of_sales += 0.
				print(total_sales)
			average_sales = '%.2f' % (total_sales / number_of_sales)
			worksheet_list.append(total_sales)
			print(worksheet_list)
			worksheet_list.append(float(average_sales))
			print(worksheet_list)
			list_of_totals.append(total_sales)
			list_of_numbers.append(float(number_of_sales))
			print(list_of_numbers)
			workbook_output.append(worksheet_list)
		workbook_total = sum(list_of_totals)
		workbook_average = sum(list_of_totals)/sum(list_of_numbers)
		for list_element in workbook_output:
			list_element.append(workbook_total)
			list_element.append(workbook_average)
			print('list_element:', list_element)
			print('workbook_total:', workbook_total)
			print('workbook_output:', workbook_output)
		print(workbook_output)
		all_data.extend(workbook_output)
		print(all_data)

for list_index, output_list in enumerate(all_data):
	print('print #1:', list_index, output_list)
	for element_index, element in enumerate(output_list):
		print('print #2:', element_index, element)
		output_worksheet.write(list_index, element_index, element)

output_workbook.save(output_file)
