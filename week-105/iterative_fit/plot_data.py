from pylab import *  
from scipy import * 
from scipy import optimize
from scipy import misc

data = genfromtxt('15_0.txt')
data1 = genfromtxt('22_0.txt')
data2 = genfromtxt('22_3.txt')
data3 = genfromtxt('30_0.txt')
data4 = genfromtxt('38_0.txt')
data5 = genfromtxt('46_6.txt')
data6 = genfromtxt('54_8.txt')
data7 = genfromtxt('60_0.txt')
data8 = genfromtxt('62_0.txt')
data9 = genfromtxt('62_8.txt')
data10 = genfromtxt('66_8.txt')
data11 = genfromtxt('70_9.txt')
data12= genfromtxt('73_2.txt')



ydata = data[:,1]
ydata1 = data1[:,1]
ydata2 = data2[:,1]
ydata3 = data3[:,1]
ydata4 = data4[:,1]
ydata5 = data5[:,1]
ydata6 = data6[:,1]
ydata7 = data7[:,1]
ydata8 = data8[:,1]
ydata9 = data9[:,1]
ydata10 = data10[:,1]
ydata11 = data11[:,1]
ydata12 = data12[:,1]

#sigmay = data[:,3]
xdata = data[:,0]
xdata1 = data1[:,0]
xdata2 = data2[:,0]
xdata3 = data3[:,0]
xdata4 = data4[:,0]
xdata5 = data5[:,0]
xdata6 = data6[:,0]
xdata7 = data7[:,0]
xdata8 = data8[:,0]
xdata9 = data9[:,0]
xdata10 = data10[:,0]
xdata11 = data11[:,0]
xdata12 = data12[:,0]
#sigmax = data[:,1]
#Attivare per scala bilog
#xscale('log');
#yscale('log')
#xlim(10,4200)
#ylim(-0.001,0.001)
grid(which='major')

############################################################
#Parte per plot dati

def fitfunc(x): 
    return (7.32 + 0.33*x)/c

#t = linspace(0, 3.2, 200)
yscale('log')
rc('font', size=16)
plot(xdata, ydata, linestyle='None', marker='o', color="red", mec='None', label='15.0°')
plot(xdata1, ydata1, linestyle='None', marker='o', color="blue", mec='None',label='22.0°')
plot(xdata2, ydata2, linestyle='None', marker='o', color="green",mec='None', label='22.3°')
plot(xdata3, ydata3, linestyle='None', marker='o', color="orange", mec='None',label='30.0°')
plot(xdata4, ydata4, linestyle='None', marker='o', color="black", mec='None',label='38.0°')
plot(xdata5, ydata5, linestyle='None', marker='o', color="brown", mec='None',label='46.6°')
plot(xdata6, ydata6, linestyle='None', marker='o', color="grey", mec='None',label='54.8°')
plot(xdata7, ydata7, linestyle='None', marker='o', color="purple", mec='None',label='60.0°')
plot(xdata8, ydata8, linestyle='None', marker='o', color="cyan", mec='None',label='62.0°')
plot(xdata9, ydata9, linestyle='None', marker='o', color="red", mec='None',label='62.8°')
plot(xdata10, ydata10, linestyle='None', marker='o', color="blue", mec='None',label='66.8°')
plot(xdata11, ydata11, linestyle='None', marker='o', color="green", mec='None',label='70.9°')
plot(xdata12, ydata12, linestyle='None', marker='o', color="orange", mec='None',label='73.2°')

legend(loc=4, fontsize=12)
xlabel('Tensione V [V]')
ylabel(r'Corrente I [$\mu $ A]')
#errorbar(xdata, ydata, sigmay, sigmax, linestyle="None",marker="o", color="black")
title("Caratteristica I-V") 
###savefig('C:\Python33\Fuso\filtro_RC\grafico1.png', dpi=200) 
savefig('tutte_temp.png', dpi=400)
show()
