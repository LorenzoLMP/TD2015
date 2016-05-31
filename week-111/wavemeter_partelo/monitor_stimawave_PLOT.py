#red: 632(17)
#green: 552(18) 1200 ca
#blue: 503(20)


from pylab import *  
from scipy import * 
from scipy import optimize
from scipy import misc

data = genfromtxt('monitor_lambda_senzaIR2_extended.txt')
data2 = genfromtxt('analog_channel_average.txt')
#data2 = genfromtxt('ws7ok.txt')



ch1 = data[:,1]
sigma1= data2[:,2]
ch2 = data[:,2]
sigma2 = data2[:,4]
#sigmay = data[:,2]
xdata = data[:,0]

lamb = data[:,3]
deltalamb = data[:,4]
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
title("Colori monitor - stima lunghezze d'onda (no IR - estrap)")
##for tl in ax1.get_yticklabels():
##    tl.set_color('brown')

ax2 = ax1.twinx()
ax2.errorbar(xdata, lamb, deltalamb, linestyle='None', marker='o', color='blue', label='lambda')
ax2.set_ylabel(r'Wavelenght [nm]')
for tl in ax2.get_yticklabels():
    tl.set_color('blue') 
###savefig('C:\Python33\Fuso\filtro_RC\grafico1.png', dpi=200) 

savefig('monitor_stima_lunghezzaonda_senzaIR_extended.png', dpi=400)
show()
