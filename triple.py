from sympy import *
x,y,z = symbols('x y z')
f= x+y+exp(z)
I = integrate(f,(z,0,x+y),(y,0,x),(x,0,1))
print(I)