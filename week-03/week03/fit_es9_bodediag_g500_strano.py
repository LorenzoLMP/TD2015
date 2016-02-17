from pylab import *  
from scipy import * 
from scipy import optimize
from scipy import misc

data = genfromtxt('es9_500_005fs-0046off')

f = data[:,0]
guad = data[:,1]
sfasa = data[:,2]

xdata = f
ydata = guad
zdata = sfasa
#sigmax = data [:,3]
#sigmay = data [:,4]

for k in range (len(zdata)):
    zdata[k]=zdata[k] - 0.0006*xdata[k]

data1 = genfromtxt('es9_500_buono')

f1 = data1[:,0]
guad1 = data1[:,1]
sfasa1 = data1[:,2]

xdata1 = f1
ydata1 = guad1
zdata1 = sfasa1
#sigmax = data [:,3]
#sigmay = data [:,4]

for k in range (len(zdata1)):
    zdata1[k]=zdata1[k] - 0.0006*xdata1[k] 

#########################################

sigmay = []
i = 0
while i < len(ydata):
        t = max(0.03/100, 2*sqrt(2)*0.002)
        w = sqrt( t**2 + 0.005/(ydata[i]*0.1) )
        sigmay.append(w)
        i = i+1

sigmay = array(sigmay)


sigmax = []
i = 0
while i < len(xdata):
        s = max(0.040, xdata[i]*5*10**(-5))
        sigmax.append(s)
        i = i +1
sigmax = array(sigmax)


sigmay1 = []
i = 0
while i < len(ydata1):
        t = max(0.03/100, 2*sqrt(2)*0.002)
        w = sqrt( t**2 + 0.005/(ydata1[i]*0.1) )
        sigmay1.append(w)
        i = i+1

sigmay1 = array(sigmay1)


sigmax1 = []
i = 0
while i < len(xdata1):
        s = max(0.040, xdata1[i]*5*10**(-5))
        sigmax1.append(s)
        i = i +1
sigmax1 = array(sigmax1)

##############################################

rc('font', size=15)
#xlabel(r'$frequenza [Hz]$')
#ylabel(r'$Gain $')
minorticks_on()

#Attivare per scala bilog
#xscale('log')
#yscale('log')
#xlim(80,30000)
#ylim(0,103)

############################################################
#Parte per plot dati
#grid('on', which = "both")
#title("Bode Diagram Gain-Phase", size = 15)
#plot(xdata, ydata, linestyle="None",marker=".", color="black", markersize= 10)
subplot(2, 1, 1)
title("Bode Diagram Gain-Phase G500 fondoscala 0.05 vs 0.5", size = 15)
errorbar(xdata, ydata, sigmay, sigmax,  linestyle="None", color="black")
errorbar(xdata1, ydata1, sigmay1, sigmax1,  linestyle="None", color="blue")
xscale('log')
xlim(100,10000)
#xlabel(r'$frequenza [Hz]$')
ylabel(r'$Gain $')
grid('on', which = "both")


##freq_tagl = r'$f_{C} =  1.64  \pm  0.04 kHz $'
##text(xdata.min()*1.5, 300, freq_tagl, family='serif', style='italic', size=15)
##
##gain = r'$G =  540 \pm  2 $'
##text(xdata.min()*1.5, 200, gain, family='serif', style='italic', size=15)
##
##prod = r'$G*f_{C} =  (887  \pm  30) kHz $'
##text(xdata.min()*1.5, 100, prod, family='serif', style='italic', size=15)


#savefig('C:\Python33\Fuso\filtro_RC\grafico1.png', dpi=200)
################################################################
subplot(2,1,2)
plot(xdata, zdata, linestyle="None",marker=".", color="black", markersize= 6)
plot(xdata1, zdata1, linestyle="None",marker=".", color="blue", markersize= 6)
#errorbar(xdata, zdata,  linestyle="None", color="black")
xscale('log')
xlabel(r'$frequenza [Hz]$')
#xlim(80,30000)
ylabel(r'$Sfasamento $')
grid('on', which = "both")

savefig('es_9_bode_g500_strano_bi.png', dpi=400)
show()
