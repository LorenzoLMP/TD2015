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
s = 630

ydata_norm = []
ydata_norm2 = []
for i in range(s):
        ydata_norm.append(cr[math.modf(i/2)[1]]*r + cg[math.modf(i/2)[1]]*g + cb[math.modf(i/2)[1]]*b)
        ydata_norm2.append( (cr[math.modf(i/2)[1]]*r + cg[math.modf(i/2)[1]]*g + cb[math.modf(i/2)[1]]*b)/(cr[math.modf(i/2)[1]] + cg[math.modf(i/2)[1]] + cb[math.modf(i/2)[1]])  )

ydata_norm = array(ydata_norm)
ydata_norm2 = array(ydata_norm2)
        

xdata_norm = []
for i in range(s):
        xdata_norm.append(l+i)

xdata_norm = array(xdata_norm)


xdata1 = []
for i in range(s):
        xdata1.append(xdata[i+718])
        #xdata1.append(xdata[i+718]*(1 - 30*i/(600*1348)) )
xdata1 = array(xdata1)

ydata1 = []
for i in range(s):
        ydata1.append(ydata[i+718])

ydata1 = array(ydata1)




sig_norm = []
for i in range(s):
        sig_norm.append(ydata1[i]/(cr[math.modf(i/2)[1]] + cg[math.modf(i/2)[1]] + cb[math.modf(i/2)[1]])  )

sig_norm = array(sig_norm)
##############################################

def fitfunc(x, *par): 
	return par[0]*10**(-27) + par[1]*10**(-25)*x 

p0 = [1 , 6] #metti il valore inizialeee


##def fitfunc(x, *par): 
##	return par[0]*10**(-25)*x 
##
##p0 = [5] #metti il valore inizialeee


rc('font', size=13)
#xlabel(r'$frequenza [Hz]$')
#ylabel(r'$Gain $')
#minorticks_on()

#Attivare per scala bilog
#xscale('log')
#yscale('log')
#xlim(80,30000)
#ylim(35,103)



sig_norm1 = []
for i in range(630):
        sig_norm1.append(ydata1[i]/(   (cr[math.modf(i/2)[1]])**2 + (cg[math.modf(i/2)[1]])**2 + (cb[math.modf(i/2)[1]])**2 )  )

sig_norm1 = array(sig_norm1)


############################################################
#Parte per plot dati
#grid('on', which = "both")
#title("Bode Diagram Gain-Phase", size = 15)
plot(xdata, ydata, linestyle="None",marker=".", color="black", markersize= 9, label='dati sperimentali')

plot(xdata1, sig_norm, linestyle="None",marker=".", color="red", markersize= 10, label='dati sp. lin-norm.')
plot(xdata1, sig_norm1, linestyle="None",marker=".", color="brown", markersize= 10, label='dati sp. quad-norm.')

#plot(xdata_norm, ydata_norm, linestyle="None",marker=".", color="green", markersize= 9, label='modello previsto')

#plot(xdata_norm, ydata_norm2, linestyle="None",marker=".", color="blue", markersize= 10, label='modello normalizzato')

#plot(xdata1, ydata1, linestyle="None",marker=".", color="brown", markersize= 10)
legend()
title("Photovoltaic cell - response from monitor (exp)", size = 15)
#errorbar(xdata, ydata, sigmay, sigmax,  linestyle="None", color="black")
#xscale('log')
xlim(690,1370)
ylim(0.001,0.020)
xlabel(r'Time $  [ms]$')
ylabel(r'Tensione $ [V]$')
grid('on', which = "both")


##annotate("Annotation",
##            xy=(718, 0.0075), xycoords='data',
##            xytext=(500, 0.001), textcoords='offset points',
##        arrowprops=dict(arrowstyle="->",
##                            connectionstyle="arc3"),
##            )

annotate("red",
            xy=(718, 0.0075), xycoords='data',
            xytext=(750, 0.0045), textcoords='data',
            size=20, va="center", ha="center",
            arrowprops=dict(arrowstyle="simple",
                            connectionstyle="arc3,rad=-0.4", color="r"), 
            )

annotate("green",
            xy=(926, 0.0086), xycoords='data',
            xytext=(900, 0.0050), textcoords='data',
            size=20, va="center", ha="center",
            arrowprops=dict(arrowstyle="simple",
                            connectionstyle="arc3,rad=-0.4", color="g"), 
            )

annotate("blue",
            xy=(1130, 0.0055), xycoords='data',
            xytext=(1100, 0.0035), textcoords='data',
            size=20, va="center", ha="center",
            arrowprops=dict(arrowstyle="simple",
                            connectionstyle="arc3,rad=-0.4", color="b"), 
            )


axvline(1138)
axvline(718)



#savefig('color_315_confr_modelli.png', dpi=400)
show()

############################################################
