from pylab import *  
from scipy import * 
from scipy import misc

data = genfromtxt('analog_LED_confront_extended.txt')

ydata = data[:,1]-data[:,0]
#sigmay = data[:,2]
xdata = data[:,0]

grid(which='major')
#rc('font', size=11)
title("LED: confronto fra $\lambda_{THEO}$ (datasheet) e da calibrazione 'estesa'", fontsize='15')
rc('font', size=14)
plot(xdata, ydata, linestyle='None', marker='o', color='r', label='scarti')
hlines(0,xdata.min()-20, xdata.max()+20, colors='k', linestyles='-', linewidth='2')
vlines(xdata,0, ydata, colors='k', linestyles='-')
xlabel('Wavelength [nm]')
ylabel(r'$\lambda_{THEO} \,  - \, \lambda_{CAL}$')
xlim(430, 900)
ylim(-25, 55)
savefig('LED_confronto_extended.png', dpi=400)
show()


