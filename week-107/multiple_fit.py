import numpy as np
import scipy.optimize
from pylab import *

def beer(x, p):
    return p[1]*np.exp(-p[0]*x)

def err(p, x, y):
    return beer(x, p) - y


data = genfromtxt('misure_7_20V.txt')

ydatatrasp = data[:,1]
sigmaytrasp = data[:,2]
ydataosc = data[:,3][1:]
sigmayosc = data[:,4][1:]

xdata = data[:,0]

p1 = [10, 4.5]
p2 = [10, 4.0]

print("Independent fitting")
p_best1, ier1 = scipy.optimize.leastsq(err, p1, args=(xdata, ydatatrasp))
print("Best fit parameter for first trajectory", p_best1)

p_best2, ier2 = scipy.optimize.leastsq(err, p2, args=(xdata[1:], ydataosc))
print("Best fit parameter for second trajectory", p_best2)


def err_global(p, x1, y1, x2, y2):#in p1 i parametri del primo fit, in p2 quelli del secondo. segna quelli in comune 
    p1 =  [p[0], p[1]]
    p2 =  [p[0], p[2]]
    err1 = err(p1, x1, y1)
    err2 = err(p2, x2, y2)
    return np.concatenate((err1, err2))

p_global = [10, 4.5,  4] #in un unico array tutti i parametri delle curve
p_best, ier = scipy.optimize.leastsq(err_global, p_global, args=(xdata, ydatatrasp, xdata[1:], ydataosc))
p_best_1 = array([p_best[0], p_best[1]])
p_best_2 = array([p_best[0], p_best[2]])
print("Global fit results")
print("Best fit parameters for first trajectory:", p_best_1)
print("Best fit parameters for second trajectory:", p_best_2)




grid(which='major')
rc('font', size=16)

plot(xdata, ydatatrasp, linestyle='None', marker='o', color="red", mec='None', label='trasp')
plot(xdata[1:], ydataosc, linestyle='None', marker='o', color="blue", mec='None',label='osc')
t = linspace(0.001,0.25, 100)
plot(t, beer(t, p1), color="red")
plot(t, beer(t, p_best_1), color="red", linestyle='--', linewidth=1.5)
plot(t, beer(t, p_best_2), color="blue", linestyle='--', linewidth=1.5)
plot(t, beer(t, p2), color="blue")
#yscale('log')
legend(loc=3, fontsize=12)
xlabel('Concentrazione')
ylabel(r'Tensione V [V]')
title("Beer-Lambert 7.20V - fit")
savefig('concentr_7_20_fit.png', dpi=400)
show()

##Independent fitting
##Best fit parameter for first trajectory [ 9.92247652  4.74991281]
##Best fit parameter for second trajectory [ 12.26800641   5.0144656 ]
##Global fit results
##Best fit parameters for first trajectory: [ 10.83262303   4.85113289]
##Best fit parameters for second trajectory: [ 10.83262303   4.78456389]
