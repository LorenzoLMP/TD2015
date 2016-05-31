from pylab import *  
from scipy import *

def jk(clk, j0, k0, q0):
    if (clk == 1):
        if (j0 != k0):
            return [j0, k0, j0] #il terzo è qnuovo
        elif ((j0== 0) & (k0 == 0)):
            return [j0, k0, q0]
        else:
            return [j0, k0, (q0+1)%2] #q0 negato
    else:
        return [j0, k0, q0]

##print(jk(1,0,1,1))
##print(jk(1,1,0,0))
##print(jk(1,0,0,1))
##print(jk(1,1,1,1))
##print(jk(0,0,0,1))


clock = [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0]

q0 = 1
##for i in range(len(clock)):
##    a = jk(clock[i], 1, 1, q0)
##    print(a[2])
##    q0 = a[2]
##

j0 = 1
for i in range(len(clock)):
    a1 = jk(clock[i], j0, 1, q0)
    a2 = jk(clock[i], q0, 1, (j0+1)%2)
    print(a1, a2)
    j0 = (a2[2]+1)%2
    q0 = a1[2]
