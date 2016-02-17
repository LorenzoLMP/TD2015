import colorsys
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm


N = 5
HSV_tuples = [(x*1.0/N, 0.5, 0.5) for x in range(N)]
RGB_tuples = map(lambda x: colorsys.hsv_to_rgb(*x), HSV_tuples)
#HSV_tuples= np.array(HSV_tuples)
rgb = colorsys.hsv_to_rgb(HSV_tuples[1][0], HSV_tuples[1][1], HSV_tuples[1][2])
print(rgb)
