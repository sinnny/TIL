import matplotlib.pyplot as plt
plt.plot([10,20,30,40])
plt.show()
plt.plot([1,2,3,4,],[10,23,34,45])
plt.show()
plt.title('multi_king!')
plt.plot([1,2,3,4,],[10,23,34,45], label = 'asc')
plt.plot([40,50,20,10], label ='desc')
plt.legend()
plt.show()
plt.title('multi_king!')
plt.plot([1,2,3,4,],[10,23,34,45], color='green', label = 'asc')
plt.plot([1,2,3,4,],[40,50,20,10], 'pink', label ='desc')
plt.legend()
plt.show()
plt.title('marker')
plt.plot([1,2,3,4,],[10,23,34,45], 'r.', label = 'circle')
plt.plot([1,2,3,4,],[40,50,20,10], 'b^', label ='triangle_up')
plt.legend()
plt.show()
## 데이터 읽어 최고 기온 데이터 출력하기
import csv
f = open("/Users/shinhee/Desktop/bigdata/multicampus/data/seoul_book.csv", encoding='cp949')
data = csv.reader(f)
result = []
next(data)
for row in data: 
    print(row[-1])
import csv
import matplotlib as ply

f = open("/Users/shinhee/Desktop/bigdata/multicampus/data/seoul_book.csv", encoding='cp949')
data = csv.reader(f)
next(data)
result = []

for row in data: 
    if row[-1] !='':
        result.append(float(row[-1]))
        
print(result)
plt.plot(result, 'b')
plt.show()
#### [참고]

s= 'hello python'
print(s.split())
date = '2021-12-28'
type(date)
print(date.split('-'))
print(date.split('-')[0])
print(date.split('-')[1])
print(date.split('-')[2])
a = date.split('-')
a
print(a[0])
print(a[1])
print(a[2])
#### 주어진 데이터에서 8월의 최고 기온 데이터 시각화 하기
for row in data:
    if row[-1] !='' :
        if row[0].split =='08':
            result.append(float(row[-1]))
plt.plot(result, 'b')
plt.show()
# 내 생일 최고 기온 데이터 시각화하기

for row in data:
    if row[-1] !='':
        if row[0].split('-')[1] == '10' and row[0].split('-')[2] == '26':
            result.append(float(row[-1]))
plt.plot(result, 'hotpink')
plt.show()
## 한글 폰트 사용 (my_modules에  copy _ paste 하세요)

plt.rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False  # 한글폰트 사용시 = 부호 표시하기 
plt.title('닥터윌 탄신일 기온 그래프')

plt.plot(result, 'hotpink')
plt.show()
