from pylab import *  
from scipy import * 
from scipy import misc

data = genfromtxt('wavelength_analog_loge_wl.txt')

data2 = genfromtxt('ws7ok.txt')


def confront(frac, frac_theo, lambda_theo):
    find = 0
    i = 0
    while (i < len(frac_theo)) and (find == 0):
        if frac > frac_theo[i]:
            find = 1
        else:
            i = i + 1
    return lambda_theo[i]


def list_confront(ydata, true_lambda):
    for i in range(len(ydata)):
        true_lambda.append(confront(ydata[i], frac_th, lambda_th))
    return true_lambda

frac_th = log(data2[:,1])
lambda_th = data2[:,0]

ydata = data[:,1]
sigmay = data[:,2]
xdata = data[:,0]


#confront(ydata, frac_th, lambda_th)
#for i in range(len(ydata)):
 #   print(xdata[i], confront(ydata[i], frac_th, lambda_th))

true_lambda = []
list_confront(ydata, true_lambda)


out_file = open('analog_LED_confront.txt', 'w')
out_file.write("#wl_theo\twl_calibr\tlog(CH1/CH2)\tdelta\n")
for i in range(len(ydata)):
    out_file.write("%s\t%s\t%s\t%s\n"%(xdata[i], true_lambda[i], ydata[i], sigmay[i]))
out_file.close()
