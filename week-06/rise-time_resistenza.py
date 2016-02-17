from pylab import *  
from scipy import *
from scipy import optimize
from scipy import misc

#data = genfromtxt('es4_flash_mod')
#data1 = genfromtxt('es4_signal50hz_def1')

#xdata = [1, 10, 98.2, 654, 2200, 14.8, 32.6, 67.1, 46.1]#kOhm
xdata = [1, 10, 14.8, 32.6, 46.1, 67.1, 98.2, 654, 2200]
ydata = [15, 34, 44, 88, 120, 190, 256, 176, 92]
#ydata = [15, 34, 256, 176, 92, 44, 88, 190, 120] #us
sigmax = [0.008, 0.08, 0.98, 6.54, 22, 0.148, 0.326, 0.671, 0.461]
sigmax.sort()
sigmay = []
for i in range(len(ydata)):
    sigmay.append(4)
#sigmay = array(sigmay)    

###Parte per plot dati
grid('on', which = "both")
title(r"Andamento del rise-time $[\mu s]$ in funzione di R $[k\Omega]$", size = 15)
plot(xdata, ydata, '--', color="black")
##title("LED880", size = 15)
errorbar(xdata, ydata, sigmay, sigmax, linestyle="None" , marker=".", color="red", markersize= 10)
#xscale('log')
#yscale('log')
xlim(0,120)
xlabel(r'Resistenza $[k\Omega]$')
ylabel(r's $[\mu]$s')
rc('font', size=15)
#minorticks_on()
#grid('on', which = "both")
savefig('rise_time_1-100', dpi=400)
show()


