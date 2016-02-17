from pylab import *  
from scipy import * 
from scipy import optimize
from scipy import misc

data1 = genfromtxt('es_8_led880_vin_vout_2ampio')
data2 = genfromtxt('es_8_hlmpc115_vin_vout_2ampio')
data3 = genfromtxt('es_8_hlmpc315_vin_vout_2ampio')
data4 = genfromtxt('es_8_la3366_vin_vout_2ampio')
data5 = genfromtxt('es_8_lb3333_vin_vout_2ampio')
data6 = genfromtxt('es_8_led365_vin_vout_2ampio')
data7 = genfromtxt('es_8_led450_vin_vout_2ampio')
data8 = genfromtxt('es_8_lo3336_vin_vout_2ampio')
data9 = genfromtxt('es_8_lpk376_vin_vout2_2ampio')
data10 = genfromtxt('es_8_ls3336_vin_vout_2ampio')
data11 = genfromtxt('es_8_tlihc4405_vin_vout_2ampio')
data12 = genfromtxt('es_8_wp9294_vin_vout_2ampio')

vin1 = data1[:,0]
vout1 = data1[:,1]

vin2 = data2[:,0]
vout2 = data2[:,1]
vin3 = data3[:,0]
vout3 = data3[:,1]
vin4 = data4[:,0]
vout4 = data4[:,1]
vin5 = data5[:,0]
vout5 = data5[:,1]
vin6 = data6[:,0]
vout6 = data6[:,1]
vin7 = data7[:,0]
vout7 = data7[:,1]
vin8 = data8[:,0]
vout8 = data8[:,1]
vin9 = data9[:,0]
vout9 = data9[:,1]
vin10 = data10[:,0]
vout10 = data10[:,1]
vin11 = data11[:,0]
vout11 = data11[:,1]
vin12 = data12[:,0]
vout12 = data12[:,1]

xdata = vin1
ydata = vout1

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


rc('font', size=13)
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
title("Curva Vin-Vout semilogy", size = 15)
errorbar(vin1, vout1, 0.00002, 0.002, color="black", label='led880')
errorbar(vin2, vout2, 0.00002, 0.002, color="grey", label='hlmpc115')
errorbar(vin3, vout3, 0.00002, 0.002,   color="blue", label='hlmpc315')
errorbar(vin4, vout4, 0.00002, 0.002,   color="green", label='la3366')
errorbar(vin5, vout5, 0.00002, 0.002,   color="purple", label='lb3333')
errorbar(vin6, vout6, 0.00002, 0.002,   color="red", label='led365')
errorbar(vin7, vout7, 0.00002, 0.002,   color="brown", label='led450')
errorbar(vin8, vout8, 0.00002, 0.002,  color="orange", label='lo3336')
errorbar(vin9, vout9, 0.00002, 0.002,   color="black", label='lpk376')
errorbar(vin10, vout10, 0.00002, 0.002, color="red", label='ls3336')
errorbar(vin11, vout11, 0.00002, 0.002,  color="blue", label='tlihc4405')
errorbar(vin12, vout12, 0.00002, 0.002, color="green", label='wp9294')

yscale('log')
ylim(0.0001,0.1)
xlim(-0.2, 3.3)
xlabel(r'$V_{in}  [V]$')
ylabel(r'$V_{out} [V]$')
grid('on', which = "both")


legend(loc=2)


##freq_tagl = r'$f_{C} =  8.77 \pm 0.09 kHz $'
##text(xdata.min()*1, 65, freq_tagl, family='serif', style='italic', size=15)
##
##gain = r'$G =  97  \pm  2 $'
##text(xdata.min()*1, 55, gain, family='serif', style='italic', size=15)
##
##prod = r'$G*f_{C} =  (850  \pm  30) kHz $'
##text(xdata.min()*1, 45, prod, family='serif', style='italic', size=15)

savefig('tuttiled.png', dpi=400)
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
##time = linspace(1.0,1.3,100) 
##plot(time, fitfunc(time, *p), color='black', linewidth = 1.1)
##grid('on')
##errorbar(xdata, ydata, sigmay, sigmax, linestyle="None", marker=".", color="red", fmt = 'o', markersize= 5)
###legend([('V_out/V_in = ' + str(round(p[0],3)) + str('+-') + str(round(var[0],3)))], prop = {'size':12})
###legend([('intercetta = ' + str(round(p[1],3)) + str('+-') + str(round(var[1],3)) + ' V')], prop = {'size':12})
##
##
##chiquadro  = r'$\chi^{2}$: $ %s $'%(round(S,1))  
##degfreedom = r'Deg. of freedom: $ %s $' %(deg)
##pendenza = r'$ p1:  %s  \pm  %s [V^{-1}]$' %(round(p[1],3),round(var[1],3))
##intercetta = r'$p0$: $ %s  \pm  %s [V]$' %(round(p[0],3),round(var[0],3))
##
##text(xdata.min()*1, ydata.max()*0.95, chiquadro, family='serif', style='italic', size=15) 
##text(xdata.min()*1, ydata.max()*0.99, degfreedom, family='serif', style='italic', size=14)
##text(xdata.min()*1, ydata.max()*0.91, pendenza, family='serif', style='italic', size=15)
##text(xdata.min()*1, ydata.max()*0.87, intercetta, family='serif', style='italic', size=15)
##
##title(r"LED880") 
##
##xlabel(r'$vin  [V]$')
##ylabel(r'$vout [V]$')
##ax = axes()
##savefig('led880.png', dpi=400)
##
##
##show()
