from pylab import *  
from scipy import * 
from scipy import optimize
from scipy import misc

data = genfromtxt('es8_470k_3treni_20ms_100msret_zoom.txt')

#data = genfromtxt('es8_150k_1treno.txt')

xdata= data[:,0]
ydata1 = data[:,1]
ydata2 = data[:,3]

rc('font', size=16)
xlabel(r'$ t [0.1ms]$')
ylabel(r'$V [V] $')
minorticks_on()
grid(which='both')


#Attivare per scala bilog
#xscale('log');yscale('log')
#xlim(10,4200)
#ylim(-0.001,0.001)

############################################################
#Parte per plot dati

#plot(xdata, ydata1, linestyle="None",marker="+", color="black")
#plot(xdata, ydata2, linestyle="None",marker="+", color="red")
plot(xdata, ydata1,marker="+", color="black", label='CLK')
plot(xdata, ydata2,marker=".", color="red", label='output')
#errorbar(xdata, ydata, sigmay, sigmax, linestyle="None",marker="o", color="black")
title("Modalita' retrigger")
legend()
savefig('es8_retrigger.png', dpi=400)
show()

############################################################
