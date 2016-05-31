from pylab import *  
from scipy import * 
#from scipy import optimize
from scipy import misc
import numpy as np


rc('font', size=16)
#xlabel(r'$V_{in} [V]$')
#ylabel(r'$V_{out} [V] $')
minorticks_on()
grid(which='major')
xticks([])
#subplot(2,1,1)
#Attivare per scala bilog
#xscale('log');yscale('log')
#ylim(-1.2,1.5)
#ylim(-0.001,0.001)

############################################################
#Parte per plot dati

##errorbar(xdata, ydata, sigmay, sigmax, linestyle="None",marker="o", color="black")
#title("Esercizio 11: pochi campionamenti per periodo") 
###savefig('C:\Python33\Fuso\filtro_RC\grafico1.png', dpi=200)


##plot1  = r'$plot1$: $ linspace(0,20,2000) $'
##plot2  = r'$plot2$: $ linspace(0,20,%s) $' %(num)
##func  = r'$f$: $ sin(4 \pi x) $'
##degfreedom = r'Deg. of freedom: $ %s $' %(deg)
##pendenza = r'$ h:  %s  \pm  %s E-34[Js]$' %(round(p[1],2),round(var[1],2))
##intercetta = r'Offset: $ %s  \pm  %s E-27[J]$' %(round(p[0],3),round(var[0],3))
##
##text(5, 1.35, plot1, family='serif', style='italic', size=16) 
##text(5, 1.2, plot2, family='serif', style='italic', size=16)
##text(5, 1.05, func, family='serif', style='italic', size=16)
##text(xdata.min()*1, ydata.max()*0.87, intercetta, family='serif', style='italic', size=15)
##
title("Esercizio 13 - scarto delle tensioni 9600baud")
data = genfromtxt('es13_4hz_nodelay_9600baud.txt')
zdata = data[200:400]*5.07/1023
s = linspace(200,400,200)
plot(s, zdata, linestyle='none',marker='o',color='black')
hlines(4.5*0.105, 200, 400, colors='red',linestyle='--')
hlines(0.5*0.105, 200, 400, colors='red',linestyle='--')
hlines(0.5*0.105-0.005, 200, 400, colors='red',linestyle='--')
ylabel(r'$V_{part} [V] $')
#xticks([])
#################################àà


savefig('hw2_9600baud.png', dpi=400)
show()

############################################################
