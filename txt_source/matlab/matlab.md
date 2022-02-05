## Matlab使用语法

注：文中所有标点符号默认为英文格式

format	loose/compact（输出松散/紧凑）	+（正数显示） rat（小数）bank两位小数

数组中，逗号或空格表示建立行向量，分号表示列向量，冒号建立连续元素

对于行列式间运算，抑或符号表示矩阵幂运算，.^表示数组元素幂运算

同样，.✳表示数组乘积，./数组右除，.\数组左除

'表示转置操作（T）,会自动将矩阵复数元素转换为共轭，如果不这样用.'

conj（a，b）求共轭复数向量

dot(a,b)求向量点乘，cross（a，b）则表示向量叉乘（必须是三维的）

linspace（a，b）建立等间隔100个，b后加，n表示具体数目

logspace（a，b，n）建立10的a到b次幂对数值等差的n个向量、

length返回数组内元素个数

引用数组内单个元素a（n），所有元素a（：），部分连续a（n1：n2）

矩阵引用，A（n1,n2）单个元素，A（：，n2/n1:n2）单列或连续列

exp表示e的幂运算，imag（）求虚部，real（）求实部

abs返回向量的绝对值，返回虚数的模

矩阵的输入：A=[n1,n2;n3,n4]，单个矩阵+变量/常数，使内部每个元素变化

建立单位矩阵，eye（n）；建立零矩阵，zeros（n/m，n）；全1矩阵，ones（）

A=[]建立空数组，A(n1,:)=[]删除某一行，E=A([1,1,1,1],:)复制A第一行四次

求行列式结果，det(A);A\b=x,系数矩阵左除常量矩阵的得方程解

rank()求矩阵的秩，inv()求逆矩阵，但由于为计算机计算，会产生-0.0000(精度范围)

当矩阵不可逆时，求伪逆矩阵pinv()

为未知数给出最小范数实数解，matlab将其中一个变量设为0

rref()函数使用高斯-乔丹（Gauss-Jordan）消元法产生矩阵降价后的阶梯形式

魔方矩阵（幻方）：magic()

LU（三角）分解[L,U]=lu(A),方程的解x=U\(L\b)

[L,U]=qr(A)（正交三角），[L,U]=svd(A)（奇异值）

定义函数：x=[start：interval：end]，表示在[start,end]上以interval间隔递增；y=f（x）；

注意，用分号可以抑制matlab进行输出

plot(x,y)进行绘图，重新命令函数进行新的定义（否则出错Vectors must be the same lengths）

fplot('function string', [xstart, xend])，避免矩阵相乘维度错误，同时尽可能产生精确的图像，绕过绘图的时间间隔，自动决定绘图的点数

不然就使用.※来避免上述错误，进行数组相乘，这也是对函数平方的正确用法

在绘图函数后接，xlabel（‘’），ylabel（‘’），title（‘’），为横纵坐标和函数提供名称

在相同位置接上grid on/off产生/关闭网格，接上axis equal产生两坐标轴比例和间距相同的图像

如果换成axis auto，则让matlab自己决定，axis（[x1 x2 y1 y2]）设置图像范围，接square使坐标系呈立方状，接equal使单位横纵坐标相同

在一个坐标系中绘制多个函数图像，（f）plot(x1,y1,x2,y2,'--')，后接单引号表示前一个函数的线形类型，实线‘-’，虚线‘--’，虚点线‘-.’，点线‘：’，关于颜色，默认不同，但是如果自己想设置，在前面的‘’中如格式‘b--’‘--b’，八种颜色：白w黑k蓝b红r青c绿g洋红m黄y

legend（‘’）可在生成的函数图像中产生图例

subplot(m,n,p)绘制子图，mn表示子图的行列数，p表示要贴上的窗口序号，接着用（f）plot就可以贴上对应的函数

hold on可以在一个坐标系上连续建立函数图像（意思是保存上一个图像）

polar和plot等价，建立极坐标图像r=aθ（阿基米德螺线);

bar则建立柱状图,barh产生横向柱状图,bar3则是立体状，内接'grouped'组合,'stacked'堆合，则输入的数据是多列数组，后接legendt贴上颜色标签

loglog建立对数图像，横纵坐标的刻度为10的幂

相应的，semilogx（x,y）是横坐标使用对数值，semilogy（）则是纵坐标

plot(x,y,'o',x,y),使得每个点都被圈上，在o的前后可加上颜色字母来改变圈的颜色

plot后接set（gca，'XTicklable',['']）可以改变横(纵Y)坐标每个点的名称，但是名称长度必须相同

set(gca,'xtick',[])表示去掉横坐标轴刻度，[n1:n2]表示规定坐标轴刻度

stem(x,y,'--dg')建立针头图（大头针),d表示标记形状，方块s菱形d五角星p圆圈o叉号x星号※点号.

在括号内后接'fill'则可以将标记填充

[x,y]=meshgrid(x1:a:x2,y1:b:y2]，产生矩阵元素，当xy范围相同时，[]中只需要一半

contour(x,y,z)建立等高线图，前接[C,h]=用来记录信息，后接

set(h,'ShowText','on','TextStep',get(h,'LevelStep')※2)，※后表示等高线标注间距,on改成off关闭

contour3(z,n)产生n个级别的三维等高线，注意n大小不要过大，100~200已经几乎看不出间隙，当1000时明显卡顿，1w时已经无法承受

 surface(x,y,z,'EdgeColor',[.8 .8 .8],'FaceColor','none'),edge使得三维等高线有边缘线,[]内调整边缘线颜色，face使得有连续面，[]同理

