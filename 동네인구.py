import csv

f=open("../data/age.csv", encoding='cp949')
data=csv.reader(f)
result=[]

for row in data:
    if '신도림' in row[0]:
        for i in row[3:]:
            result.append(int(i))

print(result)
print('신도림' in '서울특별시 구로구 신도림동(1153051000)')
import matplotlib.pyplot as plt

plt.style.use('ggplot')
plt.plot(result)
plt.show()

import csv

f=open("../data/age.csv", encoding='cp949')
data=csv.reader(f)
result=[]

for row in data:
    if '신도림' in row[0]:
        for i in row[3:]:
            result.append(int(i))

print(result)

plt.bar(range(101), result)
plt.show()

# 자동화 프로그램 만들기

import csv
import matplotlib.pyplot as plt

f=open("../data/age.csv", encoding='cp949')
data=csv.reader(f)
result=[]

name = input('인구 구조가 알고 싶나요? 알고 싶은 지역의 이름(읍명동 단위) 입력해주세요')

for row in data:
    if name in row[0]:
        for i in row[3:]:
            result.append(int(i))

print(result)


plt.style.use('ggplot')
plt.rc('font', family='AppleGothic')
plt.title(name + "지역 인구 구조 현황")
plt.plot(result)
plt.show()


import matplotlib.pyplot as plt
plt.bar([0,1,2,4,6,10], [1,2,3,5,6,7])
plt.show()
plt.barh(range(5),result)
plt.show()
# gender(성별) 인구구조_항아리 모형 그리기
import csv
f=open("../data/gender.csv", encoding='cp949')
data= csv.reader(f)

m=[]
f=[]

for row in data:
    if '신도림' in row[0]:
        for i in range(0,101):
            m.append(int(row[i+3]))
            f.append(int(row[-(i+3)]))
f.reverse()

print(m)
print(f)
# gender(성별) 인구구조_항아리 모형 그리기
import csv
f=open("../data/gender.csv", encoding='cp949')
data= csv.reader(f)

m=[]
f=[]

for row in data:
    if '신도림' in row[0]:
        for i in row[3:104]:
            m.append(-int(i)) # 겹쳐서 출력되기 때문에 - 부호 넣어서 음수로 변경
        for i in row[106:]:
            f.append(int(i))

print(m)
print(f)

import matplotlib.pyplot as plt
plt.barh(range(101), m)
plt.barh(range(101), f)
plt.show()
import matplotlib.pyplot as plt
plt.figure(figsize = (10,5), dpi=300)
plt.style.use('ggplot')
plt.rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False
plt.legend() 

plt.title("신도림 지역의 남녀 성별 인구분포")
plt.barh(range(101), m, label = "남성")
plt.barh(range(101), m, label = "여성")

plt.show()