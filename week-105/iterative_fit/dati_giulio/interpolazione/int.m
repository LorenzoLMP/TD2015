A = load("int.txt");
T = A(:,1)+273;
v = A(:,2);

err = 0.5;
pin = [0.1; 0.1];
dp = [0.001; 0.001];

F = @(x,p) p(1)+p(2)*x;
%% dFdp = @(x, f, p, dp, func) [exp(p(2)*x)-1, p(1)*x.*exp(p(2)*x)];
niter =1000;
wt = (v - v .+ 1)./err;

global verbose;
verbose = 1;

[f1, p1, kvg1, iter1, corp1, covp1, covr1, stdresid1, Z1, r21] = leasqr (v, T, pin, F, 0.0001 , niter, wt);

p1
covp1

E = -p1(1)/p1(2)

Err = sqrt(covp1)

dE = E*sqrt((Err(1,1)/p1(1))**2 + (Err(2,2)/p1(2))**2 )
