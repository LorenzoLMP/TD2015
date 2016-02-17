from pylab import *  
from scipy import *
from scipy import optimize
from scipy import misc

data = genfromtxt('es4_flash_mod')
data1 = genfromtxt('es4_signal50hz_def1')

vin = data[:,0]

vout = data[:,1]

xdata = vin/100
ydata = vout

vin1 = data1[:,0]

vout1 = data1[:,1]

xdata1 = vin1/100
ydata1 = vout1


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
freq = fftfreq(len(xdata), d=0.00005)

##subplot(2, 1, 1)
##xlim(1,10000)
##ylim(0,2.5)
###xscale('log')
##ps = abs(sp)**2
##idx = argsort(freq)
##plot(freq[idx], ps[idx])
##grid('on', which = "both")
title("Power spectrum fotodiodo luce-ambient", size = 15)
#xlabel(r'Frequenza  $[Hz]$')
#ylabel(r'Intens. segnale flash $[V^{2}]$')

#subplot(2, 1,2)

sp1 = fft(ydata1 , len(ydata1))
freq1 = fftfreq(len(xdata1), d=0.00005)
ps1 = abs(sp1)**2;idx1 = argsort(freq1);plot(freq1[idx1], ps1[idx1]);grid('on', which = "both")
xlabel(r'Frequenza  $[Hz]$')
ylabel(r'Intens. segnale ambiente $[V^{2}]$')
xlim(1,1000)
ylim(0,20)
#xscale('log')
savefig('spectral_analysis_senzaflash.png', dpi=400)
show()
#massimo.morante@gmail.com
