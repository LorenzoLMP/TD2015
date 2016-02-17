from pylab import *  
from scipy import *
from scipy import optimize
from scipy import misc

data = genfromtxt('col_mon_precisi_3.txt')
vin = data[:,0]

vout = data[:,1]

xdata = vin
ydata = vout


###Parte per plot dati
#grid('on', which = "both")
#title("segnale fotodiodo luce ambientale", size = 15)
#plot(xdata, ydata, linestyle="None",marker=".", color="black", markersize= 10)
##title("LED880", size = 15)
##errorbar(xdata, ydata, sigmay, sigmax,  linestyle="None", color="black")
##yscale('log')
###xlim(80,30000)
#xlabel(r'$vin  V$')
#ylabel(r'$vout [V]$')
#grid('on', which = "both")
##
##
####freq_tagl = r'$f_{C} =  8.77 \pm 0.09 kHz $'
####text(xdata.min()*1, 65, freq_tagl, family='serif', style='italic', size=15)
####
####gain = r'$G =  97  \pm  2 $'
####text(xdata.min()*1, 55, gain, family='serif', style='italic', size=15)
####
####prod = r'$G*f_{C} =  (850  \pm  30) kHz $'
####text(xdata.min()*1, 45, prod, family='serif', style='italic', size=15)
##
##savefig('plot_LED880.png', dpi=400)
#show()

sp = fft(ydata , len(ydata))
#sp[0] = 0
#sp = delete(sp1, 0)
#del sp[0]
#sp = sp1 - sp1[0]
#freq = fftfreq(xdata.shape[-1])
freq = fftfreq(len(xdata), d=0.0005)
#xlim(0,10)
#ylim(0,3)
#yscale('log')
ps = abs(sp)**2
idx = argsort(freq)
plot(freq[idx], ps[idx])
show()
