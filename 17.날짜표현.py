
# 17. 날짜 표현
# 월별, 일별, 요일별 집계
# 현재 날짜 - 입사일자 = 근무 일자

# 현재 날짜
run my_modules

from datetime import datetime
datetime.now()
# Out[4]: datetime.datetime(2021, 12, 29, 11, 25, 49, 240148)

d1 = datetime.now()
type(d1)
# Out[7]: datetime.datetime

datetime(year, month, day)
d1.year     # 연
df.month    # 월
d1.day      # 일

# 2. 날짜 피상
d2 = '2022/01/01'

d2.year
# AttributeError: 'str' object has no attribute 'year'

# datetime.strptime(date_string, format)
# 벡터 연산이 안됨

datetime.strptime(d2, '%Y/%m/%d')
# Out[16]: datetime.datetime(2022, 1, 1, 0, 0)

datetime.strptime('09/12/25', '%m/%d/%y')  # 2025년 09월 12일 해석
# Out[17]: datetime.datetime(2025, 9, 12, 0, 0)

# Series 벡터 연산 불
# 해결방안 : map()
s1 = Series(['2022/01/01', '2022/01/02', '2022/01/03'])
'''
0    2022/01/01
1    2022/01/02
2    2022/01/03
dtype: object'''
datetime.strptime(s1, '%Y/%m/%d')
# TypeError: strptime() argument 1 must be str, not Series

s1.map(lambda x: datetime.strptime(x,'%Y/%m/%d'))
'''
0   2022-01-01
1   2022-01-02
2   2022-01-03
dtype: datetime64[ns]'''


# 2) pd.to_datetime
# 벡터 연산가능
s1
pd.to_datetime(s1)
'''
0   2022-01-01
1   2022-01-02
2   2022-01-03
dtype: datetime64[ns]'''

s2 = pd.to_datetime(s1)
pd.to_datetime(s2, format='%Y/%m/%d')
'''
0   2022-01-01
1   2022-01-02
2   2022-01-03
dtype: datetime64[ns]'''


# 3) 날짜 포맷 변경 datetime.strftime(string format time)
# 요일 추출 (날짜에서 요일을 return 하도록 날짜 출력 형식 변경)
# *(연/월/일)  -->  (월/일/연) 순서로 변경
# (주의) 날짜 포맷 변경한 후 return 데이터 타입은 무조건 문자라는 사실!!!


d1 = datetime.now()
d1
datetime.strftime(d1, '%A') #요일리턴
# Out[30]: 'Wednesday'
datetime.strftime(d1, '%m-%d,%Y')
# Out[31]: '12-29,2021'


# 4) 날짜 연산 ***
d1          # 현재날짜
d1 + 100    # 안 됨

# 오늘 날짜로부터 100일 뒤 날짜 리턴 불가 (타입이 틀림)
TypeError: unsupported operand type(s) for +: 'datetime.datetime' and 'int'


# 1) offset

from pandas.tseries.offsets import Day, Hour, Second
d1 + Day(100)
# Out[39]: Timestamp('2022-04-08 11:42:54.862048')

# 2) timedelta(날짜와의 차이)

from datetime import timedelta

d1 + timedelta(100)
# Out[42]: datetime.datetime(2022, 4, 8, 11, 42, 54, 862048)
# 오늘 일자부터 100일 뒤 리턴해줌


# 3) (실무용) DateOffset ***(추천)
d1 + pd.DateOffset(months = 4)
# Timestamp('2022-04-29 11:42:54.862048')

# 5. 날짜 - 날짜
d1 - datetime.strptime(d2, '%Y/%m/%d')
# Out[46]: datetime.timedelta(days=-3, seconds=42174, microseconds=862048)
d3 = d1 - datetime.strptime(d2, '%Y/%m/%d')

d3.days
d2.seconds


# [연습문제]
# 요일별 통화건수 총합

deli = pd.read_csv('../data/delivery.csv', encoding = 'cp949')
deli
deli.dtypes
'''
일자       int64
시간대      int64
업종      object
시도      object
시군구     object
읍면동     object
통화건수     int64
dtype: object
'''

deli.head()
deli.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 119189 entries, 0 to 119188
Data columns (total 7 columns):
 #   Column  Non-Null Count   Dtype 
---  ------  --------------   ----- 
 0   일자      119189 non-null  int64 
 1   시간대     119189 non-null  int64 
 2   업종      119189 non-null  object
 3   시도      119189 non-null  object
 4   시군구     119189 non-null  object
 5   읍면동     119189 non-null  object
 6   통화건수    119189 non-null  int64 
dtypes: int64(3), object(4)
memory usage: 6.4+ MB'''

deli.describe()
'''
                 일자            시간대           통화건수
count  1.191890e+05  119189.000000  119189.000000
mean   2.018021e+07      15.576362       9.916486
std    8.234111e+00       5.321848      13.904536
min    2.018020e+07       0.000000       5.000000
25%    2.018021e+07      13.000000       5.000000
50%    2.018021e+07      17.000000       5.000000
75%    2.018022e+07      19.000000       7.000000
max    2.018023e+07      23.000000     229.000000'''


deli.boxplot()



# 날짜 파싱
deli
deli['일자']
type(deli['일자'])
# Out[71]: pandas.core.series.Series

pd.to_datetime(deli['일자'])
'''
0        1970-01-01 00:00:00.020180201
1        1970-01-01 00:00:00.020180201
2        1970-01-01 00:00:00.020180201
3        1970-01-01 00:00:00.020180201
4        1970-01-01 00:00:00.020180201
            
119184   1970-01-01 00:00:00.020180228
119185   1970-01-01 00:00:00.020180228
119186   1970-01-01 00:00:00.020180228
119187   1970-01-01 00:00:00.020180228
119188   1970-01-01 00:00:00.020180228
Name: 일자, Length: 119189, dtype: datetime64[ns]'''


pd.to_datetime(deli['일자'], format = '%Y/%m/%d')
deli['일자'] = pd.to_datetime(deli['일자'], format = '%Y/%m/%d')

# 요일 리턴
datetime.strftime(deli['일자'], '%A')
# descriptor 'strftime' for 'datetime.date' objects doesn't apply to a 'Series' object

deli['일자'].map(lambda x : datetime.strftime(x, '%A'))
'''
0         Thursday
1         Thursday
2         Thursday
3         Thursday
4         Thursday
  
119184    Thursday
119185    Thursday
119186    Thursday
119187    Thursday
119188    Thursday
Name: 일자, Length: 119189, dtype: object'''
deli['요일'] = deli['일자'].map(lambda x : datetime.strftime(x, '%A'))
deli

# 일자별로 그룹화
deli.groupby('일자')['통화건수'].sum()


total = deli.groupby('요일')['통화건수'].sum()
total[['Monday', 'Tjesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'] ]
# 월화수목금토 순으로 재배치 해야함
# 아직까지도 정렬로 배치 안됨, 색인으로 처리해야함
