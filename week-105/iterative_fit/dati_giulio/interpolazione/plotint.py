from numpy import *
from pylab import *

T, v = loadtxt("int.txt", unpack=True)

a = 471.59
b = -407.72
err = T-T+0.5
x = linspace(0.3,0.46,200)

def line(x, m, q):
    return m*x+q

chi = ((T+273 - line(v, b, a))**2/err**2).sum()

print(chi)
deg = len(v)-2

title("T = T(V) per I = 20 $\mu$A")
xlabel("Tensione [V]")
ylabel("Temperatura [K]")
xlim(0.29, 0.47)
ylim(280, 355)

chiquadro  = r'$\chi^{2}$: $ %s $'%(round(chi,1))  
degfreedom = r'Deg. of freedom: $ %s $' %(deg)
E = r'$E_{g}$: $( %s  \pm  %s) eV \,$' %(1.157,0.014)

text(0.30, 310, chiquadro, family='serif', style='italic', size=15) 
text(0.30, 305, degfreedom, family='serif', style='italic', size=15)
text(0.30, 300, E, family='serif', style='italic', size=15)

errorbar(v, T+273, err, linestyle = "", color = "black", marker = "o")
plot(x, line(x,b,a), color = "red")
grid()

savefig("interpol.png")

show()
