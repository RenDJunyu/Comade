# Java从入门到精通

## 1-9 基础知识

### 1-2 Java介绍

    Java是一种跨平台、面向对象的程序设计
    高级语言、在任何计算机、操作系统以及支持Java的设备上运行
    OAK-Java，语法与C++相似，一次编写、到处运行
    程序既是编译型、又是解释型的。编译后转换为Java字节码
        Java虚拟机(JVM)对字节码进行解释和运行，编译后的字节码采用针对JVM优化过的机器码形式保存
        虚拟机将字节码解释为机器码

    版本，Java SE标准板，EE企业版，ME嵌入式
    特性：简单、面向对象、分布性、可移植性、解释型、安全性、健壮性、多线程、高性能、动态

    Eclipse是一个较好的开发工具

### 3 Java语言基础

#### 3.1 Java主类结构

    Java程序的基本组成单元是类，类体中包括属性与方法两部分
    每个应用程序都必须包含一个main()方法，含有main()方法的类称为主类
    只支持英文字符，文件名必须和类名同名，Java注意大小写

    包声明
        一个Java应用程序是由若干个类组成的，语句package为声明该类所在的包，package为关键字
    声明成员变量和局部变量
        通常将类的属性称为类的全局变量(成员变量)，将方法中的属性称为局部变量；相应的声明分别在类体和方法体中，有各自的应用范围。
    编写主方法
        main()方法是类体中的主方法。该方法从{开始，从}结束。public、static和void分别是权限修饰符、静态修饰符和返回值修饰符，Java程序中的main()方法必须声明为public static void。String[] args是一个字符串类型的数组，是main()方法的参数。main()方法则是程序开始执行的位置
    导入API类库
        可以通过import关键字导入相关的类，可以通过JDK的API文档来查看这些类，主要包括类的继承结构、应用、成员变量表、构造方法表等

#### 3.2 基本数据类型

    整数类型
        用来存储整数整数值
            十进制、八进制(0开头)、十六进制(0x、0X)
        根据占据内存: byte、short、int、long，分别占8、16、32、64位
        对于long，赋给的值大于int的范围，需要后缀L或l，否则出错(后面float也是)
    浮点类型
        float 32位，double 64位
        默认情况都视为double，使用float后缀F或f，用后缀L或l来明确
    字符类型
        char 存储单个字符，占用16位，定义时，单引号，Unicode编码
            (char)和(int)显式转换
        转义字符
            \ddd    八进制数表示字符
            \uxxxx  十六进制表示字符
            \'      单引号
            \\      反斜杠
            \t      垂直制表符
            \r      回车
            \n      换行
            \b      退格
            \f      换页
            幅值时同样使用单引号
    布尔类型
        boolean 布尔逻辑的真与假，ture false

#### 3.3 变量与常量

    根据值是否能够改变：变量与场量

    标识符
        标识符由任意顺序的字母、下划线(_)、美元符号($)和数组组成，并且第一个字符不能是数字。标识符不能是JavA的保留关键字，严格区分大小写，使用Unicode字符集
    关键字
        int         public  this    finally     boolean     abstract
        continue    float   long    short       throw       throws
        return      break   for     static      new         interface
        if          goto    default byte        do          case
        strictfp    package super   void        try         switch
        else        catch   implements  private final       class
        extends     volatile    while   synchronized    instanceof  char
        protected   import  transient   double

    声明变量
        根据数据类型，确定配置空间和存放数据内容
        变量的命名是合法的标识符，可以赋初值，变量名不可重复
    声明常量
        final变量，为所有对象共享值很有用
        final 数据类型 常量名称[=值]
        定义的final变量属于成员变量时，必须在定义时就设定它的初值，否则错误
            但局部变量在使用前也需要进行初始化
    变量的有效范围
        指程序代码能够访问该变量的区域，超出该区域会错误
        成员变量
            在类体中所定义的变量被称为成员变量，成员变量在整个类中都有效。类的成员变量又可分为静态变量(类变量,static)和实例变量
            静态变量的有效范围可以跨类，甚至整个应用程序之内，能直接以"类名.静态变量"的方式在其他类内使用
        局部变量
            在类的方法体中定义的变量(方法内部定义)，只在当前代码块中有效，包括方法的参数
            只在当前定义的方法内有效，不能用于类的其他方法中。局部变量的声明周期取决于方法，当方法被调用时，Java虚拟机为方法的局部变量分配内存空间，调用结束后，释放方法中局部变量占用的内存空间，局部变量也将会销毁
            局部变量可与成员变量的名字相同，此时成员变量将被隐藏，暂时失效

#### 3.4 运算符

    用于数学函数、类型的赋值语句和逻辑比较

    赋值运算符
        =，二元运算符，优先级较低，先计算=右边的，可以连等
    算数运算符
        +、-、*、/、%
        +-还可以作为数据的正负符号
        0不能作为除数
    自增和自减运算符
        ++、--，使用方法与C相同
            在操作元的前后，使得使用和运算顺序不同
    比较运算符
        运算结果为boolean型
        <、>、==、>=、<=、!=
    逻辑运算符
        返回类型为布尔值
        &&(&)、||、!
            &判断两个表达式:非短路，&&判断boolean类型:短路
    位运算符
        & 按位与，两个操作数的精度不同，结果与精度高的相同
        | 按位或    ~ 按位取反  ^ 按位异或
        <<左移 >>右移 >>>无符号右移
            移位运算符使用的数据类型 byte、short、char、int和long
    三元运算符
        条件式?值1:值2
    运算符优先级
        从高到低:
            增量和减量、算数、比较、逻辑、赋值运算
        两个运算有相同优先级，左边的表达式先处理
        具体：
            括号、正负号、一元运算符
            乘除、加减、移位运算
            比较大小、比较是否相等
            按位与运算、按位异或运算、按位或运算
            逻辑与运算、逻辑或运算
            三元运算符、赋值运算符

#### 3.5 数据类型转换

    隐式类型转换
        从低级类型向高级类型的转换，系统将自动执行
            byte<short<int<long<float<double
        两个操作数时，也根据更高级的类型进行转换
        用目标内存块尽可能多地套取源内存中的数据
    显式类型转换
        当把高精度的变量的值赋给低精度的变量时，必须使用显式类型转换运算(强制类型转换)
        (类型名)要转换的值，可能会导致精度损失

#### 3.6 代码注释与编码规范

    代码注释
        单行注释//
        多行注释/* */，可以嵌套单行注释，但是不能嵌套多行注释
        文档注释/** */，出现在声明之前时，会被Javadoc文档工具读取作为Javadoc文档内容
    编码规范

### 4 流程控制

#### 4.1 复合语句

    以整个块区为单位的语句，又称块语句 {}起止
    为局部变量创建了一个作用域

#### 4.2 条件语句

    if条件语句
        if(){
            语句序列，只有一条语句时可以省略{}
        }
        else if(){
        }
        else{
        }
        if else可用三元运算符简化
        if();=if(){}

    switch多分支语句
        switch(表达式){
            case n:;[break;]
            default:;
        }
        表达式的值一定为整型、字符型或字符串类型
        常量值必须互不相同

    循环语句
        while(条件表达式){
        }
        do{
        }while(条件表达式);
        for(表达式1;表达式2;表达式3){
        }
            1:初始化 2:循环条件 3:循环后操作
        foreach(元素变量x:遍历对象obj){
            x引用obj中的变量
        }

#### 4.4 循环控制

    break语句
        跳出switch或者当前一层循环体
        让break跳出指定的循环体
            标签名: 循环体{
                break 标签名;
            }
    continue语句
        跳过本次循环结束前的语句，回到循环的条件测试部分
        让continue跳出指定的循环体
            标签名: 循环体{
                continue 标签名;
            }

### 5 字符串

#### 5.1 String类

    通过java.lang包中的String类来创建字符串对象

    声明字符串
        ""包围的都是字符串，不能作为其他数据类型来使用
            String str;
    创建字符串
        Java将字符串作为对象来管理，创建对象要使用类的构造方法
        String s = new String(char a[],int offset,int length);
            offset开始截取字符串的位置，length截取字符串的长度
        通过字符串常量的引用赋值给一个字符串常量
            String s1,s2;
            s1=str;s2=str;
            如果s1和s2引用相同的字符串常量，二者就具有相同的实体

#### 5.2 连接字符串

    连接多个字符串
        s1+s2
        如果一个字符串太长，可以通过+连接，并在+处换行
    连接其他数据类型
        如果字符串同其他数据类型进行连接，会将这些数据类型直接转换成字符串
        即自动调用toString()方法

#### 5.3 获取字符串信息

    获取字符串长度
        str.length();
    字符串查找
        str.indexOf(substr)，搜索字符或字符串首次出现的位置
        str.lastIndexOf(substr)，搜索的字符或字符串最后一次出现的位置
            如果参数是""空字符串，返回的结果与indexOf相同

    获取指定索引位置的字符
        str.charAt(int index)，将指定索引处的字符返回

#### 5.4 字符串操作

    获取子字符串
        str.substring(int beginIndex)，从指定的索引位置开始截取直到该字符串结尾的子串
        空格占用一个索引位置
        str.substring(int beginIndex,int endIndex)，从字符串某一索引位置开始截取至某一索引位置结束的子串
    去除空格
        str.trim()，返回字符串的副本，忽略前导空格和尾部空格
    字符串替换
        str.replace(char oldChar, char newChar)，将指定的字符或字符串替换成新的字符或字符串，如果字符串oldChar没有出现在该对象表达式中的字符串序列中，则将原字符串返回
    判断字符串的开始与结尾
        str.startsWith(String prefix)，判断当前字符串对象的前缀是否为参数指定的字符串
        str.endsWith(String suffix)，判断当前字符串对象的后缀是否为参数指定的字符串
        返回值为boolean型
    判断字符串是否相等
        不能简单的使用==，只会比较地址
        str.equals(String otherstr)，如果具有相同的字符和长度，true，区分大小写
        str.equalsIgnoreCase(String otherstr)，忽略大小写
    按字典顺序比较两个字符串
        str.compareTo(String otherstr)，基于字符串中各个字符的Unicode值，小于-1，相等0，大于1
    字母大小写转换
        str.toLowerCase()将字符串中的所有字符从大写字母改为小写字母
        str.toUpperCase()将字符串中的所有字符从小写字母改为大写字母
            没有应该被转换的字符，则将原字符串返回，数字或非字符不受影响
    字符串分割
        str.split(String sign)，根据给定的字符串进行拆分
            sign为分割字符串的分隔符，也可以使用正则表达式
            使用|用来定义多个分隔符，",|="
        str.split(String sign,int limit)，根据给定的字符串进行拆分，限定拆分的次数

#### 5.5 格式化字符串

    str.format(String format,Object ··· args)，
        String.format(String format,Object ··· args)，使用指定的格式字符串和参数返回一个格式化字符串，格式化后的新字符串使用本地默认的语言环境
        String.format(Local l,String format.Objec ··· args)，格式化过程中要应用的语言环境。若为null,则不进行本地化，args数目可以为0
    日期字符串格式化
        Date date=new Date();
        %te 一个月中的某一天            %tb 指定语言环境的月份简称
        %tB 指定语言环境的月份全称      %ta 指定语言环境的星期几简称
        %tA 指定语言环境的星期几全称    %tc 包括全部日期和时间信息
        %tY 四位年份    %tj 一年中的第几天 %tm 月份 %ty 二位年份
    时间字符串格式化
        同样是Date
        %tH 2位24小时   %tI 2位12小时   %tk 无占位0的24小时
        %tl 无占位0的12小时 %tM 2位分数 %tS 2位秒数
        %tL 3位毫秒数   %tN 9位微秒数   %tp 指定语言环境下上午或下午标记
        %tz 相对于GMT RFC 82格式的数字时区偏移
        %tZ 时区缩写形式的字符串，如CST
        %ts Unix时间，1970-01-01 00:00:00至现在经过的秒数
        %tQ 1970-01-01 00:00:00至现在经过的毫秒数
    格式化常见的日期时间组合
        %tF "年-月-日"格式(四位年份)    %tD "月/日/年"格式(两位年份)
        %tc 全部日期和时间信息          %tr "时:分:秒 PM(AM)"格式(12小时制)
        %tT "时:分:秒"格式(24小时制)    %tR "时:分"格式(24小时制)
    常规类型格式化
        %b、%B 布尔类型 %h、%H 散列码   %s、%S 字符串   %c、%C 字符类型
        %d 十进制整数   %o 八进制整数   %x、%X 十六进制 %e 用科学计数法表示的十进制
        %a 带有效位数和指数的十六级只能hi浮点值 %n 特定于平台的分隔符 %% '%'

#### 5.6 使用正则表达式

    通常被用于判断语句中，检查某一字符串是否满足某一格式。含有一些具有特殊意义字符，即元字符
        . 任意一个字符  \d 0~9任何一个数字  \D 任何一个非数字字符
        \s 空白字符 \S 非空白字符   \w 可用作标识符的字符 \W 不可用于标识符的字符
        \p{Lower} a~z \p{Upper} A~Z \p{ASCII} ASCII字符 \p{Alpha} 字母字符
        \p{Digit} 十进制数字    \p{Alnum} 数字或字母字符    \p{Graph} 可见字符
        \p{Punct} 标点符号 !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
        \p{Print} 可打印字符[\p{Graph}\x20] \p{Blank} 空格或制表符
        \p{Cntrl} 控制字符[\x00-\x1F\x7F]
        在正则表达式中\要写为\\
        []表示一个元字符
            [^456] 456以外的字符 [a-r] a-r中任何一个字母 [a-zA-Z] 任意一个英文字母
            [a-e[g-z]] 并运算 [a-o&&[def]] 交运算 [a-d&&[^bc]]差运算
    限定修饰符
        ? 0次或1次  & 0次或多次 + 1次或多次 {n} 正好出现n次 {n,} 至少出现n次
        {n,m} 出现n~m次

#### 5.7 字符串生成器

    J2SE 5.0新增了可变的字符序列StringBuilder，提高了频繁增加字符串的效率
        不像+会产生新的String实例
        StringBuilder builder = new StringBuilder("") //初始容量是16个字符，超出会自动增加长度
        builder.append(content)，向字符串生成器中追加内容，通过多个重载，接受任何类型数据
        builder.insert(int offset,arg)，向字符串生成器的指定位置插入内容，同上
        builder.delete(int start,int end)，移除从此序列的start开始到end-1处；end大于长度，只删除到末尾；start=end，不作任何更改

### 6 数组

#### 6.1 数组概述

    Java将数组看作一个对象，虽然基本数据类型不是对象，但由基本数据类型组成的数组却是对象。

#### 6.2 一维数组的创建及使用

    创建一维数组
        数组作为对象允许使用new关键字进行内存分配。在使用数组之前，必须首先定义数组变量所属的类型
        先声明，再用new运算符进行内存分配
            数组元素类型 数组名字[];
            数组元素类型[] 数组名字;
                []指明该变量是一个数组类型变量
            数组名字 = new 数组元素的类型[数组元素的个数];
                使用new关键字为数组分配内存时，整型数组中各个元素的初始值都为0
        声明的同时为数组分配内存
            数组元素的类型 数组名 = new 数组元素的类型[数组元素的个数]
    初始化一维数组
        数组元素类型 数组名字[] = new int[]{n1,n2,n3,...};
        数组元素类型 数组名字[] = {n1,n2,n3,...};
    使用一维数组
        通过数组名字[n]

#### 6.3 二维数组的创建及使用

    第一个下表代表元素所在的行，第二个下标代表元素所在的列

    二位数组的创建
        先声明，再用new元素运算符进行内存分配
                数组元素的类型 数组名字[][];
                数组元素的类型[][] 数组名字;
            对于高维数组，有两种为数组分配内存的方式
                直接为每一维分配内存空间
                    数组名字 = new 数组元素的类型[n1][n2];
                分别为每一维分配内存
                    a = new int[2][];
                    a[0] = new int[2];
                    a[1] = new int[3];
        声明的同时为数组分配内存
            可以直接为每一维分配内存空间，也可以先给最左维分配
    二维数组初始化
        type arrayname[][]={value1,value2,...,valuen};
        下标从0开始
    使用二维数组
        同样，创建成功后会初始化为0

#### 6.4 数组的基本操作

    java.util包的Arrays类包含了用来操作数组(如排序和搜索)的各种方法

    遍历数组
        通过arrayname.length获取当前维度的长度
        使用foreach遍历数组可能会更简单
    填充替换数组元素
        通过Arrays类的静态方法fill()来对数组中的元素进行替换。该方法通过各种重载形式可完成对任意类型的数组元素的替换。fill()方法有两种参数类型
            Arrays.fill(int[] a,int value)，将指定的int值分配给int型数组的每个元素
            Arrays.fill(int[] a,int fromIndex,int toIndex,int value)
                将指定的int值分配给int型数组指定范围中的每个元素。填充的范围从索引fromIndex(包括)一直到索引toIndex(不包括)，二者相等则填充范围为空
                如果指定的索引位置大于或等于要进行填充的数组的长度，则会报出ArrayIndexOutOf-BoundsException(数组越界异常)
    对数组进行排序
        Arrays.sort(object)，实现对数组的排序
    复制数组
        Arrays,copyOf(arr,int newlength)
            复制数组至指定长度，新数组长度大于数组arr的长度，用0填充整型数组，null填充char数组；小于则截取
        Arrays.copyOfRange(arr,int fromIndex,int toIndex)
            将指定数组的指定长度复制到一个新数组中
    数组查询
        Arrays.binarySearch(Object[] a,Object key)
            使用二分搜索法来搜索指定数组，所以需要预先排序；如果没有，结果是不确定的。如果数组包含多个带有指定值的元素，无法保证找到的是哪个
        Arrays.binarySearch(Object[] a,int fromIndex, int toIndex,Object key)
            在指定的范围内检索某一元素，如果找不到，返回-1或"-"插入点；如果范围内所有元素都小于指定的键值，返回toIndex(保证了当且仅当键值被找到时，返回值≥0)

#### 6.5 数组排序算法

    冒泡排序、直接选择排序、反转排序

### 7 类和对象

#### 7.1 面向对象概述

    对象是类抽象出来的一个实例，类是封装对象属性和行为的载体
    类中对象
    面向对象程序设计：封装性、继承性、多态性
        采用封装的思想保证了类内部数据结构的完整性
    继承
        类与类之间之间的关闭成为关联
        父类(超类)和子类
    多态
        将子类的对象统一看作是父类的实例对象
        将父类对象应用于子类的特征就是多态
        抽象类：不能实例化对象，只给出一个方法的标准(一般是父类)
        接口：由抽象方法组成的集合