view（α1,α2)给出三维观察视角,α1为水平旋转角度,α2为竖直旋转，0,0为前视图

mesh(x,y,z)产生三维图像，也就是plot在三维上的扩展

surf(x,y,z)、surfc绘制表面带有渐变颜色的图像，后者会在图像中留下投影

surfl绘制光照表面图像(l:lighted surface)，shading interp/flat/faceted使得阴影:使用颜色插值着色/网格着色隐藏网格/网格着色

colormap(gray)对图像调节色度

[x,y,z]=cylinder,返回高、半径为1的圆柱体，沿周长有20个等分点，加上(r,n)修改半径和等分点数

plot3(x,y,z)建立三维线图

hist产生柱状图

mean函数求均值（数组则是每一列），median求中位数，std求标准偏差

判定中，~=不相等，if(语句|语句)或if 语句，以下行都属于if，直到遇到else或end

for index = start : increment : finish（第一行）statements（中间）end（最后一行）

index从start以increment的增量到finish进行循环，每次循环执行statements

while condition（第一行）statements（中间）end（最后一行）

switch expression（第一行） case n1（第二行） do these statements（第三行） 

 case n2（第四行） do these statements （等等）end（最后一行）

disp('')表示打印，input('')表示输入

声明函数：function 变量返回名=函数名称(参数)（第一行）语句（中间）end（最后一行）

%开头表示注释，会被忽略掉

size检查数组元素个数

s=solve(方程),可以用来解方程（组）,括号内的书写格式不一，加''、[]用单括号，不加用双括号(后两者比较稳妥)，但是方程右边也可以没有，默认为0，内后接,参数，具体指明，或者将一个方程赋值给变量，就可以变为solve(变量),s.x表示x的值(类似于结构体)

syms定义符号变量,double()转换变量为double型

ezplot(y),可以绘制上述的函数图像，且已经附带标题:函数,后内接,[x1,x2,y1,y2]确定范围

expand可以展开方程，如果多变量且变量已经被确定集合了，展开就会带入具体值而很长

collect则是合并化简方程，factor则会因式分解，simplify能进行多项式相除

log对数函数，sin/cos/tan/cot/asin/acos/atan/acot三角函数

lambertw()朗伯W函数，是f(w)=w.exp(w)的反函数

taylor(函数,n)可以将函数进行泰勒展开，没有,n时默认为3项展开

好用不坏的resample(x,fs',fs),将采样率从fs改为fs'

[x,fs]=audioread('文件名称'),audiowrite('文件名称',x,fs)

stairs(x,y)生成阶梯图，即向下取整

floor(x)，向下取整

dec2bin(x) 10→2，dec2hex(x)10→16，dec2base(x,base),10→base
bin2dec('x')2→10，hex2dec('x')16→10，oct2dec(x),8→10，base2dec(x,base),base→10

A＝ifft（X，N，DIM），一维反DFT算法，X表示输入图像；N表示采样间隔点，如果X小于该数值，那么Matlab将会对X进行零填充，否则将进行截取，使之长度为N；DIM表示要进行离散傅立叶变换。IFFT函数和离散傅立叶变换函数FFT完全相同。

nargin可以判定一个函数中输入变量的个数

nextpow2求n的无符号二进制位数，亦即求指数2^a>=n的最小a解

subs(S,OLD,NEW) 表示将符号表达式S中的符号变量OLD替换为新的值NEW。

digits(n)用于规定运算精度，n位有效数字，默认的一般为32；vpa(表达式)，限定内部运算精度为digits规定的，如果没有必要表示更多有效数字，vpa只表达有意义的，如vpa(0)，显示0.0

重点：title(['{上标}_{下标}',' \alpha','x=',num2str(x)],'position',[x,y],'Fontname','字体','Fontsize',n(字号),sprintf('\n')(换行))，希腊字母第一个字母大写表示大写

希腊字母对照：Αα：阿尔法 Alpha	Ββ：贝塔 Beta	Γγ：伽玛 Gamma	
Δδ：德尔塔 Delte	Εε：艾普西龙 Epsilon	ζ ：捷塔 Zeta	Ζη：依塔 Eta
Θθ：西塔 Theta	Ιι：艾欧塔 Iota	Κκ：喀帕 Kappa	∧λ：拉姆达 Lambda	
Μμ：缪 Mu	Νν：拗 Nu	Ξξ：克西 Xi	Οο：欧麦克轮 Omicron
Ππ：派 Pi		Σσ ς：西格玛 Sigma	Ττ：陶 Tau	Υυ：伊普西隆 Upsilon
Φφ：Phi		Χχ：凯 chi	Ψψ：剖赛psi	Ωω：欧米噶  omega

三个连续的.表示续行

rgb2gray()将RGB图像转换为灰度图像，rgb2ind()真彩色图像转换为索引图象，后者可以输入参数dither_option，表示是否抖动

[X,map]=gray2ind(l,n)l是原灰度图像，n为灰度级数，默认为64，l换成BW则是二值图像，n默认为2，其实都是灰度图像，只是默认值不同

总归，图像格式的转换中，gray表示灰度，对应double型，ind表示索引，对应logical型，rgb表示真彩色，对应double型

im2bw()先将图像转换为灰度，然后通过阈值转换为二值

mat2gray()将数据矩阵转换为灰度图像

info(结构数组)=imfinfo('filename','fmt')/imfinfo('文件名.扩展名')

imread()读取图像文件，imwrite()写入文件

### TODO

