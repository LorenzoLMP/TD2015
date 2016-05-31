from pylab import *
from scipy import optimize
data= genfromtxt('46_6_fullrange.txt')
ydata = data[:,1]
xdata = data[:,0]
sigmay = 0.1
sigmax = 0.03

def linfit(x, *par):
    return par[0]*x

p0lin = [2]
lim_current = 1
sup_current = 20
#lung = 10 #numero dei dati da prendere per il primo fit lineare
g_0, pcov_lin = optimize.curve_fit(linfit, xdata[:argmax(ydata>=lim_current)], ydata[:argmax(ydata>=lim_current)], p0lin, sigmay)
g_var = sqrt(pcov_lin)
print('g0: ', g_0[0], '+-', g_var[0][0])

def errorelin(x): 
    return linfit(x,*g_0) 
Slin = 0
for i in range(lung): 
	Slin = Slin + ((((ydata[i]- errorelin(xdata[i]))/sigmay)**2))

print('chi^2 (G): ', Slin)

#########################################
def tension_junc(x, *par):
    return log(x/abs(par[1]) + 1)/par[0] + x*par[2]*10**(-6)

def fitsolve(I_j, I_s, B, R, v):
    return v - log(abs(I_j)/abs(I_s) + 1)/B + I_j*R*10**(-6)
def erroreloop(x, *par): 
	return tension_junc(x,*par)
p0_loop = [20, 0.005, 2]

##########################################
val_g = False
val_B = False
val_is = False
val_Rs = False
j = 0
while val_g==False & val_B==False & val_is==False & val_Rs==False:
    #step 2:
    jun_cur = ydata - g_0*xdata
    #step 3:
    p_loop, pcov_loop = optimize.curve_fit(tension_junc, abs(jun_cur[argmax(jun_cur>=sup_current):]), xdata[argmax(jun_cur>=sup_current):], p0_loop, sigmax)
    #p_loop, pcov_loop = optimize.curve_fit(tension_junc, abs(jun_cur), xdata, p0_loop, sigmax)
##    print("matrice di covarianza:") 
##    print(pcov_loop) 
##    if pcov_loop is inf:
##        loop_var = [1,1,1]
##    else:
    loop_var = sqrt(pcov_loop.diagonal())
##    for i in range(len(p_loop)):
##        print('p[%s]:'%(i), p_loop[i], '+-', loop_var[i])
    #step 4:
    def tens(x):
        return tension_junc(x, *p_loop)
    jun_cur_1 = optimize.fsolve(fitsolve, jun_cur, (p_loop[1], p_loop[0], p_loop[1], xdata) )
    #step 5:
    tot_cur = g_0*xdata + jun_cur_1
    #step 6:
    delta_g, delta_g_pcov = optimize.curve_fit(linfit, xdata[:argmax(tot_cur>=lim_current)], ydata[:argmax(tot_cur>=lim_current)]-tot_cur[:argmax(tot_cur>=lim_current)], g_0, sigmay)
    g_1 = g_0 + delta_g
    #print('g0, g1: (%s,%s)'%(g_0,g_1))
    #print('deltag: ', delta_g)
    #check della convergenza
    if abs(g_1 - g_0) <= abs(delta_g)/10:
        val_g = True
    elif abs(g_1 - g_0) <= 10**(-6):
        val_g = True
    if abs(p_loop[0] - p0_loop[0]) <= abs(loop_var[0])/10:
        val_B = True
    if abs(p_loop[1] - p0_loop[1]) <= abs(loop_var[1])/10:
        val_is = True
    if abs(p_loop[2] - p0_loop[2]) <= abs(loop_var[2])/10:
        val_Rs = True
    print(val_g, val_B, val_is, val_Rs)
    #ridefinizione delle variabili
    print('B: ', p_loop[0], '+-', loop_var[0], ' I_s: ', p_loop[1], '+-', loop_var[1], ' R_s: ', p_loop[2], '+-', loop_var[2], 'G:', g_1[0], '+-', delta_g[0])
##    print('G:', g_1[0], '+-', delta_g[0])
    g_0 = g_1
    p0_loop = p_loop
    j = j +1
    #print(j)

print('G:', g_0[0], '+-', delta_g[0])
print('B:', p_loop[0], '+-', loop_var[0])
print('I_s:', p_loop[1], '+-', loop_var[1])
print('R_s:', p_loop[2], '+-', loop_var[2])

def current_v(x, I_s, B, R, I_j, G):
    return G*x + I_s*(exp(B*(x-R*I_j)) - 1)

grid()
yscale('log')
t = linspace(0, 0.71, 300) 
plot(xdata, current_v(xdata, p_loop[1], p_loop[0], p_loop[2]*10**(-6), jun_cur_1, g_0), color='blue', linewidth = 1, label='C=0')   
plot(xdata, ydata, linestyle='None', marker='+', color="black")
show()
