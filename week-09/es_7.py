from pylab import *  
from scipy import * 
from scipy import optimize
from scipy import misc
data = genfromtxt('es7_59')
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
data63 = genfromtxt('es7_63')
xdata63 = data63[:,0]
ydata63 = data63[:,1]
pdata63 = ydata63*xdata63
sigmax63 = 0.0003
sigmay63 = 0.01
sigmap63 = []
for i in range(len(pdata63)):
    sigmap63.append(  (sigmay63/ydata63[i] + sigmax63/xdata63[i] )*pdata63[i]  )
sigmap63 = array(sigmap63)
#######################################
data67 = genfromtxt('es7_67')
xdata67 = data67[:,0]
ydata67 = data67[:,1]
pdata67 = ydata67*xdata67
sigmax67 = 0.0003
sigmay67 = 0.01
sigmap67 = []
for i in range(len(pdata67)):
    sigmap67.append(  (sigmay67/ydata67[i] + sigmax67/xdata67[i] )*pdata67[i]  )
sigmap67 = array(sigmap67)
########################################à
data71 = genfromtxt('es7_71')
xdata71 = data71[:,0]
ydata71 = data71[:,1]
pdata71 = ydata71*xdata71
sigmax71 = 0.0003
sigmay71 = 0.01
sigmap71 = []
for i in range(len(pdata71)):
    sigmap71.append(  (sigmay71/ydata71[i] + sigmax71/xdata71[i] )*pdata71[i]  )
sigmap71 = array(sigmap71)
####################################
data75 = genfromtxt('es7_75')
xdata75 = data75[:,0]
ydata75 = data75[:,1]
pdata75 = ydata75*xdata75
sigmax75 = 0.0003
sigmay75 = 0.01
sigmap75 = []
for i in range(len(pdata75)):
    sigmap75.append(  (sigmay/ydata75[i] + sigmax/xdata75[i] )*pdata75[i]  )
sigmap75 = array(sigmap75)
###############################################
data79 = genfromtxt('es7_79')
xdata79 = data79[:,0]
ydata79 = data79[:,1]
pdata79 = ydata79*xdata79
sigmax79 = 0.0003
sigmay79 = 0.01
sigmap79 = []
for i in range(len(pdata79)):
    sigmap79.append(  (sigmay/ydata79[i] + sigmax/xdata79[i] )*pdata79[i]  )
sigmap79 = array(sigmap79)
#########################################
data83 = genfromtxt('es7_83')
xdata83 = data83[:,0]
ydata83 = data83[:,1]
pdata83= ydata83*xdata83
sigmax83 = 0.0003
sigmay83 = 0.01
sigmap83 = []
for i in range(len(pdata83)):
    sigmap83.append(  (sigmay/ydata83[i] + sigmax/xdata83[i] )*pdata83[i]  )
sigmap83 = array(sigmap83)
#########################################àà
data87 = genfromtxt('es7_87')
xdata87 = data87[:,0]
ydata87 = data87[:,1]
pdata87 = ydata87*xdata87
sigmax87= 0.0003
sigmay87 = 0.01
sigmap87 = []
for i in range(len(pdata87)):
    sigmap87.append(  (sigmay/ydata87[i] + sigmax/xdata87[i] )*pdata87[i]  )
sigmap87 = array(sigmap87)
########################################

rc('font', size=15)


fig, ax1 = subplots()

title(r"Curva corrente-tensione $I$ $V$ per distanze diverse (cm)", size = 15)
ax1.errorbar(xdata, ydata, sigmay, sigmax, linestyle="None", color="black")
ax1.errorbar(xdata63, ydata63, sigmay63, sigmax63, linestyle="None", color="black")
ax1.errorbar(xdata67, ydata67, sigmay67, sigmax67, linestyle="None", color="black")
ax1.errorbar(xdata71, ydata71, sigmay71, sigmax71, linestyle="None", color="black")
ax1.errorbar(xdata75, ydata75, sigmay75, sigmax75, linestyle="None", color="black")
ax1.errorbar(xdata79, ydata79, sigmay79, sigmax79, linestyle="None", color="black")
ax1.errorbar(xdata83, ydata83, sigmay83, sigmax83, linestyle="None", color="black")
ax1.errorbar(xdata87, ydata87, sigmay87, sigmax87, linestyle="None", color="black")

ax1.set_xlabel(r'Tensione $V$ [V]')
ax1.set_ylabel(r'Corrente $I$ [mA]', color='black')
for tl in ax1.get_yticklabels():
    tl.set_color('black')

ax2 = ax1.twinx()
ax2.errorbar(xdata, pdata, sigmap, sigmax, linestyle="None", color="blue")
ax2.errorbar(xdata63, pdata63, sigmap63, sigmax63, linestyle="None", color="blue")
ax2.errorbar(xdata67, pdata67, sigmap67, sigmax67, linestyle="None", color="blue")
ax2.errorbar(xdata71, pdata71, sigmap71, sigmax71, linestyle="None", color="blue")
ax2.errorbar(xdata75, pdata75, sigmap75, sigmax75, linestyle="None", color="blue")
ax2.errorbar(xdata79, pdata79, sigmap79, sigmax79, linestyle="None", color="blue")
ax2.errorbar(xdata83, pdata83, sigmap83, sigmax83, linestyle="None", color="blue")
ax2.errorbar(xdata87, pdata87, sigmap87, sigmax87, linestyle="None", color="blue")


ax2.set_ylabel(r'Potenza $P$ [mW]', color='b')
for tl in ax2.get_yticklabels():
    tl.set_color('b') 



a = [max(pdata), max(pdata63), max(pdata67), max(pdata71), max(pdata75), max(pdata79), max(pdata83), max(pdata87)]
erra = [sigmap[argmax(pdata)], sigmap63[argmax(pdata63)], sigmap67[argmax(pdata67)], sigmap71[argmax(pdata71)], sigmap75[argmax(pdata75)], sigmap79[argmax(pdata79)], sigmap83[argmax(pdata83)], sigmap87[argmax(pdata87)]]
b = [xdata[argmax(pdata)], xdata63[argmax(pdata63)], xdata67[argmax(pdata67)], xdata71[argmax(pdata71)], xdata75[argmax(pdata75)], xdata79[argmax(pdata79)], xdata83[argmax(pdata83)], xdata87[argmax(pdata87)]]
ax2.plot(b, a , linestyle="None", marker="o", color="red", markersize= 10)

dist = [59,63,67,71,75,79,83,87]

out_file = open("es7_pot_dist.txt","w")
out_file.write("#potenza\terrpotenza\tdistanza\terrdistanza\n")
for i in range(len(a)):
    out_file.write("%s\t%s\t%s\t%s\n"%(a[i], erra[i], dist[i], 3 ))

out_file.close()

annotate('87', xy=(0.6, 0.07), xycoords='axes fraction')
annotate('83', xy=(0.65, 0.07), xycoords='axes fraction')
annotate('79', xy=(0.70, 0.07), xycoords='axes fraction')
annotate('75', xy=(0.75, 0.07), xycoords='axes fraction')
annotate('71', xy=(0.80, 0.07), xycoords='axes fraction')
annotate('67', xy=(0.85, 0.07), xycoords='axes fraction')
annotate('63', xy=(0.90, 0.07), xycoords='axes fraction')
annotate('59', xy=(0.95, 0.07), xycoords='axes fraction')



grid('on', which = "both")
#savefig('es7_prova.png', dpi=400)

#print('90: pmax = %s +- %s mW' %(max(pdata), sigmap[argmax(pdata)]))
show()
