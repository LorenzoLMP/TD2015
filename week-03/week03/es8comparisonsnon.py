import numpy as np
import pylab
import os

#os.chdir("C://Users/User/Desktop/recitacion")

f,g, phi= pylab.loadtxt("es2nonsim.txt", unpack=True)
xdata,ydata, Ph= pylab.loadtxt("es_8", unpack=True)

g = 10**(g/20)


sigmay = []
i = 0
while i < len(ydata):
        t = max(0.1/100, 2*np.sqrt(2)*0.002)
        w = np.sqrt( t**2 + 0.005/(ydata[i]*0.1) )
        sigmay.append(w)
        i = i+1

sigmay = np.array(sigmay)

sigmax = []
i = 0
while i < len(xdata):
        s = max(0.040, xdata[i]*5*10**(-5))
        sigmax.append(s)
        i = i +1
sigmax = np.array(sigmax)

pylab.title("Confronto simulazione 1 con dati sperimentali, gain = 100")
pylab.xlabel("Frequency [Hz]")
pylab.ylabel("Gain")
pylab.xlim(45, 20100)
pylab.ylim(35, 105)
pylab.grid('on', which = "both")
pylab.plot(f,g,color = "red")
pylab.errorbar(xdata,ydata, sigmay, sigmax, linestyle="", color="black", marker="+")
##pylab.plot(A,B, color ="red")
pylab.xscale("log")
pylab.savefig("es8comparisons_nonsim.png")
pylab.show()
