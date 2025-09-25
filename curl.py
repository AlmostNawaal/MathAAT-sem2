from sympy.vector import *
C= CoordSys3D (' ')
x,y,z = C.x, C.y,C.z
i,j,k = C.i,C.j,C.k
vecF=(2*x**2*z)*i-(x*y**2*z)*j+(3*y*z**2)*k
delop = Del()
CurlF = delop.cross(vecF)
CurlF_sim = CurlF.doit() # or use CurlF = curl(vecF)
print('Curl F = ',CurlF,'=',CurlF_sim)