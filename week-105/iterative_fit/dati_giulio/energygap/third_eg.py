from numpy import *
from pylab import *
from scipy.optimize import curve_fit


B, dB, Is, dIs, Rs, dR, G, dG, T = loadtxt("parametri.txt", unpack=True)
T = T +273

def loop(x,a,b):
	return a*exp(-b*x)

d=0
E = 1.12


k = d/E

x = B/2
y = sqrt(Is)
dy = dIs/(2*sqrt(Is))

p0 = [1, 1]

p, pcov = curve_fit(loop, x, y, p0, dy)
[dA, dE] = sqrt(pcov.diagonal())

print("E0 = %f +- %f" % (p[1], dE))
print("A = %f +- %f \n" % (p[0]**2, 2*p[0]**1*dA))

AL  = r'$A$: $ (%s \pm %s) A/K^{1.5} $'%(round(p[0]**2/1e9),round(2*dA*p[0]/1e9))  
E = r'$E_{g}$: $( %s  \pm  %s) eV \,$' %(round(p[1],2),round(dE,2))

text(20, 30, AL, family='serif', style='italic', size=15) 
text(20, 34, E, family='serif', style='italic', size=15)
xlabel("$B$ [$eV$$^{-1}$]")
ylabel("$I_{s}$ [$\mu$A]")
errorbar(B,Is,dIs,linestyle="",marker="s")
t=linspace(19.1,21.4,100)
plot(t, loop(t,p[0]**2,p[1]),color="red")
show()
savefig("energygap_second.png")



