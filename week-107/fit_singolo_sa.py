import numpy as np
import scipy.optimize
from pylab import *

def beer(x, p):
    return p[1]*np.exp(-p[0]*x)

def beer1(x, *p):
    return p[1]*np.exp(-p[0]*x)


def err(p, x, y, sigmay):
    return (beer(x, p) - y)/sigmay


data = genfromtxt('misure_7_20V.txt')

v0_trasp = 3.617
v0_osc = 3.408

ydatatrasp = data[:,1]/v0_trasp
sigmaytrasp = data[:,2]/v0_trasp
ydataosc = data[:,3][1:]/v0_osc
sigmayosc = data[:,4][1:]/v0_osc
xdata = data[:,0]

p1 = [10, 1.5]
p2 = [10, 1.0]

print("Independent fitting")
p_best1, ier1 = scipy.optimize.leastsq(err, p1, args=(xdata, ydatatrasp, sigmaytrasp))
print("Best fit parameter for first trajectory", p_best1)

p_curvefit, var = scipy.optimize.curve_fit(beer1, xdata, ydatatrasp, p1, sigmaytrasp)
print("Best curve_fit parameter for first trajectory", p_curvefit)

p_best2, ier2 = scipy.optimize.leastsq(err, p2, args=(xdata[1:], ydataosc, sigmayosc))
print("Best fit parameter for second trajectory", p_best2)

grid(which='major')
rc('font', size=16)
plot(xdata, ydatatrasp, linestyle='None', marker='o', color="red", mec='None', label='trasp')
plot(xdata[1:], ydataosc, linestyle='None', marker='o', color="blue", mec='None',label='osc')
t = linspace(0.001,0.25, 100)
plot(t, beer(t, p_best1), color="red")

plot(t, beer(t, p_best2), color="blue")
yscale('log')
legend(loc=3, fontsize=12)
xlabel('Concentrazione')
ylabel(r'$ V/V_{0} $')
title("Beer-Lambert 7.20V - fit")
savefig('concentr_7_20_fit_log.png', dpi=400)
show()
