from sympy.vector import *
from sympy import *
C = CoordSys3D (' ') # Setting the coordinate system
x,y,z = C.x, C.y,C.z # Variables x,y,z to be used with coordinate system C
A=x**2*y+z
delop = Del() #Del operator
gradA=delop(A) # substitution of A in the Del operatore
gradA_sim = gradA.doit()
print('grad A is =',gradA,'=', gradA_sim)
