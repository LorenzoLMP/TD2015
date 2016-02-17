from pylab import *  
from scipy import * 
from scipy import optimize
from scipy import misc
data = genfromtxt('es4_luceled_bello')
xdata = data[:,0]
ydata = data[:,1]
pdata = ydata*xdata
sigmax = 0.0003
sigmay = 0.01
#########################################
sigmap = []
for i in range(len(pdata)):
    sigmap.append(  (sigmay/ydata[i] + sigmax/xdata[i] )*pdata[i]  )

sigmap = array(sigmap)


rc('font', size=15)


fig, ax1 = subplots()

title(r"Curva caratteristica corrente-tensione $I$ $V$ - 90°", size = 15)
ax1.errorbar(xdata, ydata, sigmay, sigmax, linestyle="None", color="red")

ax1.set_xlabel(r'Tensione $V$ [V]')
ax1.set_ylabel(r'Corrente $I$ [mA]', color='r')
for tl in ax1.get_yticklabels():
    tl.set_color('r')

ax2 = ax1.twinx()
ax2.errorbar(xdata, pdata, sigmap, sigmax, linestyle="None", color="blue")
ax2.set_ylabel(r'Potenza $P$ [mW]', color='b')
for tl in ax2.get_yticklabels():
    tl.set_color('b') 

grid('on', which = "both")

savefig('es6_ref.png', dpi=400)

print('90: pmax = %s +- %s mW' %(max(pdata), sigmap[argmax(pdata)]))
show()
