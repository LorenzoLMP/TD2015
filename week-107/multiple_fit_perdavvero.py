##Independent fitting
##Best fit parameter for first trajectory sigmay [ 11.43265822   1.34382149]
##[ 2.44245809  0.12753036] 27499.5498275
##Best fit parameter for second trajectory [ 13.84922401   1.51294535]
##[ 2.17354134  0.15928121] 16314.7522776
##Best fit parameter for third trajectory [ 11.41139233   1.47687473]
##[ 2.17354134  0.15928121] 25739.241208
##Best fit parameter for fourth trajectory [ 12.74321084   1.51990852]
##[ 2.17354134  0.15928121] 24375.9521637
##Best fit parameter for fourth trajectory [ 10.94823041   1.50935501]
##[ 2.17354134  0.15928121] 40055.6810576
##Best fit parameter for fourth trajectory [ 12.29016937   1.53546149]
##[ 2.17354134  0.15928121] 24815.0589994
##Global fit results
##Best fit parameters for first trajectory: [ 12.00170176   1.36063813]
##Best fit parameters for second trajectory: [ 12.00170176   1.40612653]
##Best fit parameters for third trajectory: [ 12.00170176   1.50332902]
##Best fit parameters for fourth trajectory: [ 12.00170176   1.48425534]
##Best fit parameters for fifth trajectory: [ 12.00170176   1.56734657]
##Best fit parameters for sixth trajectory: [ 12.00170176   1.51992515]
##[ 12.00170176   1.36063813   1.40612653   1.50332902   1.48425534
##   1.56734657   1.51992515]
##[ 0.93054248  0.09501013  0.12266872  0.12481011  0.13224654  0.11978646
##  0.13278114]
##chi_rid 20774.0343394

import numpy as np
import scipy.optimize
from pylab import *

def beer(x, p):
    return p[1]*np.exp(-p[0]*x)

##def err(p, x, y):
##    return beer(x, p) - y

def err(p, x, y, sigmay):
    return (beer(x, p) - y)/sigmay


data = genfromtxt('misure_7_20V.txt')
data1 = genfromtxt('misure_7_60V.txt')
data2 = genfromtxt('misure_7_80V.txt')

v0_trasp = 3.617
v0_osc = 3.408

ydatatrasp = data[:,1]/v0_trasp
sigmaytrasp = data[:,2]/v0_trasp
ydataosc = data[:,3][1:]/v0_osc
sigmayosc = data[:,4][1:]/v0_osc
xdata = data[:,0]

ydatatrasp1 = data1[:,1]/v0_trasp
sigmaytrasp1 = data1[:,2]/v0_trasp
ydataosc1 = data1[:,3]/v0_osc
sigmayosc1 = data1[:,4]/v0_osc
xdata1 = data1[:,0]

ydatatrasp2 = data2[:,1]/v0_trasp
sigmaytrasp2 = data2[:,2]/v0_trasp
ydataosc2 = data2[:,3]/v0_osc
sigmayosc2 = data2[:,4]/v0_osc
xdata2 = data2[:,0]

p1 = [10, 4.5]
p2 = [10, 4.0]

p3 = [10, 4.5]
p4 = [10, 4.0]

p5 = [10, 4.5]
p6 = [10, 4.0]

print("Independent fitting")

p_best1, pcov1, infodict1, errmsg1, success1 = scipy.optimize.leastsq(err, p1, args=(xdata, ydatatrasp, sigmaytrasp) , full_output=1)
s_sq1 = (err(p_best1, xdata, ydatatrasp, sigmaytrasp)**2).sum()/(len(ydatatrasp)-len(p1))
pcov = pcov1 * s_sq1
var = sqrt(pcov.diagonal())
print("Best fit parameter for first trajectory sigmay", p_best1)
print(var, s_sq1)

p_best2, pcov2, infodict2, errmsg2, success2  = scipy.optimize.leastsq(err, p2, args=(xdata[1:], ydataosc, sigmayosc), full_output=1)
s_sq2 = (err(p_best2, xdata[1:], ydataosc, sigmayosc)**2).sum()/(len(ydataosc)-len(p2))
pcov = pcov2 * s_sq2
var = sqrt(pcov.diagonal())
print("Best fit parameter for second trajectory", p_best2)
print(var, s_sq2)

p_best3,  pcov3, infodict3, errmsg3, success3  = scipy.optimize.leastsq(err, p3, args=(xdata1, ydatatrasp1, sigmaytrasp1), full_output=1)
s_sq3 = (err(p_best3, xdata1, ydatatrasp1, sigmaytrasp1)**2).sum()/(len(ydatatrasp1)-len(p3))
print("Best fit parameter for third trajectory", p_best3)
print(var, s_sq3)

