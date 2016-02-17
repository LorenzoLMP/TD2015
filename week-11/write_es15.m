clc;clear;
filename = "es12_uscita";fid = fopen(filename,"r");fscanf(fid, '%s', 8);a = fscanf(fid, '%*s\t%*11s%4f\t%8f', [2, inf]);
m = [a'(:,1)/10000, a'(:,2)];
fid1 = fopen('es12_uscita_good', 'w');fprintf(fid1, '%4f\t%8f\n', m');
fclose(fid1)
%fid2 = fopen('es15_6pp_good2', 'w');fprintf(fid2, '%f\t%f\n', a);