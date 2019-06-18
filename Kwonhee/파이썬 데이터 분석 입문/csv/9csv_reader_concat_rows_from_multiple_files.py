#!/usr/bin/env python3
import csv
import glob
import os
import sys

input_path = "D:\OneDrive\Github\study_python\Kwonhee\파이썬 데이터 분석 입문\csv"
output_file = "D:\OneDrive\Github\study_python\Kwonhee\파이썬 데이터 분석 입문\csv\output_9.csv"

first_file = True
for input_file in glob.glob(os.path.join(input_path,'sales_*')):
	print(os.path.basename(input_file))
	with open(input_file, 'r', newline='') as csv_in_file:
		with open(output_file, 'a', newline='') as csv_out_file:
			filereader = csv.reader(csv_in_file)
			filewriter = csv.writer(csv_out_file)
			if first_file: # first_file이 True면
				for row in filereader:
					filewriter.writerow(row)
				first_file = False
			else:
				header = next(filereader)
				for row in filereader:
					filewriter.writerow(row)
