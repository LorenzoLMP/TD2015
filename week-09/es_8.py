from pylab import *  
from scipy import * 
from scipy import optimize
from scipy import misc

data = genfromtxt('es8_1')
xdata = data[:,0]
ydata = data[:,1]
pdata = ydata*xdata
sigmax = 0.0003
sigmay = 0.01
sigmap = []
for i in range(len(pdata)):
    sigmap.append(  (sigmay/ydata[i] + sigmax/xdata[i] )*pdata[i]  )
sigmap = array(sigmap)
#########################################
data2 = genfromtxt('es8_2')
xdata2 = data2[:,0]
ydata2 = data2[:,1]
pdata2 = ydata2*xdata2
sigmax2 = 0.0003
sigmay2 = 0.01
sigmap2 = []
for i in range(len(pdata2)):
    sigmap2.append(  (sigmay2/ydata2[i] + sigmax2/xdata2[i] )*pdata2[i]  )
sigmap2 = array(sigmap2)
#######################################
data3 = genfromtxt('es8_3')
xdata3 = data3[:,0]
ydata3 = data3[:,1]
pdata3 = ydata3*xdata3
sigmax3 = 0.0003
sigmay3 = 0.01
sigmap3 = []
for i in range(len(pdata3)):
    sigmap3.append(  (sigmay3/ydata3[i] + sigmax3/xdata3[i] )*pdata3[i]  )
sigmap3 = array(sigmap3)
########################################à
data4 = genfromtxt('es8_4')
xdata4 = data4[:,0]
ydata4 = data4[:,1]
pdata4 = ydata4*xdata4
sigmax4 = 0.0003
sigmay4 = 0.01
sigmap4 = []
for i in range(len(pdata4)):
    sigmap4.append(  (sigmay4/ydata4[i] + sigmax4/xdata4[i] )*pdata4[i]  )
sigmap4 = array(sigmap4)
####################################
data5 = genfromtxt('es8_5')
xdata5 = data5[:,0]
ydata5 = data5[:,1]
pdata5 = ydata5*xdata5
sigmax5 = 0.0003
sigmay5 = 0.01
sigmap5 = []
for i in range(len(pdata5)):
    sigmap5.append(  (sigmay5/ydata5[i] + sigmax5/xdata5[i] )*pdata5[i]  )
sigmap5 = array(sigmap5)
###############################################



pmax = [max(pdata), max(pdata2), max(pdata3), max(pdata4), max(pdata5)]
sigmapmax = [sigmap[argmax(pdata)], sigmap2[argmax(pdata2)], sigmap3[argmax(pdata3)], sigmap4[argmax(pdata4)], sigmap5[argmax(pdata5)]]
corrmax = [ydata[argmax(pdata)], ydata2[argmax(pdata2)], ydata3[argmax(pdata3)], ydata4[argmax(pdata4)], ydata5[argmax(pdata5)]]
vmax = [xdata[argmax(pdata)], xdata2[argmax(pdata2)], xdata3[argmax(pdata3)], xdata4[argmax(pdata4)], xdata5[argmax(pdata5)]]

rc('font', size=15)


fig, ax1 = subplots()

title(r"Curva corrente-tensione $IV$ - filtri", size = 15)

#ax1.errorbar(pmax, vmax, 0.0003, sigmapmax, linestyle="None", color="black")
#ax1.plot(pmax, vmax, linestyle="None", marker="o", color="black")
ax1.errorbar(xdata, ydata, sigmay, sigmax, linestyle="None", color="black")
ax1.errorbar(xdata2, ydata2, sigmay2, sigmax2, linestyle="None", color="black")
ax1.errorbar(xdata3, ydata3, sigmay3, sigmax3, linestyle="None", color="black")
ax1.errorbar(xdata4, ydata4, sigmay4, sigmax4, linestyle="None", color="black")
ax1.errorbar(xdata5, ydata5, sigmay5, sigmax5, linestyle="None", color="black")

ax1.set_xlabel(r'Tensione $V$ [V]')
ax1.set_ylabel(r'Corrente $I$ [mA]', color='black')
for tl in ax1.get_yticklabels():
    tl.set_color('black')

ax2 = ax1.twinx()
#ax2.errorbar(pmax, corrmax, 0.01, sigmapmax, linestyle="None", color="red")
#ax2.plot(pmax, corrmax, linestyle="None", marker="o", color="red")
ax2.errorbar(xdata, pdata, sigmap, sigmax, linestyle="None", color="blue")
ax2.errorbar(xdata2, pdata2, sigmap2, sigmax2, linestyle="None", color="blue")
ax2.errorbar(xdata3, pdata3, sigmap3, sigmax3, linestyle="None", color="blue")
ax2.errorbar(xdata4, pdata4, sigmap4, sigmax4, linestyle="None", color="blue")
ax2.errorbar(xdata5, pdata5, sigmap5, sigmax5, linestyle="None", color="blue")
ax2.set_ylabel(r'Potenza $P$ [mW]', color='b')
for tl in ax2.get_yticklabels():
    tl.set_color('b') 



#a = [max(pdata), max(pdata63), max(pdata67), max(pdata71), max(pdata75), max(pdata79), max(pdata83), max(pdata87)]
#b = [xdata[argmax(pdata)], xdata63[argmax(pdata63)], xdata67[argmax(pdata67)], xdata71[argmax(pdata71)], xdata75[argmax(pdata75)], xdata79[argmax(pdata79)], xdata83[argmax(pdata83)], xdata87[argmax(pdata87)]]
#ax2.plot(b, a , linestyle="None", marker="o", color="red", markersize= 10)


annotate('6.3%', xy=(0.35, 0.045), xycoords='axes fraction')
annotate('24.1%', xy=(0.60, 0.035), xycoords='axes fraction')
annotate('39.2%', xy=(0.70, 0.03), xycoords='axes fraction')
annotate('63.8%', xy=(0.80, 0.03), xycoords='axes fraction')
annotate('97.4%', xy=(0.90, 0.03), xycoords='axes fraction')



grid('on', which = "both")
#savefig('es_8_1.png', dpi=400)

#print('90: pmax = %s +- %s mW' %(max(pdata), sigmap[argmax(pdata)]))
show()
