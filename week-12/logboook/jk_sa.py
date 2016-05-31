from pylab import *  
from scipy import *

def jk(clk, j0, k0, q0):
    if (clk == 1):
        if (j0 != k0):
            return [j0, k0, j0] 
        elif ((j0== 0) & (k0 == 0)):
            return [j0, k0, q0]
        else:
            return [j0, k0, (q0+1)%2] #q0 negato
    else:
        return [j0, k0, q0]

clock = [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0]

q0 = 0
##for i in range(len(clock)):
##    a = jk(clock[i], 1, 1, q0)
##    print(a[2])
##    q0 = a[2]
##

q0 =0
q1 =0
q2 = 0
q3 =0

for i in range(len(clock)):
    a1 = jk(clock[i], 1, 1, q0)
    a2 = jk(clock[i], q0, q0, q1)
    a3 = jk(clock[i], q0*q1, q0*q1, q2)
    a4 = jk(clock[i], q2*q0*q1, q2*q0*q1, q3)
    a1 = [1,1, a1[2]]
    a2 = [a1[2], a1[2], a2[2]]
    a3 = [a2[2]*a1[2], a2[2]*a1[2], a3[2]]
    a4 = [a2[2]*a1[2]*a3[2], a2[2]*a1[2]*a3[2], a4[2]]
    print(a1[0], a1[1], a2[0], a2[1], a3[0], a3[1], a4[0], a4[1], a4[2], a3[2], a2[2],a1[2])
    q0 = a1[2]
    q1 = a2[2]
    q2 = a3[2]
    q3 = a4[2]

##(j0+1)%2, (q0+1)%2
