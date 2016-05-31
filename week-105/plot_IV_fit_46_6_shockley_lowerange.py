from pylab import *  
from scipy import * 
from scipy import optimize
from scipy import misc


data4 = genfromtxt('46_6_midrange.txt')
data8 = genfromtxt('46_6_lowerange.txt')
data9 = genfromtxt('46_6_fullrange.txt')



ydata4 = data4[:,1]

ydata8 = data8[:,1]
ydata9 = data9[:,1]
xdata4 = data4[:,0]
xdata9=data9[:,0]
xdata8 = data8[:,0]
#sigmax = data[:,1]
#Attivare per scala bilog
#xscale('log');
#yscale('log')
#xlim(10,4200)
#ylim(-0.001,0.001)
grid(which='major')

############################################################
#Parte per plot dati

##def fitfunc(x): 
##    return (7.32 + 0.33*x)/c
##
###t = linspace(0, 3.2, 200)
##yscale('log')
rc('font', size=16)
####plot(xdata, ydata, linestyle='None', marker='s', color="red", label='15.3°')
####plot(xdata1, ydata1, linestyle='None', marker='s', color="blue", label='22.3°')
####plot(xdata2, ydata2, linestyle='None', marker='s', color="green", label='30.0°')
####plot(xdata3, ydata3, linestyle='None', marker='s', color="orange", label='38.0°')
##plot(xdata4, ydata4, linestyle='None', marker='s', color="black", label='46.6°')
####plot(xdata5, ydata5, linestyle='None', marker='s', color="brown", label='54.8°')
####plot(xdata6, ydata6, linestyle='None', marker='s', color="grey", label='62.0°')
####plot(xdata7, ydata7, linestyle='None', marker='s', color="purple", label='64.6°')
####plot(xdata8, ydata8, linestyle='None', marker='s', color="yellow", label='67.5°')
##
##legend(loc=4, fontsize=12)
##xlabel('Tensione V [V]')
##ylabel(r'Corrente I [$\mu $ A]')
###errorbar(xdata, ydata, sigmay, sigmax, linestyle="None",marker="o", color="black")
##title("Caratteristica I-V") 
#####savefig('C:\Python33\Fuso\filtro_RC\grafico1.png', dpi=200) 
###savefig('hw3_triang.png', dpi=400)
##show()

############################################################

#Parte per il fit
sigmay = 0.1
def fitfunc(x, *par): 
    return par[0]*(exp(par[1]*x)-1) 

##def fitfunc(x, *par): 
##    return par[0] + par[1]*x

p0 = [0.4, 20] #metti il valore inizialeee

p, pcov = optimize.curve_fit(fitfunc, xdata4, ydata4, p0, sigmay)

print() 
print("matrice di covarianza:") 
print(pcov) 
var = sqrt(pcov.diagonal())

print('correlazione: ')
print(pcov[0,1]/sqrt(pcov[0,0]*pcov[1,1]))

for i in range(len(p)):
	print('p[%s]:'%(i), p[i], '+-', var[i])

def errore(x): 
	return fitfunc(x,*p) 
S=0
for i in range(len(ydata4)): 
	S = S + ((((ydata4[i]- errore(xdata4[i]))/sigmay)**2))
print() 
print('Il chi quadro vale: ') 
print(S) 
print("Degrees of freedom:")
deg = (len(ydata4)-len(p)) 
print(len(ydata4)-len(p))

chiquadro  = r'$\chi^{2}_{rid}$: $ %s $'%(round(round(S,1)/deg, 1))  
degfreedom = r'Deg. of freedom: $ %s $' %(deg)
A = r'A = $I_{s}$: $ %s  \pm  %s  \; \mu A $' %(round(p[0],5),round(var[0],5))
B = r'B: $ %s  \pm  %s  [V]^{-1}$' %(round(p[1],2),round(var[1],2))
C = r'C = $I_{0}$: $ %s  \pm  %s  \; \mu A $' %(round(p[2],2),round(var[2],2))
text(xdata4.min()*0.1, 12000, chiquadro, family='serif', style='italic', size=15) 
text(xdata4.min()*0.1, 4000, degfreedom, family='serif', style='italic', size=15)
text(xdata4.min()*0.1, 1000, A, family='serif', style='italic', size=15)
text(xdata4.min()*0.1, 400, B, family='serif', style='italic', size=15)
text(xdata4.min()*0.1, 100, C, family='serif', style='italic', size=15)

##text(xdata4.min()*1, 120, chiquadro, family='serif', style='italic', size=15) 
##text(xdata4.min()*1, 110, degfreedom, family='serif', style='italic', size=15)
##text(xdata4.min()*1, 100, A, family='serif', style='italic', size=15)
##text(xdata4.min()*1, 90, B, family='serif', style='italic', size=15)
##text(xdata4.min()*1, 80, C, family='serif', style='italic', size=15)


title(r"Caratteristica I-V T=46.6° - full range", size=14.5)
xlabel('Tensione V [V]')
ylabel(r'Corrente I [$\mu $ A]')
t = linspace(0.022, 0.704, 200) 

plot(t, fitfunc(t, 0.013589, 19.4925,0.0), color='blue', linewidth = 3, label='C=0')
#plot(xdata4, ydata4, linestyle='None', marker='s', color="black", label='46.6°')
plot(xdata9, ydata9, linestyle='None', marker='s', color="black")
plot(t, fitfunc(t, *p), color='red', linewidth = 3, label='fitfunc')
yscale('log')
#errorbar(xdata, ydata, sigmay, sigmax, linestyle="None",marker="o", color="red")
legend(loc=4)
#savefig('shockley_46_6_fullcur_visualiz.png', dpi=400)
show()
