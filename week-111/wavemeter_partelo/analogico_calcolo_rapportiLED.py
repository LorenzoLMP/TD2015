from pylab import *  
from scipy import * 
from scipy import optimize
from scipy import misc

def rapporto(name):
    data = genfromtxt(name)
    data1 = data[:,1]
    data2 = data[:,3]
    ch1 = data1.sum()/len(data1)
    err_rel1 = sqrt(var(data1))/ch1
    ch2 = data2.sum()/len(data2)
    err_rel2 = sqrt(var(data2))/ch2
    frac = ch1/ch2
    deltafrac = (err_rel1 + err_rel2)*frac
    return [log(frac), abs(deltafrac/frac)]

address = ['caratt_hlmpd101-645nm.txt', 'caratt_hlmprosso.txt', 'caratt_hlmpyellow.txt', 'caratt_la3366.txt', 'caratt_lb3333.txt', 'caratt_led365.txt', 'caratt_led450.txt', 'caratt_ledbianco.txt', 'caratt_lo3336.txt', 'caratt_lpk376.txt', 'caratt_ls3336.txt', 'caratt_lt3333.txt', 'caratt_ly3336.txt', 'caratt_sfh4873_880.txt', 'caratt_ssl-lxa.txt', 'caratt_tl4405708.txt', 'caratt_tshg8400_830nn.txt', 'caratt_vp9294.txt']


wavelength = []
deltaw = []
for i in range(len(address)):
    wavelength.append(rapporto(address[i])[0])
    deltaw.append(rapporto(address[i])[1])

out_file = open('wavelength_analog_loge.txt', 'w')
out_file.write("#led\tlog_e(ch1/ch2)\tdelta\n")
for i in range(len(address)):
    out_file.write("%s\t%s\t%s\n"%(address[i][7:], wavelength[i], deltaw[i]))
out_file.close()
