# 약국정보 리스트

list_drugs = ['병원명', '종별코드명', '시도명', '주소', '전화번호']

i = 0

for list_drug in list_drugs:
    url = api.format(list_drugs, key=apikey)
    req = requests.get(url)
    re = req.text
    soup = BeautifulSoup(re, 'html.parser')
    
    # 병원명
    yadmnm = soup.find_all('yadmnm')
    
    # 종별코드명
    sggucdnm = soup.find_all('sggucdnm')
    
    # 시도명
    sidocdnm = soup.find_all('sidocdnm')
    
    # 주소 
    addr = soup.find_all('addr')
        
    # 전화번호
    telno = soup.find_all('telno')
    
    print("병원명", yadmnm)
    print("종별코드명", sggucdnm)
    print("시도명", sidocdnm)
    print("주소", addr)
    print("전화번호", telno)