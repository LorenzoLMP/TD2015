from pylab import *  
from scipy import *

#data = genfromtxt('ES9_vrefinternal_1-10.txt')

data = genfromtxt('es10_internal_5v.txt')

#xdata= data[:,0]
#ydata = data[:,1]

rc('font', size=16)
#xlabel(r'$   $')
#ylabel(r'$   $')
minorticks_on()

n, bins, patches = plt.hist(data, bins= 10, range=(505,511), normed=True, histtype='stepfilled')

#title("Ist. INTERNAL - 5V/10")
#savefig('ist_INTERNAL_part10_5V.png', dpi=400)
show()
print('media = ', mean(data))
print('var_pop = ', var(data, ddof = 1))

##bins : int or sequence of scalars, optional
##If bins is an int, it defines the number of equal-width bins in the given range (10, by default).
##If bins is a sequence, it defines the bin edges, including the rightmost edge, allowing for non-uniform bin widths.
