#!/usr/bin/env python3
import csv
import glob
import os
import sys

input_path = "D:\OneDrive\Github\study_python\Kwonhee\파이썬 데이터 분석 입문\csv"

file_counter = 0
for input_file in glob.glob(os.path.join(input_path,'sales_*')):
	row_counter = 1
	with open(input_file, 'r', newline='') as csv_in_file:
		filereader = csv.reader(csv_in_file)
		header = next(filereader)
		for row in filereader:
			row_counter += 1
	print('{0!s}: \t{1:d} rows \t{2:d} columns'.format(\
	os.path.basename(input_file), row_counter, len(header)))
	file_counter += 1
print('Number of files: {0:d}'.format(file_counter))
