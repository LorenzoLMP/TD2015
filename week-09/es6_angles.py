from pylab import *  
from scipy import * 
from scipy import optimize
from scipy import misc

data = genfromtxt('es6_angles.txt')

xdata = 90-data[:,0]
ydata = data[:,1]
sigmay = data[:,2]

##############################################


rc('font', size=15)
#xlabel(r'$frequenza [Hz]$')
#ylabel(r'$Gain $')
#minorticks_on()

#Attivare per scala bilog
#xscale('log')
#yscale('log')
#ylim(35,103)

############################################################
###Parte per plot dati
#grid('on', which = "both")
#title("Bode Diagram Gain-Phase", size = 15)
plot(xdata, ydata, linestyle="None",marker=".", color="red", markersize= 10)
title(r"Potenza $ P $ [mW] in funzione dell'angolo $ \theta $ dalla normale [°] ", size = 15)
errorbar(xdata, ydata, sigmay, linestyle="None", color="red")
#xscale('log')
#xlim(0.1,16)
#xlim(-1,16)
xlabel(r'Angolo $\theta$ [°]')
ylabel(r'Potenza $ P $ [mW]')
grid('on', which = "both")
xlim(-5,80)
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
savefig('es6_angles_plot.png', dpi=400)
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
##time = linspace(0,3,200) 
##plot(time, fitfunc(time, *p), color='black', linewidth = 1.1)
##grid('on')
##errorbar(xdata, ydata, sigmay, linestyle="None", marker=".", color="red", fmt = 'o', markersize= 5)
###legend([('V_out/V_in = ' + str(round(p[0],3)) + str('+-') + str(round(var[0],3)))], prop = {'size':12})
###legend([('intercetta = ' + str(round(p[1],3)) + str('+-') + str(round(var[1],3)) + ' V')], prop = {'size':12})
##
##
##chiquadro  = r'$\chi^{2}$: $ %s $'%(round(S,1))  
##degfreedom = r'Deg. of freedom: $ %s $' %(deg)
##esponente = r'vsoglia $ %s  \pm  %s $' %(round(p[1],2),round(var[1],2))
##intercetta = r'fattore trans $ %s  \pm  %s E-27[J]$' %(round(p[0],3),round(var[0],3))
##
##text(xdata.max()*0.6, ydata.max()*0.90, chiquadro, family='serif', style='italic', size=15) 
##text(xdata.max()*0.6, ydata.max()*1, degfreedom, family='serif', style='italic', size=14)
##text(xdata.max()*0.6, ydata.max()*0.80, esponente, family='serif', style='italic', size=15)
###text(xdata.min()*1, ydata.max()*0.87, intercetta, family='serif', style='italic', size=15)
##
##title(r"Corrente $I_{DS}$ in funzione di $V_{GS}$", size = 15)
###xlim(-1,16)
##xlabel(r'Tensione $V_{GS}$ [V]')
##ylabel(r'Corrente $I_{DS}$ [mA]')
##ax = axes()
##savefig('fit_es8.png', dpi=400)
##
##
##show()
##
