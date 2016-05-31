from pylab import *
from scipy import optimize
data = genfromtxt('parametri.txt')

T = data[:,8]
B = data[:,0]
ydata = data[:,2]
sigmay = data[:,3]

def fitfunc(x, *par):
    return par[0]*exp(x*par[1])

k = 8.617*10**(-5) #eV/K
def sat_current(x, *par):
    return par[0]*exp(-par[1]/(k*(x+273.15)))


p0 = [1000, 0.1]
p, var = optimize.curve_fit(sat_current, T, ydata, p0, sigmay)
e_gap = p[1]*1.86
e_gap_var = sqrt(var[1][1])*1.86
print(e_gap)
errorbar(T, ydata, sigmay, 0.5, linestyle='None', color='black')
t = linspace(10,70,200)
plot(t, sat_current(t, *p), color='blue')
show()
##e_gap = 2
##j =0
##while j < 10:
##    xdata = 1.5*log(T)/(e_gap) - B
##    print(xdata[:10])
##    p0_loop = [1.0, e_gap] 
##    p1, var1 = optimize.curve_fit(fitfunc, xdata, ydata, p0_loop, sigmay)
##    print(p1)
##    e_gap = p1[1]
##    print(e_gap)
##    j = j+1



##errorbar(T, ydata, sigmay, 0.5, linestyle='None', color='black')
##t = linspace(10,70,200)
###plot(t, fitfunc(t, *p1-(0,2)), color='blue')
##show()

##title(r"Corrente di saturazione $I_{S}$ in funzione della temperatura", size=14.5)
##xlabel('Temperatura °C')
##ylabel(r'$I_{S}$ [nA]')
##grid()
##errorbar(data[:,8], data[:,2], data[:,3], 0.5, linestyle='None', marker='+', markersize=1, color="purple")
##show()
##savefig('parametro_Is_temp.png', dpi=400)
