#!/usr/bin/env python3
import pandas as pd
import glob
import os
import sys

input_path = "D:/kwonhee/OneDrive/Github/study_python/Kwonhee/파이썬 데이터 분석 입문/excel"
output_file = "D:/kwonhee/OneDrive/Github/study_python/Kwonhee/파이썬 데이터 분석 입문/excel/pandas_output.xls"

all_workbooks = glob.glob(os.path.join(input_path,'*.xlsx'))
data_frames = []
for workbook in all_workbooks:
	all_worksheets = pd.read_excel(workbook, sheetname=None, index_col=None)
	for worksheet_name, data in all_worksheets.items():
		data_frames.append(data)
all_data_concatenated = pd.concat(data_frames, axis=0, ignore_index=True)

writer = pd.ExcelWriter(output_file)
all_data_concatenated.to_excel(writer, sheet_name='all_data_all_workbooks', index=False)
writer.save()
