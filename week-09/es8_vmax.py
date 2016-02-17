from pylab import *  
from scipy import * 
from scipy import optimize
from scipy import misc

data = genfromtxt('es8_corrmax_potmax.txt')

xdata = data[:,2]
ydata = data[:,4]
sigmay = data[:,5]
sigmax = data[:,3]

##############################################



#xlabel(r'$frequenza [Hz]$')
#ylabel(r'$Gain $')
#minorticks_on()

#Attivare per scala bilog
#xscale('log')
#yscale('log')
#ylim(35,103)


def fitfunc(x, *par): 
	return par[0] + log(x)*par[1]

p0 = [0.2,0.05] #metti il valore inizialeee


############################################################
#####Parte per plot dati
###grid('on', which = "both")
###title("Bode Diagram Gain-Phase", size = 15)
###plot(xdata, ydata, linestyle="None",marker=".", color="red", markersize= 10)
##title(r"Potenza $ P $ [mW] in funzione della distanza $r$ [cm] ", size = 15)
##errorbar(xdata, ydata, sigmay, sigmax, linestyle="None", color="red")
###xscale('log')
###xlim(0.1,16)
###xlim(-1,16)
##xlabel(r'Distanza $r$ [cm]')
##ylabel(r'Potenza $ P $ [mW]')
##grid('on', which = "both")
###xlim(-5,80)
####fr = r'$ FR (I_{LED} = 14.6 mA): 2.03  \pm  0.02 [k \Omega]$'
####text(xdata.max()*0.05, ydata.max()*0.91, fr, family='serif', style='italic', size=17)
####
####
######freq_tagl = r'$f_{C} =  8.77 \pm 0.09 kHz $'
######text(xdata.min()*1, 65, freq_tagl, family='serif', style='italic', size=15)
######
###gate = r'$V_{GS} =  2V $'
###text(xdata.max()*0.1, ydata.max()*0.8, gate, family='serif', style='italic', size=18)
######
######prod = r'$G*f_{C} =  (850  \pm  30) kHz $'
######text(xdata.min()*1, 45, prod, family='serif', style='italic', size=15)
####
##savefig('es7_prova_pot_dist.png', dpi=400)
##show()
##########################################################







############################################################
#Parte per il fit
rc('font', size=15)
fig, ax1 = subplots()
#ax2 = ax1.twinx()
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

time = linspace(0.001,2,200) 
ax1.plot(time, fitfunc(time, *p), color='black', linewidth = 1.1)

ax1.errorbar(xdata, ydata, sigmay, sigmax, linestyle="None", color="red")
#legend([('V_out/V_in = ' + str(round(p[0],3)) + str('+-') + str(round(var[0],3)))], prop = {'size':12})
#legend([('intercetta = ' + str(round(p[1],3)) + str('+-') + str(round(var[1],3)) + ' V')], prop = {'size':12})


chiquadro  = r'$\chi^{2}$: $ %s $'%(round(S,1))  
degfreedom = r'Deg. of freedom: $ %s $' %(deg)
#esponente = r'esponente(-2) $ %s  \pm  %s $' %(round(p[2],2),round(var[2],2))
intercetta = r'fattore trans $ %s  \pm  %s E-27[J]$' %(round(p[0],3),round(var[0],3))

ax1.text(1, 0.2, chiquadro, family='serif', style='italic', size=15) 
ax1.text(1, 0.19, degfreedom, family='serif', style='italic', size=14)
#text(75, 0.29, esponente, family='serif', style='italic', size=15)
#text(xdata.min()*1, ydata.max()*0.87, intercetta, family='serif', style='italic', size=15)

title(r"$ I_{max} $ [mA] e $V_{max}$ [V] in funzione di $P_{max} $ [mW] ", size = 15)
ax1.set_ylim(0.10,0.30)
ax1.set_xlabel(r'Potenza max $P_{max}$ [mW]')
ax1.set_ylabel(r'V max $ V_{max} $ [V]', color='black')
for tl in ax1.get_yticklabels():
    tl.set_color('black') 
grid('on', which = "both")
#ax = axes()
savefig('es8_fit_tens.png', dpi=400)


show()

