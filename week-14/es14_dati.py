from pylab import *  
from scipy import * 
from scipy import optimize
from scipy import misc

data = genfromtxt('es14_9600baud_traing_4hz.txt')

ydata1 = data[202:231]
ydata = ydata1*5.07/1023
xdata = linspace(0, len(ydata)-1, len(ydata))
#ydata1 = data[:,1]
#ydata = ydata1*4
#sigmay = 4
fig, ax1 = subplots()
rc('font', size=16)
ax1.set_xlabel(r'$time$')
ax1.set_ylabel(r'$Volt [V] $')
minorticks_on()


#Attivare per scala bilog
#xscale('log');
#yscale('log')
#xlim(10,4200)
#ylim(-0.001,0.001)
grid(which='major')

############################################################
#Parte per plot dati

def fitfunc(x): 
	return ydata[0]+x*(ydata[28]-ydata[0])/(28)

t = linspace(0,30,200)
plot(xdata, ydata, linestyle="None",marker="o", color="red")
plot(t, fitfunc(t), color="blue")
hlines(4.5*0.105, 0, 29, colors='red',linestyle='--')
hlines(0.5*0.105, 0, 29, colors='red',linestyle='--')


s = []
for i in range(len(xdata)):
    s.append(i)
s = array(s)
def scarto(x): 
    return 10000*(fitfunc(x)-ydata[x])**2
bar(s, scarto(s), color="black")
ax2 = ax1.twinx()
ax2.set_ylabel(r'Scarto quadratico(*$10^4$) $[V^2]$', color='black')
##errorbar(xdata, ydata, sigmay, sigmax, linestyle="None",marker="o", color="black")
title("Hw. 4 - scarti campionamento") 
###savefig('C:\Python33\Fuso\filtro_RC\grafico1.png', dpi=200) 
savefig('hw3_triang.png', dpi=400)
show()

############################################################

#Parte per il fit
##
##def fitfunc(x, *par): 
##	return par[0] +  x/par[1]
##
##p0 = [0,40] #metti il valore inizialeee
##
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
##	S = S + ((((ydata[i]- errore(xdata[i]))/sigmay)**2))
##print() 
##print('Il chi quadro vale: ') 
##print(S) 
##print("Degrees of freedom:")
##deg = (len(ydata)-len(p)) 
##print(len(ydata)-len(p))
##
##chiquadro  = r'$\chi^{2}$: $ %s $'%(round(S,1))  
##degfreedom = r'Deg. of freedom: $ %s $' %(deg)
##intercetta = r'intercetta: $ %s  \pm  %s  \;Sample/s$' %(round(p[0],3),round(var[0],3))
##pendenza = r'bit/sample: $ %s  \pm  %s $' %(round(p[1],3),round(var[1],3))
##
##text(xdata.min()*1, ydata.max()*0.87, chiquadro, family='serif', style='italic', size=15) 
##text(xdata.min()*1, ydata.max()*0.82, degfreedom, family='serif', style='italic', size=15)
##text(xdata.min()*1, ydata.max()*0.76, pendenza, family='serif', style='italic', size=15)
##text(xdata.min()*1, ydata.max()*0.70, intercetta, family='serif', style='italic', size=15)
##
##
##time = linspace(9600,120000,200) 
##plot(time, fitfunc(time, *p), color='black', linewidth = 1.1, label='fitfunc')
##plot(time, fitfunc(time, 0,40), color='blue', linewidth = 1.1, label='q=0, 1/m=40')
##legend(loc=4)
##savefig('es13_samples_vs_baud.png', dpi=400)
##show()
