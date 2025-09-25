from sympy import *
x,y = symbols('x y')
f=x*y+exp(y)
I = integrate(f,(x,3,4),(y,1,2))
print(I)