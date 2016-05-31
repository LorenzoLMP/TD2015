N = 300;
dt=0.1;



A=hsv(N);
figure(1, 'Color', [0,0,0]);
pause(5);
for i=1:length(A)
    figure(1, 'Color', [A(i,:,:)]);
    pause(dt);
    
end
figure(1, 'Color', [0,0,0]);