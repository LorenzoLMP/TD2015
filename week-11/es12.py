from pylab import *  
from scipy import * 
from scipy import optimize
from scipy import misc

data = genfromtxt('es12_sorgente_good')
data1 = genfromtxt('es12_uscita_good')

xdata = data[:,0]
ydata = data[:,1]

xdata1 = data1[:,0]
ydata1 = data1[:,1]
#zdata = sfasa
#sigmay = ydata1/100
#sigmax = data [:,3]

#########################################
##xdata = []
##for i in range(len(xdata1)-3):
##    xdata.append(xdata1[i+3])
##
##xdata = array(xdata)
##
##ydata = []
##for i in range(len(ydata1)-3):
##    ydata.append(ydata1[i+3])
##
##ydata = array(ydata)
##
##sigmay = ydata/100

##############################################

##def fitfunc(x, *par): 
##	return par[0] + par[2]/((x+par[3])**(1 + par[1])) 
##
##p0 = [1, 2, 1, 1] #metti il valore inizialeee
##

##def fitfunc(x, *par): 
##	return par[0]*10**(-25)*x 
##
##p0 = [5] #metti il valore inizialeee


rc('font', size=15)
#xlabel(r'$frequenza [Hz]$')
#ylabel(r'$Gain $')
#minorticks_on()

#Attivare per scala bilog
#xscale('log')
#yscale('log')
#xlim(80,30000)
#ylim(35,103)

############################################################
###Parte per plot dati

#title("Bode Diagram Gain-Phase", size = 15)
#plot(xdata, ydata, linestyle="None",marker=".", color="red", markersize= 10)

subplot(2, 1,1)
title(r"Divisore per tre - sorgente/uscita", size = 15)
grid('on', which = "both")
errorbar(xdata, ydata, 0.01, 0.000005, linestyle="None", color="black")
#xscale('log')
#xlim(0.1,16)
#xlim(-1,16)
#xscale('log')
#yscale('log')
ylabel(r'Tensione $V$ [V]')
#xlabel(r'Tempo $t$ [ms]')
#grid('on', which = "both")

subplot(2,1,2)
xlabel(r'Tempo $t$ [ms]')
ylabel(r'Tensione $V$ [V]')
grid('on', which = "both")
#ylim(-1,5.5)
errorbar(xdata1, ydata1, 0.01, 0.000005, linestyle="None", color="black")

##fr = r'$ FR (I_{LED} = 14.6 mA): 2.03  \pm  0.02 [k \Omega]$'
##text(xdata.max()*0.05, ydata.max()*0.91, fr, family='serif', style='italic', size=17)
##
##
####freq_tagl = r'$f_{C} =  8.77 \pm 0.09 kHz $'
####text(xdata.min()*1, 65, freq_tagl, family='serif', style='italic', size=15)
####
#gate = r'$V_{GS} =  2V $'
#text(xdata.max()*0.1, ydata.max()*0.8, gate, family='serif', style='italic', size=18)
####
####prod = r'$G*f_{C} =  (850  \pm  30) kHz $'
####text(xdata.min()*1, 45, prod, family='serif', style='italic', size=15)
##
savefig('es12_prova.png', dpi=400)
show()

############################################################
#Parte per il fit

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
##time = linspace(0,17,200) 
##plot(time, fitfunc(time, *p), color='black', linewidth = 1.1)
##grid('on')
##errorbar(xdata, ydata, sigmay, linestyle="None", marker=".", color="red", fmt = 'o', markersize= 5)
###legend([('V_out/V_in = ' + str(round(p[0],3)) + str('+-') + str(round(var[0],3)))], prop = {'size':12})
###legend([('intercetta = ' + str(round(p[1],3)) + str('+-') + str(round(var[1],3)) + ' V')], prop = {'size':12})
##
##
##chiquadro  = r'$\chi^{2}$: $ %s $'%(round(S,1))  
##degfreedom = r'Deg. of freedom: $ %s $' %(deg)
##esponente = r'scarto pot 1: $ %s  \pm  %s $' %(round(p[1],2),round(var[1],2))
##intercetta = r'Offset: $ %s  \pm  %s E-27[J]$' %(round(p[0],3),round(var[0],3))
##
##text(xdata.max()*0.6, ydata.max()*0.90, chiquadro, family='serif', style='italic', size=15) 
##text(xdata.max()*0.6, ydata.max()*1, degfreedom, family='serif', style='italic', size=14)
##text(xdata.max()*0.6, ydata.max()*0.80, esponente, family='serif', style='italic', size=15)
###text(xdata.min()*1, ydata.max()*0.87, intercetta, family='serif', style='italic', size=15)
##
##title("Fotoresistenza vs. Corrente LED - loglog", size = 15)
##xlim(-1,16)
##xlabel(r'Corrente $I_{LED}$ [mA]')
##ylabel(r'Fotoresistenza $[k\Omega]$')
##ax = axes()
##savefig('fit_FR_vs_ill.png', dpi=400)
##
##
##show()

