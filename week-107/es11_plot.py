from pylab import *  
from scipy import * 
from scipy import optimize
from scipy import misc

data = genfromtxt('es11_confronto.txt')




tdata = data[:,0]
ydata1 = data[:,1]
ydata2 = data[:,3]

#Attivare per scala bilog
#xscale('log');
#yscale('log')
#xlim(10,4200)
#ylim(-0.001,0.001)
grid(which='major')

############################################################
#Parte per plot dati
#t = linspace(0, 3.2, 200)
#yscale('log')
rc('font', size=14)
subplot(2,1,1)
grid(which='major')
title("Segnale modulato sul laser e rivelato dal fotorivelatore") 
plot(tdata[0:500], ydata1[0:500], linestyle='None', marker='o', color="red", mec='None', label='v_laser')
legend(loc=3, fontsize=12)
ylabel(r'Tensione V [V]')
subplot(2,1,2)
grid(which='major')
plot(tdata[0:500], ydata2[0:500], linestyle='None', marker='o', color="blue", mec='None',label='v_photo')


legend(loc=3, fontsize=12)
xlabel('N. acquisizioni')

#errorbar(xdata, ydata, sigmay, sigmax, linestyle="None",marker="o", color="black")
#title("Segnale modulato sul laser e rivelato dal fotorivelatore") 
###savefig('C:\Python33\Fuso\filtro_RC\grafico1.png', dpi=200) 
savefig('es11_plot.png', dpi=400)
show()
