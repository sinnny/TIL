# 판다스 연습 문제

run my_modules
df1 = pd.read_csv("../data/cancer_test.csv")
df1.columns
df1.dtypes

df1.head()
df1.info()
df1.describe()

# 1. radius_mean, texture_mean, texture_se, smoothness_se
# NA인 행을 제거한 후 총 행의 수 리턴 

df1['radius_mean'].isnull().sum()       # NA => 4
df1['texture_mean'].isnull().sum()
df1['texture_se'].isnull().sum()
df1['smoothness_se'].isnull().sum()

vbool = df1['radius_mean'].isnull() & df1['texture_mean'].isnull() & df1['texture_se'].isnull() & df1['smoothness_se'].isnull()
vbool.sum() # 칼럼 4개가 모두 NA인 행의 수

df1
df1.loc[vbool,:]    # 컬럼 4개가 모두 NA인 행 확인

df1.shape  #(569,32)
df1.shape[0]    # 행의 개수  --> 569
df1.shape[1]    # 열의 개수 --> 32

df1.shape[0] - vbool.sum()  # 565 --> not null 행 수


print(df1.shape[0] - vbool.sum())

df1.dropna(subset=['radius_mean', 'texture_mean', 'texture_se', 'smoothness_se'], how='all')
nrow = df1.dropna(subset=['radius_mean', 'texture_mean', 'texture_se', 'smoothness_se'], how='all').shape[0]
nrow


# 2. concavity_mean의 standard scaling(표준화) 후, 결과가 0,1 이상인 값의 개수 출력
# standard scaling(표준화) = (연 데이터 - 평균) / 표준편차
# ㅡminmax scaling = (원 데이터 - 최소) / (최대 - 최소)


df1.columns
(df1['concavity_mean'] - df1['concavity_mean'].mean()) / df1['concavity_mean']
'''
0      0.704101
1     -0.021856
2      0.550155
3      0.632149
4      0.551519
  
564    0.635919
565    0.383338
566    0.040111
567    0.747298
568        -inf
Name: concavity_mean, Length: 569, dtype: float64'''

vscale = (df1['concavity_mean']-df1['concavity_mean'].mean())/df1['concavity_mean']
(vscale > 0.1).sum()

# 이상치 건 수 확인
# 3. texture_se의 상위 10% 값 (NA를 제외한 건수의 10%)을 이상치로 가정한다.
#   10% 제외한 값의 최대값으로 수정한 후 평균을 소수점 둘째자리로 반올림하여 출력

# 이상치 건수 확인
df1['texture_se'].dropna()
'''
0      0.9053
1      0.7339
2      0.7869
3      1.1560
4      0.7813
 
564    1.2560
565    2.4630
566    1.0750
567    1.5950
568    1.4280
Name: texture_se, Length: 565, dtype: float64'''

df1['texture_se'].shape     # (569,)
df1['texture_se'].dropna().shape   #  (565,)

df1['texture_se'].dropna().shape[0]   #565
nx = int(np.trunc(df1['texture_se'].dropna().shape[0] * 0.1))
type(nx)
nx


np.trunc?
[참고]
 a = np.array([-1.7, -1.5, -0.2, 0.2, 1.5, 1.7, 2.0])
np.trunc(a)
# Out[208]: array([-1., -1., -0.,  0.,  1.,  1.,  2.])


a = np.array([-1.7, -1.5, -0.2, 0.2, 1.5, 1.7, 2.0])




# 참고 

_df = pd.DataFrame(
    {'name': ['KIM', 'LEE', 'SMITH','BROWN', 'MILLER'],
     'age': [24, 32, 43, 24, np.nan]})

'''
     name   age
0     KIM  24.0
1     LEE  32.0
2   SMITH  43.0
3   BROWN  24.0
4  MILLER   NaN

'''

# 동점자 처리 기준 5가지

_df['rank_average'] = _df['age'].rank(method='average')
_df['rank_min'] = _df['age'].rank(method='min')
'''
0    1.0
1    3.0
2    4.0
3    1.0
4    NaN'''

_df['rank_max'] = _df['age'].rank(method='max')
'''
0    2.0
1    3.0
2    4.0
3    2.0
4    NaN
Name: age, dtype: float64'''

-df['rank_first'] = _df['age'].rank(method='first')
'''
0    1.0
1    3.0
2    4.0
3    2.0
4    NaN
Name: age, dtype: float64'''

df['rank_dense'] = _df['age'].rank(method='dense')
'''0    1.0
1    2.0
2    3.0
3    1.0
4    NaN
Name: age, dtype: float64'''
# dense는 min과 유사, 그룹 간 순위가 1씩 증가하는게 차이

_df['age'].rank(method='first', ascending=False)
'''
0    3.0
1    2.0
2    1.0
3    4.0
4    NaN
Name: age, dtype: float64'''




# 이상치를 제외한 나머지 >> 평균 
df1['texture_se'].rank(ascending = False, method='first')
vrank = df1['texture_se'].rank(ascending = False, method='first')
'''
0      393.0
1      474.0
2      448.0
3      265.0
4      451.0
 
564    221.0
565     19.0
566    292.0
567    107.0
568    159.0
Name: texture_se, Length: 569, dtype: float64'''


df1.loc[vrank > nx, 'texture_se']   # 정상치 데이터
vmax = df1.loc[vrank > nx, 'texture_se'].max()  # 정상치 데이터 최대값
   

df1.loc[vrank <= nx, 'texture_se']   # 이상치 데이터
df1.loc[~(vrank > nx), 'texture_se']
df1['texture_se'].sort_values(ascending=False)[:nx]   

# 이상치 데이터를 vmax(정상치 데이터의 최댓값)로 치환
df1.loc[vrank <= nx, 'texture_se'] = vmax
df1.isnull

round(df1['texture_se'].mean(), 2)





# 4. Symmetry_mean의 결측치를 최소값으로 수정한 후 평균을 소수점 둘째자리로 반올림하여 출력하시오

df1['symmetry_mean'].min()  # '-', 문자열 존재

from numpy import nan as NA

df1['symmetry_mean'].replace('-', NA)
df1['symmetry_mean'] = df1['symmetry_mean'].replace('-', NA)
df1['symmetry_mean'] = df1['symmetry_mean'].replace('.', NA)
df1['symmetry_mean'] = df1['symmetry_mean'].replace('pass', NA)
df1['symmetry_mean'] = df1['symmetry_mean'].replace('<=', NA)
df1['symmetry_mean'] = df1['symmetry_mean'].astype('float')


# 최소값 확인
vmin = df1['symmetry_mean'].min()  # 0.106

# 결측치 수정
df1['symmetry_mean'].fillna(vmin)
df1['symmetry_mean'] = df1['symmetry_mean'].fillna(vmin)

# 평균 확인
print(round(df1['symmetry_mean'].mean(), 2))   # 0.18














