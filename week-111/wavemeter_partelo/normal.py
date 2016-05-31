from pylab import *  
from scipy import * 
from scipy import misc

def gauss(x, height, mu, sigma):
    return height*(1/(sigma*np.sqrt(2*np.pi)))*np.exp(-((x  - mu)**2) / (2*sigma**2) )

t = linspace(0, 1400, 1000)
fig, ax1 = subplots()
grid(which='major')
rc('font', size=14)
ax1.set_title('Modellizzazione delle curve di responsività spettrale')
ax1.set_xlabel('Wavelength [nm]')
ax1.set_ylabel(r'A/W')
ax1.set_xlim(400, 1000)
ch1 = gauss(t, 100, 550, 180)
ch2 = gauss(t, 220, 890, 200)
ax1.plot(t, ch2, linewidth='2',color='b')
ax1.plot(t, ch1, linewidth='2',linestyle='--', color=(0,0.2,0.9))

ax2 = ax1.twinx()
ax2.set_xlim(400, 1000)
ax2.set_ylim(-4, 3)
ax2.set_ylabel(r'log(CH1/CH2)')
ax2.plot(t, log(ch1/ch2), linewidth='1.5',color='r')
savefig('normal_respons.png', dpi=400)
show()
