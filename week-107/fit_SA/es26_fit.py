##Independent fitting
##Best fit parameter for first trajectory [ 20.62742049   0.77788654]
##[ 4.23655707  0.22702614] 1041.20873758
import numpy as np
import scipy.optimize
from pylab import *

def beer(x, p):
    return p[1]*np.exp(-p[0]*x)

def beer1(x, *p):
    return p[1]*np.exp(-p[0]*x)


def err(p, x, y, sigmay):
    return (beer(x, p) - y)/sigmay

##def err(p, x, y):
##    return (beer(x, p) - y)


data = genfromtxt('es26.txt')

v0_in = 0.145
v0_out = 0.6767

ydataout1 = data[:,1]/v0_out
sigmayout1 = data[:,2]/v0_out

ydataout = data[:,1][2:]/v0_out
sigmayout = data[:,2][2:]/v0_out

ydatain = data[:,3]/v0_in
sigmayin = data[:,4]/v0_in
xdata = data[:,0][2:]
xdata1 = data[:,0]

p1 = [10, 1.5]
p2 = [10, 1.0]

print("Independent fitting")
p_best1, pcov1, infodict1, errmsg1, success1  = scipy.optimize.leastsq(err, p1, args=(xdata, ydataout, sigmayout), full_output=1)
#p_best1,pcov1, infodict1, errmsg1, success1 = scipy.optimize.leastsq(err, p1, args=(xdata, ydataout), full_output=1)
s_sq1 = (err(p_best1, xdata, ydataout, sigmayout)**2).sum()/(len(ydataout)-len(p1))
#s_sq1 = (err(p_best1, xdata, ydataout)**2).sum()/(len(ydataout)-len(p1))
pcov = pcov1 * s_sq1
var = sqrt(pcov.diagonal())
print("Best fit parameter for first trajectory", p_best1)
print(var, s_sq1)

##p_curvefit, var = scipy.optimize.curve_fit(beer1, xdata, ydatatrasp, p1, sigmaytrasp)
###print("Best curve_fit parameter for first trajectory", p_curvefit)
##
##
##p_best2, pcov21, infodict2, errmsg2, success2 = scipy.optimize.leastsq(err, p2, args=(xdata, ydatain, sigmayin), full_output=1)
##print("Best fit parameter for second trajectory", p_best2)
##s_sq2 = (err(p_best2, xdata, ydatain, sigmayin)**2).sum()/(len(ydatain)-len(p1))
##pcov2 = pcov21 * s_sq1
##var = sqrt(pcov2.diagonal())
##print(var, s_sq2)

grid(which='major')
rc('font', size=16)
plot(xdata1, ydataout1, linestyle='None', marker='o', color="b", mec='None', label='out')
#plot(xdata, ydatain, linestyle='None', marker='o', color="blue", mec='None',label='in')
t = linspace(0.001,0.45, 100)
plot(t, beer(t, p_best1), color="red")
#plot(t, beer1(t, *p_curvefit), color="blue")

#plot(t, beer(t, p_best2), color="blue")
#yscale('log')
legend(loc=3, fontsize=12)
xlabel('Concentrazione')
ylabel(r'$ V/V_{0} $')
title("Rilevazione piccoli segnali - fit")
savefig('es26_piccoli_segnali1.png', dpi=400)
show()