#### 7.2 类

    Java对象属性：成员变量；对象方法：成员方法

    成员变量
        在Java中对象的属性也称为成员变量
    成员方法
        使用成员方法对应于类对象的行为
            权限修饰符 返回值类型 方法名(参数类型 参数名){
                ···//方法体
                renturn 返回值;
            }
        一个成员方法可以有参数，这个参数可以是对象，也可以是基本数据类型的变量，同时成员方法有返回值和不返回任何值的选择，如果方法需要返回值，可以在方法体中使用return关键字，使用这个关键字后，方法的执行将被终止(无返回值返回值类型为void)
        在成员方法中可以定义一个变量，即局部变量
        类成员变量和成员方法可以统称为类成员
    权限修饰符
        主要包括private、public、protected，这些修饰符控制着对类和类的成员变量以及成员方法的访问。
            private：该成员变量只能在本类中被使用，在子类中是不可见的。，并且对其他包的类也是不可见的。
            public：除了可以在本类使用这些数据之外，还可以在子类和其他包的类中使用，
            类private：将隐藏其内的所有数据，以免用户直接访问它。
            类public：如果需要使类中的数据被子类或其他包中的类使用
            类protected：只有本包中的该类的子类或其他类可以访问此类中的成员变量和成员方法

            访问包位置          private     protected   public
            本类                可见        可见         可见
            同包其他类或子类     不可见      可见         可见
            其他包的类或子类     不可见      不可见       可见
        当声明类时不使用public、protected和private修饰符设置类的权限，则这个类预设为包存取范围，即只有一个包中的类可以调用这个类的成员变量或成员方法
        Java类的权限设定会约束类成员的权限设定
    局部变量
        在方法被执行时创建，在方法执行结束时被销毁。局部变量在使用时必须进行赋值操作或被初始化，否则会出现编译错误
    局部变量的有效范围
        在相互不嵌套的作用域中可以同时声明两个名称和类型相同的局部变量
    this关键字
        Java规定使用this关键字来代表本类对象的引用，this关键字被隐式地用于引用对象的成员变量和方法
        除了可以调用成员变量或成员方法之外，还可以作为方法的返回值

#### 7.3 类的构造方法

    构造方法时一个与类同名的方法，对象的创建就是通过构造方法完成的。每当类实例化一个对象时，类都会自动调用构造方法
    没有返回值(但不需要void修饰)、构造方法的名称要与本类的名称相同
        public book(){
            ···//构造方法体
        }
    如果类中没有明确定义构造方法，编译器会自动创建一个不带参数的默认构造方法
    如果在类中定义的构造方法都不是无参的构造方法，那么编译器也不会为类设置一个默认的无参构造方法，当试图调用无参构造方法实例化一个对象时，编译器会报错。所以只有在类中没有定义任何构造方法时，编译器才会在该类中自动创建一个不带参数的构造方法(多构造方法，是因为可以通过重载)
    this还可以调用类中的构造方法，在无参构造方法中使用this关键字调用有参的构造方法：只可以在无参构造方法中的第一句使用this调用有参构造方法

#### 7.4 静态变量、常量和方法

    由static修饰的变量、常量和方法被称作静态变量、常量和方法
    在处理问题时会需要两个类在同一个内存区域共享一个数据。
    被声明为static的变量、常量和方法被称为静态成员。静态成员属于类所有，区别于个别对象，可以在本类或者其他类使用类名和"."运算符调用静态成员
        类名.静态类成员
    虽然静态成员也可以使用"对象.静态成员"的形式进行调用，但通常不建议，避免混淆静态成员和非静态成员
    静态数据与静态方法的作用通常是为了提供共享数据或方法，同样遵循public、private和protected修饰符的约束
        Java在静态方法中不能使用this关键字
        在静态方法中不可以直接调用非静态方法
        不能将方法体内的局部变量声明为static的
        在执行类时，希望先执行类的初始化动作
            public class example{
                static{
                    //some
                }
            }
            当这段代码被执行时，首先执行static中的程序，并且只会执行一次

#### 7.5 类的主方法

    主方法是类的入口点，提供对程序流向的控制，Java编译器通过主方法来执行程序
        public static void main(String[] args){
            //方法体
        }
        主方法是惊天的，所以如要直接在主方法中调用其他方法，则该方法必须也是静态的
        主方法没有返回值
        主方法的形参为数组，可以用args.length获取参数的个数

#### 7.6 对象

    对象的创建：通过new操作符来创建对象
        Java对象和实例事实上可以通用
    访问对象的属性和行为
        对象.类成员，static
    对象的引用
        类名 对象引用名称
        引用只是存放一个对象的内存地址，并非存放一个对象。引用和对象是不同的，虽然可以忽略
    对象的比较
        ==比较两个对象引用的地址是否相等
        equals()比较两个对象所指的内容是否相等
    对象的销毁
        垃圾回收器会自动回收无用却占内存的资源
            对象引用超过其作用范围，将对象赋值为null，这个对象将被是为垃圾
            只能回收由new操作符创建的对象
        finalize()是Obejct类的方法，被声明为protected，用户可以在自己的类中定义这个方法，如果用户在类中定义了finalize()方法，在垃圾回收时会首先调用该方法，下一次垃圾回收动作发生时，才真正回收被对象占用的内存
            垃圾回收或finalize()方法并不保证一定会发生，Java虚拟机内存损耗殆尽，将不会执行
            System.gc()来强制启动垃圾回收器

### 8 包装类

#### 8.1 Integer

    java.lang包中的Integer类、Long类和Short类，可将基本类型int、long和short封装成一个类。这些类都是Number的子类，区别就是封装了不同的数据类型。其包含的方法基本相同
    Integer类在对象中包装了一个基本类型int的值。该类的对象包含一个int类型的字段。该类提供了多个方法，能在int类型和String类型之间互相转换，同时还提供了其他一些处理int类型时非常有用的常量和方法
    构造方法
        Integer number = Integer(int number);
        Integer number = Integer(String str); // 要用数值型String作为参数，否则NumberFormatException
    常用方法
        方法            返回值      功能描述
        byteValue()     byte        以byte类型返回该Integer的值
        compareTo(Integer anotherInteger) int   在数字上比较两个Integer对象。如果这两个值相等，则返回0；小于another负值，大于则正值
        equals(Object IntegerObj) boolean   比较此对象与指定的对象是否相等
        intValue()      int         以int型返回此Integer对象
        shortValue()    short       以short型返回此对象
        toString()      String      返回一个十进制表示该Integer值的String对象
        toBinaryString() String     返回一个二进制表示该Integer值的String对象
        toHexString()   String      返回一个十六进制表示该Integer值的String对象
        toOctalString() String      返回一个八进制表示该Integer值的String对象
        valueOf(String str) Integer 返回保存指定的String值的Integer对象
        parseInt(String str) int    返回包含在由str指定的字符串中的数字的等价整数值
    常量
        MAX_VALUE，表示int类型可取的最大值，即2^31-1
        MIN_VALUE，表示int类型可取的最小值，即-2^31
        SIZE，用来以二进制补码形式表示int值的位数
        TYPE，表示基本类型int的Class实例

#### 8.2 Boolean

    Boolean类将基本类型boolean的值包装在一个对象中。
        Boolean b = new Boolean(true);
        Boolean bool = new Boolean("ok");
    常用方法
        booleanValue()     boolean      将Boolean对象的值以对应的boolean值返回
        equals(Object obj) boolean      判断调用该方法的对象与obj是否相等。当且仅当参数不是null，而且与调用该方法的对象一样都表示同一个boolean值的Boolean对象时，才返回true
        parseBoolean(String s) boolean  将字符串参数解析为boolean值
        toString()         String       返回表示该boolean值的String对象
        valueOf(String s)  boolean      返回一个用指定的字符串表示值的boolean值
    常量
        TRUE，对应基值trued的Boolean对象
        FALSE，对应基值false的Boolean对象
        TYPE，基本类型boolean的class对象

#### 8.3 Byte

        Byte b = new Byte(mybyte);
        Byte mybyte = new Byte("12");
    常用方法
        byteValue()     byte    以一个byte值返回Byte对象
        compareTo(Byte anotherByte) int 在数字上比较两个Byte对象
        doubleValue()   double  以一个double值返回此Byte的值
        intValue()      int     以一个int值返回此Byte的值
        parseByte(String s) byte 将String型参数解析成等价的字节(byte)形式
        toString()      String  返回表示此Byte值的String对象
        valueOf(String str) byte 返回一个保持指定String所给出的值的Byte对象
        equals(Object obj) boolean 将此对象与指定对象比较，如果调用该方法的对象与obj相等，则返回true，否则返回false
    常量
        MIN_VALUE，byte类型可取的最小值
        MAX_VALUE，byte类型可取的最大值
        SIZE，用于以二进制补码形式表示byte值的位数
        TYPE，表示基本类型byte的Class实例

#### 8.4 Character

        Character mychar = new Character(String str);
    常用方法
        charvalue()     char    返回此Character对象的值
        compareTo(Character anotherCharacter) int 根据数字比较两个Character对象，若这两个对象相等则返回0
        equals(Object obj) Boolean 将调用该方法的对象与指定的对象相比较
        toUpperCase(char ch) char 将字符参数转换为大写
        toLowerCase(char ch) char 将字符参数转化为小写
        toString()      String  返回一个表示指定char值的String对象
        isUpperCase(char ch) boolean 判断指定字符是否为大写字符
        isLowerCase(char ch) boolean 判断指定字符是否为小写字符
    常量
        CONNECTOR_PUNCTUATION，返回byte值，表示Unicode规范中的常规类别"Pc"
        UNASSIGNED，返回byte型值，表示Unicode规范中的常见类别"Cn"
        TITLECASE_LEETTER，返回byte型值，表示Unicode规范中的常见类别"Lt"

#### 8.5 Double

    Double和Float都是Number类的子类
        Double mydouble = Double(double value);
        Double mydouble = Double(String str);
    常用方法
        byteValue()     byte    以byte形式返回Double对象值(通过强制转换)
        compareTo(Double d) int 对两个Double对象进行数值比较。如果两个值相等，则返回0；小于d负值，大于则正值
        equals(Object obj) boolean 将此对象与指定的对象相比较
        intValue()      int     以int形式返回double值
        isNaN()         boolean 如果此double值是非数字(NaN)值，则返回true；否则false
        toString()      String  返回此Double对象的字符串表示形式
        valueOf(String str) Double 返回保存用参数字符串str表示的double值的Double对象
        doubleValue()   double  以double形式返回此Double对象
        longValue()     long    以long形式返回此double的值(通过强制转换为long类型)
    常量
        MAX_EXPONENT，返回int值，表示有限double变量可能具有的最大指数
        MIN_EXPONENT，返回int值，表示有限double变量可能具有的最小指数
        NEGATIVE_INFINITY，返回double值，表示保存double类型的负无穷大值的常量
        POSITIVE_INFINITY，返回double值，表示保存double类型的正无穷大值的常量

#### 8.6 Number

    抽象类Number是BigDecimal、BigInteger、Byte、Double、Float、Integer、Long和Short类的父类，Number的子类必须提供将表示的数值转换为byte、double、float、int、long和short的方法
    方法
        byteValue()     byte    以相应形式返回指定的数值
        intValue()      int
        floatValue()    float
        shortValue()    short
        longValue()     long
        doubleValue()   double
    Number类的方法分别被Number的各子类所实现，它的所有子类都包含以上几种方法

### 9 数字处理类

#### 9.1 数字格式化

    数字格式化操作主要针对的是浮点型数据，包括double型和float型数据。在java.text.DecimalFormat格式化数字
    在Java中没有格式化的数据遵循
        如果数据绝对值大于0.001并且小于1e7使以常规小数形式表示
        反之，使用科学计数法表示
    DecimalFormat是NumberFormat的一个子类，用于格式化十进制数字。可以将一些数字格式化为整数、浮点数、百分数等。通过使用该类可以为要输出的数字加上单位或控制数字的精度。一般情况下可以在实例化DecimalFormat独对象时传递数字格式，也可以通过DecimalFormat类中的applyPattern()方法来实现数字格式化
    当格式化数字时，在DecimalFormat类中使用一些特殊字符构成一个格式化模板，使数字按照一定的特殊字符规则进行匹配
    DecimalFormat类中特殊字符说明
        0   代表阿拉伯数字，使用特殊字符"0"表示数字的一位阿拉伯数字，如果该位不存在数字，则显示0
        #   代表阿拉伯数字，使用特殊字符"0"表示数字的一位阿拉伯数字，如果该位不存在数字，则不显示
        .   小数分隔符或货币小数分隔符
        -   负号
        E   分隔科学计数法中的尾数和指数
        %   本符号放置在数字的前缀或后缀，将数字乘以100显示为百分数
        \u2030  本符号放置在数字的前缀或后缀，将数字乘以1000显示为百分数
        \u00A4  本符号放置在数字的前缀或后缀，作为货币记号
        '   本符号为单引号，当上述特殊字符出现在数字中时，应为特殊符号添加单引号，系统会将此符号视为普通符号处理
    调用方法
        DecimalFormat myFormat= new DecimalFormat(pattern);
        String output= myFormat.format(value);  或
        DecimalFormat myFormat= new DecimalFormat();
        myFormat.applyPattern(pattern);
        String output= myFormat.format(value);
    特殊方法
        myFormat.setGroupingSize(n);    设置数字分组的大小
        myFormat.setGroupingUsed(false);设置是否支持分组

#### 9.2 数字运算

    Math类，提供了众多数学函数方法，主要包括三角、指数、取整、取最大值、最小值以及平均值函数方法，被定义为static形式。调用方式
        Math.数学方法
    常用数学常量
        Math.PI Math.E

    常用数学方法
        三角函数方法 都是 public static double
            sin(double a)，返回角的三角正弦
            cos(double a)，返回角的三角余弦
            tan(double a)，返回角的三角正切
            asin(double a)，返回一个值的反正弦
            acis(dboble a)，返回一个值的反余弦
            atan(double a)，返回一个值的反正切
            toRadians(double angdeg)，将角度转换为弧度
            toDegrees(double angrad)，将弧度转换为角度
            角度与弧度的转换通常是不精确的，其中一个原因是Π的近似值
        指数函数方法 都是 public static double
            exp(double a)，用于获取e的a次方，即取e^n
            log(double a)，用于取自然对数，即取lna的值
            log10(double a)，用于取底数为10的对数
            sqrt(double a)，用于取a的平方根，其中a的值不能为负值
            cbrt(double a)，用于取a的立方根
            pow(double a,double b)，用于取a的b次方
        取整函数方法 基本都是 public static double
            ceil(double a)，返回大于等于参数的最小整数
            floor(doubel a)，返回大于等于参数的最大整数
            rint(double a)，返回与参数最接近的整数，如果两个同为整数且同样接近，则结果取整数
            int round(float a)，将参数加上0.5后返回与参数最近的整数
            long round(float a)，将参数加上0.5后返回与参数最近的整数，然后强制转移为长整型
                如果是一个整数的中间数，则返回接近的偶数
        取最大值、最小值、绝对值函数方法 都是 public static
            double max(double a,double b)，取a与b之间的最大值
            int min(int a,int b)，取a与b之间的最小值，参数为整型
            long min(long a,long b)，取a与b之间的最小值，参数为长整型
            float min(float a,float b)，取a与b之间的最小值，参数为浮点型
            double min(double a,double b)，取a与b之间的最小值，参数为双精度型
            int abs(int a)，返回整形参数的绝对值
            long abs(long a)，返回长整型参数的绝对值
            float abs(float a)，返回浮点型参数的绝对值
            double abs(double a)，返回双精度型参数的绝对值

#### 9.3 随机数

    Math.random()方法
        用于产生随机数字，默认生成[0,1)区间内的double型随机数
        随机生成字符(char)('a'+Math.random()*('z'-'a'+1));
        实际是伪随机数，通过当前实践作为随机数生成器的参数，所以每次执行程序都会产生不同的随机数
    Random类
        java.util.Random类  Random r= new Random();
        将以系统当前时间作为随机数生成器的种子。因为每时每刻的时间不可能相同，所以产生的随机数不同。但是如果运行速度太快，也会产生两次运行结果相同的随机数
            Random r=new Random(seedValue)
        各种数据类型随机数方法 都是public
            int nextInt()，返回随机整数
            int nextInt(int n)，返回等于0且小于n的随机整数
            long nextLong()，返回一个随机长整型值
            boolean nextBoolean()，返回一个随即布尔型值
            float nextFloat()，返回一个随机浮点型值
            double nextDouble()，返回一个随机双精度型值
            double nextGaussian()，返回一个概率密度为高斯分布的双精度值

#### 9.4 大数字运算

    BigInteger
        BigInteger类型的数字范围较Integer类型的数字范围要大得多，支持任意精度的整数，在运算中BigInteger类型可以准确地表示任何大小的整数值而不会丢失信息
        除了基本的加减乘除操作外，还提供了绝对值、相反数、最大公约数以及判断是否为质数等操作
        参数以字符串形式代表要处理的数字
            public BigInteger(String val)
            BigInteger twoInstance= new BigInteger("2")
        几种运算方法 都是 public BigInteger
            add(BigInteger val)，做加法运算
            subtract(BigInteger val)，做减法运算
            multiply(BigInteger val)，做乘法运算
            divide(BigInteger val)，做除法运算
            remainder(BigInteger val)，做取余操作
            public BigInteger[] divideAndRemainder(BigInteger val)，用数组返回余数和商，结果数组中第一个值为商，第二个值为余数
            pow(int exponent)，进行取参数的exponent次方操作
            negate()，取相反数
            shiftLeft(int n)，将数字左移n位，如果n为负数，做右移操作
            shiftRight(int n)，将数字右移n位，如果n为负数，做左移操作
            and(BigInteger val)，做与操作
            or(BigInteger val)，做或操作
            public int compareTo(BigInteger val)，做数字比较操作
            public boolean equals(Object x)，当参数x是BigInteger类型的数字并且数值相等时，返回保存用参数字符串str表示的double值的Double对象
            min(BigInteger val)，返回较小的值
            max(BigInteger val)，返回较大的值
    BigDecimal
        相比于BigInteger，加入了小数的概念。一般的float型和double型数据只可以用来做科学计算或工程计算，但由于在商业计算中要求数字精度比较高，所以要用到java.math.BigDecimal类。支持任何精度的定点数，可以用来精确计算货币值
        两个构造方法
            public BigDecimal(double val)，将双精度转换为BigDecimal
            public BigDecimal(String val)，将字符串形式转换为BigDecimal
        可以用来做超大浮点数的运算 都是public BigDecimal
            add(BigDecimal augend)，做加法操作
            subtract(BigDecimal subtrahend)，做减法操作
            multiply(BigDecimal multiplicand)，做乘法操作
            divide(BigDecimal divisor,int scale,int roundingMode)，做除法操作，三个参数分别代表除数、商的小数点后的位数、近似处理模式
        divide()方法的多种处理模式
            BigDecimal.ROUND_UP，商的最后意味如果大于0，则向前进位，正负数都是如此
            BigDecimal.ROUND_DOWN，商的最后一位无论是什么数字，都省略
            BigDecimal.ROUND_CEILING，商如果是正数，按照ROUND_UP模式去处理；商如果是负数，则按照ROUND_DOWN模式处理。这两种模式的处理都会使近似值大于等于实际值
            BigDecimal.ROUND_FLOOR，商如果是正数，按照ROUND_DOWN模式去处理；商如果是负数，则按照ROUND_UP模式处理。这两种模式的处理都会使近似值小于等于实际值
            BigDecimal.ROUND_HALF_DOWN，对商进行四舍五入操作，如果商最后一位小于等于5，则做舍弃操作；如果最后一位大于5，则做进位操作。
            BigDecimal.ROUND_HALF_UP，对商进行四舍五入操作，如果商的最后一位小于5，则舍弃；如果大于等于5，则进行进位操作
            BigDecimal.ROUND_HALF_EVEN，如果商的倒数第二位为奇数，则按照ROUND_HALF_UP处理；如果为偶数，则按照ROUND_HALF_DOWN处理

## 10-20 核心技术

### 10 接口、继承与多态

