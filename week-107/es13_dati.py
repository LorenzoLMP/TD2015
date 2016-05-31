from pylab import *  
from scipy import * 
from scipy import optimize
from scipy import misc


def vpiccopicco(name, conc):
    data = genfromtxt(name)
    ydata = data[:,1]
    vpp = abs(ydata[argmax(ydata)]-ydata[argmin(ydata)])
    return [conc, vpp]

name_trasp = ['es13_0_01M.txt', 'es13_0_1M.txt', 'es13_0_04M.txt', 'es13_0_06M.txt', 'es13_0_15M.txt', 'es13_0_025M.txt' ]

name_opaque = ['es13_0_01M_opaco.txt', 'es13_0_1M_opaco.txt', 'es13_0_04M_opaco.txt', 'es13_0_06M_opaco.txt','es13_0_15M_opaco.txt','es13_0_025M_opaco.txt']

conc = [0.01, 0.1, 0.04, 0.06, 0.15, 0.025]
##data = genfromtxt('es13_0_01M.txt')
##
##ydata = data[:,1]
##tdata = data[:,0]
##
##vpp = abs(ydata[argmax(ydata)]-ydata[argmin(ydata)])/2
##out_file.write("%s\t%s\n"%(conc, vpp))

vpp_trasp = []
vpp_opaque = []
for i in range(len(name_trasp)):
    k, j = vpiccopicco(name_trasp[i], conc[i])
    vpp_trasp.append(j)

for i in range(len(conc)):
    k,j = vpiccopicco(name_opaque[i], conc[i])
    vpp_opaque.append(j)





out_file = open('Vpp_concentr.txt', 'w')
out_file.write("#conc\tvpp_trasp\tvpp_opaque\n")
for i in range(len(conc)):
    out_file.write("%s\t%s\t%s\n"%(conc[i], vpp_trasp[i], vpp_opaque[i]))
out_file.close()
