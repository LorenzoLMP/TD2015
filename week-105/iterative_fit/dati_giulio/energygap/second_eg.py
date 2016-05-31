from numpy import *
from pylab import *
from scipy.optimize import curve_fit


B, dB, Is, dIs, Rs, dR, G, dG, T = loadtxt("parametri.txt", unpack=True)
T = T +273

def loop(x,a,b):
	return a + b*x

d=1.5
E = 1.12


k = d/E

x = k*log(T)-B
y = log(Is)
dy = dIs/Is

p0 = [10, 1]

p, pcov = curve_fit(loop, x, y, p0, dy)
[dA, dE] = sqrt(pcov.diagonal())

print("E0 = %f +- %f" % (p[1], dE))
print("A = %f +- %f \n" % (p[0], dA))

E = p[1]

k = d/E
x = k*log(T)-B
p0 = [7, 1]
p, pcov = curve_fit(loop, x, y, p0, dy)
[dA, dE] = sqrt(pcov.diagonal())
print("E0 = %f +- %f" % (p[1], dE))
print("A = %f +- %f \n" % (p[0], dA))

E = p[1]
k = d/E
x = k*log(T)-B
p0 = [7, 1]
p, pcov = curve_fit(loop, x, y, p0, dy)
[dA, dE] = sqrt(pcov.diagonal())
print("E0 = %f +- %f" % (p[1], dE))
print("A = %f +- %f \n" % (p[0], dA))

E = p[1]

k = d/E
x = k*log(T)-B
p0 = [7, 1]
p, pcov = curve_fit(loop, x, y, p0, dy)
[dA, dE] = sqrt(pcov.diagonal())
print("E0 = %f +- %f" % (p[1], dE))
print("A = %f +- %f \n" % (p[0], dA))


print("Begin loop! \n")

for j in range (0,25):
	E = p[1]
	k = d/E
	x = k*log(T)-B
	p0 = [7, 1]
	p, pcov = curve_fit(loop, x, y, p0, dy)
	print(pcov)
	print("\n")
	[dA, dE] = sqrt(pcov.diagonal())
	print("E0 = %f +- %f" % (p[1], dE))
	print("A = %f +- %f \n" % (exp(p[0])/1e6, dA*exp(p[0])/1e6))
	

AL  = r'$A$: $ (%s \pm %s) A/K^{1.5} $'%(round(exp(p[0])/1e9,2),round(dA*exp(p[0])/1e9,2))  
delta = r'$\delta$: $ %s $' %(d)
E = r'$E_{g}$: $( %s  \pm  %s) eV \,$' %(round(E,2),round(dE,2))

text(20.5, 30, AL, family='serif', style='italic', size=15) 
text(20.5, 32, delta, family='serif', style='italic', size=15)
text(20.5, 34, E, family='serif', style='italic', size=15)
	
xlabel("$B$ [$eV$$^{-1}$]")
ylabel("$I_{s}$ [$\mu$A]")
errorbar(B , Is, dIs, linestyle="", marker="s")
plot(B,exp(loop(x,p[0],p[1])), linestyle ="",marker = "o", color = "red")
savefig("energygap_first_recursive1-5.png")
show()













