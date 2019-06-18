#!/usr/bin/env python3
import pandas as pd
import sys

input_file = "D:/kwonhee/OneDrive/Github/study_python/Kwonhee/파이썬 데이터 분석 입문/excel/sales_2013.xlsx"
output_file = "D:/kwonhee/OneDrive/Github/study_python/Kwonhee/파이썬 데이터 분석 입문/excel/pandas_output.xls"


data_frame = pd.read_excel(input_file, sheetname=None, index_col=None)

column_output = []
for worksheet_name, data in data_frame.items():
	column_output.append(data.loc[:, ['Customer Name', 'Sale Amount']])
print(column_output)
selected_columns = pd.concat(column_output, axis=0, ignore_index=True)
print(selected_columns)

writer = pd.ExcelWriter(output_file)
selected_columns.to_excel(writer, sheet_name='selected_columns_all_worksheets', index=False)
writer.save()
