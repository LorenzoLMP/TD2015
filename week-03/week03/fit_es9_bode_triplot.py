from pylab import *  
from scipy import * 
from scipy import optimize
from scipy import misc

data = genfromtxt('es8_0_1')

f = data[:,0]
guad = data[:,1]
sfasa = data[:,2]

xdata = f
ydata = guad
zdata = sfasa
#sigmax = data [:,3]
#sigmay = data [:,4]

#########################################

sigmay = []
i = 0
while i < len(ydata):
        t = max(0.1/100, 2*sqrt(2)*0.002)
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

##############################################

rc('font', size=15)
#xlabel(r'$frequenza [Hz]$')
#ylabel(r'$Gain $')
minorticks_on()

#Attivare per scala bilog
#xscale('log')
#yscale('log')
#xlim(80,30000)
#ylim(35,103)

############################################################
#Parte per plot dati
#grid('on', which = "both")
#title("Bode Diagram Gain-Phase", size = 15)
#plot(xdata, ydata, linestyle="None",marker=".", color="black", markersize= 10)



subplot(3, 1, 1)

title("Bode Diagram Gain-Phase G100-G300-G500", size = 15)
errorbar(xdata, ydata, sigmay, sigmax,  linestyle="None", color="black")
xscale('log')
xlim(90,30000)
ylabel(r'$Gain $')
grid('on', which = "both")


freq_tagl = r'$f_{C} =  8.77 \pm 0.09 kHz $'
text(xdata.min()*1, 73, freq_tagl, family='serif', style='italic', size=15)

gain = r'$G =  97  \pm  2 $'
text(xdata.min()*1, 63, gain, family='serif', style='italic', size=15)

prod = r'$G*f_{C} =  (850  \pm  30) kHz $'
text(xdata.min()*1, 55, prod, family='serif', style='italic', size=15)


################################################################
data = genfromtxt('es9_300')

f2 = data[:,0]
guad2 = data[:,1]


xdata2 = f2
ydata2 = guad2

sigmay2 = []
i = 0
while i < len(ydata2):
        t = max(0.05/100, 2*sqrt(2)*0.002)
        w = sqrt( t**2 + 0.005/(ydata2[i]*0.1) )
        sigmay2.append(w)
        i = i+1

sigmay2 = array(sigmay2)


sigmax2 = []
i = 0
while i < len(xdata2):
        s = max(0.040, xdata2[i]*5*10**(-5))
        sigmax2.append(s)
        i = i +1
sigmax2 = array(sigmax2)

subplot(3,1,2)
errorbar(xdata2, ydata2, sigmay2, sigmax2, linestyle="None", color="black")
#errorbar(xdata, zdata,  linestyle="None", color="black")
xscale('log')
#xlabel(r'$frequenza [Hz]$')
xlim(90,30000)
ylabel(r'$Gain$')
grid('on', which = "both")

freq_tagl = r'$f_{C} =  2.68  \pm  0.05 kHz $'
text(xdata.min()*1, 200, freq_tagl, family='serif', style='italic', size=15)

gain = r'$G =  327 \pm  2 $'
text(xdata.min()*1, 145, gain, family='serif', style='italic', size=15)

prod = r'$G*f_{C} =  (880  \pm  30) kHz $'
text(xdata.min()*1, 95, prod, family='serif', style='italic', size=15)

######################################################################
subplot(3,1,3)

data = genfromtxt('es9_500_buono')

f3 = data[:,0]
guad3 = data[:,1]


xdata3 = f3
ydata3 = guad3

sigmay3 = []
i = 0
while i < len(ydata3):
        t = max(0.03/100, 2*sqrt(2)*0.002)
        w = sqrt( t**2 + 0.005/(ydata3[i]*0.1) )
        sigmay3.append(w)
        i = i+1

sigmay3 = array(sigmay3)


sigmax3 = []
i = 0
while i < len(xdata3):
        s = max(0.040, xdata3[i]*5*10**(-5))
        sigmax3.append(s)
        i = i +1
sigmax3 = array(sigmax3)

errorbar(xdata3, ydata3, sigmay3, sigmax3, linestyle="None", color="black")
#errorbar(xdata, zdata,  linestyle="None", color="black")
xscale('log')
xlabel(r'$frequenza [Hz]$')
xlim(90,30000)
ylabel(r'$Gain $')
grid('on', which = "both")

freq_tagl = r'$f_{C} =  1.64  \pm  0.04 kHz $'
text(xdata.min()*1, 300, freq_tagl, family='serif', style='italic', size=15)

gain = r'$G =  540 \pm  2 $'
text(xdata.min()*1, 200, gain, family='serif', style='italic', size=15)

prod = r'$G*f_{C} =  (890  \pm  30) kHz $'
text(xdata.min()*1, 100, prod, family='serif', style='italic', size=15)

savefig('es_9_bode_triplot.png', dpi=400)
show()
