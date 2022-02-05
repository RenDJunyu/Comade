%plot for rlgc2sp
y=loadsig('rlgc2sp.tr0');
char=lssig(y)
for index=1:1:length(char(:,1))
	figure(index)
	plotsig(y,char(index,:));
end
