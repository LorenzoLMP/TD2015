from pylab import *  
from scipy import * 
from scipy import optimize
from scipy import misc

data = genfromtxt('offset_dati_graf.txt')

res = data[:,0]
voff = data[:,1]
sigmay = data[:,2]

xdata = res
ydata = voff

#sigmax = data [:,3]
#sigmay = data [:,4]

#########################################
sigmax = []
i = 0
while i < len(xdata):
        t = xdata[i]*0.05
        sigmax.append(t)
        i = i+1

sigmax = array(sigmax)


sigmay2 = []
i = 0
while i < len(xdata):
        t = sqrt(  (sigmay[i])**2 + (sigmax[i]*0.0038)**2   )
        sigmay2.append(t)
        i = i+1

sigmay2 = array(sigmay2)
##############################################

def fitfunc(x, *par): 
	return par[0]*x + par[1] 

p0 = [0.005 , 0.1] #metti il valore inizialeee


rc('font', size=16)
xlabel(r'$Resistenze R_{2} [k\Omega]$')
ylabel(r'$V_{off} [mV] $')
minorticks_on()

#Attivare per scala bilog
#xscale('log');
#yscale('log')
#xlim(10,4200)
#ylim(-0.001,0.001)

############################################################
#Parte per plot dati

##plot(xdata, ydata, linestyle="None",marker="+", color="black")
#errorbar(xdata, ydata, sigmay, linestyle="None",marker="o", color="black")
#grid('on')
#title("Plot offset opamp") 
##savefig('C:\Python33\Fuso\filtro_RC\grafico1.png', dpi=200) 
#savefig('plot_offset.png', dpi=400)
#show()

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

time = logspace(-1,3.5,500)
xscale('log')
plot(time, fitfunc(time, *p), color='black', linewidth = 1.1)
grid('on')
errorbar(xdata, ydata, sigmay, sigmax, linestyle="None", marker=".", color="red", fmt = 'o', markersize= 9)
##legend([('V_out/V_in = ' + str(round(p[0],3)) + str('+-') + str(round(var[0],3)))], prop = {'size':12})
##legend([('intercetta = ' + str(round(p[1],3)) + str('+-') + str(round(var[1],3)) + ' V')], prop = {'size':12})


chiquadro  = r'$\chi^{2}$: $ %s $'%(round(S,1))  
degfreedom = r'Deg. of freedom: $ %s $' %(deg)
pendenza = r'$pendenza:  %s  \pm  %s [mV/k\Omega]$' %(round(p[0],4),round(var[0],4))
intercetta = r'Offset: $ %s  \pm  %s [mV]$' %(round(p[1],4),round(var[1],4))

text(xdata.max()*0.0001, ydata.max()*1.1, chiquadro, family='serif', style='italic', size=15) 
text(xdata.max()*0.0001, ydata.max()*1.3, degfreedom, family='serif', style='italic', size=14)
text(xdata.max()*0.0001, ydata.max()*0.9, pendenza, family='serif', style='italic', size=15)
text(xdata.max()*0.0001, ydata.max()*0.70, intercetta, family='serif', style='italic', size=15)

title("Offset Voff:R2 - fit (scala semilogx)") 

ax = axes()
savefig('fit_offset.png', dpi=400) 
show()

