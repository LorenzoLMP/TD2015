##Independent fitting
##Best fit parameter for first trajectory [ 19.40451089   1.32262773]
##[ 2.34382485  0.12252588] 5671.73132833
##Best fit parameter for second trajectory [ 20.67616098   1.17393029]
##[ 2.0239694   0.04052121] 1751.04644916

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


data = genfromtxt('tabulardata.txt')

v0_trasp = 3.617
v0_osc = 3.408

ydatatrasp = data[:,1]/v0_trasp
sigmaytrasp = data[:,2]/v0_trasp
ydataosc = data[:,3]/v0_osc
sigmayosc = data[:,4]/v0_osc
xdata = data[:,0]

p1 = [10, 1.5]
p2 = [10, 1.0]

print("Independent fitting")
p_best1, pcov1, infodict1, errmsg1, success1  = scipy.optimize.leastsq(err, p1, args=(xdata, ydatatrasp, sigmaytrasp), full_output=1)
##p_best1, ier1 = scipy.optimize.leastsq(err, p1, args=(xdata, ydatatrasp))
s_sq1 = (err(p_best1, xdata, ydatatrasp, sigmaytrasp)**2).sum()/(len(ydatatrasp)-len(p1))
pcov = pcov1 * s_sq1
var = sqrt(pcov.diagonal())
print("Best fit parameter for first trajectory", p_best1)
print(var, s_sq1)

p_curvefit, var = scipy.optimize.curve_fit(beer1, xdata, ydatatrasp, p1, sigmaytrasp)
#print("Best curve_fit parameter for first trajectory", p_curvefit)


p_best2, pcov21, infodict2, errmsg2, success2 = scipy.optimize.leastsq(err, p2, args=(xdata, ydataosc, sigmayosc), full_output=1)
print("Best fit parameter for second trajectory", p_best2)
s_sq2 = (err(p_best2, xdata, ydataosc, sigmayosc)**2).sum()/(len(ydatatrasp)-len(p1))
pcov2 = pcov21 * s_sq1
var = sqrt(pcov2.diagonal())
print(var, s_sq2)

grid(which='major')
rc('font', size=16)
plot(xdata, ydatatrasp, linestyle='None', marker='o', color="red", mec='None', label='trasp')
plot(xdata, ydataosc, linestyle='None', marker='o', color="blue", mec='None',label='osc')
t = linspace(0.001,0.45, 100)
plot(t, beer(t, p_best1), color="red")
#plot(t, beer1(t, *p_curvefit), color="blue")

plot(t, beer(t, p_best2), color="blue")
#yscale('log')
legend(loc=3, fontsize=12)
xlabel('Concentrazione')
ylabel(r'$ V/V_{0} $')
title("Beer-Lambert - fit")
#savefig('concentr_es5.png', dpi=400)
show()
