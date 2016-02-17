from pylab import * 
from numpy import *
import os

os.chdir("C://Users/User/Desktop/grafici")

f, v, ph = loadtxt("es5_300000c_3pp_40.txt", unpack = True)

l = len(f)

for k in range (0, l):
    ph[k]=ph[k] - 0.0006*f[k]


title("Sfasamento corretto")
xlabel("f [Hz]")
ylabel("$\phi$ [deg]", labelpad=15)
xscale("log")
xlim(90, 10000)
ylim(-0.05, 0.05)
grid(color="black")
errorbar(f, ph, linestyle="", color="black", marker="+")
savefig("phase300000.png")
show()
