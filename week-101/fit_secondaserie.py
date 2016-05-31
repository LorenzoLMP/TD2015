from pylab import *  
from scipy import * 
from scipy import optimize
from scipy import misc

data = genfromtxt('seconda_serie.txt')


ydata = data[:,2]
sigmay = data[:,3]
xdata = data[:,0]
sigmax = data[:,1]
c = 0.299792458
#Attivare per scala bilog
#xscale('log');
#yscale('log')
#xlim(10,4200)
#ylim(-0.001,0.001)
grid(which='major')

############################################################
#Parte per plot dati
##
##def fitfunc(x): 
##    return (7.32 + 0.33*x)/c
##
##t = linspace(0, 3.2, 200)
##plot(t, fitfunc(t), color="red")
##
##
##errorbar(xdata, ydata, sigmay, sigmax, linestyle="None",marker="o", color="black")
##title("Indice rifrazione acqua - prima serie") 
#####savefig('C:\Python33\Fuso\filtro_RC\grafico1.png', dpi=200) 
###savefig('hw3_triang.png', dpi=400)
##show()

############################################################

#Parte per il fit

def fitfunc(x, *par): 
    return (5.00 + (par[1] - 1)*x)/c + par[0]

p0 = [5, 1.5] #metti il valore inizialeee

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

chiquadro  = r'$\chi^{2}$: $ %s $'%(round(S,1))  
degfreedom = r'Deg. of freedom: $ %s $' %(deg)
intercetta = r'$\Delta T_{ret}$: $ %s  \pm  %s  \; ns $' %(round(p[0],2),round(var[0],2))
pendenza = r'$n_{a}$: $ %s  \pm  %s $' %(round(p[1],2),round(var[1],2))

text(xdata.min()*1, ydata.max()*1, chiquadro, family='serif', style='italic', size=15) 
text(xdata.min()*1, 25.2, degfreedom, family='serif', style='italic', size=15)
text(xdata.min()*1, 25.0, pendenza, family='serif', style='italic', size=15)
text(xdata.min()*1, 24.8, intercetta, family='serif', style='italic', size=15)

title("Indice rifrazione acqua - seconda serie $K = 5.00(2)$ [m]")
xlabel(r'Cammino ottico in acqua $D$ [m]')
ylabel(r'$ \Delta T$ [ns]') 
t = linspace(0, 3.2, 200) 
plot(t, fitfunc(t, *p), color='black', linewidth = 1.1, label='fitfunc')
errorbar(xdata, ydata, sigmay, sigmax, linestyle="None",marker="o", color="red")
legend(loc=4)
savefig('indice_secondaserie_tret.png', dpi=400)
show()
