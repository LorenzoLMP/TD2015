from pylab import *  
from scipy import * 
from scipy import optimize
from scipy import misc

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

#Attivare per scala bilog
#xscale('log');
#yscale('log')
#xlim(10,4200)
#ylim(-0.001,0.001)
grid(which='major')

############################################################
#Parte per plot dati

def fitfunc(x): 
    return (7.32 + 0.33*x)/c

#t = linspace(0, 3.2, 200)
#yscale('log')
rc('font', size=16)
errorbar(xdata, ydatatrasp, sigmaytrasp, linestyle='None', marker='s', markersize=7, color="red", mec='None', label='7.20V')
errorbar(xdata[1:], ydataosc, sigmayosc, linestyle='None', marker='o', markersize=7,color="red", mec='None')

errorbar(xdata1, ydatatrasp1, sigmaytrasp1, linestyle='None', marker='s', markersize=7,color="blue", mec='None', label='7.60V')
errorbar(xdata1, ydataosc1, sigmayosc1, linestyle='None', marker='o', markersize=7,color="blue", mec='None')

errorbar(xdata2, ydatatrasp2, sigmaytrasp2, linestyle='None', marker='s', markersize=7,color="green", mec='None', label='7.80V')
errorbar(xdata2, ydataosc2, sigmayosc2, linestyle='None', marker='o', markersize=7,color="green", mec='None')


legend(loc=3, fontsize=12)
xlabel('Concentrazione')
ylabel(r'$ V/V_{0} $')
#errorbar(xdata, ydata, sigmay, sigmax, linestyle="None",marker="o", color="black")
title("Beer-Lambert 7.20-7.60-7.80V") 
###savefig('C:\Python33\Fuso\filtro_RC\grafico1.png', dpi=200) 
savefig('es9_concentr.png', dpi=400)
show()

