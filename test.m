x=[0:0.001:1];
omega=x*1e9*2*pi;
R23=40*50/(40+50);
V2G=R23./(R23+50+1/1j./omega/2e-12);
A=abs(V2G);
attenuation=-20*log10(A);
phase=angle(V2G);
tg=(phase(3:end)-phase(2:end-1))/0.001;
figure(1);
semilogx(x,A);legend("V2/VG");
figure(2);
semilogx(x,attenuation);legend("attenuation");
figure(3);
semilogx(x,phase/pi*180);legend("phase");
figure(4);
semilogx(x(3:end),tg);legend("tg");
syms
% a=vpasolve(1.602e-19*16*8.85e-14*1.433*x/(2*(5+0.0259*log(1.433*x^2/(2.4e13)^2))*2.433)-(1.5e-9)^2,x)
% a=vpasolve(1e-2*1.602e-19*(1.5e10)^2*((35/2e-6)^0.5/5.6e18+(12.4/1e-6)^0.5/1.2e16)*exp(x/0.0259)-0.5e-3,x)
