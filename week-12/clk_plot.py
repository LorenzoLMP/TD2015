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



def plot_unit(bit, y0, x0, width, height):
    if (bit==0):
        hlines(y0, x0, x0+width)
    else:
        vlines(x0, y0, y0+height, color='grey')
        hlines(y0+height, x0, x0+width)
        vlines(x0+width, y0, y0+height, color='grey')
        time = linspace(x0,x0+width,50)
        fill_between(time, y0, y0+height, facecolor='grey')

def sig_plot(clk, x_start, y_start):
    x0 = x_start;y0=y_start
    for i in range(len(clk)):
        plot_unit(clk[i],y0,x0, 1, 0.5)
        x0 = x0 + 1

###############################################
#div2
##q0 = 1
##div_2 = []
##for i in range(len(clock)):
##    a = jk(clock[i], 1, 1, q0)
##    div_2.append(a[2])
##    q0 = a[2]


def jk_div2(clk, q_start):
    div_2 = []
    q0 = q_start
    for i in range(len(clk)):
        a = jk(clk[i], 1, 1, q0)
        div_2.append(a[2])
        q0 = a[2]
    return div_2

###############################################
#div3

##j0 = 1
##div_3 = []
##for i in range(len(clock)):
##    a1 = jk(clock[i], j0, 1, q0)
##    a2 = jk(clock[i], q0, 1, (j0+1)%2)
##    #print(a1, a2)
##    div_3.append(a2[2])
##    j0 = (a2[2]+1)%2
##    q0 = a1[2]
def neg(s):
    if (s==0):
        return 1
    elif (s==1):
        return 0


def jk_div3(clk, q_start, j_start):
    div_3 = []
    q0 = q_start; j0 = j_start
    for i in range(len(clk)):
        s1 = jk(clk[i], j0, 1, q0)
        print('s1: ', s1, end='\n')
        s2 = jk(clk[i], q0, 1, (j0+1)%2)
        print('s2: ', s2, end='\n')
        div_3.append(s2[2])
        j0 = (s2[2]+1)%2
        q0 = s1[2]
    return [div_3, s1, s2]
        

##################################
#print(jk_div2(clock,0))
#print(jk_div3(jk_div2(clock,0),1,1))
#print(jk_div2(jk_div3(clock,1,1)[0],0))

#print(jk_div2([0,1,0,0,1,0,0,1],0))

##div2 = []
##for i in range(len(jk_div2(clock,0))-1):
##    div2.append(jk_div2(clock,0)[i+1])

#print(div2)
#print(jk_div3([1,1,0,0,1,1,0,0,1,1,0,0,1,1], 1, 0)[0])


clock =  [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1]
div32 = [0,0,1,1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0]
div23 = [0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0]
sig_plot(clock, 0, 4);text(len(clock), 4.5, 'clock', family='serif', style='italic', size=15)
sig_plot(div32, 0, 0);text(len(clock), 0.5, 'div3->2', family='serif', style='italic', size=15)
sig_plot(div23, 0, 2);text(len(clock), 2.5, 'div2->3', family='serif', style='italic', size=15)
#plot_unit(1, 2, 0, 1, 1)
#sig_plot(jk_div3(jk_div2(clock,0), 1, 1)[0], 0, 6);
xlim(-1,len(clock)+4)
ylim(-1,6)
title('Divisori per sei asincroni')
savefig('div_sei_comparative_picture.png', dpi=400)
show()
