# 图像与视觉

## 图像处理基本知识

    彩色成像：视觉
    数字图像：灰度图像是一维矩阵、彩色图像三维矩阵
    拜尔滤光片
        排列是有规律的，一般是每四个像素为一个单元，一个通过红色，一个通过蓝色，两个通过绿色
        采用红、绿、蓝三种颜色是模拟人眼对颜色的感知特性，因为人眼对绿色最为敏感，所以绿色绿光点的数量要多一倍
        通过绿光阵列得到原始图像后，可以利用插值算法将每个像素中缺失的两个通道值计算出来
    RGB颜色空间：
        对于给定的一种颜色，其光谱分布曲线用φ(λ)表示，该颜色对应的RGB值可以分别根据三刺激值曲线计算得出
$$
R=K\int_{380}^{780}\phi(\lambda)\overline{r}d\lambda
G=K\int_{380}^{780}\phi(\lambda)\overline{g}d\lambda
B=K\int_{380}^{780}\phi(\lambda)\overline{b}d\lambda
$$
        其中的R、G、B就是颜色的三通道
        生活中所见到的显示系统基本都采用了RGB颜色空间进行图像显示，比如计算机显示器、彩色电视机等

    HSV颜色空间
        HSV是用来从颜色轮或调色板中挑选颜色时使用的彩色系统，其比RGB颜色系统更接近人们对彩色的认知
$$
V\leftarrow{max}(R,G,B)\\
S\leftarrow\frac{V-min(R,G,B)}{V} if V \neq 0 otherwise 0\\
H\leftarrow{\frac{60(G-B)}{V-min(R,G,B)}} if V=R\\
120+\frac{60(B-R)}{V-min(R,G,B)} if V=G\\
240+\frac{60(R-G)}{V-min(R,G,B)} if V=B\\
If H<0 then H\leftarrow{H+360}. On output 0\leq{V}\leq1,0\leq{S}\leq1,0\leq{H}\leq360.
$$
        H是色彩
        S是深浅，S=0时，只有灰度
        V是明暗，表示色彩的明亮程度，但与光强无直接联系
        在HSV倒锥形模型中，分别对应色彩轮的角度、深浅半径、明暗高度
    图像卷积
        图像卷积步骤
            1)将卷积核围绕中心旋转180度
            2)滑动核，使其中心位于输入图像f(i,j)像素上
            3)利用下式求和，得到输出图像的g(i,j)像素值
            4)重复上述操作，直到求出输出图像的所有像素值
$$
g(i,j)=\sum_{k,l}f(i-k,j-l)h(k,l)=\sum_{k,l}f(k,l)h(i-k,j-l)
$$
        Matlab函数：imfilter(A,h,'conv')%imfilter默认是相关算子，因此当进行卷积计算时需要传入参数'conv'
        边缘效应
            当对图像边缘进行滤波时，核的一部分会位于图像边缘外面
        常用的策略包括
            1)使用常数填充：imfilter默认用0填充，这会造成处理后的图像边缘是黑色的
            2)复制边缘像素：I2=imfilter(I,h,'replicate')
            3)周期循环边缘像素：I3=imfilter(I,h,'circular')
    图像卷积应用
        高斯模糊：h=fspecial('gaussian',[5 5])
            ex: [2 4 5 4 2; 4 9 12 9 4; 5 12 15 12 5; 4 9 12 9 4; 2 4 5 4 2]/159
        浮雕
            ex: [1 0 0; 0 0 0; 0 0 -1]
        边缘检测
            [-1 0 1; -2 0 2; -1 0 1]水平方向
            [-1 -2 -1; 0 0 0; 1 2 1]垂直方向
    二维离散傅里叶变换
        1)定义
$$
F(u,v)=\frac{1}{MN}\sum_{x=0}^{M-1}\sum_{y=0}^{N-1}f(x,y)e^{-j2\pi(\frac{ux}{M}+\frac{vy}{N})}\\
u=0,1,...,M-1\ \ \ \ v=0,1,...,N-1
$$
        2)逆傅里叶变换
$$
f(x,y)=\sum_{u=0}^{M-1}\sum_{v=0}^{N-1}F(u,v)e^{-j2\pi(\frac{ux}{M}+\frac{vy}{N})}\\
x=0,1,...,M-1\ \ \ \ y=0,1,...,N-1
$$
        离散的情况下，傅里叶变换和逆傅里叶变换始终存在
    傅里叶变换的意义
        傅里叶变换好比一个玻璃棱镜
        棱镜是可以将光分成不同颜色的物理仪器，每个成分的颜色由波长决定
        傅里叶变换可看作是"数学中的棱镜"，将函数基于频率分成不同的成分

