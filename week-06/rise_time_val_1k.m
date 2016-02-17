clear;clc;
filename = "es14_10vpp_1k";fid = fopen(filename,"r");fscanf(fid, '%s', 8);a = fscanf(fid, '%*s\t%*9s %6f\t%f', [2, inf]);
b = a'(:,1)/1000000;
m = [b(15:60), a'([15:60],2)];
xs = [m(1,1):0.000001:m(length(m(:,2)),1)];
lin = interp1(m(:,1), m(:,2), xs, "pchip");
plot(m(:,1), m(:,2),'or', xs, lin')
%plot(xs, lin', 'or')
vmin = mean(m([1:5],2));

vmax = mean(m([length(m(:,2))-26,length(m(:,2))-20],2));
%vmax = 0
v = [vmin, vmax]
delta = vmax - vmin;

for i = 1:length(xs)
  if (lin'(i) <= vmin + delta*0.1)
    tmin = xs(i);
   endif
endfor 

%for j = 1:length(xs)
%  if (lin'(j) <= vmax - delta*0.1) 
%    tmax = xs(j);
%    lin'(j)
%   endif
%endfor 

j = 1;
sent = true;
while (j < length(xs) & sent)
  if (lin'(j) <= vmax - delta*0.1) 
    tmax = xs(j);
    lin'(j);
   elseif 
    sent = false;
  endif
  j++;
endwhile

[tmin, tmax]
disp("trise ="), disp(tmax-tmin)