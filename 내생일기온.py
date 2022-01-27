import matplotlib.pyplot as plt
import csv

f = open('../data/seoul_book.csv', encoding='cp949')
data=csv.reader(f)

next(data)

high = [] # 최고 기온 담기
low = [] # 최저 기온 담기 

for row in data:
    if row[-1] != " " and row[-2] != " ":   # 최고기온(row[-1])과 최저기온(row[-2])에 값이 있다면, 
        date = row[0].split('-')            # 날짜 값을 '-' 문자 기준으로 구분 --> data 저장
        if 1988 <= int(date[0]):            # 1988년 이후 데이터라면, 
            if date[1] =='06' and date[2] == '14':  # 10월 26일이라면
                high.append(row[-1])        # 최고 기온을 high=[] 빈리스트에 담기
                low.append(row[-2])         # 최저 기온을 low=[] 빈리스트에 담기
        
plt.rc('font', family="AppleGothic")
plt.reParams['axes.unicode_minus'] = False # 마이너스 기호 깨짐 방지
plt.title('생일 기온 변화 그래프 현황')
plt.plot(high, 'red', label='high')
plt.plot(low, 'skyblue', label='low')
plt.legend()
plt.show()
