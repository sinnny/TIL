2**5
import math as ma
ma.sqrt(2)
ma.sqrt(9)
from sympy import expand, factor, Symbol
x = Symbol('x')
x
# 전개
expand((x+1)*(x+5))
factor(x**2 + 6*x + 5)
