from pylab import *  
from scipy import * 
from scipy import optimize
from scipy import misc

data = genfromtxt('baudvs_num_acquis.txt')

xdata= data[:,0]
ydata1 = data[:,1]
ydata = ydata1*4
sigmay = 4

rc('font', size=16)
xlabel(r'$baud$')
ylabel(r'$n.samples/sec $')
minorticks_on()


#Attivare per scala bilog
#xscale('log');
#yscale('log')
#xlim(10,4200)
#ylim(-0.001,0.001)
grid(which='major')

############################################################
#Parte per plot dati

plot(xdata, ydata, linestyle="None",marker="o", color="red")
##errorbar(xdata, ydata, sigmay, sigmax, linestyle="None",marker="o", color="black")
title("N. samples/s vs baud") 
###savefig('C:\Python33\Fuso\filtro_RC\grafico1.png', dpi=200) 
##savefig('diodo_new_err.png', dpi=400)
#show()

############################################################

#Parte per il fit

def fitfunc(x, *par): 
	return par[0] +  x/par[1]

p0 = [0,40] #metti il valore inizialeee

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
	S = S + ((((ydata[i]- errore(xdata[i]))/sigmay)**2))
print() 
print('Il chi quadro vale: ') 
print(S) 
print("Degrees of freedom:")
deg = (len(ydata)-len(p)) 
print(len(ydata)-len(p))

chiquadro  = r'$\chi^{2}$: $ %s $'%(round(S,1))  
degfreedom = r'Deg. of freedom: $ %s $' %(deg)
intercetta = r'intercetta: $ %s  \pm  %s  \;Sample/s$' %(round(p[0],3),round(var[0],3))
pendenza = r'bit/sample: $ %s  \pm  %s $' %(round(p[1],3),round(var[1],3))

text(xdata.min()*1, ydata.max()*0.87, chiquadro, family='serif', style='italic', size=15) 
text(xdata.min()*1, ydata.max()*0.82, degfreedom, family='serif', style='italic', size=15)
text(xdata.min()*1, ydata.max()*0.76, pendenza, family='serif', style='italic', size=15)
text(xdata.min()*1, ydata.max()*0.70, intercetta, family='serif', style='italic', size=15)


time = linspace(9600,120000,200) 
plot(time, fitfunc(time, *p), color='black', linewidth = 1.1, label='fitfunc')
plot(time, fitfunc(time, 0,40), color='blue', linewidth = 1.1, label='q=0, 1/m=40')
legend(loc=4)
savefig('es13_samples_vs_baud.png', dpi=400)
show()
