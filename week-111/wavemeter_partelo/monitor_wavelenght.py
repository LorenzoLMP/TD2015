from pylab import *  
from scipy import * 
from scipy import optimize
from scipy import misc

data = genfromtxt('analog_channel_average.txt')
data2 = genfromtxt('ws7ok.txt')
def confront(frac, frac_theo, lambda_theo):
    find = 0
    i = 0
    while (i < len(frac_theo)) and (find == 0):
        if frac > frac_theo[i]:
            find = 1
        else:
            i = i + 1
    if find==1:
        return lambda_theo[i]
    else:
        return lambda_theo[i-1]


def list_confront(ydata, true_lambda):
    for i in range(len(ydata)):
        true_lambda.append(confront(ydata[i], frac_th, lambda_th))
    return true_lambda

frac_th = log(data2[:,1])
lambda_th = data2[:,0]

ch1 = data[:,1]
sigma1 = data[:,2]
ch2 = data[:,3] + 0.006
time = data[:,0]
sigma2 = data[:,4]
true_lambda = []
list_confront(log(abs(ch1/ch2)), true_lambda)

frac = ch1/ch2
err_rel1 = sigma1/ch1
err_rel2 = sigma2/ch2
deltafrac = (err_rel1 + err_rel2)*frac
deltalog = abs(deltafrac/frac)
for i in range(len(deltalog)):
    if deltalog[i]>=1:
        deltalog[i] = 1

lamb_maj = []
list_confront(log(abs(ch1/ch2))+deltalog, lamb_maj)

lamb_min = []
list_confront(log(abs(ch1/ch2))-deltalog, lamb_min)

delta = []
for i in range(len(lamb_maj)):
    delta.append(abs(lamb_maj[i] - lamb_min[i]))


out_file = open('monitor_lambda_senzaIR2.txt', 'w')
out_file.write("#time\tch1\tch2\tlambda\tdelta\n")
for i in range(len(ch1)):
    out_file.write("%s\t%s\t%s\t%s\t%s\n"%(time[i], ch1[i], ch2[i], true_lambda[i], delta[i]))
out_file.close()
##ch1 = data[:,1]
##sigma1= data[:,2]
##ch2 = data[:,3]
##sigma2 = data[:,4]
###sigmay = data[:,2]
##xdata = data[:,0]
##
##frac = ch1/ch2
##err_rel1 = sigma1/ch1
##err_rel2 = sigma2/ch2
##deltafrac = (err_rel1 + err_rel2)*frac
##deltalog = abs(deltafrac/frac)
##for i in range(len(deltalog)):
##    if deltalog[i]>=1:
##        deltalog[i] = 1
##
##fig, ax1 = subplots()
##grid(which='major')
##rc('font', size=15)
####errorbar(xdata, ydata, sigmay, linestyle='None', marker='s', color="red", mec='None',label='led')
##ax1.errorbar(xdata, ch1, sigma1, linestyle='None', marker='o', color='red', label='ch1')
##ax1.errorbar(xdata, ch2, sigma2, linestyle='None', marker='o', color='green', label='ch2')
###legend(loc=3, fontsize=12)
##ax1.set_xlabel('Time t')
##ax1.set_ylabel(r'Tensione canali [V]')
###errorbar(xdata, ydata, sigmay, sigmax, linestyle="None",marker="o", color="black")
##title("Sensore analogico - colori lambda")
