#!/usr/bin/env python3
import pandas as pd
import glob
import os
import sys

input_path = r"D:\OneDrive\Github\study_python\Kwonhee\파이썬 데이터 분석 입문\csv"
output_file = r"D:\OneDrive\Github\study_python\Kwonhee\파이썬 데이터 분석 입문\csv\pandas_output.csv"

all_files = glob.glob(os.path.join(input_path,'sales_*'))

all_data_frames = []
for file in all_files:
	data_frame = pd.read_csv(file, index_col=None)
	all_data_frames.append(data_frame)
data_frame_concat = pd.concat(all_data_frames, axis=0, ignore_index=True)

data_frame_concat.to_csv(output_file, index = False)
