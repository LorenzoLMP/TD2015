from pylab import *  
from scipy import * 
from scipy import optimize
from scipy import misc

data = genfromtxt('misure_7_20V.txt')



ydatatrasp = data[:,1]
sigmaytrasp = data[:,2]
ydataosc = data[:,3]
sigmayosc = data[:,4]
xdata = data[:,0]

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
plot(xdata, ydatatrasp, linestyle='None', marker='o', color="red", mec='None', label='trasp')
plot(xdata, ydataosc, linestyle='None', marker='o', color="blue", mec='None',label='osc')


legend(loc=3, fontsize=12)
xlabel('Concentrazione')
ylabel(r'Tensione V [V]')
#errorbar(xdata, ydata, sigmay, sigmax, linestyle="None",marker="o", color="black")
title("Beer-Lambert 7.20V") 
###savefig('C:\Python33\Fuso\filtro_RC\grafico1.png', dpi=200) 
savefig('concentr_7_20.png', dpi=400)
show()
