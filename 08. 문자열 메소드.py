# 판다스_문자열 메소드
# 기본 메소드: 벡터 연산 불가능 ( 매 원소마다 반복 불가능)

'abc'.upper()
'a/b/c'.split('/')[1]

l1 = ['abc', 'def']
l2 = ['a/b/c', 'd/e/f']

l1.upper()  # 벡터연산 안됨
l2.upper()  # 벡터연산 안됨

list(map(lambda x: x.upper(), l1))
# ['ABC', 'DEF']
list(map(lambda x: x.split('/'), l2))
# [['a', 'b', 'c'], ['d', 'e', 'f']]

# pandas 메서드 : 벡터화 내장 (매 원소마다 반복 가능)
# Series. DataFrame 적용 가능

from pandas import Series, DataFrame

# 1) split
Series(l1)
# 0    abc
# 1    def
# dtype: object

s1 = Series(l1)
s2 = Series(l2)

s2
# 0    a/b/c
# 1    d/e/f
# dtype: object

s2.split('/')  >> 불가
s2.str.split('/')  >> 가능
# 0    [a, b, c]
# 1    [d, e, f]
# dtype: object

# 대소치환

s1.str.upper()      # 대문자 치환
s1.str.lower()      # 소문자 치
s1.str.title()
# 0    Abc
# 1    Def
# dtype: object


# replace (치환)
s1.str.replace('a', 'A')    # 문자열 치환
s1.str.replace('a','')      # 문자열 삭제
# 0     bc
# 1    def
# dtype: object



# [예제] 천단위 구분기호 처리
s3 = Series(['1,200', '3,000', '4,000'])
# 0    1,200
# 1    3,000
# 2    4,000
# dtype: object

s3.sum()    #'1,2003,0004,000'

s3.str.replace(',','').astype(int).sum()

# 패턴확인: startwith, endwith, contains
s1[s1.str.startwith('a')    # s1 각 원소에서 'a'로 시작하는 원소 추출
s1[s1.str.endwith('c')]]    # s1 각 원소에서 'cㄹ'로 끝나는 원소 추출
s1[s1.str.contains('e')]    # s1 각 원소에서 'cㄹ'로 끝나는 원소 추출

# 문자열 크기 len()
s1.str.len()    # # 각 원소의 크기

#count 포함되어 있는 개수
Series(['aabca', 'abcdsa']).str.count('a')
# 0    3
# 1    2
# dtype: int64


# 문자열 제거 (제거함수 : 공백, 문자)
Series(['         cd    ', '     df    ']).str.strip()
Series(['         cd    ', '     df    ']).str.strip().str.len()
# 0    2  
# 1    2

s1.str.strip('a')   # 문자열제거
Series(['aaabaca', 'abcda']).str.strip('a') # 문자열 제거 (중간값 삭제 불가)
# 0    bac
# 1    bcd
# dtype: object

Series(['aaabaca', 'abcda']).str.replace('a','') # 문자열 제거 (중간값 삭제 가능)
# 0     bc
# 1    bcd
# dtype: object

# find : 위치값 리턴
s3 = Series(['abc@abc.com', 'avcvdds@abc.com'])
s3.str.find('@')


# 문자열 색인(추출)
'abcded'[0:3]  # 문자열 색인
s3[0:1]        # Series에서 첫번째 원소 추출
# 0    abc@abc.com
# dtype: object

s3.str[0:3]     # Series에서 각 원소마다 1~3번째까지의 문자열 추출
# 0    abc
# 1    avc
# dtype: object


# [예제] [- 이메일 아이디 추출]
Series(['abc@abc.com', 'avcvdds@abc.com'])
s3 = Series(['abc@abc.com', 'avcvdds@abc.com'])

list(s3.map(lambda x: x[:x.find('@')]))


vno = s3.str.find('@')
vno
list(map(lambda x, y : x[0:y], s3, vno))


# 문자열 삽입 pad
s1.str.pad(5,           # 총자리수
           'Left',      # 삽입할 방향
           '!')         # 삽입할 글

s1
# 0    abc
# 1    def
# dtype: object

s1.str.pad(5,'left', '!')
# 0    !!abc
# 1    !!def
# dtype: object


s1.str.pad(5, 'right', '!')
# 0    abc!!
# 1    def!!
# dtype: object


# 문자열 결합 cat
'a'+'b' # 'ab'
'a'*3   # 'aaa'

s4 = Series(['abc', 'def', '123'])
# 0    abc
# 1    def
# 2    123
# dtype: object

s4.str.cat()   # 'abcdef123'   >> Series 내 서로 다른 원소 결합
s4.str.cat(sep='/')     #'abc/def/123'  >> Series 내 서로 다른 원소를 구분기호와 함께 결합

s5 = Series([['a', 'b', 'c'], ['d', 'e', 'f']])
# 0    [a, b, c]
# 1    [d, e, f]
# dtype: object

s5.str.join(sep='')  # >> Series 내 각 원소 내부의 문자열 결합
# 0    abc
# 1    def
# dtype: object

s5.str.join(sep=',')
# 0    a,b,c
# 1    d,e,f
# dtype: object

