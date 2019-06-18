#!/usr/bin/env python3
import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_csv(input_file, header=None)

data_frame = data_frame.drop([0,1,2,16,17,18])
data_frame.columns = data_frame.iloc[0]
data_frame = data_frame.reindex(data_frame.index.drop(3))
# 인덱스는 원래 처음 테이블의 인덱스를 그대로 따라간다. 아래 index=True를 통해 인덱스 값을 확인할 수 있다.
data_frame.to_csv(output_file, index=True)

# python pandas_select_contiguous_rows.py supplier_data_unnecessary_header_footer.csv pandas_output.csv
