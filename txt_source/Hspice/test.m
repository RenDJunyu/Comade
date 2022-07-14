%plot for test
y=loadsig('test.tr0');
char=lssig(y)
for index=2:1:length(char(:,1))
	flag=0;
	for i=1:1:length(char(index,:))
		if(char(index,i)==':')
			flag=1;
			[~,~,a]=y.data;
			legend(string(a));
		end
	end
	if(flag==0)
		figure(index)
		plotsig(y,char(index,:));
	end
end
