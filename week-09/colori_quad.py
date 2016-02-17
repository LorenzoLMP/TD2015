from pylab import *  
from scipy import * 
from scipy import optimize
from scipy import misc
import math

data = genfromtxt('col_mon_precisi_3.txt')
coeff = genfromtxt('coeffic_matrix_315')

xdata = data[:,0]
ydata = data[:,1]

cr = coeff[:,0]
cg = coeff[:,1]
cb = coeff[:,2]
#zdata = sfasa
#########################################

#r = (ydata[1348] + ydata[1347])/2
r = 0.0075
#g = (ydata[922] + ydata[923] + ydata[924] + ydata[925])/4
g = 0.0087
#b = (ydata[1131] + ydata[1132] + ydata[1133] + ydata[1134])/4
b = 0.00573

print('signal red = ', r)
print('signal green = ', g)
print('signal blue = ', b)

################################################

l = 718


ydata_norm = []
ydata_norm2 = []
for i in range(630):
        ydata_norm.append(    r*(cr[math.modf(i/2)[1]])**2 + g*(cg[math.modf(i/2)[1]])**2 + b*(cb[math.modf(i/2)[1]])**2 )
        ydata_norm2.append( (r*(cr[math.modf(i/2)[1]])**2 + g*(cg[math.modf(i/2)[1]])**2 + b*(cb[math.modf(i/2)[1]])**2)/(  (cr[math.modf(i/2)[1]])**2 + (cg[math.modf(i/2)[1]])**2 + (cb[math.modf(i/2)[1]])**2)  )

ydata_norm = array(ydata_norm)
ydata_norm2 = array(ydata_norm2)
        

xdata_norm = []
for i in range(630):
        xdata_norm.append(l+i)

xdata_norm = array(xdata_norm)


xdata1 = []
for i in range(630):
        xdata1.append(xdata[i+718])
        #xdata1.append(xdata[i+718]*(1 - 30*i/(600*1348)) )
xdata1 = array(xdata1)

ydata1 = []
for i in range(630):
        ydata1.append(ydata[i+718])

ydata1 = array(ydata1)




sig_norm = []
for i in range(630):
        sig_norm.append(ydata1[i]/(   (cr[math.modf(i/2)[1]])**2 + (cg[math.modf(i/2)[1]])**2 + (cb[math.modf(i/2)[1]])**2 )  )

sig_norm = array(sig_norm)
##############################################

def fitfunc(x, *par): 
	return par[0]*10**(-27) + par[1]*10**(-25)*x 

p0 = [1 , 6] #metti il valore inizialeee


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
#Parte per plot dati
#grid('on', which = "both")
#title("Bode Diagram Gain-Phase", size = 15)
plot(xdata, ydata, linestyle="None",marker=".", color="black", markersize= 9, label='dati sperimentali')

plot(xdata1, sig_norm, linestyle="None",marker=".", color="red", markersize= 9, label='dati sp. norm.')

plot(xdata_norm, ydata_norm, linestyle="None",marker=".", color="green", markersize= 9, label='modello quadratico')

plot(xdata_norm, ydata_norm2, linestyle="None",marker=".", color="blue", markersize= 9, label='modello normalizzato')

#plot(xdata1, ydata1, linestyle="None",marker=".", color="brown", markersize= 10)

title("Photovoltaic cell - response from monitor (quad)", size = 15)

annotate("red",
            xy=(718, 0.0075), xycoords='data',
            xytext=(750, 0.005), textcoords='data',
            size=20, va="center", ha="center",
            arrowprops=dict(arrowstyle="simple",
                            connectionstyle="arc3,rad=-0.4", color="r"), 
            )

annotate("green",
            xy=(926, 0.0086), xycoords='data',
            xytext=(900, 0.0055), textcoords='data',
            size=20, va="center", ha="center",
            arrowprops=dict(arrowstyle="simple",
                            connectionstyle="arc3,rad=-0.4", color="g"), 
            )

annotate("blue",
            xy=(1130, 0.0055), xycoords='data',
            xytext=(1100, 0.0040), textcoords='data',
            size=20, va="center", ha="center",
            arrowprops=dict(arrowstyle="simple",
                            connectionstyle="arc3,rad=-0.4", color="b"), 
            )



legend()


#errorbar(xdata, ydata, sigmay, sigmax,  linestyle="None", color="black")
#xscale('log')
xlim(690,1370)
ylim(0.001,0.022)
xlabel(r'time $  [ms]$')
ylabel(r'Tensione $ [V]$')
grid('on', which = "both")


##freq_tagl = r'$f_{C} =  8.77 \pm 0.09 kHz $'
##text(xdata.min()*1, 65, freq_tagl, family='serif', style='italic', size=15)
##
##gain = r'$G =  97  \pm  2 $'
##text(xdata.min()*1, 55, gain, family='serif', style='italic', size=15)
##
##prod = r'$G*f_{C} =  (850  \pm  30) kHz $'
##text(xdata.min()*1, 45, prod, family='serif', style='italic', size=15)

savefig('color_315_quadr_dati+modello.png', dpi=400)
show()

############################################################
#Parte per il fit

##p, pcov = optimize.curve_fit(fitfunc, xdata, ydata, p0, sigmaycorr)
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
##	S = S + ((((ydata[i]- errore(xdata[i]))/sigmaycorr[i])**2))
##print() 
##print('Il chi quadro vale: ') 
##print(S) 
##print("Degrees of freedom:")
##deg = (len(ydata)-len(p)) 
##print(len(ydata)-len(p))
##
##time = linspace(0.0010,0.0030,100) 
##plot(time, fitfunc(time, *p), color='black', linewidth = 1.1)
##grid('on')
##errorbar(xdata, ydata, sigmaycorr, sigmax, linestyle="None", marker=".", color="red", fmt = 'o', markersize= 5)
###legend([('V_out/V_in = ' + str(round(p[0],3)) + str('+-') + str(round(var[0],3)))], prop = {'size':12})
###legend([('intercetta = ' + str(round(p[1],3)) + str('+-') + str(round(var[1],3)) + ' V')], prop = {'size':12})
##
##
##chiquadro  = r'$\chi^{2}$: $ %s $'%(round(S,1))  
##degfreedom = r'Deg. of freedom: $ %s $' %(deg)
##pendenza = r'$ h:  %s  \pm  %s E-34[Js]$' %(round(p[1],2),round(var[1],2))
##intercetta = r'Offset: $ %s  \pm  %s E-27[J]$' %(round(p[0],3),round(var[0],3))
##
##text(xdata.min()*1, ydata.max()*0.95, chiquadro, family='serif', style='italic', size=15) 
##text(xdata.min()*1, ydata.max()*0.99, degfreedom, family='serif', style='italic', size=14)
##text(xdata.min()*1, ydata.max()*0.91, pendenza, family='serif', style='italic', size=15)
##text(xdata.min()*1, ydata.max()*0.87, intercetta, family='serif', style='italic', size=15)
##
##title(r"Planck Constant fit 60$\mu$A") 
##
##xlabel(r'$\lambda^{-1}  [nm^{-1}]$')
##ylabel(r'$\frac{qV_{F}}{c} [J]$')
##ax = axes()
##savefig('costante_planck_60ua.png', dpi=400)
##
##out_file = open("planck_newdata_60ua.txt","w")
##
##for i in range(len(ydata)):
##        out_file.write("%s\t%s\t%s\t%s\n"%(xdata[i], sigmax[i], ydata[i], sigmay[i]))
##out_file.close()
##
##show()
