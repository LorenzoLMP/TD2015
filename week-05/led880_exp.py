from pylab import *  
from scipy import * 
from scipy import optimize
from scipy import misc

data = genfromtxt('es_8_led880_vin_vout_2ampio')

vin = data[:,0]

vout = data[:,1]

xdata = vin
ydata = vout

#########################################

sigmay = []
i = 0
while i < len(ydata):
        sigmay.append(0.00002)
        i = i+1

sigmay = array(sigmay)


sigmax = []
i = 0
while i < len(xdata):
        sigmax.append(0.002)
        i = i +1
sigmax = array(sigmax)


##############################################

def fitfunc(x, *par): 
	return par[0]*(10**(-9))*(exp(par[1]*x) - 1) 

p0 = [1 , 6] #metti il valore inizialeee


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
###Parte per plot dati
###grid('on', which = "both")
###title("Bode Diagram Gain-Phase", size = 15)
###plot(xdata, ydata, linestyle="None",marker=".", color="black", markersize= 10)
##title("LED880", size = 15)
##errorbar(xdata, ydata, sigmay, sigmax,  linestyle="None", color="black")
##yscale('log')
###xlim(80,30000)
##xlabel(r'$vin  V$')
##ylabel(r'$vout [V]$')
##grid('on', which = "both")
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
##show()

############################################################
#Parte per il fit

p, pcov = optimize.curve_fit(fitfunc, xdata, ydata, p0, sigmay)

print() 
print("matrice di covarianza:") 
print(pcov) 
var = sqrt(pcov.diagonal())


for i in range(len(p)):
	print('p[%s]:'%(i), p[i], '+-', var[i])

def errore(x): 
	return fitfunc(x,*p) 
S=0
for i in range(len(ydata)): 
	S = S + ((((ydata[i]- errore(xdata[i]))/sigmay[i])**2))
print() 
print('Il chi quadro vale: ') 
print(S) 
print("Degrees of freedom:")
deg = (len(ydata)-len(p)) 
print(len(ydata)-len(p))

time = linspace(1.0,1.3,100) 
plot(time, fitfunc(time, *p), color='black', linewidth = 1.1)
grid('on')
errorbar(xdata, ydata, sigmay, sigmax, linestyle="None", marker=".", color="red", fmt = 'o', markersize= 5)
#legend([('V_out/V_in = ' + str(round(p[0],3)) + str('+-') + str(round(var[0],3)))], prop = {'size':12})
#legend([('intercetta = ' + str(round(p[1],3)) + str('+-') + str(round(var[1],3)) + ' V')], prop = {'size':12})


chiquadro  = r'$\chi^{2}$: $ %s $'%(round(S,1))  
degfreedom = r'Deg. of freedom: $ %s $' %(deg)
pendenza = r'$ p1:  %s  \pm  %s [V^{-1}]$' %(round(p[1],3),round(var[1],3))
intercetta = r'$p0$: $ %s  \pm  %s [V]$' %(round(p[0],3),round(var[0],3))

text(xdata.min()*1, ydata.max()*0.95, chiquadro, family='serif', style='italic', size=15) 
text(xdata.min()*1, ydata.max()*0.99, degfreedom, family='serif', style='italic', size=14)
text(xdata.min()*1, ydata.max()*0.91, pendenza, family='serif', style='italic', size=15)
text(xdata.min()*1, ydata.max()*0.87, intercetta, family='serif', style='italic', size=15)

title(r"LED880") 

xlabel(r'$vin  [V]$')
ylabel(r'$vout [V]$')
ax = axes()
savefig('led880.png', dpi=400)


show()
