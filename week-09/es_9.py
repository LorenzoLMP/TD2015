from pylab import *  
from scipy import * 
from scipy import optimize
from scipy import misc

data = genfromtxt('es9_senza')
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
data2 = genfromtxt('es9_meta')
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
data3 = genfromtxt('es9_quarto')
xdata3 = data3[:,0]
ydata3 = data3[:,1]
pdata3 = ydata3*xdata3
sigmax3 = 0.0003
sigmay3 = 0.01
sigmap3 = []
for i in range(len(pdata3)):
    sigmap3.append(  (sigmay3/ydata3[i] + sigmax3/xdata3[i] )*pdata3[i]  )
sigmap3 = array(sigmap3)
########################################



pmax = [max(pdata), max(pdata2), max(pdata3)]
sigmapmax = [sigmap[argmax(pdata)], sigmap2[argmax(pdata2)], sigmap3[argmax(pdata3)]]
corrmax = [ydata[argmax(pdata)], ydata2[argmax(pdata2)], ydata3[argmax(pdata3)]]
vmax = [xdata[argmax(pdata)],xdata2[argmax(pdata2)] , xdata3[argmax(pdata3)]]
sup_exp = [1, 0.5, 0.25]

rc('font', size=15)


fig, ax1 = subplots()

title(r"Corrente e tensione max in funzione della sup esposta", size = 15)

#ax1.errorbar(sup_exp, vmax, 0.0003, sigmapmax, linestyle="None", color="black")
ax1.plot(sup_exp, vmax, linestyle="None", marker="o", color="black")
##ax1.errorbar(xdata, ydata, sigmay, sigmax, linestyle="None", color="black")
##ax1.errorbar(xdata2, ydata2, sigmay2, sigmax2, linestyle="None", color="black")
##ax1.errorbar(xdata3, ydata3, sigmay3, sigmax3, linestyle="None", color="black")
##ax1.errorbar(xdata4, ydata4, sigmay4, sigmax4, linestyle="None", color="black")
##ax1.errorbar(xdata5, ydata5, sigmay5, sigmax5, linestyle="None", color="black")

ax1.set_xlabel(r'Superficie esposta (norm. a 1) $S$')
ax1.set_ylabel(r'Tensione max $V_{max}$ [V]', color='black')
for tl in ax1.get_yticklabels():
    tl.set_color('black')

ax1.set_xlim(0.0, 1.1)

ax2 = ax1.twinx()
#ax2.errorbar(pmax, corrmax, 0.01, sigmapmax, linestyle="None", color="red")
ax2.plot(sup_exp, corrmax, linestyle="None", marker="o", color="red")
##ax2.errorbar(xdata, pdata, sigmap, sigmax, linestyle="None", color="blue")
##ax2.errorbar(xdata2, pdata2, sigmap2, sigmax2, linestyle="None", color="blue")
##ax2.errorbar(xdata3, pdata3, sigmap3, sigmax3, linestyle="None", color="blue")
##ax2.errorbar(xdata4, pdata4, sigmap4, sigmax4, linestyle="None", color="blue")
##ax2.errorbar(xdata5, pdata5, sigmap5, sigmax5, linestyle="None", color="blue")
ax2.set_ylabel(r'Corrente max $I_{max}$ [mA]', color='r')
for tl in ax2.get_yticklabels():
    tl.set_color('r') 

ax2.set_xlim(0.0, 1.1)

#a = [max(pdata), max(pdata63), max(pdata67), max(pdata71), max(pdata75), max(pdata79), max(pdata83), max(pdata87)]
#b = [xdata[argmax(pdata)], xdata63[argmax(pdata63)], xdata67[argmax(pdata67)], xdata71[argmax(pdata71)], xdata75[argmax(pdata75)], xdata79[argmax(pdata79)], xdata83[argmax(pdata83)], xdata87[argmax(pdata87)]]
#ax2.plot(b, a , linestyle="None", marker="o", color="red", markersize= 10)


##annotate('59', xy=(0.6, 0.07), xycoords='axes fraction')
##annotate('63', xy=(0.65, 0.07), xycoords='axes fraction')
##annotate('67', xy=(0.70, 0.07), xycoords='axes fraction')
##annotate('71', xy=(0.75, 0.07), xycoords='axes fraction')
##annotate('75', xy=(0.80, 0.07), xycoords='axes fraction')
##annotate('79', xy=(0.85, 0.07), xycoords='axes fraction')
##annotate('83', xy=(0.90, 0.07), xycoords='axes fraction')
##annotate('87', xy=(0.95, 0.07), xycoords='axes fraction')



grid('on', which = "both")
savefig('es_9corr_v.png', dpi=400)

#print('90: pmax = %s +- %s mW' %(max(pdata), sigmap[argmax(pdata)]))
show()