## 图像的傅里叶变换与卷积

    二维连续傅里叶变换
        1)定义
$$
F(u)=\int_{-\inf}^{\inf}f(x)e^{-j2\pi{ux}}dx\ \ F(u,v)=\int_{-\inf}^{\inf}f(x,y)e^{-j2\pi(ux+vy)}dxdy
$$
        2)逆傅里叶变换
$$
f(x)=\int_{-\inf}^{\inf}F(u)e^{j2\pi{ux}}du\ \ f(x,y)=\int_{-\inf}^{\inf}f(x,y)e^{j2\pi(ux+vy)}dudv
$$
        3)傅里叶变换特征参数
            F(u,v)=R(u,v)+jI(u,v)
            频谱/模
$$
|F(u,v)|=\sqrt{R^2(u,v)+I^2(u,v)}
$$
            能量谱/功率谱
$$
P(u,v)=|F(u,v)|^2=R^2(u,v)+I^2(u,v)
$$
            相位角
$$
\phi(u,v)=\arctan\frac{I(u,v)}{R(u,v)}
$$
    傅里叶变换的意义：详见L71
    二维离散傅里叶变换：详见L59
    图像的频谱幅度随频率增大而迅速衰减
        许多图像的傅里叶频谱的幅度随着频率的增大而迅速减小，这使得在显示与观察一幅图像的频谱时遇到困难。但以图像的形式显示它们时，其高频项变得越来越不清楚
        解决办法：对数化
        例题：对一幅图像实施二维DFT，显示并观察其频谱。
            解：源程序如下
                %对单缝进行快速傅里叶变换，以三种方式显示频谱，
                %即：直接显示（坐标原点在左上角）；把坐标原点平
                %移至中心后显示；以对数方式显示。
                f=zeros(512,512);
                f(246:266,230:276)=1;
                subplot(221),imshow(f,[]),title('单狭缝图像')
                F=fft2(f); %对图像进行快速傅里叶变换
                S=abs(F);
                subplot(222)
                imshow(S,[]) %显示幅度谱
                title('幅度谱（频谱坐标原点在左上角）')
                Fc=fftshift(F); %把频谱坐标原点由左上角移至屏幕中央
                subplot(223)
                Fd=abs(Fc);
                imshow(Fd,[])
                ratio=max(Fd(:))/min(Fd(:))
                %ratio = 2.3306e+007,动态范围太大，显示器无法正常显示
                title('幅度谱（频谱坐标原点在屏幕中央）')
                S2=log(1+abs(Fc));
                subplot(224)
                imshow(S2,[])
                title('以对数方式显示频谱')
    二维离散傅里叶变换的性质
        线性性
$$
f_1(x,y)\leftrightarrow{F_1(u,v)},f_2(x,y)\leftrightarrow{F_2(u,v)}\Rightarrow{c_1f_1(x,y)+c_2f_2(x,y)\leftrightarrow{c_1F_1(u,v)+c_2F_2(u,v)}}
$$
            证明
$$
DFT[c_1f_1(x,y)+c_2f_2(x,y)]\\
=\sum_{x=0}^{M-1}\sum_{y=0}^{N-1}[c_1f_1(x,y)+c_2f_2(x,y)]·e^{-j2\pi(\frac{ux}{M}+\frac{vy}{N})}\\
=c_1\sum_{x=0}^{M-1}\sum_{y=0}^{N-1}f_1(x,y)·e^{-j2\pi(\frac{ux}{M}+\frac{vy}{N})}+c_2\sum_{x=0}^{M-1}\sum_{y=0}^{N-1}F_2(x,y)·e^{-j2\pi(\frac{ux}{M}+\frac{vy}{N})}\\
=c_1F_1(u,v)+c_2F_2(u,v)
$$
                %imagelinear.m
                %该程序验证了二维DFT的线性性质,注意AB两张图片的尺寸必须相同
                f=imread('A.png');
                g=imread('B.png');
                [m,n]=size(g);
                f(m,n)=0;
                f=im2double(f);
                g=im2double(g);
                subplot(221)
                imshow(f,[])
                title('f')
                subplot(222)
                imshow(g,[])
                title('g')
                F=fftshift(fft2(f));
                G=fftshift(fft2(g));
                subplot(223)
                imshow(log(abs(F+G)),[])
                FG=fftshift(fft2(f+g));
                title('DFT(f)+DFT(g)')
                subplot(224)
                imshow(log(abs(FG)),[])
                title('DFT(f+g)')
        可分离性
            二维DFT可视为由沿x,y方向的两个一维DFT所构成
            