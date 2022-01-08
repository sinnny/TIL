

!pip install sympy
from sympy import Symbol , solve
x = Symbol('x')
x
equation = 2*x - 6
solve(equation)
k = Symbol('k')
equation_2 = k-2-4
solve(equation_2)
# 방정식과 부등식

x = Symbol('x')
y = Symbol('y')
print(x)
print(y)
equation_3 = 3*x+y-2
equation_4 = x-2*y-3
solve((equation_3, equation_4), dict=True)








