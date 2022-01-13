from sympy import symbols
# 평균변화율 함수
def average(a,b):
    m=max(a,b) 
    n=min(a,b)
    x=symbols('x')
    
    fx = 2*x**2+4*x+7  # 2x^2+4x+7 함수 정의
    fb = fx.subs(x,m) # 함수 m에 대입
    fa = fx.subs(x,n)  # 함수 n에 대입
    
    result = (fb-fa)/(b-a)
    return result
print(average(0,2))
print(average(20,30))
### 순간변화율
from sympy import Derivative, symbols
# 평균변화율을 구할 수 있는 함수를 정의
x = symbols('x')
fx = 2*x**2+4*x+7
Derivative(fx,x).doit()
f_prime = Derivative(fx,x).doit()
f_prime.subs({x:3}) # 미분계수 f_prime 3
#### 다항함수의 미분
import sympy as sym
x = sym.Symbol('x')
a = sym.diff((2*x**3+3*x**2+x+1),x)
print(a)




