import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from pylab import *


import colorsys
N= 300
HSV_tuples = [(x*1.0/N, 1.0, 0.6) for x in range(N)]

x = np.array(HSV_tuples[0])
a = x.reshape((1,1,3));
i = 0


while i < N:
    if i == 0:
        plt.figure(figsize=(10,10))
        p = plt.imshow(a, interpolation='nearest', vmin=0, vmax=1)
    else:
        r = colorsys.hsv_to_rgb(HSV_tuples[i][0], HSV_tuples[i][1], HSV_tuples[i][2])[0]
        g = colorsys.hsv_to_rgb(HSV_tuples[i][0], HSV_tuples[i][1], HSV_tuples[i][2])[1]
        b = colorsys.hsv_to_rgb(HSV_tuples[i][0], HSV_tuples[i][1], HSV_tuples[i][2])[2]
        a[0,0][0] = r
        a[0,0][1] = g
        a[0,0][2] = b
        p.set_data(a)
    i = i + 1
    plt.pause(0.01)
