from pylab import *  
from scipy import * 
from scipy import optimize
from scipy import misc

data = genfromtxt('analog_channel_average.txt')

#data2 = genfromtxt('ws7ok.txt')



ch1 = data[:,1]
sigma1= data[:,2]
ch2 = data[:,3]
sigma2 = data[:,4]
#sigmay = data[:,2]
xdata = data[:,0]

##ydata_th = log(data2[:,1])
##xdata_th = data2[:,0]




fig, ax1 = subplots()
grid(which='major')
rc('font', size=15)
##errorbar(xdata, ydata, sigmay, linestyle='None', marker='s', color="red", mec='None',label='led')
ax1.errorbar(xdata, ch1, sigma1, linestyle='None', marker='o', color='red', label='ch1')
ax1.errorbar(xdata, ch2, sigma2, linestyle='None', marker='o', color='green', label='ch2')
#legend(loc=3, fontsize=12)
ax1.set_xlabel('Time t')
ax1.set_ylabel(r'Tensione canali [V]')
#errorbar(xdata, ydata, sigmay, sigmax, linestyle="None",marker="o", color="black")
title("Sensore analogico - colori monitor")
##for tl in ax1.get_yticklabels():
##    tl.set_color('brown')

ax2 = ax1.twinx()
frac = ch1/ch2
err_rel1 = sigma1/ch1
err_rel2 = sigma2/ch2
deltafrac = (err_rel1 + err_rel2)*frac
deltalog = abs(deltafrac/frac)
for i in range(len(deltalog)):
    if deltalog[i]>=1:
        deltalog[i] = 1
ax2.errorbar(xdata, log(abs(frac)), deltalog, linestyle='None', marker='o', color='blue', label='log(CH1/CH2)')
ax2.set_ylabel(r'log(CH1/CH2)')
for tl in ax2.get_yticklabels():
    tl.set_color('blue') 
###savefig('C:\Python33\Fuso\filtro_RC\grafico1.png', dpi=200) 

savefig('analog_segnale_log_average.png', dpi=400)
show()
