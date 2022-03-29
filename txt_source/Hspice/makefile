PATH := D:\HSPICE\hspice\BIN
CFLAG := -o
TARGET := test

$(TARGET):
	$(PATH)\hspice $(TARGET).sp $(CFLAG)
	echo %%plot for $(TARGET)>$(TARGET).m
	echo y=loadsig('$(TARGET).sw0');>>$(TARGET).m
	echo char=lssig(y)>>$(TARGET).m
	echo for index=2:1:length(char(:,1))>>$(TARGET).m
	echo 	flag=0;>>$(TARGET).m
	echo 	for i=1:1:length(char(index,:))>>$(TARGET).m
	echo 		if(char(index,i)==':')>>$(TARGET).m
	echo 			flag=1;>>$(TARGET).m
	echo 			[~,~,a]=y.data;>>$(TARGET).m
	echo 			legend(string(a));>>$(TARGET).m
	echo 		end>>$(TARGET).m
	echo 	end>>$(TARGET).m
	echo 	if(flag==0)>>$(TARGET).m
	echo 		figure(index)>>$(TARGET).m
	echo 		plotsig(y,char(index,:));>>$(TARGET).m
	echo 	end>>$(TARGET).m
	echo end>>$(TARGET).m

awaves:
	$(PATH)\awaves $(TARGET)

clean:
	del $(TARGET).lis $(TARGET).st0 $(TARGET).sw0 $(TARGET).ic0

allclean:
	del $(TARGET).lis $(TARGET).st0 $(TARGET).sw0 $(TARGET).ic0 $(TARGET).m