#### 10.1 类的继承

    继承使整个程序架构具有一定的弹性
    子类可以继承父类原有的属性和方法，也可以增加原来父类所不具备的属性和方法，或者直接重写父类中的某些方法
        class 子类 extends 父类{}
    在子类中可以连同初始化父类构造方法来完成子类初始化操作，既可以在子类的构造方法中使用super()语句调用父类的构造方法，也可以在子类中使用super关键字调用父类的成员方法等。但是子类没有权限调用父类中被修饰为private的方法，只有public或protected的可以
    重写(还可以称为覆盖)就是在子类中将父类的成员方法的名册灰姑娘保留，重写成员方法的实现内容，更改成员方法的存储权限，或是修改成员方法的返回值类型(重写父类成员方法的返回值类型是基于J2SE 5.0版本以上编译器提供的新功能)。
    在继承中还有一种特殊的重写方式，子类与父类的成员方法返回值、方法名称、参数类型及个数完全相同，唯一不同的是方法实现内容，这种特殊重写方式被称为重构
    当重写父类方法时，修改方法的修饰权限只能从小的范围到大的范围改变。
    子类重写父类的方法，如果修改方法的返回值类型，重写的返回值类型必须是父类中同一方法返回值类型的子类
    在Java中一切都以对象的形式进行处理，在继承的机制中，创建一个子类对象，将包含一个父类子对象，这些对象与父类创建的对象也是一样的。两者的区别在于后者来自外部，而前者来自子类对象的内部。当实例化子类对象时，父类对象也相应被实例化，在实例化子类对象时，Java编译器会在子类的构造方法中自动调用父类的无参构造方法。对于有参构造方法，只能使用super关键字显示地使用父类的构造方法
    如果使用finalize()方法对对象及性能清理，需要确保子类finalize()方法的最后一个动作是调用父类的finalize()方法，以保证当垃圾回收对象占用内存时，对象的所有部分都能被正常终止

#### 10.2 Object类

    继承原理：在Java中所有的类都直接或间接继承了java.lang.Object类，这是一个比较特殊的类，是所有类的父类，是Java类层中的最高层类。用户创建一个类时，除非已经指定要从其他类继承，否则它就是从java.lang.Object类继承而来的。Java中的每个类都源于java.lang.Object类。所以在定义类时可以省略extends Obecjt
    在Object类中主要包括clone()、finalize()、equals()、toString()等方法，常用的为equals()和toString()方法，所有类都可以重写Object类中的方法
        但是，getClass()、notify()、notifyAll()、wait()等方法不能被重写，因为被定义为final类型

    getClass()方法
        getClass().getname()，返回对象执行时的Class实例，然后使用此实例调用getName()方法可以取得类的名称
    toString()方法
        将一个对象返回为字符串形式，返回一个String实例。在实际的应用中通常重写toString()方法，为对象提供一个特定的输出模式。当这个类转换为字符串或与字符连接时，将自动调用重写的toString()方法
    equals()方法
        比较两个对象的实际内容是否相等，默认实现是使用"=="运算符比较两个对象的引用地址，真正比较两个对象的实际内容，需要在自定义类中重写equals()方法

#### 10.3 对象类型的转换

    向上转型
        把子类对象赋值给父亲类型的变量，在父类的方法中根据不同的图形对象设置不同的处理，就可以做到在父类中定义一个方法完成各个子类的功能，这样可以使同一份代码毫无差别第运用到不同类型上，这就是多态机制的基本思想
        常规的继承图都是将顶级类设置在页面的顶部，然后逐渐向下，所以将子类对象看作是父类对象 被称为"向上转型"
    向下转型
        将较抽象的类转换为较具体的类
        将父类对象强制转化为某个子类对象，这种方式称为显示类型转换
        使用向下转型技术时，必须使用显式类型转换

#### 10.4 使用instanceof操作符判断对象类型

    当在程序中使用向下转型技术时，如果父类对象不是子类对象的实例，就会发生ClassCastException异常，所以在执行向下转型之前需要养成一个良好的习惯，就是判断父类对象是否为子类对象的实例，通常使用instanceof操作符来完成。可以使用instanceof操作符判断是否一个类实现了某个接口，也可以用它来判断一个实例对象是否属于一个类
        myobject instanceof ExampleClass
        某类的对象引用       某个类
        返回值为布尔值，instanceof是Java的关键字，Java的关键字都是小写

#### 10.5 方法的重载

    构造方法的名称由类名决定，所以构造方法只有一个名称。如果希望以不同的方式来实例化对象，就需要使用多个构造方法来完成。由于这些构造方法都需要根据类名进行命名，为了让方法名相同而形参不同的构造方法同时存在，必须用到方法重载。方法重载起源于构造方法，也可以应用到其他方法中
    方法重载，就是在同一个类中允许存在一个以上的同名方法，只要这些方法的参数个数、参数顺序或类型不同即可（返回类型不同不足以区分
    定义不定长参数方法
        返回值 方法名(参数数据类型...参数名称)，在参数列表中使用"..."形式定义不定长参数，其实这个不定长参数a就是一个数组，编译器会将(int...a)这种形式看作是(int[]a)

#### 10.6 多态

    利用多态可以使程序具有良好的扩展性，并可以对所有类对象进行通用的处理。
    无需在所有的子类中定义执行相同功能的方法，避免了大量重复代码的编写。只要实例化一个继承父类的子类对象，即可调用相应的方法

#### 10.7 抽象类与接口

    抽象类
        一般将父类定义为抽象类，需要使用这个父类进行继承与多态处理。
        抽象类语法
            public abstract class Test {
                abstract void testAbstract();
            }
        使用abstract关键字定义的类成为抽象类，而使用这个关键字定义的方法称为抽象方法。抽象方法没有方法体，这个方法本身没有任何意义，除非它被重写，而承载这个抽象方法的抽象类必须被继承，实际上抽象类除了被继承之外没有任何意义
        如果声明一个抽象的方法，就必须将承载这个抽象方法的类定义为抽象类，不可能在非抽象类中获取抽象方法。只要类中有一个抽象方法，此类就被标记为抽象类。
        抽象类被继承后需要实现其中所有的抽象方法，也就是保证相同的方法名称、参数列表和相同返回值类型创建出非抽象方法，当然也可以是抽象方法。
        继承抽象类的所有子类需要将抽象类中的抽象方法进行覆盖。这样在多态机制中，就可以将父类修改为抽象类，然后每个子类都重写这个方法来处理。Java中规定类不能同时继承多个父类，为了解决：接口
    接口
        接口是对象的延伸，可以将它看作是纯粹的抽象类，接口中的所有方法都没有方法体。
            public interface drawTest{
                void draw();
            }
            public class Parallelogram extends Quadrangle implements drawTest{
                ...//
            }
        在接口中，方法必须被定义为public或abstract形式，其他修饰权限不被Java编译器认可。或者说，即使不将方法声明为public形式，也是public
        在接口中定义的任何字段都自动是static和final的
        Java中无论是将一个类向上转型为父类对象、抽象父类对象、该类实现接口，都是可以的
        接口与继承
            Java中不允许出现多重继承，但使用接口就可以实现多重继承。一个类可以实现多个接口，因此可以将所有需要继承的接口方法在implements关键字后并使用逗号隔开
            interface intf1{
            }
            interface intf2 extends intf1{
            }

### 11 类的高级特性

