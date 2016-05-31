from pylab import *  
from scipy import * 
from scipy import optimize
from scipy import misc

data = genfromtxt('analog_colori2.txt')

ch1 = data[:,1]
ch2 = data[:,3]
xdata = data[:,0]

def media(array, j):
    s = array[j:j+10].sum()/10
    d = sqrt(var(array[j:j+10]))
    return [s, d]

def scorre(array, array_final, delta, t_final):
    t = 102
    while t < 3470:
        array_final.append(media(array, t)[0])
        delta.append(media(array, t)[1])
        t_final.append(t)
        t = t + 10
    return [array_final, t_final, delta]


ch1_fin = [];t_fin = []; delta_ch1 = []
scorre(ch1, ch1_fin, delta_ch1, t_fin)

ch2_fin = [];t2_fin = []; delta_ch2 = []
scorre(ch2, ch2_fin, delta_ch2, t2_fin)

out_file = open('analog_channel_average.txt', 'w')
out_file.write("#time\tch1\tdelta1\tch2\tdelta2\n")
for i in range(len(ch1_fin)):
    out_file.write("%s\t%s\t%s\t%s\t%s\n"%(t_fin[i], ch1_fin[i], delta_ch1[i], ch2_fin[i], delta_ch2[i]))
out_file.close()
