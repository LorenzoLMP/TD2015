from pylab import *
from scipy import optimize
def linfit(x, *par):
    return par[0]*x
def linexp(x, *par):
    return par[0]*x + par[1]*(exp(par[2]*x) +1 )
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

def prop_error(x, sigmax, I_s, deltais, B, deltaB, R, deltaR, G, deltaG, I_j, deltaIj  ):
    return( sqrt(   ((G + I_s*(exp(B*(x-R*I_j)) - 1) )**2)*sigmax**2 + ( (exp(B*(x-R*I_j)) - 1)**2)*deltais**2 + ( (x*I_s*(exp(B*(x-R*I_j)) - 1))**2)*deltaB**2 + ( (I_s*B*(exp(B*(x-R*I_j)) - 1))**2)*deltaR**2 + (x**2)*deltaG**2 + ( (R*B*I_s*(exp(B*(x-R*I_j)) - 1))**2)*deltaIj**2 ) )

def loop_fit(indirizzo, lim_current_inf, sup_current, matrix):
    data= genfromtxt(indirizzo)
    ydata = data[:,1]
    xdata = data[:,0]
    sigmay = 0.05
    sigmax = 0.0003
    p0lin = [2]
    p0exp = [2, 0.005, 20]
    #g_0, pcov_lin = optimize.curve_fit(linfit, xdata[:argmax(ydata>=lim_current_inf)], ydata[:argmax(ydata>=lim_current_inf)], p0lin, sigmay)
    g_0, pcov_lin = optimize.curve_fit(linexp, xdata[:argmax(ydata>=lim_current_inf)], ydata[:argmax(ydata>=lim_current_inf)], p0exp, sigmay)
    g_0 = g_0[0]
    pcov_lin = pcov_lin[0][0]
    g_var = sqrt(pcov_lin)
    #print('g0: ', g_0, '+-', g_var[0][0])
    p0_loop = [20, 0.005, 2]
    val_g = False
    val_B = False
    val_is = False
    val_Rs = False
    j = 0
    while val_g==False or val_B==False or val_is==False or val_Rs==False:
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
        if abs(g_1 - g_0) <= abs(delta_g):
            val_g = True
        elif abs(g_1 - g_0) <= 10**(-6):
            val_g = True
        if abs(p_loop[0] - p0_loop[0]) <= abs(loop_var[0]):
            val_B = True
        #print(val_B)
        #print(abs(p_loop[0] - p0_loop[0]) - abs(loop_var[0]))
        if abs(p_loop[1] - p0_loop[1]) <= abs(loop_var[1])/100:
            val_is = True
        if abs(p_loop[2] - p0_loop[2]) <= abs(loop_var[2])/100:
            val_Rs = True
        print(val_g, val_B, val_is, val_Rs)
    #ridefinizione delle variabili
        print('B: ', p_loop[0], '+-', loop_var[0], ' I_s: ', p_loop[1], '+-', loop_var[1], ' R_s: ', p_loop[2], '+-', loop_var[2], 'G:', g_1[0], '+-', delta_g[0])
        deltaIj = jun_cur_1 - jun_cur
        g_0 = g_1
        p0_loop = p_loop
        j = j +1
        #print(j)
        #plot(xdata, ydata-tot_cur)
        #show()
    grid()
    yscale('log')
    rc('font', size=16)
    title(r"Caratteristica I-V T=%s° - fit"%(data[:,2][1]), size=14.5)
    xlabel('Tensione V [V]')
    ylabel(r'Corrente I [$\mu $ A]')
    ylim(0.02, 10000)
    lim_err = 2300
    plot(xdata, current_v(xdata, p_loop[1], p_loop[0], p_loop[2]*10**(-6), jun_cur_1, g_0), color='blue', linewidth = 1.5)   
    errorbar(xdata[:argmax(ydata>=lim_err)], current_v(xdata, p_loop[1], p_loop[0], p_loop[2]*10**(-6), jun_cur_1, g_0)[:argmax(ydata>=lim_err)], prop_error(xdata,sigmax,p_loop[1],loop_var[1],p_loop[0],loop_var[0], p_loop[2], loop_var[2],g_1[0],delta_g[0],jun_cur_1,deltaIj)[:argmax(ydata>=lim_err)], sigmax, linestyle='None',  color="blue")
    errorbar(xdata, ydata, sigmay, sigmax, linestyle='None', marker='o', markersize=1, color="red")
    B  = r'B: $ %s  \pm  %s \, [V^{-1}] $'%(round(p_loop[0], 2), round(loop_var[0], 2))
    I_s  = r'$I_{S}$: $ %s  \pm  %s \, [nA] $'%(round(p_loop[1]*10**3, 2), round(loop_var[1]*10**3, 2))
    R_s  = r'$R_{S}$: $ %s  \pm  %s \, [\Omega] $'%(round(p_loop[2], 2), round(loop_var[2], 2))
    G  = r'G: $ %s  \pm  %s \, [\mu S]$ '%(round(g_1[0], 2), round(delta_g[0], 2))    
    text(0.45, 10, B, family='serif', style='italic', size=15)
    text(0.45, 3, I_s, family='serif', style='italic', size=15)
    text(0.45, 1, R_s, family='serif', style='italic', size=15)
    text(0.45, 0.3, G, family='serif', style='italic', size=15)
    savefig('%s.png'%(indirizzo), dpi=400)
    show()
    matrix.append( ((p_loop[0], p_loop[1]*10**3, p_loop[2], g_1[0]), (loop_var[0], loop_var[1]*10**3, loop_var[2], delta_g[0]), data[:,2][1] ) )

