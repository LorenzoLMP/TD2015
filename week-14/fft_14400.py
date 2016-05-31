from pylab import *  
from scipy import *
from scipy import optimize
from scipy import misc
import numpy as np
data = genfromtxt('es13_4hz_nodelay_9600baud.txt')

ydata = data
title("Power Spectrum - 9600", size = 15)
rc('font', size=16)
grid()

sp = fft(ydata , len(ydata))
freq = fftfreq(len(ydata), d=0.004166666)
xlim(0,5)
ps1 = abs(sp)**2
ps = ps1/np.amax(ps1)
idx = argsort(freq)

xlabel(r'$f [Hz]$')
ylabel(r'$ps_{norm} [V^2]$')
plot(freq[idx], ps[idx])
#savefig('fft_115200b.png', dpi=400)
show()
