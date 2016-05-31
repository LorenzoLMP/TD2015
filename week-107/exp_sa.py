from pylab import *  
from scipy import *

grid(which='major')
t = linspace(0, 0.5, 100)
s = linspace(0.5, 1, 100)
plot(t, exp(-t/1), 'r')
plot(s, exp(0.5)*exp(-s/0.5), 'r')

plot(t, exp(-t/0.5), 'b')
plot(s, exp(-0.5)*exp(-s/1), 'b')

show()
