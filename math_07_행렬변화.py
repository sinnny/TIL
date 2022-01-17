1. 역함수와 역변환
- 역행렬
import numpy as np 
A= np.matrix([[1,0,0,0,],[2,1,0,0,],[3,0,1,0],[4,0,0,1]])
print(A)
print()
print(np.linalg.inv(A))
# 전치행렬(Transpose)
a = np.arange(15).reshape(3,5)
a
np.transpose(a)
# 고유값, 고유벡터

a = np.array([[5,-1], [-2,1]])
np.linalg.eig(a)
# w: 고유값, v: 고유벡터 
w, v= np.linalg.eig(a)

print(w)  # 고유값
print()
print(v) # 고유벡터 (단위벡터로 정규화)






