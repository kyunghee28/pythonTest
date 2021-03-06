import numpy as np
import pandas as pd
import pythonTest.day0408.bitutil

df = pythonTest.day0408.bitutil.getMovies()

# 연습 ) 성별별로 별점의 평균을 알고 싶어요
#   오라클                                             ==>    pandas
# select gender, avg(rating) from df group by gender    ==> pivot_table (~별로)

# help(pd.DataFrame.pivot_table)
# pivot_table(self, values=None, index=None, columns=None, aggfunc='mean', fill_value=None,
# index => group by gender
# values => rating
# aggfunc ==> values 에서 어떤 함수를 적용할 껀지
# fill_value ==> null인 경우 어떤 데이터로 채울까?

gender_mean = df.pivot_table(values='rating', index='gender')
# print(gender_mean)
'''
          rating
gender          
F       3.620366
M       3.568879
'''

gender_mean2 = df.pivot_table(values='rating', index='gender',aggfunc='mean')
# print(gender_mean2)
'''
gender          
F       3.620366
M       3.568879
'''

gender_sum = df.pivot_table(values='rating', index='gender',aggfunc='sum')
# print(gender_sum)
'''
         rating
gender         
F        892203
M       2690110
'''
gender_max = df.pivot_table(values='rating', index='gender',aggfunc='max')
# print(gender_max)
'''
        rating
gender        
F            5
M            5
'''
gender_min = df.pivot_table(values='rating', index='gender',aggfunc='min')
# print(gender_min)
'''
        rating
gender        
F            1
M            1
'''

# 연습 ) 나이별로 별점의 평균을 구하세요
#   오라클                                             ==>    pandas
# select age, avg(rating) from df group by age    ==> pivot_table (~별로)

age_mean = df.pivot_table(values='rating', index='age',aggfunc='mean')
# print(age_mean)
'''
       rating
age          
1    3.549520
18   3.507573
25   3.545235
35   3.618162
45   3.638062
50   3.714512
56   3.766632
'''

# 연습 ) 성별,나이별로 별점(rating)의 평균을 구하세요
'''
age       M        F  
1    3.549520  3.549520
    ...
이런식으로 출력되도록 
'''

# help(pd.DataFrame.pivot_table)

age_mean_gender = df.pivot_table(values='rating', index='age',columns='gender', aggfunc='mean')
# print(type(age_mean_gender))    #<class 'pandas.core.frame.DataFrame'>

gender_mean_age = df.pivot_table(values='rating', index='gender',columns='age', aggfunc='mean')
# print(gender_mean_age)


# 연습 ) 성별,나이별로 별점(rating)의 평균을 시각화
import matplotlib.pyplot as plt

r = df.pivot_table(values='rating', index='age',columns='gender', aggfunc='mean')
# print(r)
'''
gender         F         M
age
1       3.616291  3.517461
18      3.453145  3.525476
25      3.606700  3.526780
35      3.659653  3.604434
45      3.663044  3.627942
50      3.797110  3.687098
56      3.915534  3.720327
'''
# print(type(r))    #<class 'pandas.core.frame.DataFrame'>

# 행의 이름 설정
r.index = ['unber 18','18-24','25-34','35-44','45-49','50-55','56+']
# print(r)
'''
gender           F         M
unber 18  3.616291  3.517461
18-24     3.453145  3.525476
25-34     3.606700  3.526780
35-44     3.659653  3.604434
45-49     3.663044  3.627942
50-55     3.797110  3.687098
56+       3.915534  3.720327
'''
r.plot(kind='bar')
# plt.show()

# r = df.pivot_table(values='rating', index='gender', aggfunc='mean')
# print(r)
#
# r2 = df.pivot_table(values='rating', index='gender', aggfunc='mean', columns='age')
# print(r2)
#
# r3 = df.pivot_table(values='rating', index=['age','gender'],  aggfunc='mean')
# print(r3)
#
# r4 = df.pivot_table(values='rating', index=['gender','age'],  aggfunc='mean')
# print(r4)

# 연습 ) 직업별, 성별,나이대별 평균평점을 알려주세요, 단, 결측치는 0으로 채워주세요
r = df.pivot_table(values='rating', index=['gender','age'], columns='job', aggfunc='mean')
# print(r)

# print("--"*10,"결측치를 0으로 - 1. ","--"*20)
r_mean = df.pivot_table(values='rating', index=['gender','age'], columns='job', aggfunc='mean', fill_value=0)
# print(r_mean)

# print("--"*10,"결측치를 0으로 - 2. ","--"*20)
r_mean2 = df.pivot_table(values='rating', index=['job','age'], columns='gender', aggfunc='mean', fill_value=0)
# print(r_mean2)

# print("--"*10,"결측치를 0으로 - 3. ","--"*20)
r_mean3 = df.pivot_table(values='rating', index=['age','job'], columns='gender', aggfunc='mean', fill_value=0)
# print(r_mean3)

# pivot_table 시에 어떤것을 index로 하고 어떤것을 columns으로 하는지에 대한 제약은 없지만
# 항목의 수가 많은 것을 columns으로 두는 것이 읽기가 쉬운것 같다.


# unstack() : index를 columns으로 바꿔준다.
m = df.pivot_table(values='rating', index='age', columns='gender', aggfunc='mean')
# print(m)
'''
gender         F         M
age                       
1       3.616291  3.517461
18      3.453145  3.525476
25      3.606700  3.526780
35      3.659653  3.604434
45      3.663044  3.627942
50      3.797110  3.687098
56      3.915534  3.720327
'''
m2 = m.unstack()
print(m2)
