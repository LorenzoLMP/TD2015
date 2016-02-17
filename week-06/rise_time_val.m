filename = "es14_10vpp_10k";fid = fopen(filename,"r");fscanf(fid, '%s', 8);a = fscanf(fid, '%*s\t%*9s %6f\t%f', [2, inf]);
b = a'(:,1)/1000000;
m = [b(40:60), a'([40:60],2)];
xs = [m(1,1):0.000002:m(21,1)];
lin = interp1(m(:,1), m(:,2), xs, "pchip");
plot(m(:,1), m(:,2),'or', xs, lin')
vmin = mean(m([1:4],2));
vmax = mean(m([15:20],2));
v = [vmin, vmax]
delta = vmax - vmin;

for i = 1:201
  if (lin'(i) <= vmin + delta*0.1)
    tmin = xs(i);
   endif
endfor 

for j = 1:201
  if (lin'(j) <= vmin + delta*0.9)
    tmax = xs(j);
   endif
endfor 

[tmin, tmax]
disp("trise ="), disp(tmax-tmin)