from pylab import *  
from scipy import * 
from scipy import optimize
from scipy import misc

data = genfromtxt('non-inv_0_8-21_no_rgen_2mo')

vin = data[:,0]
vout = data[:,1]

xdata = vin
ydata = vout

deltard = 9
#sigmax = data [:,3]
#sigmay = data [:,4]

#########################################

sigmay = []
i = 0
while i < len(ydata):
        t = 0.005
        sigmay.append(t)
        i = i+1

sigmay = array(sigmay)

##############################################

def fitfunc(x, *par): 
	return par[0]*x + par[1] 

p0 = [11 , 0.1] #metti il valore inizialeee


rc('font', size=16)
xlabel(r'$V_{in} [V]$')
ylabel(r'$V_{out} [V] $')
minorticks_on()

#Attivare per scala bilog
#xscale('log');yscale('log')
#xlim(10,4200)
#ylim(-0.001,0.001)

############################################################
#Parte per plot dati

##plot(xdata, ydata, linestyle="None",marker="+", color="black")
##errorbar(xdata, ydata, sigmay, sigmax, linestyle="None",marker="o", color="black")
##title("Curva caratteristica diodo n-p") 
###savefig('C:\Python33\Fuso\filtro_RC\grafico1.png', dpi=200) 
##savefig('diodo_new_err.png', dpi=400)
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

time = linspace(-0.8,0.8,100) 
plot(time, fitfunc(time, *p), color='black', linewidth = 1.1)
grid('on')
errorbar(xdata, ydata, sigmay, linestyle="None", marker=".", color="red", fmt = 'o', markersize= 5)
#legend([('V_out/V_in = ' + str(round(p[0],3)) + str('+-') + str(round(var[0],3)))], prop = {'size':12})
#legend([('intercetta = ' + str(round(p[1],3)) + str('+-') + str(round(var[1],3)) + ' V')], prop = {'size':12})


chiquadro  = r'$\chi^{2}$: $ %s $'%(round(S,1))  
degfreedom = r'Deg. of freedom: $ %s $' %(deg)
pendenza = r'$V_{out}/V_{in}:  %s  \pm  %s $' %(round(p[0],3),round(var[0],3))
intercetta = r'Offset: $ %s  \pm  %s [V]$' %(round(p[1],3),round(var[1],3))

text(xdata.min()*0.9, ydata.max()*0.7, chiquadro, family='serif', style='italic', size=15) 
text(xdata.min()*0.9, ydata.max()*0.81, degfreedom, family='serif', style='italic', size=14)
text(xdata.min()*0.9, ydata.max()*0.6, pendenza, family='serif', style='italic', size=15)
text(xdata.min()*0.9, ydata.max()*0.47, intercetta, family='serif', style='italic', size=15)

title(r"Amplificatore non-invertente fit") 

ax = axes()
savefig('fit_non-invertente.png', dpi=400) 
show()
