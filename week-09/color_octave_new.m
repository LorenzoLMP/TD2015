N = 315;
dt=0.01;



A=hsv(N);
figure(1, 'Color', [0,0,0]);
pause(5);
for i=1:length(A)
    figure(1, 'Color', [A(i,:,:)]);
    pause(dt);
    
end
figure(1, 'Color', [0,0,0]);

%fid1 = fopen('coeffic_matrix', 'w');fprintf(fid1, '%f\t%f\t%f\n', A);