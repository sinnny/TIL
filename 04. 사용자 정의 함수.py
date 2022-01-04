
# 사용자 정의 함수
# 사용자가 정의한 함수의 형태
# input과 output 관계를 내부에 정의
# def, lambda(축약형)


# 함수 정의
# f(x) =  x+1

# 1. def 방식

# def 함수이름(인수1, 인수2, 인수3): 
#     험수 본문
#     return 반환할 객체 

# 숫자를 넣어서 곱하기 10한 값을 반환

def f_mul(x):
    v1 = x*10
    return v1

f_mul(10)

# 두 숫자 (두개의 인자를 넣는구나!) 넣어서 두 숫자의 곱 반화

def f_2_mul(x, y):
    v2 = x * y
    return v2


def f_2_mul(x, y):
    return (x*y)

print(f_2_mul(2,10))


# 인수의 default 값 (기본값 선언)

def f_d(x=1, y):
    return(x*y)

#non-default argument follows default argument
# 첫 번째 인수에 기본값을 정의하면, 뒤에 나로는 인수도 기본값을 정의해야함



def f_d(y, x=1):
    return(x*y)
# default 값을 갖는 인수는 맨 뒤에 배치


def f_d(x=1, y=1):
    return(x*y)

print(f_d())


# lambda 축약형
# 비교적 단순한 연산 및 리턴시 사용

# 예제 : 숫자를 넣을거에요. 여기에 10을 곱한 값을 리턴하세요

f1 = lambda x: x*10
f1(10)

# 문제
# 3개 숫자를 전달받아 첫 번째와 두 번째 합에 세번째 숫자의 곱 리턴

f2 = lambda x, y, z : (x+y)*z
f2(2, 5, 3)


# map 함수
f1 = lambda x: x*10
f1(4)

l1 = [1, 2, 5, 10]
f1(l1)
# 리스트가 10번 반


# 1) for문 처리
l2 = []
for i in l1:
    l2.append(i+10)
    
print(l2)


# 2) 사용자 정의 함수 + map

map(func,           # 적용할 함수
    iterable)       # 추가할 인수


f1(4)
l1
map(f1, l1)
list(map(f1, l1))

# 하나의 숫자를 전달받을거에요. 10보다 크면 3을 곱하고, 작거나 같으면 2를 곱한 결과물 리턴하세요

l2 = [3, 5, 7, 10]

def f3(x):
    if x>10:
        v1 = x*3
    else:
        v1 = x*2
    return v1

f3(11)
f3(5)
f3(l1) #error

list(map(f3, l1))





