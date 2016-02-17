from pylab import *  
from scipy import * 
from scipy import optimize
from scipy import misc

data = genfromtxt('es17_360ohm')

xdata = data[:,0]
ydata = data[:,1]
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

sigmax = []
for i in range(len(xdata)):
    sigmax.append(0.01)

sigmax = array(sigmax)

sigmay = []
for i in range(len(ydata)):
    sigmay.append(0.005)

sigmay = array(sigmay)
##############################################

def fitfunc(x, *par): 
	return par[0] + par[1]*x 

p0 = [0, 2.5] #metti il valore inizialeee


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
#grid('on', which = "both")
#title("Bode Diagram Gain-Phase", size = 15)
#plot(xdata, ydata, linestyle="None",marker=".", color="red", markersize= 10)
title(r"Tensione source $V_{S}$ in funzione di $V_{in}$", size = 15)
errorbar(xdata, ydata, sigmay, sigmax, linestyle="None", color="red")
#xscale('log')
#xlim(0.1,16)
#xlim(-1,16)
#xscale('log')
#yscale('log')
xlabel(r'Tensione $V_{in}$ [V]')
ylabel(r'Tensione $V_{s}$ [V]')
grid('on', which = "both")

##fr = r'$ FR (I_{LED} = 14.6 mA): 2.03  \pm  0.02 [k \Omega]$'
##text(xdata.max()*0.05, ydata.max()*0.91, fr, family='serif', style='italic', size=17)
##
##
####freq_tagl = r'$f_{C} =  8.77 \pm 0.09 kHz $'
####text(xdata.min()*1, 65, freq_tagl, family='serif', style='italic', size=15)
####
##gate = r'$V_{GS} =  2V $'
##text(xdata.max()*0.1, ydata.max()*0.8, gate, family='serif', style='italic', size=18)
####
####prod = r'$G*f_{C} =  (850  \pm  30) kHz $'
####text(xdata.min()*1, 45, prod, family='serif', style='italic', size=15)
##
savefig('es17_360bis.png', dpi=400)
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
##correlazione = pcov[0][1]/sqrt(pcov[0][0]*pcov[1][1])
##print("Correlazione:")
##print(correlazione)
##
##time = linspace(0,3,200) 
##plot(time, fitfunc(time, *p), color='black', linewidth = 1.1)
##grid('on')
##errorbar(xdata, ydata, sigmay, sigmax, linestyle="None", marker=".", color="red", fmt = 'o', markersize= 5)
###legend([('V_out/V_in = ' + str(round(p[0],3)) + str('+-') + str(round(var[0],3)))], prop = {'size':12})
###legend([('intercetta = ' + str(round(p[1],3)) + str('+-') + str(round(var[1],3)) + ' V')], prop = {'size':12})
##
##
##chiquadro  = r'$\chi^{2}$: $ %s $'%(round(S,1))  
##degfreedom = r'Deg. of freedom: $ %s $' %(deg)
##pendenza = r'coeff. angolare: $ %s  \pm  %s $' %(round(p[1],3),round(var[1],3))
##intercetta = r'Offset: $ %s(%s) [mV]$' %(3,1)
##coefexp = r'$1 + \frac{R_{2}}{R_{1}} = %s(%s) $' %( 2.674, 33)
##text(xdata.min(), ydata.max()*0.90, chiquadro, family='serif', style='italic', size=15) 
##text(xdata.min(), ydata.max()*0.83, degfreedom, family='serif', style='italic', size=14)
##text(xdata.min(), ydata.max()*0.76, pendenza, family='serif', style='italic', size=15)
##text(xdata.min(), ydata.max()*0.69, coefexp, family='serif', style='italic', size=15)
##text(xdata.min(), ydata.max()*0.60, intercetta, family='serif', style='italic', size=15)
##
##title(r"Tensione source $V_{S}$ in funzione di $V_{in}$", size = 15)
###xlim(-1,16)
##xlabel(r'Tensione $V_{in}$ [V]')
##ylabel(r'Tensione $V_{s}$ [V]')
##ax = axes()
##savefig('es17_fit.png', dpi=400)
##
##
##show()

