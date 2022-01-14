import numpy as np

x= np.array([1,2,3])
print(x)
# 크기가 (1,3)인 2차원
np.array([[1,2,3]])
# 크기가 (1,3)인 2차원 열벡터
np.array([[[1],[2],[3]]])
# 크기가 (1,3)인 2차원
np.array([[1,2,3]])
from scipy import linalg
s = np.array([2,3,1])
# 단위 벡터

s / linalg.norm(s)
# Norm
x = np.array([1,-3])
x/linalg.norm(x)
# Norm 2
x / (x**2).sum()**0.5
# 영벡터(zeros())
np.zeros(5) # 실수로 반환
np.zeros(5).shape
s = (2,2)
np.zeros(s)
# 선형 독립, 선형 종속
# Rank

#matrix_rank()

x = np.array([[2,7], [5,1]])
np.linalg.matrix_rank(x)
x_2 = np.array([[2,4],[3,6]])
np.linalg.matrix_rank(x_2)
x_3 = np.array([[1,2],[3,5]])
np.linalg.matrix_rank(x_3)
# 벡터의 내적과 외적  *** 시험문제

x = [2,3]
y = [3,1]

# 벡터의 내적 (zip 함수 활용)

z = [i + j for i, j in zip(x,y)]
z
z_2= [i-j for i,j in zip[(x,y)]
print(z_2)
# 벡터의 곱셈 (inner product, outer product)

x= [3,4]
c= 8

z = [c*i for i in x]
print(z)
# 내적 (inner product)
u = np.array([6,6])
v = np.array([12,0])

np.dot(u, v)
# zip 함수

list(zip([1,2,3],[4,5,6]))
list(zip([1,2,3],[4,5,6],[7,8,9]))
# 벡터의 내적 원리
A= np.arange(1*2*3).reshape((1,2,3))
B1= np.arange(1*2*3).reshape((1,2,3))
B2= np.arange(1*2*3).reshape((1,3,2))
B3= np.arange(1*2*3).reshape((2,1,3))
B4= np.arange(1*2*3).reshape((2,3,1))
B5= np.arange(1*2*3).reshape((3,1,2))
B6= np.arange(1*2*3).reshape((3,2,1))
np.dot(A,B1)  #value error
np.dot(A, B2)
# np.dat(A,B3)  #value error 발생
np.dot(A, B4)
np.dot(A, B1) #value error 발생
np.dot(A, B6) #value error 발생
import numpy as np

u = np.array([3.-6])
v = np.array([-7, 9])

uv = np.dot(u,v)
print(uv)
# 외적 (cross() 함수 적용)

a = (1,3,5)
b= (2,4,6)

def cross(a,b):
    c=[a[1]*b[2]-a[2]*b[1],
       a[2]*b[0]-a[0]*b[2],
       a[1]*b[2]-a[1]*b[0]]
    return c
cross(a,b)
# numpy dldyd qprxj dhlwjr rngkrl
import numpy as np

print(np.cross(a,b))
# 직교 벡터
import numpy as np

# 크기가 (1,2)인 2차원 배열

a = np.array([1,2])
print(a)
np.linalg.norm(a) # a의 길이
# L1 norm

np.linalg.norm(a, ord=2)
# 유클리디언 거리 구하기

from scipy.spatial import distance

p1 = (1,2,3)
p2 = (4,5,6)

# p1, p2 사이 유클리디언 거리

distance.euclidean(p1,p2)
# 맨하튼 거리

from math import *

p1 = (1,2,3)
p2 = (4,5,6)

# p1, p2 사이 맨해튼 거리

def manhattan_dist(x,y):
    return sum(abs(a-b) for a, b in zip(x,y))

manhattan_dist(p1,p2)
# 코사인 유사도 - 문서 유사도

from numpy import dot
from numpy.linalg import norm
import numpy as np

def cos_sim(A, B):
    return dot(A,B)/(norm(A)*norm(B))
doc1 = np.array([1,1,1,1,0])
doc2 = np.array([1,0,1,0,1])
doc3 = np.array([2,1,1,1,1])
# 코사인 함수에 따라 문서 간 유사도 출력하기

print(cos_sim(doc1, doc2))
print(cos_sim(doc1, doc3)) # 문서 1과 문서 3 유사도가 가장 높음
print(cos_sim(doc2, doc3))

