from pylab import *  
from scipy import * 
#from scipy import optimize
from scipy import misc
import numpy as np

data = genfromtxt('es11_4hz_100ms.txt')

#xdata= data[:,0]
ydata = data

rc('font', size=16)
#xlabel(r'$V_{in} [V]$')
#ylabel(r'$V_{out} [V] $')
minorticks_on()


subplot(2,1,1)
#Attivare per scala bilog
#xscale('log');yscale('log')
ylim(-1.2,1.5)
#ylim(-0.001,0.001)

t = linspace(0,20,2000)#num massimi è lin.max*2
y = sin(4*pi*t)
##z = []
##s = []
##for i in range(100):
##    z.append(y[i*20])
##    s.append(i*20/(4*pi))
num = 84
s = linspace(0,20,num) #prendo 2 punti ogni periodo
z = sin(4*pi*s)


############################################################
#Parte per plot dati

plot(t, y,marker="+", color="black")
plot(s, z, marker="+", color="blue")
##errorbar(xdata, ydata, sigmay, sigmax, linestyle="None",marker="o", color="black")
title("Esercizio 11: pochi campionamenti per periodo") 
###savefig('C:\Python33\Fuso\filtro_RC\grafico1.png', dpi=200)


plot1  = r'$plot1$: $ linspace(0,20,2000) $'
plot2  = r'$plot2$: $ linspace(0,20,%s) $' %(num)
func  = r'$f$: $ sin(4 \pi x) $'
##degfreedom = r'Deg. of freedom: $ %s $' %(deg)
##pendenza = r'$ h:  %s  \pm  %s E-34[Js]$' %(round(p[1],2),round(var[1],2))
##intercetta = r'Offset: $ %s  \pm  %s E-27[J]$' %(round(p[0],3),round(var[0],3))
##
text(5, 1.35, plot1, family='serif', style='italic', size=16) 
text(5, 1.2, plot2, family='serif', style='italic', size=16)
text(5, 1.05, func, family='serif', style='italic', size=16)
##text(xdata.min()*1, ydata.max()*0.87, intercetta, family='serif', style='italic', size=15)
##

subplot(2,1,2)
s = linspace(0,len(ydata),len(ydata))
plot(s, ydata, marker='o',color='black')


savefig('soluzione_es11_biplot.png', dpi=400)
show()

############################################################
