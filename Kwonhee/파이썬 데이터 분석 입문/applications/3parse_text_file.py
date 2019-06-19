#!/usr/bin/env python3
import sys

input_file = "D:/Kwonhee/OneDrive/Github/study_python/Kwonhee/파이썬 데이터 분석 입문/applications/mysql_server_error_log.txt"
output_file = "D:/Kwonhee/OneDrive/Github/study_python/Kwonhee/파이썬 데이터 분석 입문/applications/output_files/3output.csv"

messages = {} # 딕셔너리
notes = [] # 리스트
with open(input_file, 'r', newline='') as text_file:
	for row in text_file:
		if '[Note]' in row:
			row_list = row.split(' ', 4)
			day = row_list[0].strip()
			note = row_list[4].strip('\n').strip()
			if note not in notes:
				notes.append(note) # 동일한 로그 리스트에 채우기
			if day not in messages:
				messages[day] = {}
			if note not in messages[day]:
				messages[day][note] = 1
			else:
				messages[day][note] += 1

filewriter = open(output_file, 'w', newline='')
header = ['Date']
header.extend(notes)
header = ','.join(map(str,header)) + '\n'
print(header)
filewriter.write(header)
print(messages)
for day, day_value in messages.items():
	row_of_output = []
	row_of_output.append(day)
	for index in range(len(notes)):
		if notes[index] in day_value.keys():
			row_of_output.append(day_value[notes[index]])
			print(day)
			print(day_value)
			print(notes[index])
			print(day_value[notes[index]])
		else:
			row_of_output.append(0)
	output = ','.join(map(str,row_of_output)) + '\n'
	print(output)
	filewriter.write(output)
filewriter.close()
