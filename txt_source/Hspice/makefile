PATH := D:\HSPICE\hspice\BIN
CFLAG := -o
TARGET := test

$(TARGET):
	$(PATH)\hspice $(TARGET).sp $(CFLAG)
	echo %%plot for $(TARGET)>$(TARGET).m
	echo y=loadsig('$(TARGET).sw0');>>$(TARGET).m
	echo char=lssig(y)>>$(TARGET).m
	echo for index=1:1:length(char(:,1))>>$(TARGET).m
	echo 	figure(index)>>$(TARGET).m
	echo 	plotsig(y,char(index,:));>>$(TARGET).m
	echo end>>$(TARGET).m

awaves:
	$(PATH)\awaves $(TARGET)

clean:
	del $(TARGET).lis $(TARGET).st0 $(TARGET).sw0 $(TARGET).ic0

allclean:
	del $(TARGET).lis $(TARGET).st0 $(TARGET).sw0 $(TARGET).ic0 $(TARGET).m