filename = "es_8_lb3333_vin_vout.txt"; fid = fopen(filename,"r");[y, ny] = fscanf(fid, '%f\t%f\t%f', [2, Inf]);




filename = "es_8_wp9294_vin_vout_2ampio"; fid = fopen(filename,"r");[y, ny] = fscanf(fid, '%f\t%f\t', [2, Inf]); c = polyfit(y'(:,1), y'(:,2), 25);x1 = linspace(2.1, 2.5, 500); z = polyval(c, x1); u = [c, -0.0094];roots(u)