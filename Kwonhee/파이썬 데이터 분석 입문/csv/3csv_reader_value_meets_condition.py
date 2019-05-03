#!/usr/bin/env python3
import csv
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file, 'r', newline='') as csv_in_file:
	with open(output_file, 'w', newline='') as csv_out_file:
		filereader = csv.reader(csv_in_file)
		filewriter = csv.writer(csv_out_file)
		header = next(filereader)
		filewriter.writerow(header)
		for row_list in filereader:
			supplier = str(row_list[0]).strip()
			cost = str(row_list[3]).strip('$').replace(',', '')
			# 아직까지는 cost는 문자
			if supplier == 'Supplier Z' or float(cost) > 600.0:
				filewriter.writerow(row_list)

# python 3csv_reader_value_meets_condition.py supplier_data_with_comma.csv output_03.csv

# 여기서는 ,으로 구분된 숫자들을 제대로 읽어서 변환하는구나... 2번 파일은 그럼 표기만 오류인건가?