dati = ['15_0.txt', '22_0.txt', '22_3.txt', '30_0.txt', '38_0.txt' ]

##for i in range(len(dati)):
##    loop_fit(dati[i], 1, 20)

parametri = []
array(parametri)
loop_fit('C1.txt', 1, 10, parametri)
loop_fit('C2', 1, 10, parametri)
loop_fit('C3', 1, 10, parametri)
loop_fit('C4', 1, 10, parametri)
loop_fit('C5', 1, 10, parametri)
loop_fit('C6', 1, 10, parametri)
loop_fit('C7', 1, 10, parametri)
loop_fit('C8', 1, 10, parametri)
loop_fit('C9', 1, 10, parametri)
loop_fit('C10', 5, 10, parametri)
loop_fit('C11', 5, 10, parametri)
loop_fit('C12', 5, 10, parametri)
loop_fit('C13', 5, 10, parametri)
loop_fit('C14', 5, 10, parametri)
loop_fit('C15', 5, 0, parametri)

out_file = open('parametri.txt', 'w')
out_file.write("B\tdeltaB\tI_s\tdeltais\tR_s\tdeltaR\tG\tdeltaG\tTemp\n")
for i in range(len(parametri)):
    out_file.write('%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n'%(parametri[i][0][0], parametri[i][1][0], parametri[i][0][1], parametri[i][1][1], parametri[i][0][2], parametri[i][1][2], parametri[i][0][3], parametri[i][1][3], parametri[i][2]) )
out_file.close()


##data = genfromtxt('parametri.txt')
##title(r"Parametro B in funzione della temperatura", size=14.5)
##xlabel('Temperatura °C')
##ylabel(r'B [$V^{-1}$]')
##grid()
##errorbar(data[:,8], data[:,0], data[:,1], 0.5, linestyle='None', marker='+', markersize=1, color="green")
##show()
##savefig('parametro_B_temp.png', dpi=400)
##
##title(r"Corrente di saturazione $I_{S}$ in funzione della temperatura", size=14.5)
##xlabel('Temperatura °C')
##ylabel(r'$I_{S}$ [nA]')
##grid()
##errorbar(data[:,8], data[:,2], data[:,3], 0.5, linestyle='None', marker='+', markersize=1, color="purple")
##show()
##savefig('parametro_Is_temp.png', dpi=400)
##
##
##title(r"Resistenzain serie $R_{S}$ in funzione della temperatura", size=14.5)
##xlabel('Temperatura °C')
##ylabel(r'$R_{S}$ [$\Omega $]')
##grid()
##errorbar(data[:,8], data[:,4], data[:,5], 0.5, linestyle='None', marker='+', markersize=1, color="blue")
##show()
##savefig('parametro_Rs_temp.png', dpi=400)

#data = genfromtxt('parametri.txt')
title(r"Parametro G in funzione della temperatura", size=14.5)
xlabel('Temperatura °C')
ylabel(r'G [$\mu $ S]')
grid()
errorbar(data[:,8], data[:,6], data[:,7], 0.5, linestyle='None', marker='+', markersize=2, color="orange")
show()
savefig('parametro_G_temp.png', dpi=400)
