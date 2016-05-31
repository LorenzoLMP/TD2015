from pylab import *  
from scipy import * 
import scipy.optimize
from scipy import misc

data = genfromtxt('Vpp_concentr_mod.txt')

conc = data[:,0]
v_trasp = data[:,1]
v_osc = data[:,2]

def beer(x, p):
    return p[1]*np.exp(-p[0]*x)

def err(p, x, y, sigmay):
    return (beer(x, p) - y)/sigmay

p1 = [10, 1.5]
print("Independent fitting")
p_best1, pcov1, infodict1, errmsg1, success1 = scipy.optimize.leastsq(err, p1, args=(conc, v_trasp, 0.001) , full_output=1)
s_sq1 = (err(p_best1, conc, v_trasp, 0.001)**2).sum()/(len(v_trasp)-len(p1))
pcov = pcov1 * s_sq1
var = sqrt(pcov.diagonal())
print("Best fit parameter for first trajectory sigmay", p_best1)
print(var, s_sq1)

grid(which='major')
rc('font', size=16)
plot(conc, v_trasp, linestyle='None', marker='s', color="b", mec='None', label='trasp')
#plot(conc, v_osc, linestyle='None', marker='s', color="blue", mec='None',label='osc')
t = linspace(0.001,0.25, 100)
plot(t, beer(t, p_best1), color="red")


legend(loc=3, fontsize=12)
xlabel('Concentrazione')
ylabel(r'Tensione $V_{PP}$ [V]')
#errorbar(xdata, ydata, sigmay, sigmax, linestyle="None",marker="o", color="black")
title("Tensioni picco-picco") 
###savefig('C:\Python33\Fuso\filtro_RC\grafico1.png', dpi=200) 
savefig('es13_tens_piccopicco_plot_mod.png', dpi=400)
show()
