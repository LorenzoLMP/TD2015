from pylab import *  
from scipy import * 
from scipy import optimize
from scipy import misc

data = genfromtxt('analog_colori2.txt')

#data2 = genfromtxt('ws7ok.txt')



ch1 = data[:,1]
ch2 = data[:,3]
#sigmay = data[:,2]
xdata = data[:,0]

##ydata_th = log(data2[:,1])
##xdata_th = data2[:,0]




fig, ax1 = subplots()
grid(which='major')
rc('font', size=15)
##errorbar(xdata, ydata, sigmay, linestyle='None', marker='s', color="red", mec='None',label='led')
ax1.plot(xdata, ch1, linestyle='None', marker='+', color='brown', label='ch1')
ax1.plot(xdata, ch2, linestyle='None', marker='+', color='green', label='ch2')
#legend(loc=3, fontsize=12)
ax1.set_xlabel('Time t')
ax1.set_ylabel(r'Tensione canali [V]')
#errorbar(xdata, ydata, sigmay, sigmax, linestyle="None",marker="o", color="black")
title("Sensore analogico - colori monitor")
for tl in ax1.get_yticklabels():
    tl.set_color('brown')

ax2 = ax1.twinx()
plot(xdata, log(abs(ch1/ch2)), linestyle='None', marker='o', color='blue', label='log(CH1/CH2)')
ax2.set_ylabel(r'log(CH1/CH2)')
for tl in ax2.get_yticklabels():
    tl.set_color('blue') 
###savefig('C:\Python33\Fuso\filtro_RC\grafico1.png', dpi=200) 

savefig('analog_segnale_log.png', dpi=400)
show()
