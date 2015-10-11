from pylab import *  
from scipy import * 
from scipy import optimize

#TOOLS UTILI

data = genfromtxt('datioffset.txt') #inserire nome file dati

#inserire dopo virgola numero colonna di dati su cui lavorare (la prima colonna è 0)
data_avail = data [:,8]

media = mean(data_avail)
var_pop = var(data_avail, ddof = 1)
var_media = var_pop/len(data_avail)

dev_st_pop = sqrt(var_pop)
dev_st_media = sqrt(var_media)

print('la stima della media della popolazione è: ')
print('%s +/- %s' %(media, dev_st_media))

print('La varianza della popolazione (sigma^2) è: ', var_pop)
print('la deviazione standard è: ', dev_st_pop)

##if len(data_avail) <= 8:
##    print('Dato che il numero di dati non è alto (%d), forse vorrai considerare la t di Student appropriata' %(len(data_avail)))
##
##
##dati_sospetti = []
##dati_buoni = list(data_avail)
##
##def check(x, mean, sigma):
##    scarto = abs(x - mean)
##    if scarto >= 3*sigma:
##        dati_sospetti.append(x)
##        dati_buoni.remove(x)
##
##for i in range(len(data_avail)):
##    check(data_avail[i], media, dev_st_pop)
##
##print(array(dati_buoni))
##
##media1 = mean(dati_buoni)
##var_pop1 = var(dati_buoni, ddof = 1)
##var_media1 = var_pop1/len(dati_buoni)
##
##dev_st_pop1 = sqrt(var_pop1)
##dev_st_media1 = sqrt(var_media1)
##
##print('la stima della media della popolazione è: ')
##print('%s +/- %s' %(media1, dev_st_media1))
##
##print('La varianza della popolazione (sigma^2) è: ', var_pop1)
##print('la deviazione standard è: ', dev_st_pop1)
##
##if len(data_avail) <= 8:
##    print('Dato che il numero di dati non è alto (%d), forse vorrai considerare la t di Student appropriata' %(len(dati_buoni)))
