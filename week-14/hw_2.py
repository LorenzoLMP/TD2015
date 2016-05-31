from pylab import *  
from scipy import * 
#from scipy import optimize
from scipy import misc
import numpy as np


rc('font', size=12)
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

subplot(3,2,1)
data = genfromtxt('es13_4hz_nodelay_9600baud.txt')
zdata = data[200:400]*5.07/1023
s = linspace(200,400,200)
plot(s, zdata, linestyle='none',marker='o',color='black', label='9600b')
hlines(4.5*0.105, 200, 400, colors='red',linestyle='--')
hlines(0.5*0.105, 200, 400, colors='red',linestyle='--')
xticks([])
legend(loc=1)
#################################àà
subplot(3,2,2)
data2 = genfromtxt('es13_4hz_nodelay_14400baud.txt')
zdata2 = data2[:,1][200:400]*5.07/1023
s2 = linspace(200,400,200)
plot(s2, zdata2, linestyle='none',marker='o',color='black', label='14400b')
hlines(4.5*0.105, 200, 400, colors='red',linestyle='--')
hlines(0.5*0.105, 200, 400, colors='red',linestyle='--')
xticks([])
legend(loc=1)
######################################
subplot(3,2,3)
data3 = genfromtxt('es13_4hz_nodelay_19200baud.txt')
zdata3 = data3[200:400]*5.07/1023
s3 = linspace(200,400,200)
plot(s3, zdata3, linestyle='none',marker='o',color='black', label='19200b')
hlines(4.5*0.105, 200, 400, colors='red',linestyle='--')
hlines(0.5*0.105, 200, 400, colors='red',linestyle='--')
ylabel(r'$V_{part} [V] $')
xticks([])
legend(loc=1)
#######################################
subplot(3,2,4)
data4 = genfromtxt('es13_4hz_nodelay_38400baud.txt')
zdata4 = data4[200:400]*5.07/1023
s4 = linspace(200,400,200)
plot(s4, zdata4, linestyle='none',marker='o',color='black', label='38400b')
hlines(4.5*0.105, 200, 400, colors='red',linestyle='--')
hlines(0.5*0.105, 200, 400, colors='red',linestyle='--')
xticks([])
#xticks([])
legend(loc=1)
###########################################
subplot(3,2,5)
data5 = genfromtxt('es13_4hz_nodelay_57600baud.txt')
zdata5 = data5[200:600]*5.07/1023
s5 = linspace(200,600,400)
plot(s5, zdata5, linestyle='none',marker='o',color='black', label='57600b')
hlines(4.5*0.105, 200, 600, colors='red',linestyle='--')
hlines(0.5*0.105, 200, 600, colors='red',linestyle='--')
ylim(0,0.5)
xticks([])
legend(loc=1)

##############################################
subplot(3,2,6)
data6 = genfromtxt('es13_4hz_nodelay_115200baud.txt')
zdata6 = data6[200:800]*5.07/1023
s6 = linspace(200,800,600)
plot(s6, zdata6, linestyle='none',marker='o',color='black', label='115200b')
hlines(4.5*0.105, 200, 800, colors='red',linestyle='--')
hlines(0.5*0.105, 200, 800, colors='red',linestyle='--')
xlim(200,800)
xticks([])
legend(loc=1)


savefig('hw2_multiplot.png', dpi=400)
show()

############################################################
