from pylab import *  
from scipy import *
from scipy import optimize
from scipy import misc



subplot(3,2,1)
title(r"Risposta ad un impulso", size = 17)
data = genfromtxt('es15_6pp_good')

xdata = data[:,0]/1000000
ydata = data[:,1]
plot(xdata, ydata, '--', color="black", marker='.')
grid('on', which = "both")

subplot(3,2,2)
data2 = genfromtxt('es15_6pp_10pF_good')

xdata2 = data2[:,0]/1000000
ydata2 = data2[:,1]
plot(xdata2, ydata2, '--', color="black", marker='.', label='10pF')
grid('on', which = "both")
legend()
subplot(3,2,3)
data3 = genfromtxt('es15_6pp_22pF_good')

xdata3 = data3[:,0]/1000000
ydata3 = data3[:,1]
plot(xdata3, ydata3, '--', color="black", marker='.', label='22pF')
grid('on', which = "both")
ylabel(r'$V \, [V]$')
legend()
subplot(3,2,4)
data4 = genfromtxt('es15_6pp_100pF_good')

xdata4 = data4[:,0]/1000000
ydata4 = data4[:,1]
plot(xdata4, ydata4, '--', color="black", marker='.', label='100pF')
grid('on', which = "both")
legend()
subplot(3,2,5)
data5 = genfromtxt('es15_6pp_100pF_680k_good')
xlabel(r'$t  \, [s]$')
xdata5 = data5[:,0]/1000000
ydata5 = data5[:,1]
plot(xdata5, ydata5, '--', color="black", marker='.', label='100pF-680kOhm')
grid('on', which = "both")
legend()
subplot(3,2,6)
data6 = genfromtxt('es15_6pp_220pF_good')

xdata6 = data6[:,0]/1000000
ydata6 = data6[:,1]
plot(xdata6, ydata6, '--', color="black", marker='.', label='220pF')
grid('on', which = "both")
xlabel(r'$t \, [s]$')
legend()

savefig('rispo_impulso_multiplot.png', dpi=400)
show()
