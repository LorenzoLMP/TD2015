filename = "ws7ok.txt";fid = fopen(filename,"r");a = fscanf(fid, '%f\t%f', [2, inf]);
xf = (a'(:,1)-450)/1000;
yf = log(a'(:,2));
xpch = ([450:1:500]-450)/1000;
%ypch = interp1 (xf, yf, [450:1:500], "pchip");
%ypch = ppval (interp1(xf, yf, "spline", "pp"), xpch);
%YI = pchip (xf, yf, xpch)
p = polyfit(xf, yf, 11);
y = polyval (p, xpch);
y0 = polyval (p, xf);

%plot (xf,yf,"r", xpch,y,"b", xf,y0,"g");

X = [(xpch'*1000)+450; a'(:,1)];
Y = [y'; yf];
b = [X,Y];
plot (a'(:,1),log(a'(:,2)),"r", "markersize", 100, X,Y,"--k");
title("Estrapolazione curva di calibrazione");
xlabel('Wavelength [nm]');ylabel('log(CH1/CH2)');
fid1 = fopen('ws7ok_extended.txt', 'w');fprintf(fid1, '%f\t%f\n', b.');fclose("all");