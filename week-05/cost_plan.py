from pylab import *  
from scipy import * 
from scipy import optimize
from scipy import misc

data = genfromtxt('planck_constant.txt')

v = data[:,0]
lamb = data[:,2]
#sfasa = data[:,2]

xdata1 = lamb
ydata1 = v
#zdata = sfasa
sigmay1 = data [:,1]
sigmax1 = data [:,3]

q = 1.602176565E-19
deltaq = 0.000000035E-19

c = 299792458
#Vout = gain * Vin 
#########################################

ydata = []
i = 0
while i < len(ydata1):
        t = q*v[i]/c
        ydata.append(t)
        i = i+1

ydata = array(ydata)

xdata = []
i = 0
while i < len(xdata1):
        t = 1/xdata1[i]
        xdata.append(t)
        i = i+1

xdata = array(xdata)



sigmay = []
i = 0
while i < len(ydata):
        a = sigmay1[i]/v[i]
        b = deltaq/q
        w = sqrt( a**2 + b**2 )
        sigmay.append(w*ydata[i])
        i = i+1

sigmay = array(sigmay)


sigmax = []
i = 0
while i < len(xdata1):
        s = sigmax1[i]/(xdata1[i]**2)
        sigmax.append(s)
        i = i +1
sigmax = array(sigmax)

##############################################

def fitfunc(x, *par): 
	return par[0]*10**(-27) + par[1]*10**(-25)*x 

p0 = [1 , 5] #metti il valore inizialeee


rc('font', size=15)
#xlabel(r'$frequenza [Hz]$')
#ylabel(r'$Gain $')
minorticks_on()

#Attivare per scala bilog
#xscale('log')
#yscale('log')
#xlim(80,30000)
#ylim(35,103)

############################################################
###Parte per plot dati
###grid('on', which = "both")
###title("Bode Diagram Gain-Phase", size = 15)
###plot(xdata, ydata, linestyle="None",marker=".", color="black", markersize= 10)
##title("Planck Constant fit", size = 15)
##errorbar(xdata, ydata, sigmay, sigmax,  linestyle="None", color="black")
###xscale('log')
###xlim(80,30000)
##xlabel(r'$\lambda^{-1}  [nm^{-1}]$')
##ylabel(r'$\frac{qV}{c} [J]$')
##grid('on', which = "both")
##
##
####freq_tagl = r'$f_{C} =  8.77 \pm 0.09 kHz $'
####text(xdata.min()*1, 65, freq_tagl, family='serif', style='italic', size=15)
####
####gain = r'$G =  97  \pm  2 $'
####text(xdata.min()*1, 55, gain, family='serif', style='italic', size=15)
####
####prod = r'$G*f_{C} =  (850  \pm  30) kHz $'
####text(xdata.min()*1, 45, prod, family='serif', style='italic', size=15)
##
##savefig('plot_planck.png', dpi=400)
##show()

############################################################
###Parte per il fit

p, pcov = optimize.curve_fit(fitfunc, xdata, ydata, p0, sigmay)

print() 
print("matrice di covarianza:") 
print(pcov) 
var = sqrt(pcov.diagonal())


for i in range(len(p)):
	print('p[%s]:'%(i), p[i], '+-', var[i])

def errore(x): 
	return fitfunc(x,*p) 
S=0
for i in range(len(ydata)): 
	S = S + ((((ydata[i]- errore(xdata[i]))/sigmay[i])**2))
print() 
print('Il chi quadro vale: ') 
print(S) 
print("Degrees of freedom:")
deg = (len(ydata)-len(p)) 
print(len(ydata)-len(p))

time = linspace(0.0015,0.0023,100) 
plot(time, fitfunc(time, *p), color='black', linewidth = 1.1)
grid('on')
errorbar(xdata, ydata, sigmay, linestyle="None", marker=".", color="red", fmt = 'o', markersize= 5)
#legend([('V_out/V_in = ' + str(round(p[0],3)) + str('+-') + str(round(var[0],3)))], prop = {'size':12})
#legend([('intercetta = ' + str(round(p[1],3)) + str('+-') + str(round(var[1],3)) + ' V')], prop = {'size':12})


chiquadro  = r'$\chi^{2}$: $ %s $'%(round(S,1))  
degfreedom = r'Deg. of freedom: $ %s $' %(deg)
pendenza = r'$ h:  %s  \pm  %s [Js]$' %(round(p[1],3),round(var[1],3))
intercetta = r'Offset: $ %s  \pm  %s E-[J]$' %(round(p[0],3),round(var[0],3))

text(xdata.min()*1, ydata.max()*0.95, chiquadro, family='serif', style='italic', size=15) 
text(xdata.min()*1, ydata.max()*0.99, degfreedom, family='serif', style='italic', size=14)
text(xdata.min()*1, ydata.max()*0.91, pendenza, family='serif', style='italic', size=15)
text(xdata.min()*1, ydata.max()*0.87, intercetta, family='serif', style='italic', size=15)

title(r"Planck Constant fit") 

xlabel(r'$\lambda^{-1}  [nm^{-1}]$')
ylabel(r'$\frac{qV}{c} [J]$')
ax = axes()
savefig('costante_planck.png', dpi=400) 
show()
