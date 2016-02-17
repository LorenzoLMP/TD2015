clear;clc;
filename = "es14_10vpp_33k";fid = fopen(filename,"r");fscanf(fid, '%s', 8);a = fscanf(fid, '%*s\t%*9s %6f\t%f', [2, inf]);
b = a'(:,1)/1000000;
m = [b(95:130), a'([95:130],2)];
xs = [m(1,1):0.000002:m(length(m(:,2)),1)];
lin = interp1(m(:,1), m(:,2), xs, "pchip");
plot(m(:,1), m(:,2),'or', xs, lin', 'LineWidth',1.5,'k')
grid on;
title('Interpolazione rise-time R = 32.6kOhm', 'FontSize',14);
xlabel('t [s]','FontSize',16);ylabel('tensione [V]','FontSize', 16);
vmin = mean(m([1:5],2));

vmax = mean(m([length(m(:,2))-5,length(m(:,2))],2));
v = [vmin, vmax]
delta = vmax - vmin;

for i = 1:length(xs)
  if (lin'(i) <= vmin + delta*0.1)
    tmin = xs(i);
   endif
endfor 

for j = 1:length(xs)
  if (lin'(j) <= vmin + delta*0.9)
    tmax = xs(j);
   endif
endfor 

[tmin, tmax]
disp("trise ="), disp(tmax-tmin)

print('es14_10vpp_33k_hermite_epsc2', '-depsc2','-r400')