#!/usr/bin/env python3
import sys
from xlrd import open_workbook

input_file = "D:\OneDrive\Github\study_python\Kwonhee\파이썬 데이터 분석 입문\excel\sales_2013.xlsx"

workbook = open_workbook(input_file)
print('Number of worksheets:', workbook.nsheets)
for worksheet in workbook.sheets():
	print("Worksheet name:", worksheet.name, "\tRows:", \
			worksheet.nrows, "\tColumns:", worksheet.ncols)
