clc;clear;
filename = "es15_6pp_220pF";fid = fopen(filename,"r");fscanf(fid, '%s', 8);a = fscanf(fid, '%*s\t%*9s %6f\t%f', [2, inf]);
fid1 = fopen('es15_6pp_220pF_good', 'w');fprintf(fid1, '%f\t%f\n', a);
%fid2 = fopen('es15_6pp_good2', 'w');fprintf(fid2, '%f\t%f\n', a);