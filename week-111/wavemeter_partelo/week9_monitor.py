from pylab import *  
from scipy import *

data = genfromtxt('monitor_300_lambda.txt')
data2 = genfromtxt('intens_screen_week9.txt')

ydata = data2[:,1]
xdata = data[:,3]

grid(which='major')
rc('font', size=15)
plot(xdata[:301], ydata[:301], linestyle='None', marker='o', color='red', label='ch1')
xlabel(r'pseudo-wavelength [$\lambda$]')
ylabel('Intensità relativa')
savefig('nostro_gamut.png', dpi=400)
show()

