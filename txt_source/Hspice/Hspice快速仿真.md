### 目的

为摆脱已有的11和15版本较为“陈旧”的UI界面，可以借助vscode等可运行终端的编辑器

### 步骤

主要内容为makefile(暑期认知实习所学可以拿出来用了)

```makefile
PATH := .\hspice\BIN(path_of_hspice.exe)
CFLAG := -o
TARGET := xx(name_from_xx.sp)

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
```

使用时和.sp放置在一起，于终端执行make命令即可

​	将生成仿真文件和相应的matlab运行脚本，绘制结果图形

​	因为终端当前路径与众多文件相同，在此处唤出matlab也尤为方便

(至于vscode等的文件打开、复制方便性不言而喻)

此处如果电脑没有配置make的话，请使用mingw等安装

hspice还有其他命令行，可以通过程序内部的help等说明文件了解