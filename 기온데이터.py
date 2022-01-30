import csv
data = csv.reader(f, delimiter=',')
for row in data:
    print(row)
f.close()
['\t\t지점번호', '지점명', '일시', '평균기온(℃)', '평균최고기온(℃)', '최고기온(℃)', '\t최고기온일자', '평균최저기온(℃)', '최저기온(℃)', '최저기온일자']
['\t\t108', '서울', '2008-01', '-1.7', '1.9', '7.3', '2008-01-06', '-5.0', '-11.1', '2008-01-17']
# import csv
# f = open('/Users/shinhee/Desktop/bigdata/multicampus/data/seoul.csv', 'r', encoding='cp949')
# data = csv.reader(f, delimiter=',')
# for row in data:
#     print(row)
# f.close()
# # 데이터에서 최고 기온을 실수로 변환, 한 행씩 출력

# import csv
# f = open('/Users/shinhee/Desktop/bigdata/multicampus/data/seoul.csv', 'r', encoding='cp949')
# data = csv.reader(f, delimiter=',')
# header = next(data)
# # print(header)
# for row in data:
#     row[5] = float(row[5]) # 최고 기온을 실수로 변환
#     print(row)
# f.close()
import csv
f = open('/Users/shinhee/Desktop/bigdata/multicampus/data/seoul_1.csv', 'r', encoding='cp949')
data = csv.reader(f)

# 초기화
max_temp = -999
max_date = ''
header = next(data

#print(header)
for row in data:
# 1. 누락된 데이터 처리
    if row[5] == '':
        row[5] = -999
    row[5] = float(row[5]) # 문자를 실수형 변경
    
    # 2. 비교해서 최고 기온 찾아서, 최고 기온과 해당되는 일자를 출력
    if max_temp<row[5]:
        max_temp = row[5]
        max_date = row[6]
        

f.close()





import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
# 최고 기온과 최고 기온이었던 날짜를 찾으세요.
data = pd.read_csv('/Users/shinhee/Desktop/bigdata/multicampus/data/seoul_1.csv', encoding='cp949')
data
data.info()
data.isnull()
data1 = data[['\t최고기온일자', '최고기온(℃)']]
data1
data_asc = data1.sort_values('최고기온(℃)', ascending = False)
data_asc
data_asc.iloc[1]
data_asc.iloc[1]
