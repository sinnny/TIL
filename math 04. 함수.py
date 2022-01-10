from sympy import Limit, S, Symbol
# x 변수 생성, x가 0에 한 없이 가까워질 떄
# 1/x에 대한 극한값

x = Symbol('x')
Limit(1/x, x, S.Infinity).doit()
# 우극한 값 구하기
Limit(1/x, x, 0).doit()
# 좌극한 값 구하기
Limit(1/x, x, 0, dir='-').doit()




