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
for i in range(len(clock)):
    a = jk(clock[i], 1, 1, q0)
    print(a[2])
    q0 = a[2]


q0 =0
q1 =0
q2 = 0
q3 =0

##out_file = open("dati_prova_sa2.txt","w")
##out_file.write("a10\ta11\ta20\ta21\ta30\ta31\ta40\ta41\ta42\ta32\ta22\ta12")
for i in range(len(clock)):
    a1 = jk(clock[i], j0, 1, q0)
    a2 = jk(clock[i], (q0+1)%2, 1, (j0+1)%2)
##    a3 = jk(clock[i], q0*q1, q0*q1, q2)
##    a4 = jk(clock[i], q2*q0*q1, q2*q0*q1, q3)
    a1 = [(a2[2]+1)%2,1, a1[2]]
    a2 = [(a1[2]+1)%2, 1, a2[2]]
##    a3 = [a2[2]*a1[2], a2[2]*a1[2], a3[2]]
##    a4 = [a2[2]*a1[2]*a3[2], a2[2]*a1[2]*a3[2], a4[2]]
    print(a1[0], a1[1], a2[0], a2[1], a2[2],a1[2])
##    out_file.write("\n%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s"%(a1[0], a1[1], a2[0], a2[1], a3[0], a3[1], a4[0], a4[1], a4[2], a3[2], a2[2],a1[2]))
    j0 = a1[0]
    q0 = a1[2]
##    q2 = a3[2]
##    q3 = a4[2]

out_file.close()

(j0+1)%2, (q0+1)%2

out_file = open("planck_newdata_60ua.txt","w")

##for i in range(len(ydata)):
##        out_file.write("%s\t%s\t%s\t%s\n"%(xdata[i], sigmax[i], ydata[i], sigmay[i]))
##out_file.close()
##def neg(s):
##    if (s==0):
##        return 1
##    elif (s==1):
##        return 0


##q0 =0
##q1 =0
##q2 = 0
##q3 =0
##c = 0
##out_file = open("dati_prova_hw7_down.txt","w")
##out_file.write("j1\tk1\tj2\tk2\tj3\tk3\tq3\tq2\tq1")
##for i in range(len(clock)):
##    a1 = jk(clock[i], 1, 1, q0)
##    x = c*q0
##    y = neg(c)*neg(q0)
##    a2 = jk(clock[i], x or y, x or y, q1)
##    z = x*q1
##    w = y*neg(q1)
##    a3 = jk(clock[i], z or w, z or w, q2)
####    a4 = jk(clock[i], q2*q0*q1, q2*q0*q1, q3)
##    a1 = [1,1, a1[2]]
##    x1 = c*a1[2]
##    y1 = neg(c)*neg(a1[2])
##    a2 = [x1 or y1, x1 or y1, a2[2]]
##    z = x1*a2[2]
##    w = y1*neg(a2[2])
##    a3 = [z or w, z or w, a3[2]]
####    a4 = [a2[2]*a1[2]*a3[2], a2[2]*a1[2]*a3[2], a4[2]]
##    print(a1[0], a1[1], a2[0], a2[1], a3[0], a3[1], a3[2], a2[2],a1[2])
##    out_file.write("\n%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s"%(a1[0], a1[1], a2[0], a2[1], a3[0], a3[1], a3[2], a2[2],a1[2]))
##    q0 = a1[2]
##    q1 = a2[2]
##    q2 = a3[2]
####    q3 = a4[2]
##
##out_file.close()




