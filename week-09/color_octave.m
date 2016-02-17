N = 300; %quanti punti campiono
dt = 0.1; %quanto tempo aspetto


A = hsv(N);


for i=1:length(A)
  figure(1, 'Color', [A(i,:,:)]);
  pause(dt);
  
end