from pylab import *  
from scipy import *
from scipy import optimize
from scipy import misc

data = genfromtxt('luce_stanza_50hz.txt')

ydata = data[:,1]
ydata1 = data[:,3]
title("Power Spectrum", size = 15)
rc('font', size=16)
grid()

sp = fft(ydata , len(ydata))
sp1 = fft(ydata1, len(ydata1))
freq = fftfreq(len(ydata), d=0.00002)
freq1 = fftfreq(len(ydata1), d=0.00002)
xlim(0,800)
ps1 = abs(sp)**2
ps21 = abs(sp1)**2
ps2 = ps21/max(ps21)
ps = ps1/max(ps1)
ps[0] = 0
ps2[0] = 0
idx = argsort(freq)


xlabel(r'$f [Hz]$')
ylabel(r'$ps_{norm} [V^2]$')
plot(freq[idx], ps[idx], linewidth = '1.5', color='b', label='CH2')
plot(freq1[idx], ps2[idx], linewidth = '1.5', color='r', label='CH1')
legend(loc=1)
savefig('fft_lucestanza.png', dpi=400)
show()
