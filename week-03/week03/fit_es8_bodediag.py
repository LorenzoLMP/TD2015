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

Vin = 0.1
#Vout = gain * Vin 
#########################################

sigmay = []
i = 0
while i < len(ydata):
        t = max(Vin/100, 2*sqrt(2)*0.002)
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

def fitfunc(x, *par): 
	return par[0]*x + par[1] 

p0 = [11 , 0.1] #metti il valore inizialeee


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
subplot(2, 1, 1)
title("Bode Diagram Gain-Phase G100", size = 15)
errorbar(xdata, ydata, sigmay, sigmax,  linestyle="None", color="black")
xscale('log')
xlim(80,30000)
#xlabel(r'$frequenza [Hz]$')
ylabel(r'$Gain $')
grid('on', which = "both")


freq_tagl = r'$f_{C} =  8.77 \pm 0.09 kHz $'
text(xdata.min()*1, 65, freq_tagl, family='serif', style='italic', size=15)

gain = r'$G =  97  \pm  2 $'
text(xdata.min()*1, 55, gain, family='serif', style='italic', size=15)

prod = r'$G*f_{C} =  (850  \pm  30) kHz $'
text(xdata.min()*1, 45, prod, family='serif', style='italic', size=15)


#savefig('C:\Python33\Fuso\filtro_RC\grafico1.png', dpi=200)
################################################################
subplot(2,1,2)
plot(xdata, zdata, linestyle="None",marker=".", color="black", markersize= 6)
#errorbar(xdata, zdata,  linestyle="None", color="black")
xscale('log')
xlabel(r'$frequenza [Hz]$')
xlim(80,30000)
ylabel(r'$Sfasamento $')
grid('on', which = "both")

savefig('es_8_bode_diag.png', dpi=400)
show()

############################################################
###Parte per il fit

##p, pcov = optimize.curve_fit(fitfunc, xdata, ydata, p0, sigmay)
##
##print() 
##print("matrice di covarianza:") 
##print(pcov) 
##var = sqrt(pcov.diagonal())
##
##
##for i in range(len(p)):
##	print('p[%s]:'%(i), p[i], '+-', var[i])
##
##def errore(x): 
##	return fitfunc(x,*p) 
##S=0
##for i in range(len(ydata)): 
##	S = S + ((((ydata[i]- errore(xdata[i]))/sigmay[i])**2))
##print() 
##print('Il chi quadro vale: ') 
##print(S) 
##print("Degrees of freedom:")
##deg = (len(ydata)-len(p)) 
##print(len(ydata)-len(p))
##
##time = linspace(-0.8,0.8,100) 
##plot(time, fitfunc(time, *p), color='black', linewidth = 1.1)
##grid('on')
##errorbar(xdata, ydata, sigmay, linestyle="None", marker=".", color="red", fmt = 'o', markersize= 5)
###legend([('V_out/V_in = ' + str(round(p[0],3)) + str('+-') + str(round(var[0],3)))], prop = {'size':12})
###legend([('intercetta = ' + str(round(p[1],3)) + str('+-') + str(round(var[1],3)) + ' V')], prop = {'size':12})
##
##
##chiquadro  = r'$\chi^{2}$: $ %s $'%(round(S,1))  
##degfreedom = r'Deg. of freedom: $ %s $' %(deg)
##pendenza = r'$V_{out}/V_{in}:  %s  \pm  %s $' %(round(p[0],3),round(var[0],3))
##intercetta = r'Offset: $ %s  \pm  %s [V]$' %(round(p[1],3),round(var[1],3))
##
##text(xdata.min()*0.9, ydata.max()*0.7, chiquadro, family='serif', style='italic', size=15) 
##text(xdata.min()*0.9, ydata.max()*0.81, degfreedom, family='serif', style='italic', size=14)
##text(xdata.min()*0.9, ydata.max()*0.6, pendenza, family='serif', style='italic', size=15)
##text(xdata.min()*0.9, ydata.max()*0.47, intercetta, family='serif', style='italic', size=15)
##
##title(r"Amplificatore non-invertente fit") 
##
##ax = axes()
##savefig('fit_non-invertente.png', dpi=400) 
##show()
