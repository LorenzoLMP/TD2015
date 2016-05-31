from pylab import *
from scipy import optimize
def linfit(x, *par):
    return par[0]*x
def errorelin(x): 
    return linfit(x,*g_0)
def tension_junc(x, *par):
    return log(x/abs(par[1]) + 1)/par[0] + x*par[2]*10**(-6)
def fitsolve(I_j, I_s, B, R, v):
    return v - log(abs(I_j)/abs(I_s) + 1)/B + I_j*R*10**(-6)
def erroreloop(x, *par):
    return tension_junc(x,*par)
def tens(x):
    return tension_junc(x, *p_loop)
def current_v(x, I_s, B, R, I_j, G):
    return G*x + I_s*(exp(B*(x-R*I_j)) - 1)

def loop_fit(indirizzo, lim_current_inf, sup_current):
    data= genfromtxt(indirizzo)
    ydata = data[:,1]
    xdata = data[:,0]
    sigmay = 0.1
    sigmax = 0.0003
    p0lin = [2]
    g_0, pcov_lin = optimize.curve_fit(linfit, xdata[:argmax(ydata>=lim_current_inf)], ydata[:argmax(ydata>=lim_current_inf)], p0lin, sigmay)
    g_var = sqrt(pcov_lin)
    print('g0: ', g_0[0], '+-', g_var[0][0])
    p0_loop = [20, 0.005, 2]
    val_g = False
    val_B = False
    val_is = False
    val_Rs = False
    j = 0
    while j<20:
        #print(val_g==False & val_B==False & val_is==False & val_Rs==False)
    #step 2:
        jun_cur = ydata - g_0*xdata
    #step 3:
        p_loop, pcov_loop = optimize.curve_fit(tension_junc, abs(jun_cur[argmax(jun_cur>=sup_current):]), xdata[argmax(jun_cur>=sup_current):], p0_loop, sigmax)
        #p_loop, pcov_loop = optimize.curve_fit(tension_junc, abs(jun_cur), xdata, p0_loop, sigmax)
        loop_var = sqrt(pcov_loop.diagonal())
    #step 4:
        jun_cur_1 = optimize.fsolve(fitsolve, jun_cur, (p_loop[1], p_loop[0], p_loop[2], xdata) )
    #step 5:
        tot_cur = g_0*xdata + jun_cur_1
    #step 6:
        delta_g, delta_g_pcov = optimize.curve_fit(linfit, xdata[:argmax(tot_cur>=lim_current_inf)], ydata[:argmax(tot_cur>=lim_current_inf)]-tot_cur[:argmax(tot_cur>=lim_current_inf)], g_0, sigmay)
        g_1 = g_0 + delta_g
    #check della convergenza
        if abs(g_1 - g_0) <= abs(delta_g)/2:
            val_g = True
        elif abs(g_1 - g_0) <= 10**(-6):
            val_g = True
        if abs(p_loop[0] - p0_loop[0]) <= abs(loop_var[0])/100:
            val_B = True
        if abs(p_loop[1] - p0_loop[1]) <= abs(loop_var[1])/100:
            val_is = True
        if abs(p_loop[2] - p0_loop[2]) <= abs(loop_var[2])/100:
            val_Rs = True
        print(val_g, val_B, val_is, val_Rs)
    #ridefinizione delle variabili
        print('B: ', p_loop[0], '+-', loop_var[0], ' I_s: ', p_loop[1], '+-', loop_var[1], ' R_s: ', p_loop[2], '+-', loop_var[2], 'G:', g_1[0], '+-', delta_g[0])
        g_0 = g_1
        p0_loop = p_loop
        j = j +1
        #print(val_g==False & val_B==False & val_is==False & val_Rs==False)
        #print(j)
    grid()
    yscale('log')
    rc('font', size=16)
    title(r"Caratteristica I-V T=%s° - fit"%(indirizzo[:4]), size=14.5)
    xlabel('Tensione V [V]')
    ylabel(r'Corrente I [$\mu $ A]')
    #ylim(0.1, 10000)
    plot(xdata, current_v(xdata, p_loop[1], p_loop[0], p_loop[2]*10**(-6), jun_cur_1, g_0), color='red', linewidth = 1.5, label='C=0')   
    #errorbar(xdata, ydata, sigmay, sigmax, linestyle='None', marker='o', color="black")
    plot(xdata, ydata, linestyle='None', marker='o', markersize=1, color="black")
    B  = r'B: $ %s  \pm  %s \, [V^{-1}] $'%(round(p_loop[0], 2), round(loop_var[0], 2))
    I_s  = r'$I_{S}$: $ %s  \pm  %s \, [nA] $'%(round(p_loop[1]*10**3, 2), round(loop_var[1]*10**3, 2))
    R_s  = r'$R_{S}$: $ %s  \pm  %s \, [\Omega] $'%(round(p_loop[2], 2), round(loop_var[2], 2))
    G  = r'G: $ %s  \pm  %s \, [\mu S]$ '%(round(g_1[0], 2), round(delta_g[0], 2))    
    text(0.45, 10, B, family='serif', style='italic', size=15)
    text(0.45, 3, I_s, family='serif', style='italic', size=15)
    text(0.45, 1, R_s, family='serif', style='italic', size=15)
    text(0.45, 0.3, G, family='serif', style='italic', size=15)
    savefig('%s.png'%(indirizzo[:4]), dpi=400)
    show()

dati = ['15_0.txt', '22_0.txt', '22_3.txt', '30_0.txt', '38_0.txt' ]

##for i in range(len(dati)):
##    loop_fit(dati[i], 1, 20)

loop_fit('15_0.txt', 1, 1)