#### 11.1 Java类包

    Java中提供了一种的管理类文件的机制

    类名冲突
        Java中每个接口或类都来自不同的类包，无论是Java API中的类与接口还是自定义的类与接口，都需要隶属于某一个雷暴，这个类包包含了一些了类和接口。
    完整的类路径
        一个完整的类名需要包名与类名的组合，每一个类都隶属于一个类包，只要保证同一类包中的类不同名，就可以有效地避免同名类冲突的情况
        同一个包中的类相互访问时，可以不指定包名
        同一个包中的类不必存放在同一个位置，只要将CLASSPATH分别指向这两个位置即可
    创建包
        在Java中包名设计应与文件系统结构相对应。没有定义包的类，会被归纳在预设包(默认包)中
        在类中定义包名语法
            package 包名
        在类中指定包名，需要将package表达式放置在程序的第一行，它必须是文件中的第一行非注释代码。使用package关键字为类指定包名之后，包名将会成为类名中的一部分，预示着这个类必须指定全名。
            Java包的命名规则是全部使用小写字母(但是某些工程管理也能创建大小写结合的)
        为了避免包名冲突现象，在Java中定义包名时通常使用创建者的Internet域名的反序，由于Internet域名是独一无二的，包名自然不会发生冲突
    导入包
        使用import关键字导入包
            如果在程序中使用import com.lzw表达式，在程序中使用Math类时就会选择com.lzw.Math类来使用，当然也可以直接在程序中使用Math类时指定com.lzw.Math类
        import关键字语法
            import com.lzw.*;
            import com.lzw.math;
        在使用import关键字时，可以指定类的完整描述，如果为了使用包中更多的类，可以在使用import关键字指定时在包指定后加上*，这表示可以在程序中使用包中的所有类
        如果类定义中已经导入com.lzw.Math类，在类体中再使用其他包中的Math类时就必须指定完整的带有包格式的类名。
        在程序中添加import关键字时，就开始在CLASSPATH指定的目录中进行寻找，查找子目录com.lzw，然后从这个目录下编译完成的文件中查找是否有名称符合者，最后寻找到Math.class文件。当使用import指定了一个包中的所有类时，并不会指定这个包的子包中的类，如果用到这个包中的类，需要再次对子包作单独引用
        在Java中将Java源文件与类文件放在一起管理是极为不好的管理方式。可以在编译时使用-d参数设置编译后类文件产生的位置。
            javac -d ./bin/ ./com/lzw/*.java
    使用import导入静态成员
        import关键字除了导入包之外，还可以导入静态成员，这是JDK 5.0以上版本提供的功能。导入静态成员可以使鞭策和功能更为方便
        使用import导入静态成员
            import static 静态成员

#### 11.2 final变量

    final关键字可用于变量声明，一旦该变量被设定，就不可以再改变该变量的值。用final定义的变量为常量
        final double PI=3.14
    如果在程序中再次对定义为final的常量赋值，编译器将不会接受
    final关键字定义的变量必须在声明时对其进行赋值操作。final除了可以修饰基本数据类型的常量，还可以修饰对象引用。由于数组也可以被看作一个对象来引用，所以final可以修饰数组。一旦一个对象引用被修饰为final后，它只能恒定指向一个对象，无法将其改变以指向另一个对象。一个既是static又是final的字段只占据一段不能改变的存储空间。
    被定义为final的常量定义时需要使用大写字母命名，并且中间使用下划线进行连接，这是Java中的编码规则。同时，定义为final的数据无论是常量、对象引用还是数组，在主函数中都不可以被改变。
    一个被定义为final的对象引用只能指向唯一一个对象，不可以将它再指向其他对象。但由于一个对象本身的值是可以改变的，因此为了使一个常量真正做到不可更改，可以将常量声明为static final。
    定义为final的常量不是恒定不变的，将随机数赋予定义为final的常量，可以做到每次运行程序时改变这个值，如果有static形式，就不会改变。
    在Java中定义全局变量，通常使用public static final修饰，这样的常量只能在定义时被赋值

#### 11.3 final方法

    将方法定义为final类型，可以防止子类修改该类的定义与实现方式，同时定义为final的方法的执行效率要高于非final方法。在修饰权限中的private，如果一个父类的某个方法被设置为private修饰符，子类将无法访问该方法，自然无法覆盖该方法。一个定义为private的方式隐式被指定为final类型，因此无须将一个定义为private的方法再定义为final类型
    覆盖必须满足一个对象向上转型为它的基本类型并调用相同方法这样一个条件。
        对于private final的重写，并不是正常覆盖父类方法，而是生成了一个新的方法

#### 11.4 final类

    定义为final的类不能被继承。如果希望一个类不被任何类继承，并且不允许其他人对这个类进行任何改动，可以将这个类设置为final形式
        final类的语法
            final 类名{}
    如果将某个类设置为final形式，则类中的所有方法都被隐式设置为final形式，但是final类中的成员变量可以被定义为final或非finali形式

#### 11.5 内部类

    在一个文件中定义两个类，则其中任何一个类都不在另一个类的内部；如果在类中再定义一个类，则将在类中再顶一个的那个类称为内部类。内部类可分为成员内部类、局部内部类以及匿名类

    成员内部类
        在一个类中使用内部类，可以在内部类中直接存取其所在类的私有成员变量。
            成员内部类的语法
                public class OuterClass{
                    private class InnerClass{
                        ...///
                    }
                }
        在内部类中可以随意使用外部类的成员方法以及成员变量，尽管这些类成员被修饰为private。
        内部类的实例一定要绑定在外部类的实例上，如果从外部类中初始化一个内部类对象，那么内部类对象就会绑定在外部类对象上。内部类初始化方式与其他类初始化方式相同，都是使用new关键字
        内部类可以访问它的外部类成员，但内部类的成员只有在内部类的范围之内是可知的，不能被外部类使用。
        如果在外部类和非静态方法之外实例化内部类对象，需要使用外部类。内部类的形式指定该对象的类型。
        可以直接使用内部类实例化内部类对象，但在主方法中实例化内部类对象，需要在new操作符之前提供一个外部类的引用
        在实例化内部类对象时，不能在new操作符之前使用外部类名称实例化内部类对象，而是应该使用外部类的对象来创建其内部类的对象
        内部类对象会依赖于外部类对象，除非已经存在一个外部类对象，否则类中不会出现内部类对象
        内部类向上转型为接口
            如果将一个权限修饰符为private的内部类向上转型为其父类对象，或者直接向上转型为一个接口，在程序就可以完全按隐藏内部类的实现过程。可以在外部提供一个接口，在接口中声明一个方法。如果在实现该接口的内部类中实现该接口的方法，就可以定义多个内部类以不同的方式实现接口中的同一个方法，而在一般的类中是不能多次实现接口中同一个方法的，这种技巧经常被应用在Swing编程中，可以在一个类中做出多个不同的响应事件
            在继承接口的内部类中实现方法，如果某个类继承了外部类，由于内部的权限不可以向下转型为内部类，同时也不能访问该方法，但是却可以访问接口中的该方法。很好地对继承该类的子类隐藏了实现细节，仅为编写子类的人留下一个接口和一个外部类，同时也可以调用该方法，但是该方法的具体的实现过程却被很好地隐藏了，这就是内部类最基本的用途
            非内部类不能被声明为private或protected访问类型
        使用this关键字获取内部类与外部类的引用
            如果在外部类中定义的成员变量与内部类的成员变量名称相同，可以使用this关键字
                x   形参    this.x  内部类的变量    外部类名称.this.x   调用外部类的变量
            在内存中所有对象均被放置在堆中，方法以及方法中的形参或局部变量放置在栈中

    局部内部类
        内部类不仅可以在类中进行定义，也可以在类的局部位置定义，如在类的方法或任意的作用域中均可以定义内部类
        定义在方法内部的内部类，是方法的一部分，并非外部类的一部分，所以在方法的外部不能访问该内部类，但是该内部类可以访问当前代码块的常量以及此外部类的所有成员
        在方法中定义的内部类只能访问方法中final类型的局部变量，因为在方法中定义的局部变量相当于一个常量，它的周期超出方法运行的生命周期，由于该局部变量被设置为final，所以不能再内部类中改变该局部变量的值

    匿名内部类
        创建一个实现于一个接口的匿名类的对象
        匿名类的所有实现代码都需要在大括号之间进行编写
            return new A(){
                ...//内部类体
            }
        由于匿名内部类没有名称，所以匿名内部类使用默认构造方法来生成接口对象。在匿名内部类定义结束后，需要加分号进行标识，这个分号并不代表内部类的结束，而是代表接口引用表达式的创建
        匿名内部类编译以后，会产生以“外部类名$序号”为名称的.class文件，序号以1-n排列，分别代表1-n个匿名内部类

    静态内部类
        在内部类前添加修饰符static，这个内部类就变成静态内部类了。一个静态内部类中可以声明static成员，但是在非静态内部类中不可以声明静态成员。静态内部类有一个最大的特点，就是不可以使用外部类的非静态成员，所以静态内部类在程序开发中比较少见
        普通的内部类对象隐式地在外部保存了一个引用，指向创建它的外部类对象，但如果内部类被定义为static，就会有更多的限制。静态内部类具有以下两个特点
            如果创建静态内部类的对象，不需要其外部类的对象
            不能从静态内部类的对象中访问非静态外部类的对象
        进行程序测试时，如果在每一个Java文件中都设置一个主方法，将出现很多额外代码，而程序本身并不需要这些主方法，为了解决这个问题，可以将主方法写入静态内部类中
            编译写好的类后，将生成一个名称为ClassName$Innerclass的独立类和ClassName类，只要使用java ClassName$Innerclass，就可以运行主方法中的内容，这样当完成测试，需要将所有.class打包时，只要删除这个独立类即可

    内部类的继承
        内部类和其他普通类一样，可以被继承。但是继承内部类比继承普通类复杂，需要设置专门的语法来完成。
            public class OutputInnerClass extends ClassA.ClassB{
                public OutputInnerClass(ClassA a){
                    a.super();
                }
            }
            class ClassA{
                class ClassB{
                }
            }

### 12 异常处理

#### 12.1 异常概述

    在程序中，错误可能产生于程序员没有预料到的各种情况，或者是超出了程序员可控范围的环境因素，如用户的坏数据、试图打开一个根本不存在的文件等。在Java中这种在程序运行时可能出现的一些错误称为异常。异常是一个程序执行期间发生的事件，它中断了正在执行的程序的正常指令流
    Java语言是一门面向对象的编程语言，因此，异常在Java语言中也是作为类的实例的形式出现的。当某一方法中发生错误时，这个方法会创建一个对象，并且把它传递给正在运行的系统。这个对象就是异常对象。通过异常处理机制，可以将非正常情况下的处理代码于程序的主逻辑分离，即在编写代码主流程的同时在其他地方处理异常

#### 12.2 处理程序异常错误

    为了保证程序有效地执行，需要对发生的异常进行相应的处理。在Java中，如果某个方法抛出异常，既可以在当前方法中进行捕捉，然后处理该异常，也可以将异常向上抛出，由方法调用者来处理。

    错误
        异常产生后，如果不做任何处理，程序就会被终止。
    捕捉异常
        Java语言的异常捕获结构由try、catch和finally3部分组成。其中，try语句块存放的是可能发生异常的Java语句；catch语句块在try语句块之后，用来激发被捕获的异常；finally语句块是异常处理结构的最后执行部分，无论try语句块中的代码如何退出，都将被执行finally语句块
        语法
            try{
                //程序代码块
            }
            catch(Exceptiontype1 e){
                //对该异常的处理
            }
            catch(Exceptiontype2 e){
            }
            ...
            finally{
                //程序块
            }
        try-catch语句块
            将可能出现异常的代码用try-catch语句块进行处理，当try代码块中的语句发生异常时，程序就会调转到catch代码块中执行，执行完catch代码中的程序代码后，将继续执行catch代码块后的其他代码，而不会执行try代码块中发生异常语句后面的代码。Java的异常处理是结构化的，不会因为一个异常影响整个程序的执行
            Exception是try代码块传递给catch代码块的变量类型，e是变量名。catch代码块中语句"e.getMessage();"用于输出错误性质。通常，异常处理常用以下3个函数来获取异常的有关信息
                getMessage()函数：输出错误性质
                toString()函数：给出异常的类型与性质
                printStackTrace()函数：指出异常的类型、性质、栈层次及出现在程序中的位置
            最好不要为了简单而忽略catch语句后的代码
        finally语句块
            完整的异常处理语句一定要包含finally语句，无论程序中有无异常发生，并且无论之间的try-catch是否顺利执行完毕，都会执行finally语句
            在以下4种特殊情况下，finally块不会被执行
                在finally语句块中发生了异常
                在前面的代码中使用了System.exit()退出程序
                程序所在的线程死亡
                关闭CPU

#### 12.3 Java常见异常

    在Java中提供了一些异常用来描述经常发生的错误，其中，有的需要程序员进行捕获处理或声明抛出，有的是由Java虚拟机自动进行捕获处理的。Java中常见的异常类
        ClassCastException      类型转换异常
        ClassNptFoundException  未找到相应类异常
        ArithmeticException     算数异常
        ArrayIndexOutOfBoundsException  数组下标越界异常
        ArrayStoreException     数组中包含不兼容的值抛出的异常
        SQLException            操作数据库异常类
        NullPointerException    空指针异常
        NoSuchFieldException    字段未找到异常
        NoSuchMethodException   方法未找到抛出的异常
        NumberFormatException   字符串转换为数字抛出的异常
        NegativeArraySizeException  数组元素个体为负数抛出的异常
        StringIndexOutOfBoundsException 字符串索引超出范围抛出的异常
        IOException             输入输出异常
        IllegalAccessException  不允许访问某类异常
        InstantiationException  当应用程序试图使用Class类中的newInstance()方法创建一个类的实例，而指定的类对象无法被实例化时，抛出该异常
        EOFException            文件已结束异常
        FileNotFoundException   文件未找到异常

#### 12.4 自定义异常

    使用Java内置的异常类可以描述编程时出现的大部分异常情况。除此之外，用户只需继承Exception类即可自定义异常类。
    在程序中使用自定义异常类，大体可分为以下几个步骤：
        (1)创建自定义异常类
        (2)在方法中通过throw关键字抛出异常对象
        (3)如果在当前抛出异常的方法中处理异常，可以使用try-catch语句块捕获并处理，否则在方法的声明处通过throws关键字指明要抛出给方法调用者的异常，继续进行下一步操作
        (4)在出现异常方法的调用者中捕获并处理异常

#### 12.5 在方法中抛出异常

    使用throws关键字抛出异常
        throws关键字通常被应用在声明方法时，用来指定方法可能抛出的异常。多个异常可使用逗号分隔
        使用throws关键字将异常抛给上一级后，如果不想处理该异常，可以继续向上抛出，但最终要有能够处理该异常的代码
        如果是Error、RuntimeException或它们的子类，可以不使用throws关键字来声明要抛出的异常，编译仍能顺利通过，但在运行时会被系统抛出
    使用throw关键字抛出异常
        throw关键字通常用于方法体中，并且抛出一个异常对象。程序在执行到throw语句时立即终止，它后面的语句都不执行。通过throw抛出异常后，如果想在上一级代码中来捕获并处理异常，则需要在抛出异常的方法中使用throws关键在方法的声明中指明要抛出的异常；如果要捕捉throw抛出的异常，则必须使用try-catch语句块
        throw通常用来抛出用户自定义异常

#### 12.6 运行时异常

    RuntimeException异常是程序运行过程中产生的异常。Java类库中的每个包中都定义了异常类，所有这些类都是Throwable类的子类。Throwable类派生了两个子类，分别是Exception和Error类。Error类及其子类用来描述Java运行系统中的内部错误以及资源耗尽的错误，这类错误比较严重。Exception类称为非致命性类，可以通过捕捉处理使程序继续执行。Exception类又根据错误发生的原因分为RuntimeException异常和除RuntimeException之外的异常
    Java中提供了常见的RuntimeException异常，这些异常可通过try-catch语句捕获
        NullPointerException        空指针异常
        ArrayIndexOutOfBoundsException  数组下标越界异常
        ArithmeticException         算术异常
        ArrayStoreException         数组中包含不兼容的值抛出的异常
        IllegalArgumentException    非法参数异常
        SecurityException           安全性异常
        NegativeArraySizeException  数组长度为负异常

#### 12.7 异常的使用原则

    Java异常强制用户去考虑程序的强健性和安全性。异常处理不应用来控制程序的正常流程，其主要原则是捕获程序在运行时发生的异常并进行相应的处理。编写代码处理某个方法可能出现的异常时，可遵循以下几条原则
        在当前方法声明中使用try-catch语句捕获异常
        一个方法被覆盖时，覆盖它的方法必须抛出相同的异常或异常的子类
        如果父类抛出多个异常，则覆盖方法必须抛出那些异常的一个子集，不能抛出新异常

### 13 Swing程序设计

#### 13.1 Swing概述

    GUI为程序提供图形界面，它最初的设计目的是为程序员构建一个通用的GUI，使其能够在所有的平台上运行，但Java 1.0中基础类AWT(抽象窗口工具箱)并没有达到这个要求，于是Swing出现了，它是AWT组件的增强组件，但是它并不能完全替代AWT组件，这两种组件需要同时出现在一个图形用户界面中

    Swing特点
        原来的AWT组件来自java.awt包，当含有AWT组件的Java应用程序在不同的平台上执行时，每个平台的GUI组件的显示会有所不同，但是在不同平台上运行使用Swing开发的应用程序时，就可以统一GUI组件的显示风格，因为Swing组件允许编程人员在跨平台时指定统一的外观和风格
        Swing组件通常被称为“轻量级组件”，因为它完全由Java语言编写，而Java是不依赖于操作系统的语言，它可以在任何平台上运行；相反，依赖于本地平台的组件被称为“重量级组件”，如AWT组件就是依赖本地平台的窗口系统来决定组件的功能、外观和风格。Swing主要具有以下特点
            轻量级组件
            可插入外观组件
    Swing包
        为了有效地使用Swing组件，必须了解Swing包的层次结构和继承关系，其中比较重要的类是Component类、Container类和JComponent类。以下是这些类的层次和继承关系
            Java.lang.Object类>Java.awt.Component类>Java.awt.Container类>Javax.swing.Jcomponent类
        在Swing组件中大多数GUI组件都是Component类的直接子类或间接子类，Jcomponent类是Swing组件各种特性的存放位置，这些组件的特性包括设定组件边界、GUI组件自动滚动等
        在Swing组件中最重要的父类是Container类，而Container类有两个最重要的子类，分别为java.awt.Window与java.awt.Frame，除了以往的AWT类组件会继承这两个类之外，现在的Swing组件也扩展了这两个类。顶层父类是Component类与Container类，所以Java关于窗口组件的编写，都与组件以及容器的概念相关联
    常用Swing组件概述
        JButton     代表Swing按钮，按钮可以带一些图片或文字
        JCheckBox   代表Swing中的复选框组件
        JComBox     代表下拉列表框，可以在下拉显示区域显示多个选项
        JFrame      代表Swing的框架类
        JDialog     代表Swing版本的对话框
        JLabel      代表Swing中的标签组件
        JRadioButton    代表Swing中的单选按钮
        JList       代表能够在用户界面中显示一系列条目的组件
        JTextField  代表文本框
        JPasswordField  代表密码框
        JTextArea   代表Swing中的文本区域
        JOptionPane 代表Swing中的一些对话框

#### 13.2 常用窗体

    窗体作为Swing应用程序中组件的承载体，处于非常重要的位置。Swing中常用的窗体包括JFrame和JDialog。
    JFrame窗体
        JFrame窗体是一个容器，它是Swing程序中各个组件的载体，可以将Frame看作是承载这些Swing组件的容器。在开放应用程序时可以通过继承java.swing.JFrame类创建一个窗体，在这个窗体中添加组件，同时为组件设置事件。由于该窗体继承了JFrame类，所以它拥有“最大化”“最小化”“关闭”等按钮
        JFrame在程序中的语法格式
            JFrame jf=new JFrame(title);
            Container container=jf.getContentPane();
                jf为JFrame类的对象
                container为Container类的对象，可以使用JFrame对象调用getContentPane()方法获取
        Swing组件的窗体通常与组件和容器有关，所以在JFrame对象创建完成后，需要调用getContentPane()方法将窗体转换为容器，然后在容器中添加组件或设置布局管理器。通常，这个容器用来包含和显示组件。如果需要将组件添加至容器，可以使用来自Container类的add()方法进行设置。
            container.add(new JButton("按钮"))
        在容器中添加组件后，也可以使用Contain类的remove()方法将这些组件从容器中删除
            container.remove(new JButton("按钮"))
        JFrame类的常用构造方法包括以下两种形式
            public JFrame()
            public JFrame(String title)
        JFrame类中的两种构造方法分别为无参的构造方法与有参的构造方法，第1种形式的构造方法可以创建一个初始不可见、没有标题的新窗体；第2种形式的构造方法在实例化该JFrame对象时可以创建一个不可见但具有标题的窗体。可以使用JFrame对象调用show()方法使窗体可见，但是该方法早已被新版JDK所弃用，通常使用setVisible(true)方法使窗体可见
        同时可以使用setSize(int x,int y)方法设置窗体大小，其中x中y变量分别代表窗体的宽与高。
        创建窗体后，需要给予窗体一个关闭方式，可以调用setDefaultCloseOperation()方法关闭窗体。Java为窗体关闭提供了多种方式，常用的有以下4种
            DO_NOTHING_ON_CLOSE
            DISPOSE_ON_CLOSE
            HIDE_ON_CLOSE
            EXIT_ON_CLOSE
        这几种操作实质上是将一个int类型的常量封装在javax.swing.WindowConstants接口中
        第1种窗体退出方式代表什么都不做就将窗体关闭；第2种退出方式则代表任何注册监听程序对象后会自动隐藏并释放窗体；第3种方式表示隐藏窗口的默认窗口关闭；第4种退出方式表示退出应用程序默认窗口关闭
    JDialog窗体
        JDialog窗体是Swing组件中的对话框，它继承了AWT组件中的java.awt.Dialog类
        JDialog窗体的功能是从一个窗体中弹出另一个窗体，就像是在使用浏览器时弹出的确定对话框一样。JDialog窗体实质上就是另一种类型的窗体，它与JFrame窗体类似，在使用时也需要调用getContentPane()方法将窗体转换为容器，然后在容器中设置窗体的特性
        在应用程序中创建JDialog窗体需要实例化JDialog类，通常使用以下几个JDialog类的构造方法
            public JDialog()：创建一个没有标题和父窗体的对话框
            public JDialog(Frame f)；创建一个指定父窗体的对话框，但该窗体没有标题
            public JDialog(Frame f,boolean model)：创建一个指定类型的对话框，并指定父窗体，但该窗体没有指定标题
            public JDialog(Frame f,String title)：创建一个指定标题和父窗体的对话框
            public JDialog(Frame f,String title,boolean model)：创建一个指定标题、窗体和模式的对话框
        为了使对话框在父窗体中弹出，定义了一个JFrame窗体，首先在该窗体中定义一个按钮，然后为此按钮添加一个鼠标单击监听事件(在这里使用了匿名内部类的形式)，这里使用new MyDialog().setVisible(true)语句使对话框窗体可见，这样就实现了用户单击该按钮后弹出对话框的功能。
        JDialog窗体与JFrame窗体形式基本相同，甚至在设置窗体的特性时调用的方法名称都基本相同，如设置窗体大小、窗体关闭状态等

#### 13.3 标签组件与图标

    在Swing中显示文本或提示信息的方法是使用标签，它支持文本字符串和图标。在应用程序的用户界面中，一个简短的文本标签可以使用户知道这些组件的目的，所以标签在Swing中是比较常用的组件

    标签的使用
        标签由JLabel类定义，它的父类为JComponent类。
        标签可以显示一行只读文本、一个图像或带图像的文本，它并不能产生任何类型的事件，只是简单地显示文本和图片，但是可以使用标签的特性指定标签上文本的对齐方式、
        JLabel类提供了多种构造方法，可以创建多种标签，如显示只有文本/图标的标签或者两种都有
        常用构造方法
            public JLabel()，创建一个不带图标和文本的JLabel对象
            public JLabel(Icon icon)，创建一个带图标的JLabel对象
            public JLabel(icon icon,int aligment)，创建一个带图标的JLabel对象，并设置图标水平对齐方式
            public JLabel(String text,int aligment)，创建一个带文本的JLabel对象，并设置文本水平对齐方式
            public JLabel(String text,Icon icon,int aligment)，创建一个带文本、带图标的JLabel对象，并设置标签内容的水平对齐方式
    图标的使用
        Swing中的图标可以放置在按钮、标签等组件上用于描述组件的用途。图标可以用Java支持的图片文件类型进行创建，也可以使用java.awt.Graphics类提供的功能方法来创建
        创建图标
            在Swing中通过Icon接口来创建图标，可以在创建时给定图标的大小、颜色等特性。如果使用Icon接口，必须实现Icon接口中的3个方法
                public int getIconHeight()
                public int getIconWidth()
                public void paintIcon(Component arg0,Graphics arg1,int arg2,int arg3)
            getIconHeight()与getIconWeight()方法用于获取图标的长与宽，paintIcon()方法用于实现在指定坐标位置画图
            一般情况下会将图标放置在按钮或标签上，然后将标签或按钮添加到容器中看，这样就实现了在窗体中使用图片的功能
    使用图片图标
        Swing中的图标除了可以绘制之外，还可以使用某个特定的图片创建。Swing利用javax.swing.ImageIcon类根据现有图片创建图标，ImageIcon类实现了Icon接口，同时Java支持多种图片格式
        ImageIcon类常用的构造方法
            public ImageIcon()，该构造方法创建一个通用的ImageIcon对象，当真正需要设置图片时再使用ImageIcon对象调用setImage(Image image)方法来操作
            public ImageIcon(Image image)，可以直接从图片源创建图标
            public ImageIcon(Image image,String description)，除了可以从图片源创建图标之外，还可以为这个图标添加简短的描述，但这个描述不会在图标上显示，可以使用getDesciption()方法获取这个描述
            public ImageIcon(URL url)，该构造方法利用位于计算机网络上的图像文件创建图标
        java.lang.Class类中的getResource()方法可以获取资源文件的URL路径。

#### 13.4 常用布局管理器

    在Swing中，每个组件在容器中都具有一个具体的位置和大小，而在容器中摆放各种组件时很难判断其具体位置和大小。布局管理器提供了Swing组件安排、展示在容器中的方法及基本的布局功能。使用布局管理器较程序员直接在容器中控制swing组件的位置和大小方便得多，可以有效地处理整个窗体的布局。Swing提供的常用布局管理器包括流布局管理器、边界布局管理器和网格布局管理器，

    绝对布局
        在Swing中，除了使用布局管理器之外还可以使用绝对布局。绝对布局，就是硬性指定组件在容器中的位置和大小，可以使用绝对坐标的方式来指定组件的位置
        使用绝对布局的步骤
            (1)使用Container.setLayout(null)方法取消布局管理器
            (2)使用Component.setBounds()方法设置每个组件的大小与位置
        绝对布局使用setBounds(int x,int y,int width,int height)方法进行设置，如果使窗体对象调用setBounds()方法，它的参数x与y分别代表这个窗体在整个屏幕上出现的位置，width与height则代表这个窗体的宽与长；如果使窗体内的组件调用setBounds()方法，参数x与y则代表这个组件在整个窗体摆放的位置，width与height则代表这个组件的大小
        需要注意的是，在使用绝对布局之前需要调用setLayout(null)方法告知编译器，这里不再使用布局管理器
    流布局管理器
        流(FlowLayout)布局管理器是最基本的布局管理器，在整个容器中的布局正如其名，像"流"一样从左到右摆放组件，直到占据了这一行的所有空间，然后再向下移动一行。默认情况下，组件在每一行中都是居中排列的，但是通过设置也可以更改组件在每一行上的排列位置
        FlowLayout类中具有以下常用的构造方法
            public FlowLayout()
            public FlowLayout(int alignment)
            public FlowLayout(int alignment,int horizGap,int vertGap)
            构造方法中的alignment参数表示使用流布局管理器后组件在每一行的具体摆放位置。它可以被赋予以下3个值之一
                FlowLayout.LEFT=0   //左对齐
                FlowLayout.CENTER=1 //居中
                FlowLayout.RIGHT=2  //右对齐
        在public FlowLayout(int alignment,int horizGap,int vertGap)构造方法中还存在horizGap与vertGap两个参数，这两个参数分别以像素为单位指定组件之间的水平间隔与垂直间隔
    边界布局管理器
        在默认不指定窗体布局的情况下，Swing组件的布局模式是边界布局管理器。
        边界布局管理器可以将容器划分为东南西北中5个区域，可以将组件加入到这5个区域中。容器调用Container类的add()方法添加组件时可以设置此组件在边界布局管理器中的区域，区域的控制可以有BorderLayout类中的成员变量来决定，这些成员变量的具体含义：
            BorderLayout.NORTH  在容器中添加组件时，组件置于顶端
            BorderLayout.SOUTH  在容器中添加组件时，组件置于底端
            BorderLayout.EAST   在容器中添加组件时，组件置于右端
            BorderLayout.WEST   在容器中添加组件时，组件置于左端
            BorderLayout.CENTER 在容器中添加组件时，组件置于中间开始填充，直到与其他组件边界连接
    网格布局管理器
        网格布局管理器将容器划分为网格，所以组件可以按行和列进行排列。在网格布局管理器中，每一个组件的大小都相同，并且网格中空格的个数由网格的行数和列数决定，如一个两行两列的网格能产生4个大小相等的网格。组件从网格的左上角开始，按照从左到右、从上到下的顺序加入网格中，而且每一个组件都会填满整个网格，改变窗体的大小，组件的大小也会随之改变
        网格布局管理器主要有以下两个常用的构造方法
            public GridLayout(int rows,int columns)
            public GridLayout(int rows,int columns,int horizGap,int vertGap)
            在上述构造方法中，rows与colunmns参数代表网格的行数与列数，这两个参数只有一个参数可以为0，代表一行或一列可以排列任意多个组件；参数horizGap与vertGap指定网格之间的距离，分别指定水平和垂直距离
    网格组布局管理器
        由GridBagLayout类实现的布局管理器称为网格组布局管理器，它实现了一个动态的矩形网格，这个矩形网格由无数个矩形单元格组成，每个组件可以占用一个或多个这样的单元格。所谓动态的矩形网格，就是可以根据实际需要随意增减矩形网格中的行数和列数
        在向由GridBagLayout类管理的容器中添加组件时，需要为每个组件创建一个与之关联的GridBagConstraints类的对象，通过该类中的属性可以设置组件的布局信息，如组件在网格组中位于第几行、第几列，以及需要占用几行几列等
        通过GridBagLayout类实现的矩形网格的绘制方向由容器决定，如果容器的方向是从左到右，则位于矩形网格左上角的单元格列索引为0，此时组件左上角的点为起始点；反之亦然
            (1)gridx和gridy属性
                这两个属性用来设置组件起始点所在单元格的索引值。需要注意的是，属性gridx设置的是X轴(即网格水平方向)的索引值，所以它表示的是组件起始点所在列的索引；属性gridy设置的是Y轴(即网格垂直方向)的索引值，所以它表示的是组件起始点所在行的索引
            (2)gridwidth和gridheight属性
                这两个属性用来设置组件占用网格组的行数和列数。属性gridwidth为组件占用网格组的列数，也可以理解为以单元格为单位组件的宽度；属性gridheight为组件占用网格组的行数，也可以理解为以单元格为单位组件的高度
            (3)anchor属性
                属性anchor用来设置组件在其所在显示区域的显示位置。通常将显示区域从方向上划分为9个方位，分别为北方(NORTH)、东北(NORTHEAST)、东方(EAST)、东南(SOUTHEAST)、南方(SOUTH)、西南(SOUTHWEST)、西方(WEST)、西北(NORTHWEST)和中心(CENTER)。代表这9个方位的单词也是该类中的静态常量，可以利用这9个静态常量设置anchor属性，其中常量CENTER为默认位置。
            (4)fill属性
                属性fill用来设置组件的填充方式。当单元格显示区域的面积大于组件面积，或者一个组件占用多个单元格时，显示组件可能不必占用所有显示区域，在这种情况下可以通过fill属性设置组件的填充方式。可以利用4个静态常量设置该属性，默认情况下是将该属性设置为静态常量NONE，即不调整子组件大小至填满显示区域；如果将该属性设置为静态常量VERTICAL，表示只调整组件垂直方向的大小(即组件高度)至填满显示区域；如果将该属性设置为静态常量BOTH，则表示同时调整组件的宽度至填满显示区域
            (5)insets属性
                属性insets用来设置组件四周与单元格边缘之间的最小距离。该属性的类型为Insets，Insets类仅有一个构造方法Insets(int top,int left,int bottom, int right)，它的4个入口参数依次为组件上方、左侧、下方和右侧的最小距离，单位为像素。默认为没有距离
            (6)ipadx和ipady属性
                这两个属性用来修改组件的首选大小。属性ipadx用来修改组件的宽度，属性ipady用来修改组件的高度。如果为正数，则在首选大小的基础上增加指定的宽度和高度；如果为负数，则在首选大小的基础上减小指定的宽度和高度
            (7)weightx和weighty属性
                这两个属性只用来设置网格组的每一行和每一列对额外空间的分布方式。不在设置属性weightx和weighty(即采用默认设置)的情况下，当窗体调整到足够大时，组件全部聚集在窗体的中央，在组件四周出现了大片的额外空间。为了避免这种情况出现，可以通过这两个属性设置网格组的每一行和每一类对额外空间的分布方式
                这两个属性的默认值均为0，表示不分布容器的额外空间。属性weightx用来设置其所在列额外空间的分布方式，如果在该列中设置了多个weightx属性，则取它们的最大值为该列的分布方式；属性weighty用来设置其所在行对额外空间的分布方式，如果在该行中设置了多个weighty属性，则取它们的最大值为该行的分布方式
                在设置网格组的每一行和每一列对额外空间的分布方式时，建议只设置第一行的weightx属性和第一列的weighty属性，这样会方便前期调试和后期维护
                网格组的行和列对额外空间的分布方式完全相同。网格组布局管理器首先计算出每一行的分布方式，即获取每一行的weighty属性的最大值，然后计算每个最大值所占有最大值总和的百分比，最后将额外空间的相应百分比分配给对应行。
                在设置网格组的每一行和每一列对额外空间的分布方式时，建议为各个属性按百分比取值
        辅助组件只起到占位作用

#### 13.5 常用面板

    面板也是一个Swing容器，它可以作为容器容纳其他组件，但它也必须被添加到其他容器中。Swing中常用的面板包括JPanel面板以及JScrollPane面板。

    JPanel面板
        JPanel面板可以聚集一些组件来布局。面板也是一种容器，因为它也继承自java.awt.Container类
    JScrollPane面板
        在设置界面时，可能会遇到在一个较小的容器窗体中显示一个较大部分的内容的情况，这是可以使用JScrollPane面板。JScrollPane面板是带滚动条的面板，它也是一种容器，但是JScrollPane只能放置一组组件，并且不可以使用布局管理器。如果需要在JScrollPane面板中放置多个组件，需要将多个组件放置在JPanel面板上，然后将JPanel面板作为一个整体组件添加在JScrollPane组件上
        在窗体中创建一个带滚动条的文字编译器，首先需要初始化编译器(在Swing中编译器类为JTextArea类)，并在初始化时指定编译器的大小完成。当创建带滚动条的面板时，需将编译器加入面板中，最后将带滚动条的编译器放置在容器中即可

#### 13.6 按钮组件

    按钮在Swing中是较为常见的组件，用于触发特定动作。Swing中提供多种按钮，包括提交按钮、复选框、单选按钮等，这些按钮都是从AbstractButton类中继承而来的。

    提交按钮组件
        Swing中的提交按钮(JButton)由JButton对象表示，其构造方法主要有以下几种形式
            public JButton()
            public JButton(String text)
            public JButton(Icon icon)
            public JButton(String text,Icon icon)
        通过使用上述构造方法，在Swing按钮上不仅能显示文本标签，还可以显示图标。上述构造方法中的第一个构造方法可以生成不带任何文本组件的对象和图标，可以在以后使用相应方法为按钮设置指定的文本和图标；其他构造方法都在初始化时制定了按钮上显示的图标或文字。
        创建一个没有定义图标和文字的按钮对象，然后使用setIcon()方法为这个按钮定制一个图标，其中setToolTipText()方法是为按钮设置提示文字，setBorderPainted()方法设置按钮边界是否显示。使用setMaximumSize()方法设置按钮的大小与图标的大小一直，该方法需要的参数类型为Dimension类对象，这样看上去此图片就如同按钮一样摆放在窗体中，同时也可以使用setEnabled()方法设置按钮是否可用
        上述这些设置按钮属性的方法多来自JButton的父类AbstractButton类，这里只是简单列表了几个常用的方法。
    单选按钮组件
        在默认情况下，单选按钮显示一个圆形图标，并且通常在该图标旁放置一些说明性文字，而在应用程序中，一般将多个单选按钮放置在按钮组中，使这些单选按钮表现出某种功能，当用户选中某个单选按钮后，按钮组中其他按钮将被自动取消。单选按钮是Swing组件中JRadioButton类的对象，该类是JToggleButton的子类，而JToggleButton类又是AbstractButton类的子类，所以控制单选按钮的诸多方法都是AbstractButton类中的方法
        1.单选按钮
            可以使用JRadioButton类中的构造方法创建单选按钮对象。JRadioButton类的常用构造方法主要有以下几种形式
                public JRadioButton()
                public JRadioButton(Icon icon)
                public JRadioButton(Icon icon,boolean selected)
                public JRadioButton(String text)
                public JRadioButton(String text,Icon icon)
                public JRadioButton(String text,Icon icon,boolean selected)
            根据上述构造方法的方式，可以知道在初始化单选按钮时，可以同时设置单选按钮的图标、文字以及默认是否被选中等属性
        2.按钮组
            在Swing中存在一个ButtonGroup类，用于产生按钮组，如果希望将所有的单选按钮放置在按钮组中，需要实例化一个JRadioButton对象，并使用该对象调用add()方法添加单选按钮
    复选框组件
        复选框在Swing组件中的使用也非常广泛，它具有一个方块图标，外加一段描述性文字。与单选按钮唯一不同的是，复选框可以进行多选设置，每一个复选框都提供“选中”与“不选中”两种状态。复选框用JCheckBox类的对象表示，它同样继承于AbstractButton类，所以复选框组件的属性设置也来源于AbstractButton类
        JCheckBox的常用构造方法如下
            public JCheckBox()
            public JCheckBox(Icon icon,boolean checked)
            public JCheckBox(String text,boolean checked)
        复选框与其他按钮设置基本相同，除了可以在初始化时设置图标之外，还可以设置复选框的文字是否被选中

#### 13.7 列表组件

    Swing中提供两种列表组件，分别为下拉列表框与列表框。下拉列表框与列表框都是带有一系列项目的组件，用户可以从中选择需要的项目。列表框较下拉列表框更直观，它将所有的项目罗列在列表框中；但下拉列表框较列表框更为便捷、美观，它将所有的项目隐藏起来，当用户选用其中的项目时才会显现出来。

    下拉列表框组件
        JComboBox类
            初次使用Swing中的下拉列表框时，会感觉到该类下拉列表框与Windows操作系统中的下拉列表框有一些相似，实质上两者并不相同，因为Swing中的下拉列表框不仅可以供用户从中选择项目，也提供编辑项目中内容的功能
            下拉列表框是一个带条状的显示区，它具有下拉功能。在下拉列表框的右方存在一个倒三角形的按钮，当用户单击该按钮时，下拉列表框中的项目将会以列表形式显示出来
            Swing中的下拉列表框使用JComboBox类对象来显示，它是javax.swing.JComponent类的子类。它的常用构造方法如下
                public JComboBox()
                public JComboBox(ComboBoxModel dataModel)
                public JComboBox(Object[] arrayData)
                public JComboBox(Vector vector)
            在初始化下拉列表框时，可以选择同时指定下拉列表框中的项目内容，也可以在程序中使用其他方法设置下拉列表框中的内容，下拉列表框中的内容可以被封装在ComboBoxModel类型、数组或Vector类型中
        JComboBox模型
            在开发程序中，一般将下拉列表框中的项目封装为ComboBoxModel的情况比较多。ComboBoxModel为接口，它代表一般模型，可以自定义一个类实现该接口，然后在初始化JComboBox对象时向上转型为ComboBoxModel接口类型，但是必须实现以下两种方法
                public void setSelectedItem(Object item)
                public Object getSelectedItem()
            其中，setSelectedItem()方法用于设置下列列表框的选中项，getSelectedItem()方法用于返回下拉列表框中的选中项，有了这两个方法，就可以轻松地对下拉列表框中的项目进行操作
            自定义这个类除了实现该接口之外，还可以继承AbstractListModel类，在该类中也有两个操作下拉列表框的重要方法
                getSize()，返回列表的长度
                getElementAt(int index)，返回指定索引处的值
    列表框组件
        列表框与下拉列表框的区别不仅表现在外观上，当激活下拉列表框时，还会出现下拉列表框中的内容；但列表框只是在窗体上占据固定的大小，如果需要列表框具有滚动效果，可以将列表框放入滚动面板中。用户在选择列表框中的某一项时，按住Shift键并选择列表框中的其他项目，则当前选项和其他项目之间的选项将全部被选中；也可以按住Ctrl键并单击列表框中的单个项目，这样可以使列表框中被单机的项目反复切换非选择状态或选择状态
        Swing中使用JList类对象来表示列表框，常用的构造方法
            public void JList()
            public void JList(Object[] listData)
            public void JList(Vector listData)
            public void JList(ListModel dataModel)
        在上述构造方法中，存在一个没有参数的构造方法，可以通过在初始化列表框后使用setListData()方法对列表框进行设置，也可以在初始化的过程中对列表框中的项目进行设置。设置的方式有3种类型，包括数组、Vector类型和ListModel模型
        当使用数组作为构造方法的参数时，首先需要创建列表项目的数组，然后再利用构造方法来初始化列表框
        如果使用ListModel模型为参数，需要创建ListModel对象。ListModel是Swing包中的一个接口，它提供了获取列表框属性的方法。但是在通常情况下，为了使用户不完全实现ListModel接口中的方法，通常自定义一个类继承实现该接口的抽象类AbstractListModel。在这个类中提供了getElementAt()与getSize()方法，其中getElementAt()方法代表根据项目的索引获取列表框中的值，而getSize()方法用于获取列表框中的项目个数。
        还可以使用DefaultListModel类创建列表框，该类扩展了AbstractListModel类，所以也可以通过DefaultListModel对象向上转型为ListModel接口初始化列表框，同时DefaultListModel类提供addElement()方法实现将内容添加至列表框中

#### 13.8 文本组件

    文本组件在实际项目开发中使用最为广泛，尤其是文本框与密码框组件。通过文本组件可以很轻松地处理单行文字、多行文字、口令字段

    文本框组件
        文本框用来显示或编辑一个单行文本，在Swing中通过javax.swing.JTextField类对象创建，该类继承了javax.swing.text.JTextComponent类。常用构造方法
            public JTextField()
            public JTextField(String text)
            public JTextField(int fieldwidth)
            public JTextField(String text,int fieldwidth)
            public JTextField(Document docModel,String text,int fieldwidth)
        从上述构造方法可以看出，定义JTextField组件很简单，可以通过在初始化文本框时设置文本框的默认文字、文本框的长度等实现
    密码框组件
        密码框与文本框定义与用法基本相同，唯一不同的是密码框将用户输入的字符串以某种符号进行加密。密码框对象是通过javax.swing.JPasswordField类来创建的，JPasswordField类的构造方法与JTextField类的构造方法非常相似。常用的构造方法
            public JPasswordField()
            public JPasswordField(String text)
            public JPasswordField(int fieldwidth)
            public JPasswordField(String text,int fieldwidth)
            public JPasswordField(Document docModel,String text,int fieldwidth)
    文本域组件
        在程序中接受用户的多行文字输入
        Swing中任何一个文本区域都是JTextArea类型的对象。常用构造方法
            public JTextArea()
            public JTextArea(String text)
            public JTextArea(int rows,int columns)
            public JTextArea(Document doc)
            public JTextArea(Document doc,String text,int rows,int columns)
        上述构造方法可以在初始化文本域时提供默认文本以及文本域的长与宽
        JTextArea类中存在一个setLineWrap()方法，该方法用于设置文本域是否可以自动换行，如果将该方法的参数设置为true，文本域将自动换行

#### 13.9 常用事件监听器

    组件本身并不带有任何功能。
    在Swing事件模型中由三个分离的对象完成对事件的处理，分别为事件源、事件以及监听程序，事件源触发一个事件，它被一个或多个“监听器”接收，监听器负责处理事件
    所谓事件监听器，实质上就是一个“实现特定类型监听器接口”的类对象。事件几乎都以对象来表示，它是某种事件类的对象，事件源（如按钮）会在用户做出相应的动作（如按钮被按下）时产生事件对象，如动作时间对应ActionEvent类对象，同时要编写一个监听器的类必须实现相应的接口，如ActionEvent类对应的是ActionListener接口，需要获取某个事件对象就必须实现相应的接口，同时需要将接口的方法一一实现。最后事件源（按钮）调用相应的方法加载这个“实现特定类型监听器接口”的类对象，所有的事件源都具有addXXXListener()和removeXXXListener()方法（其中“XXX”表示监听事件类型），这样就可以为组件添加或移除相应的事件监听器

    动作事件监听器
        动作事件监听器是Swing中比较常见的事件监听器，很多组件的动作都会使用它监听，如按钮被单击。
            事件名称     事件源                         监听接口
            ActionEvent JButton、JList、JTextField等   ActionListener
            添加或删除相应类型监听器的方法
            addActionListener()、removeActionListener()
        可以通过定义类实现ActionListener接口，不需要使用内部类实现事件监听。一般情况下，为事件源做监听事件应使用匿名内部类形式。
    焦点事件监听器
        焦点事件监听器在实际项目开发中应用也比较广泛，如将光标焦点离开一个文本框时需要弹出一个对话框，或者将焦点返回给该文本框等。
            事件名称     事件源                 监听接口
            FocusEvent  Component以及派生类     FocusListener
            添加或删除相应类型监听器的方法
            addFocusListener()、removeFocusListener()

### 14 集合类

#### 14.1 集合类概述

    java.util包中提供了一些集合类，这些集合类又被称为容器。提到容器不难想到数组，集合类与数组的不同之处是，数组的长度是固定的，集合的长度是可变的；数组用来存放基本类型的数据，集合用来存放对象的引用。常用的集合有List集合、Set集合和Map集合，其中List与Set继承了Collection接口，各接口还提供了不同的实现类。

#### 14.2 Collection接口

    Collection接口是层次结构中的根接口。构成Collection的单位称为元素。Collection接口通常不能直接使用，但该接口提供了添加元素、删除元素、管理数据的方法。由于List接口与Set接口都继承了Collection接口，因此这些方法对List集合与Set集合是通用。
        add(E e)            将指定的对象添加到该集合中
        remove(Object o)    将指定的对象从该集合中移除
        isEmpty()           返回boolean值，用于判断当前集合是否为空
        iterator()          返回在此Collection的元素上进行迭代的迭代器。用于遍历集合中的对象
        size()              返回int型值，获取该集合中元素的个数
    通常遍历集合，都是通过迭代器来实现。Collection接口中的itertor()方法可返回在此Collection进行迭代的迭代器。
        iterator的next()方法返回的是Object

#### 14.3 List集合

    List集合包括List接口以及List接口的所有实现类。List集合中的元素允许重复，个元素的顺序就是对象插入的顺序。类似Java数组，用户可通过使用索引(元素在集合中的位置)来访问集合中的元素。

    List接口
        List接口继承了Collection接口，因此包含Collection中的所有方法。此外，List接口还定义了以下两个非常重要的方法
            get(int index)，获得指定索引位置的元素
            set(int index,Object obj)，将集合中指定索引位置的对象修改为指定的对象
    List接口的实现类
        List接口的常用实现类有ArrayList与LinkedList
            ArrayList类实现了可变的数组，允许保存所有元素，包括null，并可以根据索引位置对集合进行快速的随机访问；缺点是向指定的索引位置插入对象或删除对象的速度较慢
            LinkedList采用链表结构保存对象。这种结构的优点是便于向集合中插入和删除对象，需要向集合中插入、删除对象时，使用LinkedList类实现的List集合的效率较高；但对于随机访问集合中的对象，使用LinkedList类实现List集合的效率较低
        使用List集合时通常声明为List类型，可通过不同的实现类来实例化集合
        与数组相同，集合的索引也是从0开始

#### 14.4 Set集合

    Set集合中的对象不按特定的方式排序，只是简单地把对象加入集合中，但Set集合中不能包含重复对象。Set集合由Set接口和Set接口的实现类组成。Set接口继承了Collection接口，因此包含了Collection接口的所有方法
    Set的构造有一个约束条件，传入的Collection对象不能有重复值，必须小心操作可变对象(Mutable Object)。如果一个Set中的可变元素改变了自身状态导致Object.equals(Oeject)=true，则会出现一些问题
    Set接口常用的实现类有HashSet类与TreeSet类
        HashSet类实现Set接口，由哈希表（实际上是一个HashMap实例）支持。它不保证Set的迭代顺序，特别是它不保证该顺序恒久不变。此类允许使用null元素
        TreeSet类不仅实现了Set接口，还实现了java.util.SortedSet接口，因此，TreeSet类实现的Set集合在遍历集合时按照自然顺序递增顺序，也可以按照指定比较器递增顺序，即可以通过比较器对用TreeSet实现的Set集合中的对象进行排序。TreeSet类新增的方法：
            first()         返回此Set中当前第一个（最低）元素
            last()          返回此Set中当前最后一个（最高）元素
            comparator()    返回对此Set中的元素进行排序的比较器。如果此Set使用自然顺序，则返回null
            headSet(E toElement)    返回一个新的Set集合，新集合是toElement(不包含)之前的所有对象
            subSet(E fromElement,E toElement)     返回一个新的Set集合，是fromElement(包含)对象与toElement(不包含)对象之间的所有对象
            tailSet(E fromElement)  返回一个新的Set集合，新集合包含对象fromElement(包含)之后的所有对象
        headSet()、subSet()、tailSet()方法截取对象生成新集合时是否包含指定的参数，可通过如下方式来判别：如果指定参数位于新集合的起始位置，则包含该对象，如subSet()方法的第一个参数和tailSet()方法的参数；如果指定参数是新集合的终止位置，则不包含该参数，如headSet()方法的入口参数和subSet()方法的第二个入口参数

#### 14.5 Map集合

    Map集合没有继承Collection接口，其提供的是key到value的映射。Map中不能包含相同的key，每个key只能映射一个value。key还决定了存储对象在映射中的存储位置，但不是由key对象本身决定的，而是通过一种“散列技术”进行处理，产生一个散列码的整数值。散列码通常用作一个偏移量，该偏移量对应分配给映射的内存区域的起始位置，从而确定存储对象在映射中的存储位置。Map集合包括Map接口以及Map接口的所有实现类

    Map接口
        Map接口提供了将key映射到值得对象。一个映射不能包含重复的key，每个key最多只能映射到一个值。Map接口中同样提供了集合的常用方法，除此之外的常用方法
            put(K key,V value)      向集合中添加指定的key与value的映射关系
            containKey(Object key)  如果此映射包含指定的key的映射关系，则返回true
            containsValue(Object value) 如果此映射将一个或多个key映射到指定值，则返回true
            get(Object key) 如果存在指定的key对象，则返回对象对应的值，否则返回null
            keySet()    返回该集合中的所有key对象形成的Set集合
            values()    返回该集合中所有值对象形成的Collection集合
        Map集合中允许值对象是null，而且没有个数限制
    Map接口的实现类
        Map接口常用的实现类有HashMap和TreeMap。建议使用HashMap类实现Map集合，因为由HashMap类实现的Map集合添加和删除映射关系效率更高。HashMap是基于哈希表的Map接口的实现，HashMap通过哈希码对其内部的映射关系进行快速查找；而TreeMap中的映射关系存在一定的顺序，如果希望Map集合中的对象也存在一定的顺序，应该使用TreeMap类实现Map集合
            HashMap类是基于哈希表的Map接口的实现，此实现提供所有可选的映射操作，并允许使用null值和null键，但必须保证键的唯一性。HashMap通过哈希表对其内部的映射关系进行快速查找。此类不保证映射的顺序，特别是它不保证该顺序恒久不变
            TreeMap类不仅实现了Map接口，还实现了java.util.SortedMap接口，因此，集合中的映射关系具有一定的顺序。但在添加、删除和定位映射关系时，TreeMap类比HashMap类性能稍差。由于TreeMap类实现的Map集合中的映射关系是根据键对象按照一定的顺序排列的，因此不允许键对象是null
        可以通过HashMap类创建Map集合，当需要顺序输出时，再创建一个完成相同映射关系的TreeMap实例

### 15 I/O(输入/输出)

#### 15.1 流概述

    流是一组有序的数据序列，根据操作的类型，可分为输入流和输出流两种。I/O(Input/Output,输入输出)流提供了一条通道程序，可以使用这条通道把源中的字节序列送到目的地。虽然I/O流通常与磁盘文件存取有关，但是程序的源和目的地也可以是键盘、鼠标、内存或显示器窗口等。
    Java由数据流处理输入/输出模式，程序从指向源的输入流中读取源中的数据。源可以是文件、网络、压缩包或其他数据源
    输出流的指向是数据要到达的目的地，程序通过向输出流中写入数据把信息传递到目的地。输出流的目标可以是文件、网络、压缩包、控制台和其他数据输出目标

#### 15.2 输入/输出流

    Java语言定义了许多类专门负责各种方式的输入/输出，这些类都被放在java.io包中。其中，所有输入流类都是抽象类InputStream(字节输入流)或抽象类Reader(字符输入流)的子类；而所有输出流都是抽象类OutputStream(字节输出流)或抽象类Writer(字符输出流)的子类
    输入流
        InputStream类是字节输入流的抽象类，是所有字节输入流的父类。InputStream类的具体层次结构
            AudioInputStream
            ByteArrayInputStream
            StringBufferInputStream
            FileInputStream
            FilterInputStream
                BufferedInputStream
                DataInputStream
                PushbackInputStream
                ......
            InputStream
            ObjectInputStream
            SequenceInputStream
            PipeInputStream
        该类中所有方法遇到错误时都会引发IOException异常。对该类中的一些方法的简要说明
            read()方法：从输入流中读取数据的下一个字节。返回0-255范围内的int字节值。如果因为已经到达流末尾而没有可用的字节，则返回值为-1
            read(byte[] b)：从输入流中读入一定长度的字节，并以整数的形式返回字节数
            mark(int readlimit)方法：在输入流的当前位置放置一个标记，readlimit参数告知此输入流在标记位置是小之前允许读取的字节数
            reset()方法：将输入指针返回到当前所做的标记处
            skip(long n)方法：跳过输入流上的n个字节并返回实际跳过的字节数
            markSupported()方法：如果当前流支持mark()/reset()操作就返回true
            close方法：关闭此输入流并释放与该流关联的所有系统资源
        并不是所有的InputStream类的子类都支持InputStream中定义的所有方法，如skip()、mark()、reset()等方法只对某些子类有用
        Java中的字符是Unicode编码，是双字节的。InputStream是用来处理字节的，并不适合处理字符文本。Java为字符文本的输入专门提供了一套单独的类Reader，但Reader类并不是InputStream类的替换者，只是在处理字符串时简化了编程。Reader类是字符输入流的抽象类，所有字符输入流的实现都是它的子类。Reader类的具体层次结构
            CharArrayReader
            BufferedReader
                LineNumberReader
            FilterReader
                PushbackReader
            InputStreamReader
                FileReader
            PipedReader
            StringReader
        Reader类中的方法与InputStream类中的方法类似
    输出流
        OutputStream类是字节输出流的抽象类，此抽象类是表示输出字节流的所有类的超类(父类)。OutputStream类的具体层次结构
            ByteArrayOutputStream
            FileOutputStream
            FilterOutputStream
                BufferedOutputStream
                DataOutputStream
                ......
            ObjectOutputStream
            OutputStream
                OutputStream
            PipedOutputStream
        OutputStream类中的所有方法军返回void，在遇到错误时会引发IOException异常。对该类中的一些方法的简要说明
            write(int b)方法：将指定的字节写入此输入流
            write(byte[] b)方法：将b个字节从指定的byte整组写入此输入流
            write(byte[] b,int off,int len)方法：将指定byte数组中从偏移量off开始的len个字节写入此输入流
            flush()方法：彻底完成输出并清空缓存区
            close()方法：关闭输出流
        Writer类是字符输出流的抽象类，所有字符输出类的实现都是它的子类。Writer类的层次结构
            BufferedWriter
            CharArrayWriter
            FilterWriter
            OutputStreamWriter
                FileWriter
            PipedWriter
            PrintWriter
            StringWriter

#### 15.3 File类

    File类是java.io包中唯一代表磁盘文件本身的对象。File类定义了一些与平台无关的方法来操作文件，可以通过调用File类中的方法，实现创建、删除、重命名文件等操作。File类的对象主要用来获取文件本身的一些信息，如文件所在的目录、文件的长度、文件读写权限等。数据流可以将数据写入到文件中，文件也是数据流最常用的数据媒体
    文件的创建与删除
        可以使用File类创建一个文件对象。通常使用以下3种构造方法来创建文件对象
            (1)File(String pathname)
                该构造方法通过将给定路径名字字符串转换为抽象路径名来创建一个新File实例
                    new File(String pathname)
                其中，pathname指路径名称(包含文件名)
                    File file=new File("d:/1.txt");
            (2)File(String parent,String child)
                该构造方法根据定义的父路径和子路径字符串(包含文件名)创建一个新的File对象
                    new File(String parent,String child)
                        parent:父路径字符串，例如D:/或D:/doc
                        child:子路径字符串，例如letter.txt
            (3)File(File f,String child)
                该构造方法根据parent抽象路径名和child路径名字字符串创建一个新的File实例
                    new File(File f,String child)
                        f:路径对象，例如D:/doc/
                        child:子路径字符串，例如letter.txt
            对于Microsoft Windows平台，包含盘符的路径名前缀由驱动器号和一个":"组成。如果路径名是绝对路径名，还可能后跟"\\"
        当使用File类创建一个文件对象后，例如：
            File file=new File("word.txt");
        如果当前目录中不存在名称为word的文件，File类对象可通过调用createNewFile()方法创建一个名称为word.txt的文件；如果存在word.txt文件，可以通过文件对象的delete()方法将其删除
    获取文件信息
        File类提供了很多方法以获取文件本身信息
            方法            返回值      说明
            getName()       String      获取文件的名称
            canRead()       boolean     判断文件是否为可读的
            canWrite()      boolean     判断文件是否可被写入
            exits()         boolean     判断文件是否存在
            length()        long        获取文件的长度(以字节为单位)
            getAbsolutePath()   String  获取文件的绝对路径
            getParent()     String      获取文件的父路径
            isFile()        boolean     判断文件是否存在
            isDiretory()    boolean     判断文件是否为一个目录
            isHidden()      boolean     判断文件是否为隐藏文件
            lastModified()  long        获取文件最后修改时间

#### 15.4 文件输入/输出流

    程序运行器件，大部分数据都在内存中进行操作，当程序结束或关闭时，这些数据将消失。如果需要将数据永久保存，可使用文件输入/输出流与指定的文件建立连接，将需要的数据永久保存到文本中。
    FileInputStream与FileOutputStream类
        FileIinputStream类与FileOutputStream都用来操作磁盘文件。如果用户的文件读取需求比较简单，则可以使用FileInputStream类，该类继承自InputStream类。FileOutputStream类与FileInputStream类对应，提供了基本的文件写入能力。FileOutputStream类是OutputStream类的子类。
        FileInputStream类常用的构造方法
            FileInputStream(String name)
            FileInputStream(File file)
        第一个构造方法使用给定的文件名name创建一个FileInputStream对象，第二个构造方法使用File对象创建FileInputStream对象。第一个构造方法比较简单，但第二个构造方法允许在把文件连接输入流之前对文件作进一步分析
        FileOutputStream类有与FileInputStream类相同的参数构造方法，创建一个FileOutputStream对象时，可以指定不存在的文件名，单词文件不能是一个已被其他程序打开的文件。
        虽然Java在程序结束时自动关闭所有打开的流，但是当使用完成后，显式地关闭所有打开的流仍是一个好习惯。一个被打开的流有可能会用尽系统资源，这取决于平台和实现。如果没有将打开的流关闭，当另一个程序试图打开另一个流时，可能会得不到需要的资源
    FileReader和FileWriter类
        使用FileOutputStream类向文件中写入数据与使用FileInputStream类从文件中将内容读出来，都存在一点不足，即这两个类都只提供了对字节或字节数组的读取方法。由于汉字在文件中占用两个字节，如果使用字节流，读取不好可能会出现乱码现象，此时采用字符流Reader或Writer类即可避免这种现象。
        FileReader和FileWriter字符流对应了FileInputStream和FileOutputStream类。FileReader流顺序地读取文件，只要不关闭流，每次调用read()方法就顺序地读取源中其余的内容，直到源的末尾或流被关闭。

#### 15.5 带缓存的输入/输出流

    缓存是I/O的一种性能优化。缓存流为I/O流增加了内存缓存区。有了缓存区，使得在流上执行skip()、mark()和reset()方法都成为可能。
    BufferedInputStream与BufferedOutputStream类
        BufferedInputStream类可以对所有InputStream类进行带缓存区的包装以达到性能的优化。BufferedInputStream类有两个构造方法
            BufferedInputStream(InputStream in)
            BufferedInputStream(inputStream in,int size)
        第一种形式的构造方法创建了一个带有32个字节的缓存流；第二种形式的构造方法按指定的大小来创建缓存区。一个最优的缓存区的大小，取决于它所在的操作系统、可用的内存空间以及机器配置。从上述构造方法可以看出，BufferedInputStream对象位于InputStream类对象之前。
        使用BufferedOutputStream输出信息和用OutputStream输出信息完全一样，只不过BufferedOutputStream有一个flush()方法用来将缓存区的数据强制输出完。BufferedOutputStream类也有两个构造方法
            BufferedOutputStream(OutputStream out)
            BufferedOutputStream(OutputStream out,int size)
        第一种构造方法创建一个有32个字节的缓存区，第二种构造方法以指定的大小来创建缓存区
        flush()方法就是用于即使在缓存区没有满的情况下，也将缓存区的内容强制写入到外设，习惯上称这个过程为刷新。flush()方法只对使用缓存区的OutputStream类的子类有效。当调用close()方法时，系统在关闭流之前，也会将缓存区中的信息刷新到磁盘文件中。
    BufferedReader与BufferedWriter类
        BufferedReader类与BufferedWriter类分别继承Reader类与Writer类。这两个类同样具有内部缓存机制，并可以以行为单位进行输入/输出
        BufferedReader类常用的方法如下
            read()方法：读取单个字符
            readLine()方法：读取一个文本行，并将其返回为字符串。若无数据可读，则返回null
        BufferedWriter类中的方法都返回void。常用的方法如下：
            write(String s,int off,int len)方法：写入字符串的某一部分
            flush()方法：刷新该流的缓存
            newline()方法：写入一个行分隔符
        在使用BufferedWriter类的Writer()方法时，数据并没有立刻被写入输出流，而是首先进入缓存区中。如果想立刻将缓存区中的数据写入输出流，一定要调用flush()方法

#### 15.6 数据输入/输出流

    数据输入/输出流允许应用程序以与机器无关的方式从底层输入流中读取基本Java类型。当读入一个数据时，不必再关心这个数值应当是哪种字节。
    DataInputStream类与DataOutputStream类的构造方法如下
        DataInputStream(InputStream in)：使用指定的基础InputStream创建一个DataInputStream
        DataOutputStream(OutputStream out)：创建一个新的数据输出流，将数据写入指定基础输出流。
        DataOutputStream类提供了如下3种写入字符串的方法。
            writeBytes(String s)
            writeChars(String s)
            writeUTF(String s)
        由于Java中的字符是Unicode编码，是双字节的，writeBytes只是将字符串中的每一个字符的低字节内容写入目标设备中；而writeChars将字符串中的每一个字符的两个字节的内容都写到目标设备中；writeUTF将字符串按照UTF编码后的字节长度写入目标设备，然后才是每一个字节的UTF编码。
        DataInputStream类只提供了一个readUTF()方法返回字符串。这是因为要在一个连续的字节流读取一个字符串，如果没有特殊的标记作为一个字符串的结尾，并且不知道这个字符串的长度，就无法知道读取到什么位置才是这个字符串的结束。DataOutputStream类中只有writeUTF()方法向目标设备中写入字符串的长度，所以也能准确地读回写入字符串。

#### 15.7 ZIP压缩输入/输出流

    ZIP压缩管理文件是一种十分典型的文件压缩格式，使用它可以节省存储空间。关于ZIP压缩的I/O实现，在Java的内置类中提供了非常好用的相关类，所以实现方式非常简单。使用java.util.zip包中的ZipOutputStream与ZipInputStream类来实现文件的压缩/解压缩。如要从ZIP压缩管理文件内读取某个文件，要先找到对应该文件的"目录进入点"（从它可知该文件在ZIP文件内的位置），才能读取这个文件的内容。如果要将文件内容写入ZIP文件内，必须先写入对应于该文件的"目录进入点"，并且把要写入文件内容的位置移到此进入点所指的位置，然后再写入文件内容。
    Java实现了I/O数据流与网络数据流的单一接口，因此数据的压缩、网络传输和解压缩的实现比较容易。ZipEntry类产生的对象，是用来代表一个ZIP压缩文件内的进入点。ZipInputStream类用来读取ZIP压缩格式的文件，所支持的包括已压缩及未压缩的进入点。
    压缩文件
        利用ZipOutputStream类对象，可将文件压缩为.zip文件。ZipOutputStream类的构造方法如下
            ZipOutputStream(OutputStream out)
        ZipOutputStream类的常用方法，返回值都为null
            putNextEntry(ZipEntry e)：开始写一个新的ZipEntry，并将流内的位置移至此entry所指数据的开头
            write(byte[] b,int off,int len)：将字节数组写入当前ZIP条目数据
            finish()：完成写入ZIP输出流的内容，无须关闭它所配合的OutputStream
            setComment(String comment)：可设置此ZIP文件的注释文字
    解压缩ZIP文件
        ZipInputStream类可读取ZIP压缩格式的文件，包括已压缩和未压缩的条目。ZipInputStream类的构造方法如下
            ZipInputStream(InputStream in)
        ZipInputStream类的常用方法
            read(byte[] b,int off,int len)：int，读取目标b数组内off偏移量的位置，长度是len字节
            available()：int，判断是否已读完目前entry所指定的数据。已读完返回0，否则返回1
            closeEntry()：void，关闭当前ZIP条目并定位流以读取下一个条目
            skip(long n)：long，跳过当前ZIP条目中指定的字节数
            getNextEntry()：ZipEntry，读取下一个ZipEntry，并将流内的位置移至此entry所指数据的开头
            createZipEntry(String name)：ZipEntry，以指定的name参数新建一个ZipEntry对象

### 16 反射

#### 16.1 Class类与Java反射

    通过Java反射机制，可以在程序中访问已经装载到JVM中的Java对象的描述，实现访问、检测和修改描述Java对象本身信息的功能。Java反射机制的功能十分强大，在java.lang.reflect包中提供了对该功能的支持。
    所有Java类都继承了Object类，在Object类中定义了一个getClass()方法，该方法返回一个类型为Class的对象
        ex: Class textFieldC = textField.getClass();
    利用Class类的对象textFiledC，可用访问用来返回该对象的textField对象的描述信息。可用访问的主要描述信息：
        组成部分        访问方法            返回值类型          说明
        包路径          getPackage()        package对象         获得该类的存放路径
        类名称          getName()           String对象          获得该类的名称
        继承类          getSuperclass()     Class对象           获得该类继承的类
        实现接口        getInterfaces()     Class型数组         获得该类实现的所有接口
        构造方法        getConstructors()   Constructor型数组   获得所有权限为public的构造方法
getConstructor(Class<?>...parameterTypes)   ...对象             获得权限为public的指定构造方法
            getDeclaredConstructors()       Constructor型数组   获得所有构造方法，按声明顺序返回
getDeclaredConstructor(Class<?>...parameterTypes)   ...对象     获得指定构造方法
        方法            getMethods()        Method型数组        获得所有权限为public的方法
getMethod(String name,Class<?>...parameterTypes)  ...对象       获得权限为public的指定方法
            getDeclaredMethods()            Method型数组        获得所有方法，按声明顺序返回
getMethod(String name,Class<?>...parameterTypes)  ...对象       获得指定方法
        成员变量        getFields()         Field型数组         获得所有权限为public的成员变量
                getField(String name)       Field对象           获得权限为public的指定成员变量
                        getDecla redFields() Field型数组         获得所有成员变量，按声明顺序返回
                getField(String name)       Field对象           获得指定成员变量
        内部类          getClasses()        Class型数组         获得所有权限为public的内部类
                    getDeclaredClasses()    Class型数组         获得所有内部类
        内部类的声明类  getDeclaringClass() Class对象           如果该类为内部类，则返回它的成员类，否则返回null
    在通过getFields()和getMethods()方法依次获得权限为public的成员变量和方法时，将包含从超类中继承到的成员变量和方法；而通过方法getDeclaredFields()和getDeclaredMethods()只是获得在本类中定义的所有成员变量和方法

    访问构造方法
        在通过下列一组方法访问构造方法时，将返回Constructor类型的对象或数组。每个Constructor对象代表一个构造方法，利用Constructor对象可以操纵相应的构造方法。
            getConstructors()
            getConstructor(Class<?>...parameterTypes)
            getDeclaredConstructors()
            getDeclaredConstructor(Class<?>...parameterTypes)
        如果是访问指定的构造方法，根据需要该构造方法的入口参数的类型来访问。例如，访问一个入口参数类型依次为String和int型的构造方法，通过下面两种方式均可实现
            objectClass.getDeclaredConstructor(String.class,int.class);
            objectClass.getDeclaredConstructor(new Class[] {String.class,int.class})
        Constructor类中提供的常用方法
            isVarArgs()：查看该构造方法是否允许带有可变数量的参数，如果允许则返回true，否则返回false
            getParameterTypes()：按照声明顺序以Class数组的形式获得该构造方法的各个参数的类型
            getExceptionTypes()：以Class数组的形式获得该构造方法可能抛出的异常类型
            newInstance(Object...initargs)：通过该构造方法利用指定参数创建一个该类的对象，如果未设置参数则表示采用默认无参数的构造方法
            setAccessible(boolean flag)：如果该构造方法的权限为private，默认为不允许通过反射利用newInstance(Object...initargs)方法创建对象。如果先执行该方法，并将入口参数设置为true，则允许创建
            getModifiers()：获得可以解析出该构造方法所采用修饰符的整数
        通过java.lang.reflect.Modifier类可以解析出getModifiers()方法的返回值所表示的修饰符信息，在该类中提供了一系列用来解析的静态方法，既可以查看是否被指定的修饰符修饰，还可以以字符串的形式获得所有修饰符。该类常用静态方法
            isPublic(int mod)：查看是否被public修饰符修饰，如果是返回true，否则返回false
            isProtected(int mod)：查看是否被protected修饰符修饰，如果是返回true，否则返回false
            isPrivate(int mod)：查看是否被private修饰符修饰，如果是返回true，否则返回false
            isStatic(int mod)：查看是否被static修饰符修饰，如果是返回true，否则返回false
            isFinal(int mod)：查看是否被final修饰符修饰，如果是返回true，否则返回false
            toString(int mod)：以字符串的形式返回所有修饰符
        判断对象constructor所代表的构造方法是否被private修饰，以及以字符串形式获得该构造方法的所有修饰符的典型代码如下
            int modifiers=constructor.getModifiers();
            boolean isEmbellishByPrivate=Modifier.isPrivate(modifiers);
            String embellishment=Modifier.toString(modifiers);
        访问成员变量
            在通过下列一组方法访问成员变量时，将返回Field类型的对象或数组。每个Field对象代表一个成员变量，利用Field对象可以操纵相应的成员变量。
                getFields()
                getField(String name)
                getDeclaredFields()
                getDeclaredField(String name)
            如果是访问指定的成员变量，可以通过该成员变量的名称来访问。例如，访问一个名称为birthday的成员变量，访问方法如下
                object.getDeclaredField("birthday")
            Field类中提供的常用方法
                getName()                       获得该成员变量的名称
                getType()                       获得表示该成员变量类型的Class对象
                get(Object obj)                 获得指定对象obj中成员变量的值，返回值为Object型
                set(Object obj,Object value)    将指定对象obj中成员变量的值设置为value
                getInt(Object obj)              获得指定对象obj中类型为int的成员变量的值
                serInt(Object obj,int i)        将指定对象obj中类型为int的成员变量设置为i
                getFloat(Object obj)            获得指定对象obj中类型为float的成员变量的值
                setFloat(Object obj,flaot f)    将指定对象obj中类型为float的成员变量的值设置为f
                getBoolean(Object obj)          获得指定对象obj中类型为boolean的成员变量的值
                setBoolean(Object obj,boolean z)将指定对象obj中类型为boolean的成员变量的值设置为z
                setAccessible(boolean flag)     此方法可以设置是否忽略权限限制直接访问private等私有权限的成员变量
                getModifiers()                  获得可以解析出该成员变量所采用修饰符的整数
        访问方法
            在通过下列一组方法访问方法时，将返回Method类型的对象或数组。每个Method对象代表一个方法，利用Method对象可以操纵相应的方法。
                getMethods()
                getMethod(String name,class<?>...parameterTypes)
                getDeclaredMethods()
                getDeclaredMethod(String name,Class<?>...parameterTypes)
            如果是访问指定的方法，需要根据该方法的名称和入口参数的类型来访问。访问一个名称为print、入口参数类型依次为String和int型的方法，通过下面两种方式均可实现
                objectClass.getDeclaredMethod("print",String.class,int.class)
                objectClass.getDeclaredMethod("print",new Class[] {String.class,int.class})
            Method类中提供的常用方法
                getName()                       获得该方法的名称
                getParameterTypes()             按照声明顺序以Class数组的形式获得该构造方法的各个参数的类型
                gerReturnType()                 以Class对象的形式获得该方法的返回值的类型
                getExceptionTypes()             以Class数组的形式获得该方法可能抛出的异常类型
                invoke(Object obj,Object...args)利用指定参数args指定对象obj中的该方法，返回值为Object型
                isVarArgs()                     查看该构造方法是否允许带有可变数量的参数，如果允许则返回true，否则返回false
                getModifiers()                  获得可以解析出该方法所采用修饰符的整数
            在反射中执行具有可变数量的参数的构造方法时，需要将入口参数定义成二维数组。

#### 16.2 使用Annotation功能

    Java中提供了Annotation功能，该功能可用于类、构造方法、成员变量、方法、参数等的声明中。该功能并不影响程序的运行，但是会对编译器警告等辅助工具产生影响。

    定义Annotation类型
        在定义Annotation类型时，也需要用到用来定义接口的interface关键字，但需要在interface关键字前加一个"@"符号，即定义Annotation类型的关键字为@interface，这个关键字的隐含意思是继承了java.lang.annotation.Annotation接口。下面的代码就定义了一个Annotation
            public @interface NoMemberAnnotation{
            }
        上面定义的Annotation类型@NoMemberAnnotation未包含任何成员，这样的Annotation类型被称为marker annotation。下面的代码定义了一个只包含一个成员的Annotation类型。
            public @interface OneMemberAnnotation{
                String value();
            }
            String：成员类型，可用的成员类型有String、Class、primitive、enumerated和annotation，以及所列类型的数组
            value：成员名称。如果在所定义的Annotation类型中只包含一个成员，通常将成员名称命名为value
        在为Annotation类型定义成员变量时，也可以为成员设置默认值。
            public @interface DefaultValueAnnotation{
                String decribe();   //default "<默认值>"
                Class type() default void class;
            }
        在定义Annotation类型时，还可以通过Annotation类型@Target来设置Annotation类型适用的程序元素种类。如果未设置@Target，则表示适用于所有程序元素。枚举类ElementType中的枚举常量用来设置@Target
            ANNOTATION_TYPE 表示用于Annotation类型
            TYPE            表示用于类、接口和枚举，以及Annotation类型
            CONSTRUCTOR     表示用于构造方法
            FIELD           表示用于成员变量和枚举常量
            METHOD          表示用于方法
            PARAMETER       表示用于参数
            LOCAL_VARIABLE  表示用于局部变量
            PACKAGE         表示用于包
        通过Annotation类型@Retention可以设置Annotation的有效范围。枚举类RetentionPolicy中的枚举常量用来设置@Retention。如果未设置@Retention，Annotation的有效范围为枚举常量CLASS表示的范围
            SOURCE  表示不编译Annotation到类文件中，有效范围最小
            CLASS   表示编译Annotation到类文件中，但是在运行时不加载Annotation到JVM中
            RUNTIME 表示在运行时加载Annotation到JVM中，有效范围最大
    访问Annotation信息
        如果在定义Annotation类型时将@Retention设置为RetentionPolicy.RUNTIME，那么在运行程序时通过反射就可以获取到相关的Annotation信息，如获取构造方法、字段和方法的Annotation信息。
        类Constructor、Field和Method均继承了AccessibleObject类，在AccessibleObject中定义了3个关于Annotation的方法，其中方法isAnnotationPresent(Class<? extends Annotation> annotationClass)用来查看是否添加了指定类型的Annotation，如果是则返回true，否则返回false；方法getAnnotation(Class<T> annotationClass)用来获得指定类型的Annotation，如果存在则返回相应的对象，否则返回null；方法getAnnotation()用来获得所有的Annotation，该方法将返回一个Annotation数组。
        在类Constructor和Method中还定义了方法getParameterAnnotations()，用来获得为所有参数添加的Annotation，将以Annotation类型的二维数组返回，在数组中的顺序与声明的顺序相同，如果没有参数则返回一个长度为0的数组；如果存在未添加Annotation的参数，将用一个长度为0的嵌套数组占位。

### 17 枚举类型与泛型

#### 17.1 枚举类型

    使用枚举类型，可以取代前面定义常量的方式，同时枚举类型还赋予程序在编译时进行检查的功能。
    使用枚举类型设置常量
        设置常量时，通常将常量放置在接口中，这样在程序中就可以直接使用。该常量不能被直接修改，因为在接口中定义常量时，该常量的修饰符为final与static。常规定义常量：
            public interface Constants{
                public static final int Constants_A=1;
                public static final int Constants_B=12;
            }
        使用枚举类型
            public enum Constants{
                Constants_A,
                Constants_B,
                Constants_C
            }
        其中，enum时定义枚举类型的关键字。当需要在程序中使用该常量时，可以使用Constants.Constants_A来表示
        枚举类型也可以在类的内部进行定义，这种形式类似于内部类形式，当编译该类时，除了ConstantsTest.class外，还存在ConstantsTest$1.class与ConstantsTest$Constants2.class文件
            public class ConstantsTest{
                enum Constants{
                    Constants_A,
                    Constants_B,
                    Constants_C
                }
                ...
            }
    深入了解枚举类型
        操作枚举类型成员的方法
            枚举类型较传统定义常量的方式，除了具有参数类型检测的优势之外，还具有其他方面的优势。
            用户可以将一个枚举类型看作是一个类，它继承于java.lang.Enum类，当定义一个枚举类型时，每一个枚举类型成员都可以看作是枚举类型的的一个实例，这些枚举类型成员都默认被final、public、static修饰，所以当使用枚举类型成员时直接使用枚举类型名称调用枚举类型成员即可。
            由于枚举类型对象继承于java.lang.Enum类，所以该类中一些操作枚举类型的方法都可以应用到枚举类型中。下面是枚举类型的常用方法
                方法名称    具体含义                                使用方法                    举例
                values()    该方法可以将枚举类型成员以数组的方式返回  枚举类型名称.values()       Constants2.values()
                valueOf()   该方法可以实现将普通字符串转换为枚举实例  枚举类型名称.valueOf("abc") Constants2.valueOf("abc")
                compareTo() 该方法用于比较两个枚举对象在定义时的顺序  枚举对象.compareTo()        Constants_A.compareTo(Constants_B)
                ordinal()   该方法用于得到枚u举成员的位置索引        枚举对象.ordinal()          Constants_A.ordinal()
                (1)values()
                    枚举类型实例包含一个values()方法，该方法将枚举类型的成员变量实例以数组的形式返回，也可以通过该方法获取枚举类型的成员
                (2)valueOf()与compareTo()
                    枚举类型中静态方法valueOf()可以将普通字符串转换为枚举类型，而compareTo()方法用于比较两个枚举类型对象定义时的顺序。
                    调用compareTo()方法返回的结果，正值代表方法中参数在调用该方法的枚举对象位置之前；0代表两个互相比较的枚举成员的位置相同；负值代表方法中参数在调用该方法的枚举对象位置之后。
                (3)ordinal()
                    枚举类型中的ordinal()方法用于获取某个枚举对象的位置索引值
        枚举类型中的构造方法
            在枚举类型中，可以添加构造方法，但是规定这个构造方法必须为private修饰符所修饰。
            定义个有参构造方法后，需要对枚举类型成员相应地使用该构造方法。然后可以在枚举类型中定义成员变量，在构造方法中为成员变量赋值，这样就可以在枚举类型中定义该成员变量的getXXX()方法了。
    使用枚举类型的优势
        枚举类型声明提供了一种用户友好的变量定义方法，枚举了某种数据类型所有可能出现的点
            类型安全、紧凑有效的数据定义、可以和程序其他部分完美交互、运行效率高

#### 17.2 泛型

    泛型实质上就是使程序员定义安全的类型。在没有出现泛型之前，Java也提供了对Object的引用"任意化"操作，这种"任意化"操作就是对Object引用进行向下转型及向上转型操作，但某些强制类型转换的错误也许不会被编译器捕捉，而在运行后出现异常，可见强制类型转换存在安全隐患，所以在此提供了泛型机制。
    定义泛型类
        Object类为最上层的父类，很多程序员为了使程序更为通用，设计程序时通常使传入的值与返回的值都以Object类型为主。当需要使用这些实例时，必须正确地将该实例转换为原来的类型，否则在运行时将会发生ClassCastException异常。
        在JDK 1.5版本以后，提出了泛型机制。
            类名<T>，其中T代表一个类型的名称
        在类名后添加<T>语句，便使用了泛型机制。使用泛型定义的类在声明该类对象时可以根据不同的需求指定<T>真正的类型，而在使用类中的方法传递或返回数据类型时将不再需要进行类型转换操作，而是使用在声明泛型类对象时"<>"富豪中设置的数据类型
        使用泛型这种形式将不会发生ClassCastException异常，因为在编译器中就可以检查类型匹配是否正确。
        在定义泛型类时，一般类型名称使用T来表达，而容器的元素使用E来表达，具体的设置可以参看JDK 5.0以上版本的API
    泛型的常规用法
        定义泛型类时声明多个类型
            在定义泛型类，可以声明多个类型
                MutiOverClass<T1,T2>
                MutiOverClass:泛型类名称，其中T1和T2为可能被定义的类型
            这样在实例化指定类型的对象时就可以指定多个类型
                MutiOverClass<Boolean,Float>=new MutiOverClass<Boolean,Float>
        定义泛型类时声明数组类型
            定义泛型类时也可以声明数组类型。
            可以在使用泛型机制时声明一个数组，但是不可以使用泛型来建立数组的实例
        集合类声明容器的元素
            可以使用K和V两个字符代表容器中的键值和与键值相对应的具体值
            在Java中许多集合框架已经都被反省话了，可以在主方法中直接使用来创建实例，然后相应调用接口中的方法完成填充容器或根据键名获取集合中具体的功能。常用的被泛型化的集合类
                集合类      泛型定义        集合类        泛型定义
                ArrayList   ArrayList<E>    HashSet     HashSet<E>>
                HashMap     HashMap<K,V>    Vector      Vector<E>
        泛型的高级用法
            泛型的高级用法包括限制泛型可用类型和使用类型通配符等
            限制泛型可用类型
                默认可用使用任何类型来实例化一个泛型对象，但Java中也对泛型类实例的类型作了限制。
                    class 类名称<T extends anyCLass>，anyClass指某个接口或类
                使用泛型限制后，泛型类的类型必须实现或继承了anyClass这个接口或类。无论anyClass是接口还是类，在进行泛型限制时都必须使用extends关键字。
                例如，ArrayList和LinkedList都实现了List接口，而HashMap没有实现List接口，所以在这里不能实例化HashMap类型的泛型对象。
                当没有使用extends关键字限制泛型类型时，默认Object类下的所有子类都可以实例化泛型类对象
            使用类型通配符
                在泛型机制中，提供了类型通配符，其主要作用是在创建一个泛型类对象时限制这个泛型类的类型实现或继承某个接口或类的子类。要声明这样一个对象可以使用"?"通配符来表示，同时使用关键字来对泛型加以限制。
                    泛型类名称<? extends List> a=null;//其中，<? extends List>=表示类型未知，当需要使用该泛型对象时，可以单独实例化。
                除了可以实例化一个限制泛型类型的实例之外，还可以将该实例放置在方法的参数中
                如果使用A<?>这种形式实例化泛型类对象，则默认表示可以将A指定为实例化Object及以下的子类类型。
                使用通配符声明的名称实例化的对象不能对其加入新的信息，只能获取或删除。
                泛型类型限制除了可以向下限制之外，还可以进行向上限制，只要在定义时使用super关键字即可。例如
                    A<? super List>a=null;
                    这样定义后，对象a只接受List接口或上层父类类型，如
                        a=new A<Object>()
            继承泛型类与实现泛型接口
                定义为泛型的类和接口也可以被继承与实现
                如果子类继承父类时保留父类的泛型类型，需要在继承时指明，如果没有指明，直接使用extends ExtendsClass语句进行继承操作，则子类中的T会自动变为Object，所以在一般情况下都将父类的泛型类型保留。
                定义的泛型接口也可以被实现。

### 18 多线程

#### 18.1 线程

    并行在Java中被称为并发，而将并发完成的每一件事情称为线程
    在Java中，并发机制非常重要，但并不是所有的程序语言都支持线程。在以往的程序中，多以一个任务完成后再进行下一个项目的模式开发，这样下一个任务的开始必须等待前一个任务的结束。Java语言提供了并发机制，程序员可以在程序中执行多个线程，每一个线程完成一个功能，并与其他线程并发执行，这种机制被称为多线程。
    Java在每个操作系统中的运行方式也存在差异。Windows操作系统是多任务操作系统，它以进程为单位。一个进程是一个包含有自身地址的程序，每个独立执行的程序都称为进程，也就是正在执行的程序。程序可以分配个每个进程一段有限的使用CPU的时间（可以称为CPU时间片），CPU在这段时间中执行某个进程，然后下一个时间片又跳至另一个进程中去执行。由于CPU转换较快，所以使得每个进程好像是同时执行一样。
    一个线程则是进程中的执行流程，一个进程中可以同时包括多个线程，每个线程也可以得到一小段程序的执行时间，这样一个进程就可以具有多个并发执行的线程。在单线程中，程序代码按调用顺序往下执行，如果需要一个进程同时完成多段代码的操作，就需要产生多线程。

#### 18.2 实现线程的两种方式

    在Java中主要提供两种方式实现线程，分别为继承java.lang.Thread类与实现java.lang.Runnable接口。
    继承Thread类
        Thread类是java.lang包中的一个类，从这个类中实例化的对象代表线程，程序员启动一个新线程需要建立Thread实例。Thread类中常用的两个构造方法如下：
            public Thread()：创建一个新的线程对象
            public Thread(String threadName)：创建一个名称为threadName的线程对象
        继承Thread类创建一个新的线程的语法
            public class ThreadTest extends Thread{
            }
        完成线程真正功能的代码放在类的run()方法中，当一个类继承Thread后，就可以在该类中覆盖run()方法，将实现该线程功能的代码写入run()方法中，然后同时调用Thread类中的start()方法执行线程，也就是调用run()方法。
        Thread对象需要一个任务来执行，任务是指线程在启动时执行的工作，该工作的功能代码被写在run()方法中。run()方法必须使用以下语法格式
            public void run(){
            }
        如果start()方法调用一个已经启动的线程，系统将抛出IllegalThreadStateException异常
        当执行一个线程程序时，就自动产生一个线程，主方法正是在这个线程上运行的。当不再启动其他线程时，该程序就为单线程程序。主方法线程启动由Java虚拟机负责，程序员负责启动自己的线程
            public static void main(String[] args){
                new ThreadTest().start();
            }
        在mian方法中，使线程执行需要调用Thread类中的start()方法，start()方法调用被覆盖之前的run()方法，如果不调用start()方法，线程永远都不会启动，在主方法没有调用start()方法之前，Thread对象只是一个实例，而不是真正的线程。
    实现Runnable接口
        如果程序员需要继承其他类(非Thread类)，而且还要使当前类实现多线程，那么可以通过Runnable接口来实现。例如，一个扩展JFrame类的GUI程序不可能再继承Thread类，因为Java语言中不支持多继承，这时该类就需要实现Runnable接口使其具有使用线程的功能。
            public class Thread extends Object implements Runnable
        实质上Thread类实现了Runnable接口，其中的run()方法正式对Runnable接口中的run()方法的具体实现
        实现Runnable接口的程序会创建一个Thread对象，并将Runnable对象与Thread对象相关联。Thread类中有以下两个构造方法
            public Thread(Runnable target)
            public Thread(Runnable target,String name)
        这两个构造方法的参数中都存在Runnable实例，使用以上构造方法就可以将Runnable实例与Thread实例相关联
        使用Runnable接口启动新的线程的步骤如下
            (1)建立Runnable对象
            (2)使用参数为Runnable对象的构造方法创建Thread实例
            (3)调用start方法启动线程
        通过Runnable接口创建线程时程序员首先需要编写一个实现Runnable接口的类，然后实例化该类的对象，这样就建立了Runnable对象；接下来使用相应的构造方法创建Thread实例；最后使用该实例调用Thread类中的start()方法启动线程。
        线程最引人注目的部分应该是与Swing相结合创建GUI程序。
        启动一个新的线程，不是直接调用Thread子类对象的run()方法，而是调用Thread子类的start()方法，Thread类的start()方法产生一个新的线程，该线程运行Thread子类的run()方法

#### 18.3 线程的生命周期

    线程具有生命周期，其中包含7种状态，分别为出生状态、就绪状态、运行状态、等待状态、休眠状态、阻塞状态和死亡状态。出生状态就是线程被创建时处于的状态，在用户使用该线程实例调用start()方法之前线程都处于出生状态；当用户调用start()方法后，线程处于就绪状态(又被称为可执行状态)；当线程得到系统资源后就进入运行状态。
    一旦线程进入可执行状态，它会在就绪与运行状态下转换，同时也有可能进入等待、休眠、阻塞或死亡状态。当处于运行状态下的线程调用Thread类中的wait()方法时，该线程便进入等待状态，进入等待状态的线程必须调用Thread类中的notify()方法才能被唤醒，而notifyAll()方法是将所有处于等待状态下的线程唤醒：当线程调用Thread类中的sleep()方法时，则会进入休眠状态。如果一个线程在运行状态下发出输入/输出请求，该线程进阻塞状态，在其等待输入/输出结束时线程进入就绪状态，对于阻塞的线程来说，即使系统资源空闲，线程依然不能回到运行状态。当线程的run()方法执行完毕时，线程进入死亡状态
    虽然多线程看起来像同时执行，但事实上在同一时间点上只有一个线程被执行，只是线程之间切换较快，所以才会使人产生线程是同时进行的假象。在Windows操作系统中，系统会为每个线程分配一小段CPU时间片，一旦CPU时间片结束就会将当前线程换为下一个线程，即使该线程没有结束
    使线程处于就绪状态的方法：调用sleep()、wait()方法、等待输入/输出完成
    当线程处于就绪状态后，使线程再次进入运行状态：线程调用notify()、notifyAll()、interrupt()方法、线程的休眠时间结束、输入/输出结束

#### 18.4 操作线程的方法

    操作线程有很多方法，这些方法可以使线程从某一种状态过渡到另一种状态
    线程的休眠
        一种能控制线程行为的方法是调用sleep()方法，sleep()方法需要一个参数用于指定该线程休眠的时间，该时间以毫秒为单位。通常是run()方法内的循环中使用。sleep()方法的语法
            try{
                Thread.sleep(2000);
            }catch(InterruptedException e){
                e.printStackTrace();
            }
        由于sleep()方法的执行有可能抛出InterruptException异常，所以将sleep()方法的调用放在try-catch块中。虽然使用了sleep()方法的线程在一段时间内会醒来，但是并不能保证它醒来后进入运行状态，只能保证它进入就绪状态。
    线程的加入
        如果当前某程序为多线程程序，加入存在一个线程A，现在需要插入线程B，并要求线程B先执行完毕，然后再继续执行线程A，此时可以使用Thread类中的join()方法来完成。
        当某个线程使用join()方法加入到另外一个线程时，另一个线程会等待该线程执行完毕后再继续执行。
    线程的中断
        有的时候会使用stop()方法停止线程，但当前版本的JDK早已废除了stop()方法。不建议使用stop()方法来停止一个线程的运行。更适合再run()方法中使用无限循环的形式，然后使用一个布尔型标记控制循环的停止。
        如果线程是因为是用了sleep()或wait()方法进入了就绪状态，可以使用Thread类中interrupt()方法使线程离开run()方法，同时结束线程，但程序会抛出InterruptedException异常，用户可以在处理该异常时完成线程的中断业务处理，如终止while循环。
    线程的礼让
        Thread类中提供了一种礼让方法，使用yield()方法表示，它只是给当前正处于运行状态的线程一个提醒，告知它可以将资源礼让给其他线程，但这仅仅是一种暗示，没有任何一种机制保证当前线程会将资源礼让。
        yield()方法使具有同样优先级的线程有进入可执行状态的机会，当当前线程放弃执行权时会再度回到就绪状态。对于支持多任务的操作系统来说，不需要调用yield()方法，因为操作系统会为线程自动分配CPU时间片来执行

#### 18.5 线程的优先级

    每个线程都具有各自的优先级，线程的优先级可以表明在程序中该线程的重要性，如果有很多线程处于就绪状态，系统会根据优先级来决定首先使哪个线程进入运行状态。但这并不意味着低优先级的线程得不到运行，而只是它的运行概率比较小，如垃圾回收线程的优先级就较低。
    Thread类中包含的成员变量代表了线程的某些优先级，如Thread.MIN_PRIORITY(常数1)、Thread.MAX_PRIORITY(常数10)、Thread.NORM_PRIORITY(常数5)。其中每个线程的优先级都在Thread.MIN_PRIORITY~Thread.MAX_PRIORITY之间，在默认情况下其优先级都是Thread.NORM_PRIORITY。每个新产生的线程都继承了父线程的优先级。
    在多任务操作系统中，每个线程都会得到一小段CPU时间片运行，在时间结束时，将轮换另一个线程进入运行状态，这时系统会选择与当前线程优先级相同的线程予以运行。系统始终选择就绪状态下优先级较高的线程进入运行状态。
    线程的优先级可以使用setPriority()方法调整，如果使用该方法设置的优先级不在1~10之内，将产生IllegalArgumentException异常

#### 18.6 线程同步

    在单线程程序中，每次只能做一件事情，后面的事情需要等待前面的事情完成后才可以进行，但是如果使用多线程程序，就会发生两个线程抢占资源的问题。所以在多线程编程中需要防止这些资源访问的冲突。Java提供了线程同步的机制来防止资源访问的冲突。
    线程安全
        线程安全问题来源于两个线程同时存取单一对象的数据。
    线程同步机制
        基本上所有解决多线程资源池冲突问题的解决方法都是采用给定时间只允许一个线程访问共享资源，这时就需要给共享资源上一道锁。
        同步块
            在Java中提供了同步机制，可以有效地防止资源冲突。
            将资源放置在同步块中，也称为临界区，使用synchronized关键字
                synchronized(Object){
                }
            通常将共享资源的操作放置在synchronized定义的区域内，这样当其他线程也获取到这个锁时，必须等待锁被释放时才能进入该区域。Object为任意一个对象，每个对象都存在一个标志位，并具有两个值，分别为0和1.一个线程运行到同步块时首先检查该对象的标志位，如果为0状态，表明此同步块中存在其他线程在运行。这时该线程处于就绪状态，直到处于同步块中的线程执行完同步块中的代码为止。这时该对象的标志位被设置为1，该线程才能执行同步块中的代码，并将Object对象的标志位设置为0，防止其他线程执行同步块中的代码。
        同步方法
            同步方法就是在方法前面修饰synchronized关键字的方法
                synchronized void f(){
                }
            当某个对象调用了同步方法时，该对象上的其他同步方法必须等待该同步方法执行完毕后才能被执行。必须将每个能访问共享资源的方法修饰为synchronized，否则就会出错

### 19 网络通信

#### 19.1 网络程序设计基础

    网络程序设计编写的是与其他计算机进行通信的程序。Java已经将网络程序所需要的东西封装成不同的类，用户只需要创建这些类的对象，使用相应的方法，即使不具备有关的网络知识，也可以编写出高质量的网络通信程序。
    局域网与因特网
        为了实现两台计算机的通信，必须用一个网络线路连接两台计算机。
        服务器是指提供信息的计算机或程序，客户机是指请求信息的计算机或程序。网络用于连接服务器与客户机，实现两者之间的相互通信。但有时在某个网络中很难将服务器与客户机区分开。通常所说的局域网(LAN)，就是一群通过一定形式连接起来的计算机。它可以由两台计算机组成，也可以由同一区域内的上千台计算机组成。将LAN延伸到更大的范围，这样的网络成为广域网(WAN)。因特网，就是由无数的LAN和WAN组成的。
    网络协议
        网络协议规定了计算机之间连接的物理、机械(网线与网卡的连接规定)、电气（有效的电平范围）等特征，计算机之间的相互寻址机制，数据发送冲突的解决方式，长数据如何分段传递与接收等内容。
        1、IP协议
            IP是Internet Protocol的简称，是一种网络协议。Internet网络采用的协议是TCP/IP协议，其全称是Transmission Control Protocol/Internet Protocol。Internet依靠TCP/IP协议，在全球范围内实现了不同硬件结构、不同操作系统、不同网络系统之间的互联。在Internet网络上存在着数以亿计的主机，每台主机都用网络为其分配的Internet地址代表自己，这个地址就是IP地址。到目前为止，IP地址用4个字节，也就是32位的二进制数来表示，成为IPv4。为了便于使用，通常取用每个字节的十进制数，并且每个字节之间用圆点隔开来表示IP地址。现在IPv6也投入了使用。
            TCP/IP模式是一种层次结构，共分为4层，分别为应用层、传输层、互联网层和网络层。各层实现特定的功能，提供特定的服务和访问接口，并具有相对的独立性。
                应用程序->可靠的传递服务->无连接分组投递服务->物理层、网络接口层
        2、TCP与UDP协议
            在TCP/IP协议栈中，有两个高级协议是网络应用程序编写者应该了解的，即传输控制协议(TCP)与用户数据报协议(UDP)。
            TCP协议是一种以固接连线为基础的协议，它提供两台计算机间可靠的数据传送。TCP可以保证从一端数据送至连接的另一端时，数据能够确实送达，而且抵达的数据的排列顺序和送出时的顺序相同。因此，TCP协议适合可靠性要求比较高的场合。
            HTTP、FTP和Telnet等需要使用可靠的通信频道。
            UDP是无连接通信协议，不保证数据的可靠传输，但能够向若干个目标发送数据，或接收来自若干个源的数据。UDP以独立发送数据包的方式进行。
            UDP协议适合于一些对数据准确性要求不高，但对传输速度和时效性要求非常高的网站等。这是由于TCP协议在认证上存在额外耗费，可能使传输速度变慢，而UDP协议即使有一小部分数据遗失或传送顺序有所不同，也不会严重危害该项通信。
        一些防火墙和路由器会设置成不允许UDP数据包传输，因此若遇到UDP连接方面的问题，应先确定所在网络是否允许UDP协议。
    端口和套接字
        一般而言，一台计算只有单一的连到网络的物理连接，所有的数据都通过此连接对内、对外送达特定的计算机，这就是端口。网络程序设计中的端口(port)并非真实的物理存在，而是一个假想的连接装置。端口被规定为一个在0~65535之间的整数。HTTP服务一般使用80端口，FTP服务使用21端口。假如一台计算机提供了HTTP、FTP等多种服务，那么客户机会通过不同的端口来确定连接到服务器的哪项服务上。
        通常，0~1023之间的端口数用于一些知名的网络服务和应用，用户的普通网络应该使用1024以上的端口数，以避免端口号与另一个应用或系统服务所用端口冲突。
        网络程序中的套接字(Socket)用于将应用程序与端口连接起来。套接字是一个假想的连接装置，就像插座一样可连接电器与电线。Java将套接字抽象化为类，程序设计值只需创建Socket类对象，即可使用套接字。

#### 19.2 TCP程序设计基础

    TCP网络程序设计是指利用Socket类编写通信程序。利用TCP协议进行通信的两个应用程序是有主次之分的，一个称为服务器程序，另一个称为客户机程序，两者的功能和编写方法大不一样。
    InetAddress类
        java.net包中的InetAddress类是与IP地址相关的类，利用该类可以获取IP地址、主机地址等信息。InetAddress类的常用方法
            getByName(String host)  InetAddress 获取与host相对应的InetAddress对象
            getHostAddress()        String      获取InetAddress对象所包含的IP地址
            getHostName()           String      获取此IP地址的主机名
            getLocalHost()          InetAddress 返回本地主机的InetAddress对象
    InetAddress类的方法会抛出UnknownHostException异常，所以必须进行异常处理。这个异常在主机不存在或网络连接错误时发生。
    ServerSocket类
        java.net包中的ServerSocket类用于表示服务器套接字，其主要功能是等待来自网络上的"请求"，它可通过指定的端口来等待连接的套接字。服务器套接字一次可以与一个套接字连接。如果多台客户机同时提出连接请求，服务器套接字会将请求连接的客户机存入列队中，然后从中取出一个套接字，与服务器新建的套接字连接起来。若请求连接数大于最大容纳数，则多出的连接请求被拒绝。队列的默认大小是50.
        ServerSocket类的构造方法通常会抛出IOException异常，具体有以下几种形式。
            ServerSocket()：创建非绑定服务器套接字
            ServerSocket(int port)：创建绑定到特定端口的服务器套接字
            ServerSocket(int port,int backlog)：利用指定的backlog创建服务器套接字，并将其绑定到指定的本地端口号上。
            ServerSocket(int port,int backlog,InetAddress bindAddress)：使用指定的端口、侦听backlog和要绑定到的本地IP地址创建服务器。这种情况适用于计算机上有多块网卡和多个IP地址的情况，用户可以明确规定ServerSocket在哪块网卡或哪个IP地址上等待客户的连接请求。
        ServerSocket类的常见方法
            accept()            Socket      等待客户机的连接。若连接，则创建一个套接字
            isBound()           boolean     判断ServerSocket的绑定状态
            getInetAddress()    InetAddress 返回此服务器套接字的本地地址
            isClosed()          boolean     返回服务器套接字的关闭状态
            close()             void        关闭服务器套接字
            bind(SocketAddress endpoint)    void    将ServerSocket绑定到特定地址(IP地址和端口号)
            getInetAddress()    int         返回服务器套接字等待的端口号
        调用ServerSocket类的accept()方法，会返回一个和客户端Socket对象和相连接的Socket对象。服务器端的Socket对象使用getOutputStream()方法获得的那个输出流。也就是说，当服务器向输出流写入信息时，客户端通过相应的输入流就能读取，反之亦然。
        accept()方法会阻塞线程的继续执行，直到接收到客户的呼叫。如果没有客户呼叫服务器，那么System.out.println("连接中")语句将不会执行。语句如果没有客户请求，accept()方法没有发生阻塞，肯定是程序出现了问题。通常是使用了一个被其他程序占用的端口号，ServerSocket绑定没有成功。
            yu =server.accept();
            System.out.println("连接中");
    TCP网络程序
        在网络编程中如果只要求客户机向服务器发送消息，不要求服务器向客户机发送消息，称为单向通信。客户机套接字和服务器套接字连接成功后，客户机通过输出流发送数据，服务器则通过输入流接收数据。
        当一台机器上安装了多个网络应用程序时，很可能指定的端口号已被占用。还可能遇到以前运行良好的网络程序突然运行不了的情况，这种情况很可能也是由于端口被别的程序占用了。此时可以运行netstat -help来获得帮助，使用命令netstat -an来查看该程序所使用的端口。

### 19.3 UDP程序设计基础

    用户数据报协议(UDP)是网络信息传输的另一种形式。基于UDP的通信和基于TCP的通信不同，基于UDP的信息传递更快，但不提供可靠的保证。使用UDP传递数据时，用户无法知道数据能否正确地到达主机，也不能确定到达目的地的顺序是否和发送的顺序相同。虽然UDP是一种不可靠的协议，但如果需要较快地传输信息，并能容忍小的错误，可以考虑使用UDP。
    基于UDP通信的基本模式如下
        将数据打包(称为数据包)，然后将数据包发往目的地
        接收别人发来的数据包，然后查看数据包
    发送数据包的步骤如下
        (1)使用DatagramSocket()创建一个数据包套接字
        (2)使用DatagramPacket(byte[] buf,int offset,int length,InetAddress address,int port)创建要发送的数据包
        (3)使用DatagramSocket类的send()方法发送数据包
    接收数据包的步骤如下
        (1)使用DatagramSocket(int port)创建数据包套接字，绑定到指定的端口
        (2)使用DatagramPacket(byte[] buf,int length)创建字节数组来接收数据包
        (3)使用DatagramPacket类的receive()方法接收UDP包
    使用DatagramSocket类的receive()方法接收数据时，如果还没有可以接收的数据，在正常情况下receive()方法将阻塞，一直等到网络上有数据传来，receive()方法接收该数据并返回。如果网络上没有数据发送过来，receive()方法也没有阻塞，肯定是程序有问题，大多数情况下是因为使用了一个被其他程序占用的端口号
    使用DatagramPacket类
        java.net包的DatagramPacket类用来表示数据包。DatagramPacket类的构造函数有
            DatagramPacket(byte[] buf,int length)
            DatagramPacket(byte[] buf,int length,InetAddress address,int port)
        第一种构造函数在创建DatagramPacket对象时，指定了数据包的内存空间和大小。第二种构造函数不仅指定了数据包的内存空间和大小，还指定了数据包的目标地址和端口。在发送数据时，必须指定接收方的Socket地址和端口号，因此使用第二种构造函数可创建发送数据的DatagramPacket对象
    DatagramSocket类
        java.net包中的DatagramSocket类用于表示发送和接收数据包的套接字。该类的构造函数有
            DatagramSocket()
            DatagramSocket(int port)
            DatagramSocket(int port,InetAddress addr)
        第一种构造函数创建DatagramSocket对象，构造数据报套接字，并将其绑定到本地主机任何可用的端口上。第二种构造函数创建DatagramSocket对象，创建数据报套接字，并将其绑定到本地主机的指定端口上。第三种构造函数创建DatagramSocket对象，创建数据报套接字，并将其绑定到指定的本地地址上。第三种构造函数适用于有多块网卡和多个IP地址的情况。
        在接收程序时必须指定一个端口号，不允许系统随机产生，此时可用使用第二种构造函数。
    UDP网络程序
        广播数据报是一项较新的技术，其原理类似于电台广播。广播电台需要在指定的波段和频率上广播信息，收听者也要讲收音机调到指定的波段、频段，才可以听到广播内容。
    发出广播和接收广播的主机地址必须位于同一个组内，地址范围为224.0.0.0~224.255.255.255，该地址并不代表某个特定主机的位置。加入到同一个组的主机可以在某个端口上广播信息，也可以在某个端口上接收信息。

### 20 数据库操作

#### 20.1 数据库基础知识

    数据库在应用程序开发中占据着非常重要的地位。从原来的Sybase数据库，发展到今天的SQL、Server、MySQL、Oracle等高级数据库，整个技术已经相当成熟了。
    数据库
        数据库是一种存储结构，它允许使用各种格式输入、处理和检索数据，不必在每次需要数据时重新输入。数据口具有以下主要特点
            实现数据共享。数据共享包含所有用户可同时存取数据库中的数据，