p_best4,  pcov4, infodict4, errmsg4, success4  = scipy.optimize.leastsq(err, p4, args=(xdata1, ydataosc1, sigmayosc1), full_output=1)
s_sq4 = (err(p_best4, xdata1, ydataosc1, sigmayosc1)**2).sum()/(len(ydataosc1)-len(p4))
print("Best fit parameter for fourth trajectory", p_best4)
print(var, s_sq4)

p_best5,  pcov5, infodict5, errmsg5, success5  = scipy.optimize.leastsq(err, p5, args=(xdata2, ydatatrasp2, sigmaytrasp2), full_output=1)
s_sq5 = (err(p_best5, xdata2, ydatatrasp2, sigmaytrasp2)**2).sum()/(len(ydatatrasp2)-len(p5))
print("Best fit parameter for fourth trajectory", p_best5)
print(var, s_sq5)

p_best6,  pcov6, infodict6, errmsg6, success6  = scipy.optimize.leastsq(err, p6, args=(xdata2, ydataosc2, sigmayosc2), full_output=1)
s_sq6 = (err(p_best6, xdata2, ydataosc2, sigmayosc2)**2).sum()/(len(ydataosc2)-len(p6))
print("Best fit parameter for fourth trajectory", p_best6)
print(var, s_sq6)



def err_global(p, x1, y1, sigmay1, x2, y2, sigmay2, x3, y3, sigmay3, x4, y4, sigmay4, x5, y5, sigmay5, x6, y6, sigmay6):#in p1 i parametri del primo fit, in p2 quelli del secondo. segna quelli in comune 
    p1 =  [p[0], p[1]]
    p2 =  [p[0], p[2]]
    p3 =  [p[0], p[3]]
    p4 =  [p[0], p[4]]
    p5 =  [p[0], p[5]]
    p6 =  [p[0], p[6]]
    err1 = err(p1, x1, y1, sigmay1)
    err2 = err(p2, x2, y2, sigmay2)
    err3 = err(p3, x3, y3, sigmay3)
    err4 = err(p4, x4, y4, sigmay4)
    err5 = err(p5, x5, y5, sigmay5)
    err6 = err(p6, x6, y6, sigmay6)
    return np.concatenate((err1, err2, err3, err4, err5, err6))

p_global = [10, 4.5,  4, 4.5, 4.0, 4.5, 4.0] #in un unico array tutti i parametri delle curve
p_best, pcov, infodict, errmsg, success = scipy.optimize.leastsq(err_global, p_global, args=(xdata, ydatatrasp, sigmaytrasp, xdata[1:], ydataosc, sigmayosc, xdata1, ydatatrasp1, sigmaytrasp1, xdata1, ydataosc1, sigmayosc1,xdata2, ydatatrasp2, sigmaytrasp2, xdata2, ydataosc2, sigmayosc2), full_output=1)
s_sq = (err_global(p_best, xdata, ydatatrasp, sigmaytrasp, xdata[1:], ydataosc, sigmayosc, xdata1, ydatatrasp1, sigmaytrasp1, xdata1, ydataosc1, sigmayosc1, xdata2, ydatatrasp2, sigmaytrasp2, xdata2, ydataosc2, sigmayosc2)**2).sum()/(6*len(ydatatrasp)-len(p_global))
pcov = pcov * s_sq
var = sqrt(pcov.diagonal())


p_best_1 = array([p_best[0], p_best[1]])
p_best_2 = array([p_best[0], p_best[2]])
p_best_3 = array([p_best[0], p_best[3]])
p_best_4 = array([p_best[0], p_best[4]])
p_best_5 = array([p_best[0], p_best[5]])
p_best_6 = array([p_best[0], p_best[6]])
print("Global fit results")
print("Best fit parameters for first trajectory:", p_best_1)
print("Best fit parameters for second trajectory:", p_best_2)
print("Best fit parameters for third trajectory:", p_best_3)
print("Best fit parameters for fourth trajectory:", p_best_4)
print("Best fit parameters for fifth trajectory:", p_best_5)
print("Best fit parameters for sixth trajectory:", p_best_6)
print(p_best)
print(var)
print('chi_rid', s_sq)


grid(which='major')
rc('font', size=16)

##plot(xdata, ydatatrasp, linestyle='None', marker='o', color="red", mec='None', label='trasp')
##plot(xdata[1:], ydataosc, linestyle='None', marker='o', color="blue", mec='None',label='osc')
##t = linspace(0.001,0.25, 100)
##plot(t, beer(t, p1), color="red")
##plot(t, beer(t, p_best_1), color="red", linestyle='--', linewidth=1.5)
##plot(t, beer(t, p_best_2), color="blue", linestyle='--', linewidth=1.5)
##plot(t, beer(t, p2), color="blue")
###yscale('log')
##legend(loc=3, fontsize=12)
##xlabel('Concentrazione')
##ylabel(r'Tensione V [V]')
##title("Beer-Lambert 7.20V - fit")
##savefig('concentr_7_20_fit.png', dpi=400)
##show()

