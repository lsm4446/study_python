#!/usr/bin/env python3
import csv
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file, 'r', newline='') as csv_in_file:
	with open(output_file, 'w', newline='') as csv_out_file:
		filereader = csv.reader(csv_in_file, delimiter=',')
		filewriter = csv.writer(csv_out_file, delimiter='\t')
		for row_list in filereader:
			print(row_list)
			filewriter.writerow(row_list)


# delimiter는 기본값, 입력하지 않아도 된다. 만약 세미콜론(;)이나 탭(\t)으로 구분된 입력파일을 읽고 싶으면 입력. 즉, csv 모듈은 csv 외에 다른 형태도 읽을 수 있다는 것. 이번에는 \t으로 변환하여 출력

# 교재에서는 이 경우 ,가 포함된 자료를 구분한다고 하였으나 실제로는 전혀 그렇지 않았다.

# python 2csv_reader_parsing_and_write.py supplier_data_with_comma.csv pandas_output.csv
