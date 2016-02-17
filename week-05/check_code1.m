f = '(0.000001)*e.^(40*x)';a = eval(f);c = polyfit(x, a, 16);x1 = linspace(2, 2.5, 1000); z = polyval(c, x1);
plot(x, a, 'o-r', x1, z)

filename = "es_8_lb3333_vin_vout"; fid = fopen(filename,"r");[y, ny] = fscanf(fid, '%f\t%f\t%f', [2, Inf]); c = polyfit(y'(:,1), y'(:,2), 25);x1 = linspace(2.1, 2.5, 500); z = polyval(c, x1); c(26) = c(26) - 0.0094;roots(c);plot(y'(:,1), y'(:,2), 'o-r', x1, z)