
# 문자열 메서드
# 문자열 처리와 관련된 메서드

# 1. 기본 메서드 : 벡터 연산 불가 (매 원소마다 반복 불가)

'abc'.upper()
'a/b/c'.split('/')
'a/b/c'.split('/')[1]

l1 = ['abc', 'def']
l2 = ['a/b/c', 'd/e/f']


l1.upper()  # 불가
l2.split()  # 불가

list(map(lambda x: x.upper(), l1))
# Out[139]: ['ABC', 'DEF']

list(map(lambda x: x.split(), l2))
# Out[140]: [['a/b/c'], ['d/e/f']]

list(map(lambda x: x.split('/'), l2))
# Out[141]: [['a', 'b', 'c'], ['d', 'e', 'f']]

list(map(lambda x: x.split('/')[1], l2))
# Out[142]: ['b', 'e']




#  pandas 메서드: 벡터화 내장(매 원소마다 반복 가능)
# Series, DataFrame

# 1) split

from pandas import Series, DataFrame

l1    # Out[146]: ['abc', 'def']

Series(l1)
# 0    abc
# 1    def
# dtype: object

s1 = Series(l1)

l2      # ['a/b/c', 'd/e/f']
Series(l2)
# 0    a/b/c
# 1    d/e/f
# dtype: object

s2=Series(l2)

s2.str.split('/')
# 0    [a, b, c]
# 1    [d, e, f]
# dtype: object


s1.str.upper()
# 0    ABC
# 1    DEF
# dtype: object
s1.str.lower()
s1.str.title()


# 3) replace
s1.str.replace('a','A')
# Out[154]: 
# 0    Abc
# 1    def
# dtype: object

s1.str.replace('a','')
# 0     bc
# 1    def
# dtype: object


# 예제 -천단위 구분기호 처리

s3 = Series(['1,200', '3,000', '4,000'])
s3.sum()

# 천 단위 구분기호 때문에 문자로 입력된 값이라 문자를 결합으로 인식됨

s3.str.replace(',','').astype('int').sum()




# 4) 패턴 확인:startswith, endwith, contains
s1.str.startswith('a')
# 0     True
# 1    False
# dtype: bool

s1[s1.str.startswith('a')]      # s1 각 원소에서 'a'로 시작하는 원소 추출
# 0    abc
# dtype: object

s1[s1.str.endswith('c')]
s1[s1.str.contains('e')]


# 문자열 크기 len()

s1.str.len()
# 0    3
# 1    3


# count 포함 개수
Series(['aabbbb', 'abcdadd']).str.count('a')
# 0    2
# 1    2


# 제거 함수 (공백, 문자)
Series(['       cd       ', '          df        '])
Series(['       cd       ', '          df        ']).str.strip()
# 0    cd
# 1    df

Series(['       cd       ', '          df        ']).str.strip().str.len()
# 0    2
# 1    2
# dtype: int64

s1.str.strip('a')       # 문자열 제거
Series(['aavvsafgaa', 'abcabcbabc']).str.strip('a')
# 0       vvsafg
# 1    bcabcbabc
# dtype: object



# 문자열제거
Series(['aavvsafgaa', 'abcabcbabc']).str.replace('a','')
# 0      vvsfg
# 1    bcbcbbc
# dtype: object
# 문자열 제거 (중간값 삭제 가능)


# find(위치값 return)
s3 = Series(['abc@drwill.kr', 'abcdef@drwill.com'])
s3.str.find('@')

# 문자열 색인(추출)
'abcde'[0:3]
s3[0:3]     # Series에서 1번째, 2번째, 3번째 원소 추출

s3.str[0:3] # Series에서 각 원소마다 1번째, 2번째, 3번째 문자열 추출
# 0    abc
# 1    abc
# dtype: object

# 이메일 아이디 추출
s4 = Series(['drwill@naver.com', 'zzuyu@drwill.kr'])
s4.str.find('@')
print(s4[0][0:6], s4[1][0:5])

vno=s4.str.find('@')
vno

list(map(lambda x, y : x[0:y], s4, vno))
# y = 추출 범위

s4.map(lambda x : x[:x.find('@')])


# pad : 문자열 삽









