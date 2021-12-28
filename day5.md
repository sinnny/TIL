### 함수와 메소드

##### 함수: 함수(대상) 함수 대상이 있어야함

###### 메서드: 대상.메소드

##### 대소 치환

v1 = 'abcde' #string
v1.upper() #대문자 치환
'ABCDE'.lower() #소문자 치환
'abc def'.title() # camel 표기법 (단어의 첫글자만 대문자로 표시)

##### 색인 (문자열 추출)

'abcd'[0]
'abcd'[-2]
'abcd'[0:3]

#####  ex) '031)345-0834

vtel = '031)345-0834'
vtel[0:3]

####  문자열의 시작, 끝 여부 확인

#####  v1.startswith(prefix,   # 시작 값 확인 문자

#####               start,    # 확인할 시작 위치

#####                end)      # 확인할 끝 위치

v1.startswith('b')
v1.startswith('b',1)
v1[1:].startswith('b')

##### v1.endswith(suffix,

#####             start,

#####             end)

v1
v1.endswith('e')
v1.endswith('E')

#### 앞 뒤 공백 또는 문자 제거 

'abc' == 'abc'
'  abc'.strip() # 양쪽 공백 제거
'abc'.strip('a') # 문자 제거
'abaca'.strip('a') # 양쪽 문자 제거(중간 글자 삭제 불가)

'abcd'.lstrip() # 왼쪽 공백 또는 글자 제거
'  abcd '.rstrip() #오른쪽 공백 또는 글자 제거 


#### 치환

##### 'abcace'.replace(old,     # 찾을 문자열

#####                  new)     # 바꿀 문자열


'abcabc'.replace('a','A')
'abcabc'.replace('ac','AB')
'abcabc'.replace('ab','')

#### 문자열 분열

##### v1.split(sep) #분리 구분기호

'a/b/c/d'.split('/')
'a/b/c/d'.split('/')[1]
'a/b/c/d'.split('/')[0:2]


#### 위치값 리턴

##### 'abcd'.find(sub,    #위치값을 찾을 대상

#####             start,   찾을 위치(시작점)

#####            end)     찾을 위치(끝점)

v1
v1.find('b')


vte1 = [031)345-0834]
vnum = vte1.find(')')
vnum[0:vnum]

##### 포함 함수

'abcabcabc'.count('a')

##### gud(type) 확인

type(v1) #데이터 타입 확인
v1.isalpha() # 문자 확인
v1.isnumeric() # 숫자 확인

##### 대소문자 확인

v1.isupper()
v1.islower()

##### 문자열 결합

'a' + 'b'

##### 문자열 길이

len(v1)
3/len(v1)

vname ='dfwill'
vemail = 'drwill@naver.com'
jumin = '901026-111111'

vname[1] == 'm'
vname[1] == 'r'

vemail.split('@')[0]
vemail[0:5]

idx = vemail.find('@')
vemail[:idx]


##### 3. 주민번호에서 여자인지 확인 

jumin[7] == '2'
jumin.split('-')[1][0] == 2



 