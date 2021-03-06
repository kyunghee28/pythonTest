# 합치고자 하는 두개의 파일에 데이터 수가 일치하지 않아요
# dan 학생의 점수정보는 없다.

import numpy as np
import pandas as pd

# 서로 일치하지 않는 데이터 dan의 정보도 나타내 봅니다.
# 			그 학생의 정보는 0으로 출력합니다.
# help(pd.merge)

df1 = pd.read_csv('../data/stu01', sep="::", engine='python')
df2 = pd.read_csv('../data/stu02', sep="::", engine='python')

df = pd.merge(df1,df2, how="outer")
'''
      name    kor   eng   mat   bio  class  age
0     adam   67.0  87.0  90.0  98.0      1   27
1   andrew   45.0  45.0  56.0  98.0      1   25
2      ben   95.0  59.0  96.0  88.0      1   24
3    clark   65.0  94.0  89.0  98.0      1   26
4     noel   78.0  76.0  98.0  89.0      1   28
5     paul   87.0  67.0  65.0  56.0      2   55
6   walter   89.0  98.0  78.0  78.0      2   29
7    oscar  100.0  78.0  56.0  65.0      2   20
8   martin   99.0  89.0  87.0  87.0      2   29
9     hugh   98.0  45.0  56.0  54.0      2   28
10   henry   65.0  89.0  87.0  78.0      2   25
11     dan    NaN   NaN   NaN   NaN      1   45
'''
df.fillna(0, inplace=True)    # 결측치를 0으로 채워줘!

print(df)

