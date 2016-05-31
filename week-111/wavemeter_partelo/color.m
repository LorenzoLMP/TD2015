N = 300;
dt=0.1;



A=hsv(N);

for i=1:length(A)
    figure(1, [A(i,:,:)]);
    pause(dt);
    
end