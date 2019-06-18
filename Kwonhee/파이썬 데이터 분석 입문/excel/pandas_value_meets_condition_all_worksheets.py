#!/usr/bin/env python3
import pandas as pd
import sys

input_file = "D:/kwonhee/OneDrive/Github/study_python/Kwonhee/파이썬 데이터 분석 입문/excel/sales_2013.xlsx"
output_file = "D:/kwonhee/OneDrive/Github/study_python/Kwonhee/파이썬 데이터 분석 입문/excel/pandas_output.xls"

data_frame = pd.read_excel(input_file, sheetname=None, index_col=None)

row_output = []
print(data_frame)
print(data_frame.items())
for worksheet_name, data in data_frame.items():
	row_output.append(data[data['Sale Amount'].replace('$', '').replace(',', '').astype(float) > 2000.0])
filtered_rows = pd.concat(row_output, axis=0, ignore_index=True)

writer = pd.ExcelWriter(output_file)
filtered_rows.to_excel(writer, sheet_name='sale_amount_gt2000', index=False)
writer.save()
