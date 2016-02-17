from pylab import *  
from scipy import * 
from scipy import optimize
from scipy import misc

rc('font', size=15)
minorticks_on()

time = linspace(0.0010,0.0030,100)
def fitfunc(x, *par): 
	return par[0]*10**(-27) + par[1]*10**(-25)*x 


p20 = [-0.107, 6.142]
p40 = [-0.099, 6.231]
p60 = [-0.094, 6.288]
p80 = [-0.084, 6.298]

plot(time, fitfunc(time, *p20), '--', color='black', linewidth = 1.1, label='20uA')
plot(time, fitfunc(time, *p40), '--', color='blue', linewidth = 1.1, label='40uA')
plot(time, fitfunc(time, *p60),'--', color='green', linewidth = 1.1, label='60uA')
plot(time, fitfunc(time, *p80), '--', color='red', linewidth = 1.1, label='80uA')
grid('on')

title(r"Planck Constant - comparison 20-40-60-80$\mu$A") 

data20 = genfromtxt('planck_newdata_20ua.txt')
data40 = genfromtxt('planck_newdata_40ua.txt')
data60 = genfromtxt('planck_newdata_60ua.txt')
data80 = genfromtxt('planck_newdata_80ua.txt')

xdata20 = data20[:,0];sigmax20 = data20[:,1];ydata20 = data20[:,2];sigmay20 = data20[:,3]
xdata40 = data40[:,0];sigmax40 = data40[:,1];ydata40 = data40[:,2];sigmay40 = data40[:,3]
xdata60 = data60[:,0];sigmax60 = data60[:,1];ydata60 = data60[:,2];sigmay60 = data60[:,3]
xdata80 = data80[:,0];sigmax80 = data80[:,1];ydata80 = data80[:,2];sigmay80 = data80[:,3]

errorbar(xdata20, ydata20, sigmay20, sigmax20, linestyle="None", marker=".", color="black", fmt = 'o', markersize= 5)
errorbar(xdata40, ydata40, sigmay40, sigmax40, linestyle="None", marker=".", color="blue", fmt = 'o', markersize= 5)
errorbar(xdata60, ydata60, sigmay60, sigmax60, linestyle="None", marker=".", color="green", fmt = 'o', markersize= 5)
errorbar(xdata80, ydata80, sigmay80, sigmax80, linestyle="None", marker=".", color="red", fmt = 'o', markersize= 5)

legend(loc=2)

xlabel(r'$\lambda^{-1}  [nm^{-1}]$')
ylabel(r'$\frac{qV_{F}}{c} [J]$')
ax = axes()
savefig('costante_planck_comparison.png', dpi=400) 
show()
