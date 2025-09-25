from sympy.vector import *
C= CoordSys3D (' ')
x,y,z = C.x, C.y,C.z
i,j,k = C.i,C.j,C.k
vecF=(2*x**2*z)*i-(x*y**2*z)*j+(3*y*z**2)*k
delop=Del()
divF = delop.dot(vecF)
divF_sim = divF.doit()
print('div vec F =',divF,'=',divF_sim)