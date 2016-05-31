from pylab import *  
from scipy import * 
from scipy import optimize
from scipy import misc

data = genfromtxt('LEDwavelength_analog_loge.txt')

data2 = genfromtxt('ws7ok_extended.txt')



ydata = data[:,1]
sigmay = data[:,2]
xdata = data[:,0]

ydata_th = data2[:,1]
xdata_th = data2[:,0]


grid(which='major')
rc('font', size=15)
#errorbar(xdata, ydata, sigmay, linestyle='None', marker='s', color="red", mec='None',label='led')
plot(xdata_th, ydata_th, linestyle='--', linewidth='2', color='b', label='th')
#legend(loc=3, fontsize=12)
xlabel('Wavelength [nm]')
ylabel(r'$Log_e (CH1/CH2)$')
xlim(300,1000)
errorbar(xdata, ydata, sigmay, linestyle="None",marker="s", color="red", mec='None',label='led')
title("LED + calibrazione 'estesa' - sensore analogico") 
###savefig('C:\Python33\Fuso\filtro_RC\grafico1.png', dpi=200) 
savefig('calibrazione_LED_extended.png', dpi=400)
show()
