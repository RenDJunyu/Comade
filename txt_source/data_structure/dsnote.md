# 数据结构

## 第1章 数据结构导论

### 1.3 数据结构起源

    数据结构是一门研究非数值计算的程序设计问题中的操作对象,以及它们之间的关系和操作等相关问题的学科
    1969年美国的高德纳《计算机程序设计艺术》第一卷《基本算法》,较系统地阐述了数据的逻辑结构和存储结构及其操作,开创了数据结构的课程体系

### 1.2 基本概念和术语

    数据:是描述客观事物的符号,是计算机中可以操作的对象,是能被计算机识别,并输入给计算机处理的符号集合
    数据,其实就是符号,具备两个前提
        可以输入到计算机中
        能被计算机程序处理

    数据元素:是组成数据的、有一定意义的基本单位,在计算机中通常作为整体处理.也被称为记录

    数据项:一个数据元素可以由若干个数据项组成
    数据项是数据不可分割的最小单位

    数据对象:是性质相同的数据元素的集合,是数据的子集

    不同数据元素之间不是独立的,而是存在特定的关系,我们将这些元素称为结构
    数据结构:是相互之间存在一种或多种特性关系的数据元素的集合

### 1.3 逻辑结构与物理结构

    逻辑结构:是指数据对象中数据元素之间的相互关系.逻辑结构分为四种:
        集合结构:集合结构中的数据元素除了同属于要给集合外,它们之间没有其他关系
        线性结构:线性结构中的数据元素之间是一对一的关系
        树形结构:树形结构中的数据元素之间存在一种一对多的层次关系
        图形结构:图形结构的数据元素是多对多的关系
    用示意图表示数据的逻辑结构时
        将每个数据结构看作一个结点,用圆圈表示
        元素之间的逻辑关系用结点之间的连线表示,如果这个关系是有方向的,那么带箭头的连线表示

    物理结构:是指数据的逻辑结构在计算机中的存储形式.存储结构形式有两种
        顺序存储结构:是把数据元素存放在地址连续的存储单元里,其数据间的逻辑关系和物理关系是一致的
        链式存储结构:是把数据元素存放在任意的存储单元里,这组存储单元可以是连续的,也可以是不连续的

### 1.4 抽象数据类型

    数据类型:是指一组性质相同的值的集合及定义在此集合上的一些操作的总称
    按照取值的不同,数据类型可以分为两类
        原子类型:是不可以再分解的基本类型,包括整型、实型、字符型等
        结构类型:由若干个类型组合而成,是可以再分解的.例如,整型数组是由若干整型数据组成的
    抽象是指取出事物具有的普遍性的本质

    抽象数据类型(Abstract Data Type,ADT):是指一个数学模型及定义在该模型上的一组操作
    "抽象"的意义在于数据类型的数学抽象特性
    抽象数据类型的标准格式
        ADT 抽象数据类型名
        Data
            数据元素之间逻辑关系的定义
        Operation
            操作1
                初始条件
                操作结果表述
            操作2
                ...
            操作n
                ...
        endADT

## 第2章 算法

### 2.1 算法定义

    算法是解决特定问题求解步骤的描述,在计算机中表现为指令的有限序列,并且每条指令表示一个或多个操作

### 2.2 算法特性

    输入:算法具有零个或多个输入
    输出:算法至少有一个或多个输出
    有穷性:指算法在执行有限的步骤之后,自动结束而不会出现无限循环,并且每一个步骤在可接受的事件内完成
    确定性:算法的每一步骤都具有确定的定义,不会出现二义性
    可行性:算法的每一步都必须是可行的,也就是说,每一步都能够通过执行有限次数完成

### 2.3 算法设计的要求

    正确性:算法的正确性是指算法至少应该具有输入、输出和加工处理无歧义性、能正确反映问题的需求、能够得到问题的正确答案
    在用法上大体分为四个层次
        1、算法程序没有语法错误
        2、算法程序对于合法的输入能够产生满足要求的输出结果
        3、算法程序对于非法的输入能够得出满足规格说明的结果
        4、算法程序对于精心选择的,甚至刁难的测试数据都有满足要求的输出结果
    
    可读性:算法设计的另一目的是为了便于阅读、理解和交流

    健壮性:当输入数据不合法时,算法也能做出相关处理,而不是产生异常或莫名奇妙的结果

    时间效率高和存储量低
    设计算法应该尽量满足时间效率高和存储量低的需求

### 2.4 算法效率的度量方法

    事后统计方法:这种方法主要是通过设计好的测试程序和数据,利用计算机计时器对不同算法编制的程序的运行时间进行比较,从而确定算法效率的高低
    这种方法存在很大的缺陷
        必须依据算法事先编制好程序,这通常需要花费大量的时间和精力
        时间的比较依赖计算机硬件和软件等环境因素,有时会掩盖算法本身的优劣.不同的计算机在处理算法的运算速度上不能进行比较;而所用的操作系统、运行框架等软件的不同,也可以影响结果;同一台机器,CPU使用率和内存占用情况不一样,也会造成细微的差异
        算法的测试数据设计困难,并且程序的运行时间往往还与测试数据的规模有很大的关系,效率高的算法在小的测试数据面前往往还得不到体现.
    
    事前分析估算方法:在计算机程序编制前,依据统计方法对算法进行估算
    一个高级程序语言编写的程序在计算机上运行时所消耗的时间取决于:
        1、算法采用的策略、方法
        2、编译产生的代码质量
        3、问题的输入规模
        4、机器执行指令的速度
    一个程序的运行时间,依赖于算法的好坏和问题的输入规模.问题输入规模是指输入量的多少
    在分析程序的运行时间时,最重要的是把程序看成是独立于程序设计语言的算法或一系列步骤

### 2.5 函数的渐近增长

    函数的渐近增长:给定两个函数f(n)和g(n),如果存在一个整数N,使得对于所有的n>N,f(n)总是比g(n)大,那么,我们说f(n)的增长渐近快于g(n)
    可以忽略这些加法常数,与最高次项相乘的常数并不重要
    最高次项的指数大的,函数随着n的增长,结果也会变得增长特别快
    判断一个算法的效率时,函数中的常数和其他次要项常常可以忽略,而更应该关注主项(最高阶项)的阶数
    某个算法,随着n的增大,它会越来越优于另一算法,或者越来越差于另一算法

### 2.6 算法时间复杂度

    算法时间复杂度定义
        在进行算法分析时,语句总的执行次数T(n)时关于问题规模n的函数,进而分析T(n)随n的变化情况并确定T(n)的数量级.算法的时间复杂度,也就是算法的时间量度,记作:T(n)=O(f(n)).它表示随问题规模n的增大,算法执行时间的增长率和f(n)的增长率相同,称作算法的渐近时间复杂度,简称为时间复杂度.其中f(n)是问题规模n的某个函数
        用大写O()来体现算法时间复杂度的记法,称之为大O记法
    
    推导大O阶方法
        1、用常数1取代运行时间中的所有加法常数
        2、在修改后的运行次数函数中,只保留最高阶项
        3、如果最高阶项存在且不是1,则去除与这个项相乘的常数.得到的结果就是大O阶

    常数阶
        对于分支结构而言,取分支中max{O()}
        但也有进行平均复杂度分析

    线性阶
        分析算法的复杂度,关键就是要分析循环结构的运行情况
    
    对数阶
        含有二分思想的都属于
    
    平方阶
        循环的时间复杂度等于循环体的复杂度乘以该循环运行的次数

### 2.7 常见的时间复杂度

    O(1)        常数阶      O(n)    线性阶
    O(n^2)      平方阶      O(logn) 对数阶
    O(nlogn)    nlogn阶     O(n^3)  立方阶
    O(2^n)      指数阶      O(n!)   阶乘阶

### 2.8 最坏情况与平均情况

    最坏情况运行时间是一种保证,那就是运行时间将不会再坏了.在应用中,这是一种最重要的需求,通常,除非特别指定,提到的运行时间都是最坏情况的运行时间
    平均运行时间是所有情况中最有意义的,因为它是期望的运行时间
    一般在没有特殊说明的情况下,都是指最坏时间复杂度

### 2.9 算法空间复杂度

    算法的空间复杂度通过计算算法所需的储存空间实现,算法空间复杂度的计算公式记作:S(n)=O(f(n)),其中,n为问题的规模,f(n)为语句关于n所占存储空间的函数

## 第3章 线性表

### 3.1 线性表的定义

    线性表(List):零个或多个数据元素的有限序列
    若将线性表记为(a1,...ai-1,ai,ai+1,...,an),则表中ai-1领先于ai,ai领先于ai+i,称ai-1是ai的直接前驱元素,ai+1是ai的直接后继元素.当i=1,2,...,n-1时,ai有且仅有一个直接后继,当i=2,3,...,n时,ai有且仅有一个直接前驱
    线性表元素的个数n(n>=0)定义为线性表的长度,当a=0时,称为空表
    在较复杂的线性表中,一个数据元素可以由若干个数据项组成

### 3.2 线性表的抽象数据类型

    线性表的抽象数据类型定义
        ADT 线性表(List)
        Data
            线性表的数据对象集合为{a1,a2,...,an},每个元素的类型均为DataType.其中,除第一个元素a1外,每一个元素有且只有一个直接前驱元素,除了最后一个元素an外,每一个元素有且只有一个直接后继元素.数据元素之间的关系是一对一的关系
            Operation
                InitList(*L):   初始化操作,建立一个空的线性表L
                ListEmpty(L):   若线性表为空,返回true,否则返回false
                ClearList(*L):  将线性表清空
                GetElem(L,i,*e):将线性表L中的第i个位置元素返回给e
                LocateElem(L,e):在线性表L中查找与给定值e相等的元素,如果查找成功,返回该元素在表中序号表示成功;否则,返回零表示失败
                ListInsert(*L,i,e): 在线性表L中的第i个位置插入新元素e
                ListDelete(*L,i,*e):删除线性表L中第i个位置元素,并用e返回其值
                ListLength(L):  返回线性表L的元素个书
            endADT

### 3.3 线性表的顺序存储结构

    顺序存储定义
        线性表的顺序存储结构,指的是用一段地址连续的存储单元依次存储线性表的数据元素
    
    顺序存储方式
        可以用C语言(其他语言也相同)的一位数组来实现顺序存储结构
        线性表的顺序存储的结构代码
        #define MAXSIZE 20
        typedef int ElemType;
        typedef struct
        {
            ElemType data[MAXSIZE];
            int length;
        }Sqlist;
        顺序存储结构的三个属性
            存储空间的起始位置:数组data,它的存储位置就是存储空间的存储位置
            线性表的最大存储容量:数组长度MAXSIZE
            线性表的当前长度:length

    数据长度与线性表长度区别
        数组长度是存放线性表的存储空间的长度,存储分配后一般不变(动态分配除外)
        线性表的长度是线性表中数据元素的个数,动态变化
        前者≥后者

    地址计算方法
        存储器中的每个存储单元都有自己的编号,这个编号称为地址
            LOC(ai+1)=LOC(ai)+c
            LOC(ai)=LOC(ai)+(i-1)*c

### 3.4 顺序存储结构的插入与删除

    获得元素操作
        #define OK 1
        #define ERROR 0
        #define TRUE 1
        #define FALSE 0
        typedef int Status
        Status GetElem(SqList L,int i,ElemType *e)
        {
            if(L.length==0||i<1||i>L.length)
                return ERROR
            *e=L.data[i-1];
            return OK;
        }
    
    插入操作
        插入算法的思路
            如果插入位置不合理,抛出异常
            如果线性表长度大于等于数组长度,则抛出异常或动态增加容量
            从最后一个元素开始向前遍历到第i个位置,分别将它们都向后移动一个位置
            将要插入元素填入位置i处
            表长加1
        Status ListInsert(SqList *L,int i,ElemType e)
        {
            int k;
            if(L->Length==MAXSIZE)
                return ERROR;
            if(i<1||i>L->Length+1)
                return ERROR;
            if(i<=L->length)
            {
                for(k=L->length-1;k>=i-1;k--)
                    L->data[k+1]=L->data[k];
            }
            L->data[i-1]=e;
            L->length++;
            return OK;
        }

    删除操作
        删除算法的思路
            如果删除位置不合理,抛出异常
            取出删除元素
            从删除元素位置开始遍历到最后一个元素位置,分别将它们都向前移动一个位置
            表长减1
        Status ListDelete(SqList *L,int i,ElemType *e)
        {
            int k;
            if(L->length==0)
                return ERROR;
            if(i<1||i>L->length)
                return ERROR;
            *e=L->data[i-1];
            if(i<L->length)
            {
                for(k=i;k<L->length;k++)
                    L->data[k-1]=L->data[k];
            }
            L->length--;
            return OK;
        }
    
    线性表顺序存储结构的优缺点
        优点
            无须为表示表中元素之间的逻辑关系而增加额外的存储空间
            可以快速地存取表中任一位置的元素
        缺点
            插入和删除操作需要移动大量元素
            当线性表长度变化较大时,难以确定存储空间的容量
            造成存储空间的"碎片"

### 3.5 线性表的链式存储结构

    顺序存储结构不足的解决办法
        链式存储结构
    
    线性表链式存储结构定义
        为了表示每个数据元素ai与其直接后继数据元素ai+1之间的逻辑关系,对数据元素ai来说,除了存储其本身的信息之外,还需存储一个指示其直接后继的信息(即直接后继的存储位置).把存储数据元素信息的域成为数据域,把存储直接后继位置的域称为指针域.指针域中存储的信息称作指针或链.这来国内部分信息组成数据元素ai的存储映像,称为结点(Node)
        n个结点(ai的存储映像)链结成一个链表,即为线性表(a1,a2,...,an)的链式存储结构,因为此链表的每个结点中只包含一个指针域,所以叫做单链表
        链表中的第一个结点的存储位置叫做头指针
        为了更加方便地对链表进行操作,会在单链表的第一个结点前附设一个结点,称为头结点

    头指针与头结点的异同
        头指针
            头指针是指链表指向第一个结点的指针,若链表有头结点,则是指向头结点的指针
            头指针具有标识作用,所以常用头指针冠以链表的名字
            无论链表是否为空,头指针均不为空.头指针是链表的必要元素
        头结点
            头结点是为了操作的统一和方便而设立的,放在第一元素的结点之前,其数据域一般无意义(也可存放链表的长度)
            有了头结点,对在第一元素结点前插入结点和删除第一结点,其操作与其他结点的操作就统一了
            头结点不一定是链表必须要素

    线性表链式存储结构代码描述
        线性表为空表,则头结点的指针域为"空"
        在C语言中可用结构指针来描述
            typedef struct Node
            {
                ElemType data;
                struct Node *next;
            }Node;
            typedef struct Node *LinkList;
        结点由存放数据元素的数据域存放后继结点地址的指针域组成

### 3.6 单链表的读取

    获得链表第i个数据的算法思路
        1、声明一个结点p指向链表第一个结点,初始化j从1开始
        2、当j<i时,就遍历链表,让p的指针向后移动,不断指向下一结点,j累加1
        3、若到链表末尾p为空,则说明第i个元素不存在
        4、否则查找成功,返回结点p的数据
    Status GetElem(LinkList L,int i,ElemType *e)
    {
        int j;
        LinkList p;
        p=L->next;
        j=1;
        while(p&&j<i)
        {
            p=p->next;
            ++j;
        }
        if(!p||j>i)
            return ERROR;
        *e=p->data;
        return OK;
    }
    主要核心思想是"工作指针后移"

### 3.7 单链表的插入与删除

    单链表的插入
        s->next=p->next;
        p->next=s;
        单链表第i个数据插入结点的算法思路
            1、声明一结点p指向链表第一个节点,初始化j从1开始
            2、当j<i时,就遍历链表,让p的指针向后移动,不断指向下一结点,j累加1
            3、若到链表末尾p为空,则说明第i个元素不存在
            4、否则查找成功,在系统中生成一个空结点s
            5、将数据元素e赋值给s->data
            6、单链表的插入标准语句s->next=p->next;p->next=s;
            7、返回成功
        Status ListInsert(LinkList *L,int i,ElemType e)
        {
            int j;
            LinkList p,s;
            p=*L;
            j=l;
            while(p&&j<i)
            {
                p=p->next;
                ++j;
            }
            if(!p||j>i)
                return ERROR;
            s=(LinkList)malloc(sizeof(Node));
            s->data=e;
            s->next=p->next;
            p->next=s;
            return OK;
        }

    单链表的删除
        q=p->next;
        p->next=q->next;
        单链表第i个数据删除结点的算法思路
            1、声明一结点p指向链表第一个结点,初始化j从1开始
            2、当j<i时,就遍历链表,让p的指针向后移动,不断指向下一个结点,j累加1
            3、若到链表末尾p为空,则说明第i个元素不存在
            4、否则查找成功,将欲删除的结点p->next赋值给q
            5、单链表的删除标准语句p->next=q->next
            6、将q结点中的数据赋值给e,作为返回
            7、释放q结点
            8、返回成功
        Status ListDelete(LinkList *L,int i,ElemType *e)
        {
            int j;
            LinkList p,q;
            p=*L;
            j=l;
            while(p->next&&j<i)
            {
                p=p->next;
                ++j;
            }
            if(!(p->next)||j>i)
                return ERROR;
            q=p->next;
            p->next=q->next;
            *e=q->data;
            free(q);
            return OK;
        }
    
    对于插入或删除数据越频繁的操作,单链表的效率优势就越是明显

### 3.8 单链表的整表创建

    单链表整表创建的算法思路
        1、声明一结点p和计数器变量i
        2、初始化一空链表L
        3、让L的头结点的指针指向NULL,即建立一个带头结点的单链表
        4、循环
            生成一新结点赋值给p
            随机生成一数字赋值给p的数据域p->data
            将p插入到头结点与前一新结点之间
        void CreateListHead(LinkList *L,int n)
        {
            LinkList p;
            int i;
            srand(time(0));
            *L=(LinkList)malloc(sizeof(Node));
            (*L)->next=NULL;
            for(i=0;i<n;i++)
            {
                p=(LinkList)malloc(sizeof(Node));
                p->data=rand()%100+1;
                p->next=(*L)->next;
                (*L)->next=p;
            }
        }//头插法
        void CreateListTail(LinkList *L,int n)
        {
            LinkList p,r;
            int i;
            srand(time(0));
            *L=(LinkList)malloc(sizeof(Node));
            r=*L;
            for(i=0;i<n;i++)
            {
                p=(Node *)malloc(sizeof(Node));
                p->data=rand()%100+1;
                r->next=p;
                r=p;
            }
            r->next=NULL;
        }//尾插法

### 3.9 单链表的整表删除

    单链表整表删除的算法思路
        1、声明一结点p和q
        2、将第一个结点赋值给p
        3、循环
            将下一结点赋值给q
            释放p
            将q赋值给p
    Status ClearList(LinkList *L)
    {
        LinkList p,q;
        p=(*L)->next;
        while(p)
        {
            q=p->next;
            free(p);
            p=q;
        }
        (*L)->next=NULL;
        return OK;
    }

### 3.10 单链表结构与顺序存储结构优缺点

    储存分配方式
        顺序存储结构用一段连续的存储单元依次存储线性表的数据元素
        单链表采用链式存储结构,用一组任意的存储单元存放线性表的元素
    时间性能
        查找
            顺序存储结构O(1)
            单链表O(n)
        插入和删除
            顺序存储结构需要平均移动表长一半的元素,时间为O(n)
            单链表在找出某位置的指针后,插入和删除时间仅为O(1)
        空间性能
            顺序存储结构需要预分配存储空间,分大了浪费,分小了易发生上溢
            单链表不需要分配存储空间,只要有就可以分配,元素个数也不受限制
        
    若线性表需要频繁查找,很少进行插入和删除操作时,宜采用顺序存储结构.若需要频繁插入和删除时,宜采用单链表结构
    当线性表中的元素个数变化较大或者根本不知道有多大时,最好用单链表结构,这样可以不需要考虑存储空间的大小问题

### 3.11 静态链表

    用数组描述的链表叫做静态链表,这种描述方法还有起名叫做游标实现法
    #define MAXSIZE 1000
    typedef struct
    {
        ELemType data;
        int cur;
    }Component,StaticLinkList{MAXSIZE};
    初始化数组
    Status InitList(StaticLinkList space)
    {
        int i;
        for(i=0;i<MAXSIZE-1;i++)
            space[i].cur=i+1;
        space[MAXSIZE-1].cur=0;
        return OK;
    }

    静态链表的插入操作
        获取备用空间链表中非空的结点下标
            int Malloc_SLL(StaticLinkList space)
            {
                int i=space[0].cur;
                if(space[0].cur)
                    space[0].cur=space[i].cur;
                return i;
            }
        插入数据元素
            Status ListInsert(StaticLinkList L,int i,ElemType e)
            {
                int j,k,l;
                k=MAX_SIZE=1;
                if(i<1||i>ListLength(L)+1)
                    return ERROR;
                j=Malloc_SSL(L);
                if(j)
                {
                    L[j].data=e;
                    for(l=1;l<=i-1;l++)
                        k=L[k].cur;
                    L[j].cur=L[k].cur;
                    L[k].cur=j;
                    return OK;
                }
                return ERROR;
            }
    
    静态链表的删除操作
        删除元素
            Status ListDelete(StaticLinkList L,int i)
            {
                int j,k;
                if(i<1||i>ListLength(L))
                    return ERROR;
                k=MAX_SIZE-1;
                for(j=1;j<=i-1;j++)
                    k=L[k].cur;
                j=L[k].cur;
                L[k].cur=L[j].cur;
                Free_SSL(L,j);
                return OK;
            }
        将空闲结点回收到备用链表
            void Free_SSL(StaticLinkList space,int k)
            {
                space[k].cur=space[0].cur;
                space[0].cur=k;
            }
        获得数据元素的个数
            int ListLength(StaticLinkList L)
            {
                int j=0;
                int i=L[MAXSIZE-1].cur;
                while(i)
                {
                    i=L[i].cur;
                    j++;
                }
                return j;
            }
    
    静态链表优缺点
        优点
            在插入和删除操作时,只需要修改游标,不需要移动元素,从而改进了在顺序存储结构中的插入和删除操作需要移动大量元素的缺点
        缺点
            没有解决连续存储分配带来的表长难以确定的问题
            失去了顺序存储结构随机存储的特性

### 3.12 循环链表

    将单链表中终端结点的指针端由空指针改为指向头结点,就使整个单链表形成一个环,这种头尾相接的单链表称为单循环链表,简称循环链表(circular linked list)
        p=rearA->next;
        rearA->next=rearB->next->next;
        rearB->next=p;
        free(p);

### 3.13 双向链表

    双向链表(double linked list)是在单链表的每个结点中,再设置一个指向其前驱结点的指针域.
        typedef struct DulNode
        {
            ElemType data;
            struct DuLNode *prior;
            struct DuLNode *next;
        }DulNode,*DuLinkList;
        p->next->prior=p=p->prior->next;
        插入数据元素
            s->prior=p;
            s->next=p->next;
            p->next->prior=s;
            p->next=s;
        删除数据元素
            p->prior->next=p->next;
            p->next->prior=p->prior;
            free(p);

## 第4章 栈与队列

### 4.1 栈的定义

    栈的定义:栈(stack)是限定仅在表尾进行插入和删除操作的线性表
    把允许插入和删除的一端称为栈顶(top),另一端称为栈底(bottom),不含任何数据元素的栈称为空栈.栈又称为后进先出(Last In First Out)的线性表,简称LIFO结构
    栈的插入操作,叫做进栈,也称压栈、入栈
    栈的删除操作,叫做出栈,也有的叫做弹栈

    进栈出栈变化形式
        栈对线性表的插入和删除的位置进行了限制,并没有对元素的进出的时间进行限制

### 4.2 栈的抽象数据类型

    插入和删除改名为push和pop
    ADT 栈(stack)
    Data
        同线性表.元素具有相同类型,相邻元素具有前驱和后继关系
    Operation
        InitStack(*S):初始化操作,建立一个空栈S
        DestroyStack(*S):若栈存在,则销毁它
        ClearStack(*S):将栈清空
        StackEmpty(S):若栈为空,返回true,否则返回false
        GetTop(S,*e):若栈存在且非空,用e返回S的栈顶元素
        Push(*S,e):若栈S存在,插入新元素e到栈S中并成为栈顶元素
        Pop(*S,*e):删除栈S中栈顶元素,并用e返回其值
        StackLength(S):返回栈S的元素个数
    endADT

### 4.3 栈的顺序存储结构及实现

    栈的顺序存储结构
        栈的结构定义
            typedef int SElemType;
            typedef struct
            {
                SElemType data[MAXSIZE];
                int top;
            }Sqstack;

    栈的顺序存储结构——进栈操作
        Status Push(SqStack *S,SElemType e)
        {
            if(S->top==MAXSIZE-1)
            {
                return ERROR;
            }
            S->top++;
            S->data[S->top]=e;
            return OK;
        }
    
    栈的顺序存储结构——出栈操作
        Status Pop(SqStack *S,SElemType *e)
        {
            if(S->top==-1)
                return ERROR;
            *e=S->data[S->top];
            S->top--;
            return OK;
        }

### 4.5 两栈共享空间

    结构代码
        typedef struct
        {
            SElemType data[MAXSIZE];
            int top1;
            int top2;
        }SqDoubleStack;
    插入元素
        Status Push(SqDoubleStack *S,SElemType e,int stackNumber)
        {
            if(S->top1+1==S->top2)
                return ERROR;
            if(stackNumber==1)
                S->data[++S->top1]=e;
            else if(stackNumber==2)
                S->data[--S->top2]=e;
            return OK;
        }
    删除元素
        Status Pop(SqDoubleStack *S,SElemType *e,int stackNumber)
        {
            if(stackNumber==1)
            {
                if(S->top1==-1)
                    return ERROR;
                *e=S->data[S->top1--];
            }
            else if(stackNumber==2)
            {
                if(S->top2==MAXSIZE)
                    return ERROR;
                *e=S->data[S->top2++];
            }
            return OK;
        }

### 4.5 栈的链式存储结构及实现

    栈的链式存储结构
        简称为链栈
        typedef struct StackNode
        {
            SElemType data;
            struct StackNode *next;
        }StackNode,*LinkStackPtr;
        typedef struct LinkStack
        {
            LinkStackPtr top;
            int count;
        }LinkStack;
    
    栈的链式存储结构——进栈操作
        Status Push(LinkStack *S,SElemType e)
        {
            LinkStackPtr s=(LinkStackPtr)malloc(sizeof(StackNode));
            s->data=e;
            s->next=S->top;
            S->top=s;
            S->count++;
            return OK;
        }
    
    栈的链式存储结构——出栈操作
        Status Pop(LinkStack *S,SElemType *e)
        {
            LinkStackPtr p;
            if(StackEmpty(*S))
                return ERROR;
            *e=S->top->data;
            p=S->top;
            S->top=S->top->next;
            free(p);
            S->count--;
            return OK;
        }
    
    如果栈的使用过程中元素变化不可预料,有时很小,有时非常大,那么最好是用栈,反之,如果它的变化在可控范围内,建议使用顺序栈会更好一些

### 4.6 栈的作用

    栈的引入简化了程序设计的问题,划分了不同关注层次,使得思考范围缩小,更加聚焦与要解决的问题核心.

### 4.7 栈的应用——递归

    斐波那契数列实现
    递归定义
        把一个直接调用自己或通过一系列的调用语句间接地调用自己的函数,称作递归函数
        每个递归定义必须至少有一个条件,满足时递归不再进行,即不再引用自身而是返回值退出

### 4.8 栈的应用——四则运算表法式求值

    后缀(逆波兰)表示法定义
        一种不需要括号的后缀表达法,也把它称为逆波兰(Reverse Polish Notation,RPN)表示
        后缀表达式,所有的符号都是要在运算数字后面出现

    后缀表达式计算结果
        规则:从左到右遍历表达式的每个数字和符号,遇到是数字就进栈,遇到是符号,就将处于栈顶的两个数字出栈,进行运算,运算结果进栈,一直到最终获得结果
    
    中缀表达式转后缀表达式
        标准四则运算表法式,叫做中缀表达式
        规则:从左到右遍历中缀表达式的每个数字和符号,若是数字就输出,即成为后缀表达式的一部分;若是符号,则判断其与栈顶符号的优先级,是右括号或优先级低于栈顶符号的(乘除优先加减)则栈顶元素依次出栈并输出,并将当前符号进栈,一直到最终输出后缀表达式为止

### 4.9 队列的定义

    队列(queue)是只允许在一端进行插入操作,而在另一端进行删除操作的线性表
    队列是一种先进先出(First In First Out)的线性表,简称FIFO.允许插入的一端称为队尾,允许删除的一端称为队头.

### 4.10 队列的抽象数据类型

    ADT 队列(Queue)
    Data
        同线性表.元素具有相同的类型,相邻元素具有前驱和后继关系
    Operation
        InitQueue(*Q):      初始化操作,建立一个空队列Q
        DestroyQueue(*Q):   若队列Q存在,则销毁他
        ClearQueue(*Q):     若队列Q清空
        QueueEmpty(Q):      若队列Q为空,返回true,否则返回false
        GetHead(Q,*e):      若队列Q存在且非空,用e返队列Q的队头元素
        EnQueue(*Q,e):      若队列Q存在,插入新元素e到队列Q中并成为队尾元素
        DeQueue(*Q,*e):     删除队列Q中的队头元素,并用e返回其值
        QueueLength(Q):     返回队列Q的元素个数

### 4.11 循环队列

    队列顺序存储的不足
        队列元素的出列是在队头,时间复杂度为O(n)
    循环队列定义
        把队列的这种头尾相接的顺序存储结构称为循环队列
        队列满的条件是(rear+1)%QueueSize==front
        通用的计算队列长度公式为:
            (rear-front+QueueSize)%QueueSize
    循环队列的顺序存储结构代码
        typedef int QElemType;
        typedef struct
        {
            QElemType data[MAXSIZE];
            int front;
            int rear;
        }
    循环队列的初始化
        Status InitQueue(SqQueue *Q)
        {
            Q->front=0;
            Q->rear=0;
            return OK;
        }
    循环队列求队列长度
        int QueueLength(SqQueue Q)
        {
            return (Q.rear-Q.front+MAXSIZE)%MAXSIZE;
        }
    循环队列的入队列操作
        Status EnQueue(SqQueue *Q,QElemType e)
        {
            if((Q->rear+1)%MAXSIZE==Q->front)
                return ERROR;
            Q->data[Q->rear]=e;
            Q->rear=(Q->rear+1)%MAXSIZE;
            return OK;
        }
    循环队列的出队列操作
        Status DeQueue(SqQueue *Q,QElemType *e)
        {
            if(Q->front==Q->rear)
                return ERROR;
                *e=Q->data[Q->front];
                Q->front=(Q->front+q)%MAXSIZE;
                return OK;
        }

### 4.12 队列的链式存储结构及实现

    队列的链式存储结构,其实就是线性表的单链表,只不过是它只能尾进头出而已,我们把它简称为链队列
        typedef int QElemType;
        typedef struct QNode;
        {
            QElemType data;
            struct QNode *next;
        }QNode,*QueuePtr;
        typedef struct
        {
            QueuePtr front,rear;
        }LinkQueue;
    
    队列的链式存储结构——入队操作
        Status EnQueue(LinkQueue *Q,QElemType e)
        {
            QueuePtr s=(QueuePtr)malloc(sizeof(QNode));
            if(!s)
                exit(OVERFLOW);
            s->data=e;
            s->next=NULL;
            Q->rear->next=s;
            Q->rear=s;
            return OK;
        }
    
    队列的链式存储结构——出队操作
        Status DeQueue(LinkQueue *Q,QElemType *e)
        {
            QueuePtr p;
            if(Q->front==Q->rear)
                return ERROR;
            p=Q->front->next;
            *e=p->data;
            Q->front->next=p->next;
            if(Q->rear==p)
                Q->rear=Q->front;
            free(p);
            return OK;
        }

## 第5章 串

### 5.1 开场白

    宋代 李禺
        枯眼遥望山隔水,往来曾见几心知?
        壶空怕酌一杯酒,笔下难成和韵诗?
        途路阻人离别久,讯音无雁寄回迟.
        孤灯夜守长寥寂,夫忆妻兮父忆儿.
    也是一首回文诗

### 5.2 串的定义

    串(string)是由零个或多个字符组成的有限序列,又名叫字符串
    一般记为s="a1a2...an"(n>0)
    串中的字符数目n称为串的长度
    零个字符的串称为空串(null string),""或者Φ
    空格串,是只包含空格的串.注意与空串的区别,空格串是有内容有长度的,而且可以不止一个空格
    子串与主串,串中任意个数的连续字符组成的子序列称为该串的子串,包含子串的串称为主串
    子串在主串中的位置就是子串的第一个字符在主串中的序号

### 5.3 串的比较

    串的比较是通过组成串的字符之间的编码来进行的,而字符的编码指的是字符在对应字符集中的序号
    计算机中的常用字符是使用标准的ASCII编码,更精准一点,由7位二进制表示一个字符,总共可以表示128个字符.后来发现一些特殊符号的出现,128个不够用,于是扩展ASCII码由8位二进制数表示一个字符,总共可以表示256个字符,这已经足够满足以英语为主的语言和特殊符号进行输入、存储、输出等操作的字符需要了.为满足全世界的语言和文字,使用Unicode编码,比较常用的是由16位的二进制数表示一个字符,总共可以表示216个字符,约是65万多个字符.为了和ASCII码兼容,Unicode的前256个字符与ASCII码完全相同
    给定两个串:s="a1a2...an",t="b1b2...bm",当满足一下条件之一时,s<t
        1.n<m,且ai=bi(i=1,2,...,n)
        2.存在某个k≤min(m,n),使得ai=bi(i=1,2,...,k-1),ak<bk

### 5.4 串的抽象数据类型

    ADT 串(string)
    Data
        串中元素仅有一个字符组成,相邻元素具有前驱和后继关系
    Operation
        StrAssign(T,*chars):生成一个其值等于字符串常量chars的串T
        StrCopy(T,S):串S存在,由串S复制得串T
        ClearString(S):串S存在,将串清空
        StringEmpty(S):若串S为空,返回true,否则返回false
        StrLength(S):返回串S的元素个数,即串的长度
        StrCompare(S,T):若S>T,返回值>0,若S=T,返回0,若S<T,返回值<0
        Concat(T,S1,S2):用T返回由S1和S2联接而成的新串
        SubString(Sub,S,pos,len):串S存在,1≤pos≤StrLength(S),且0≤len≤StrLength(S)-pos+1,用Sub返回串S的第pos个字符起长度为len的子串
        Index(S,T,pos):串S和T存在,T是非空串,1≤pos≤StrLength(S).若主串S中存在和串T值相同的子串,则返回它在主串S中第pos个字符之后第一次出现的位置,否则返回0
        Replace(S,T,V):串S、T和V存在,T是非空串.用V替换主串S中出现的所有与T相等的不重叠的子串
        StrInsert(S,pos,T):串S和T存在,1≤pos≤StrLength(S)+1.在串S的第pos个字符之前插入串T
        StrDelete(S,pos,len):串S存在,1≤pos≤StrLength(S)-len+1.从串S中删除第pos个字符起长度为len的子串
    endADT
    在C#中,字符串操作还有ToLower转小写、ToUpper转大写、IndexOf从左查找子串位置(操作名有修改)、LastIndexOf从右、Trim去除两边空格等比较方便的操作
        int Index(String S,String T,int pos)
        {
            int n,m,i;
            String sub;
            if(pos>0)
            {
                n=StrLength(S);
                m=StrLength(T);
                i=pos;
                while(i<=n-m+1)
                {
                    SubString(sub,S,i,m);
                    if(StrCompare(sub,T)!=0)
                        ++i;
                    else
                        return i;
                }
            }
            return 0;
        }

### 5.5 串的存储结构

    串的顺序存储结构
        用一组地址连续的存储单元来存储串中的字符序列
    串的链式存储结构
        一个结点对应一个字符会存在很大的空间浪费,可以考虑存在多个字符

### 5.6 朴素的模式匹配算法

    子串的定位操作通常称作串的模式匹配
        int Index(String S,String T,int pos)
        {
            int i=pos;
            int j=1;
            while(i<=S[0]&&j<=T[0])
            {
                if(S[i]==T[j])
                {
                    ++i;
                    ++j;
                }
                else
                {
                    i=i-j+2;
                    j=1;
                }
            }
            if(j>T[0])
                return i-T[0];
            else
                return 0;
        }

### 5.7 KMP模式匹配算法

    一个模式匹配算法,可以大大避免重复遍历的情况,我们把它称之为克努特——莫里斯——普拉特算法,简称KMP算法

    KMP模式匹配算法原理
        KMP模式匹配算法就是为了让没必要的回溯不发生
                {0,当j=1时}
        next[j]={Max{k|1<k<j,且'p1...k-1'='pj-k+1...pj-1'}当此集合不空时}
                {1,其他情况}
    
    next数组值推导
        返回子串T的next数组
            void get_next(String T,int *next)
            {
                int i,j;
                i=1;
                j=0;
                next[1]=0;
                while(i<T[0])
                {
                    if(j==0||T[i]==T[j])
                    {
                        ++i;
                        ++j;
                        next[i]=j;
                    }
                    else
                        j=next[j];
                }
            }
        返回子串T在主串S中第pos个字符之后的位置
            int Index_KMP(String S,String T,int pos)
            {
                int i=pos;
                int j=1;
                int next[255];
                get_next(T,next);
                while(i<=S[0]&&j<=T[0])
                {
                    if(j==0||S[i]==T[j])
                    {
                        ++i;
                        ++j;
                    }
                    else
                    {
                        j=next[j];
                    }

                }
                if(j>T[0])
                    return i-T[0];
                else
                    return 0;
            }
    
    KMP模式匹配算法改进
        void get_nextval(String T,int *nextval)
        {
            int i,j;
            i=1;
            j=0;
            nextval[1]=0;
            while(i<T[0])
            {
                if(j==0||T[i]==T[j])
                {
                    ++i;
                    ++j;
                    if(T[i]!=T[j])
                        nextval[i]=j;
                    else
                        nextval[i]=nextval[j];
                }
                else
                    j=nextval[j];
            }
        }

    nextval数组值推导
        根据next[j]可以直接换算

## 第6章 树

### 6.1 树的定义

    树(Tree)是n(n≥0)个结点的有限集.n=0时称为空树.在任意一颗非空树中:有且仅有一个特定的称为根(Root)的结点;(2)当n>1时,其余节点可分为m(m>0)个互不相交的有限集T1、T2、...、Tm,其中每一个集合本身又是一棵树,并且称为根的子树(SubTree)
        1、n>0时根结点是唯一的,不可能存在多个根节点
        2、m>0时,子树的个数没有限制,但它们一定是互不相交的

    结点分类
        结点拥有的子树数称为结点的度(Degree).度为0的结点称为叶结点(Leaf)或终端结点;度不为0的结点称为非终端结点或分支结点.除根节点之外,分支结点也称为内部结点.树的度是树内部各结点的度的最大值
    
    结点间关系
        结点的子树的根称为该结点的孩子(Child),相应地,该结点称为孩子的双亲(Parent).同一个双亲的孩子之间互称兄弟(Sibling).结点的祖先是从根到该结点所经分支上的所有结点.以某结点为根的子树中的任一结点都称为该结点的子孙
    
    树的其他相关概念
        结点的层次(Level)从根开始定义起,根为第一层,根的孩子为第二层.双亲在同一层的结点互为堂兄弟.树中结点的最大层次称为树的深度(Depth)或高度
        如果将树中结点的各子树看成从左至右是有次序的,不能互换的,则称该树为有序树,否则称为无序树
        森林(Forest)是m(m≥0)棵互不相交的树的集合

### 6.2 树的抽象数据类型

    ADT 树(Tree)
    Data
        树是由一个根节点和若干棵子树构成.树中结点具有相同的数据类型及层次关系
    Operation
        InitTree(*T):构造空树T
        DestroyTree(*T):销毁树T
        CreateTree(*T,definition):按definition中给出树的定义来构造树
        ClearTree(*T):若树存在,则将树T清为空树
        TreeEmpty(T):若T为空树,返回True,否则返回false
        TreeDepth(T):返回T的深度
        Root(T):返回T的根节点
        Value(T,cur_e):cur_e是树T中一个结点,返回此结点的值
        Assign(T,cur_e,value):给树T的结点cur_e赋值为value
        Parent(T,cur_e):若cur_e是树T的非根节点,则返回它的双亲,否则返回空
        LeftChild(T,cur_e):若cur_e是树T的非叶结点,则返回它的最左孩子,否则返回空
        RightSibling(T,cur_e):若cur_e有右兄弟,则返回它的右兄弟,否则返回空
        InsertChild(*T,*p,i,c):其中p指向树T的某个结点,i为所指结点p的度加上1,非空树c与T不相交,操作结果为插入c为树T中所指结点的第i棵子树
        DeleteChild(*T,*p,i):其中p指向树T的某个结点,i为所致结点p的度,操作结果为删除T中p所指结点的第i棵子树
    endADT

### 6.3 树的存储结构

    双亲表示法
        在每个结点中,附设一个指示器特指其双亲结点到链表中的位置
        #define MAX_TREE_SIZE 100
        typedef int TElemType;
        typedef struct PTNode
        {
            TElemType data;
            int parent;
        }PTNode;
        typedef struct
        {
            PTNode nodes[MAX_TREE_SIZE];
            int r,n;
        }PTree;
        存储结构的设计是一个非常灵活的过程.一个存储结构设计的是否合理,取决与基于该存储结构的运算是否适合、是否方便,时间复杂度好不好等

    孩子表示法
        每个结点有多个指针域,其中每个指针指向一颗子树的根结点,把这种方法叫做多重链表表示法
        方案一:指针域的个数等于树的度
        方案二:每个结点指针域的个数等于该结点的度
        把每个结点的孩子结点排列起来,以单链表作存储结构,则n个结点有n个孩子链表,如果是叶子结点则此但链表为空.然后n个头指针又组成一个线性表,采用顺序存储结构,存放进一个一维数组中
            #define MAX_TREE_SIZE 100
            typedef struct CTNode
            {
                int child;
                struct CTNode *next;
            }*ChildPtr;
            typedef struct
            {
                TElemType data;
                ChildPtr firstchild;
            }CTBox;
            typedef struct
            {
                CTBox nodes[MAX_TREE_SIZE];
                int r,n;
            }CTree;

    孩子兄弟表示法
        任意一棵树,它的结点的第一个孩子如果存在就是唯一的,它的右兄弟如果存在也是唯一的.设置两个指针,分别指向该结点的第一个孩子和此结点的右兄弟
            typedef struct CSNode
            {
                TElemType data;
                struct CSNode *firstchild,*rightsib;
            }CSNode,*CSTree;

### 6.4 二叉树的定义

    二叉树(Binary Tree)是n(n≥0)个结点的有限集合,该集合或者为空集(称为空二叉树),或者由一个根结点和两颗互不相交的、分别称为根结点的左子树和右子树的二叉树组成

    二叉树的特点
        每个结点最多有两颗子树,在二叉树中不存在度大于2的结点
        左子树和右子树是有顺序的,次序不能任意颠倒
        即使树中某结点只有一颗子树,也要区分它是左子树还是右子树
        二叉树具有五种基本形态
            空二叉树
            只有一个根结点
            根结点只有左子树
            根结点只有右子树
            根节点既有左子树又有右子树
    
    特殊二叉树
        斜树:所有的结点都只有左子树的二叉树叫左斜树.所有的结点都只有右子树的二叉树叫右斜树.这两者统称为斜树
        满二叉树:在一棵二叉树中,如果所有分支结点都存在左子树和右子树,并且所有叶子都在同一层上,这样的二叉树称为满二叉树
            特点:
                叶子只能出现在最下一层
                非叶子结点的度一定是2
                在同样深度的二叉树中,满二叉树的结点个数最多,叶子数最多
        完全二叉树:对一颗具有n个结点的二叉树按层序编号,如果i(1≤i≤n)的结点与同样深度的满二叉树中编号为i的结点在二叉树中位置完全相同,则这颗二叉树称为完全二叉树
            特点:
                叶子节点只能出现在最下两层
                最下层的叶子一定集中在左部连续位置
                倒数第二层,若有叶子结点,一定都在右部连续位置
                如果结点度为1,则该结点只有左孩子,即不存在只有右子树的情况
                同样节点树的二叉树,完全二叉树的深度最小

### 6.5 二叉树的性质

    性质1:在二叉树的第i层上至多有2^(i-1)个结点(i≥1)
    性质2:深度为k的二叉树至多有2^k-1个结点(k≥1)
    性质3:对任何一颗二叉树T,如果终端结点数为n0,度为2的结点数为n2,则n0=n2+1
    性质4:具有n个结点的完全二叉树的深度为[log2n]+1([x]表示不大于x的最大整数)
    性质5:如果对一颗有n个结点的完全二叉树(其深度为[log2n]+1)的结点按层序编号(从第1层到第[log2n]+1层,每层从左到右),对任一结点i(1≤i≤n)有
        1、如果i=1,则结点i是二叉树的根,无双亲;如果i>1,则其双亲是结点[i/2]
        2、如果2i>n,则结点i无左孩子(结点i为叶子结点);否则其左孩子是结点2i
        3、如果2i+1>n,则结点i无右孩子;否则其右孩子是结点2i+1

### 6.6 二叉树的存储结构

    二叉树顺序存储结构
        一般只用于完全二叉树

    二叉链表
        二叉树每个结点最多有两个孩子,为它设计一个数据域和两个指针域.称这样的链表叫做二叉链表
            typedef struct BiTNode
            {
                TElemType data;
                struct BiTNode *lchild,*rchild;
            }BiTNode,*BiTree;

### 6.7 遍历二叉树

    二叉树遍历原理
        二叉树的遍历(traversing binary tree)是指从根节点出发,按照某种次序依次访问二叉树中所有结点,使得每个结点被访问一次且仅被访问一次

    二叉树遍历方法
        1、前序遍历
            规则是若二叉树为空,则空操作返回,否则先访问根结点,然后前序遍历左子树,再前序遍历右子树
        2、中序遍历
            规则是若树为空,则空操作返回,否则从根节点开始(注意并不是先访问根结点),中序遍历根结点的左子树,然后是访问根结点,最后中序遍历右子树
        3、后序遍历
            规则是若数为空,则空操作返回,否则从左到右先叶子后结点的方式遍历访问左右子树,最后是访问根结点
        4、层序遍历
            规则是若树为空,则空操作返回,否则从树的第一层,也就是根结点开始访问,从上而下层序遍历,在同一层中,按从左到右的顺序对结点逐个访问
    
    前序遍历算法
        void PreOrderTraverse(BiTree T)
        {
            if(T=NULL)
                return ;
            printf("%c",T->data);
            PreOrderTraverse(T->lchild);
            PreOrderTraverse(T->rchild);
        }
    
    中序遍历算法
        void InOrderTraverse(BiTree T)
        {
            if(T=NULL)
                return ;
            InOrderTraverse(T->lchild);
            printf("%c",T->data);
            InOrderTraverse(T->rchild);
        }

    后序遍历算法

        void PostOrderTraverse(BiTree T)
        {
            if(T=NULL)
                return ;
            PostOrderTraverse(T->lchild);
            PostOrderTraverse(T->rchild);
            printf("%c",T->data);
        }

    推导遍历结果
        已知前序遍历和中序遍历序列,可以唯一确定一颗二叉树
        已知后序遍历和中序遍历序列,可以唯一确定一颗二叉树
        已知前序遍历和后序遍历序列,不能确定一颗二叉树

### 6.8 二叉树的建立

    void CreateBiTree(BiTree *T)
    {
        TElemType ch;
        scanf("%c",&ch);
        if(ch=='#')
            *T=NULL;
        else
        {
            *T=(BiTree)malloc(sizeof(BiTNode));
            if(!*T)
                exit(OVERFLOW);
            (*T)->data=ch;
            CreateBiTree(&(*T)->lchild);
            CreateBiTree(&(*T)->rchild);
        }
    }

### 6.9 线索二叉树

    线索二叉树原理
        指向前驱和后继的指针称为线索,加上线索的二叉链表称为线索链表,相应的二叉树就称为线索二叉树(Threaded Binary Tree)
        对二叉树以某种次序遍历使其变为线索二叉树的过程称作是线索化
    
    线索二叉树结构
        typedef enum {Link,Thread} PointerTag;
        typedef struct BiThrNode
        {
            TElemType data;
            struct BiThrNode *lchild,*rchild;
            PointerTag Ltag;
            PointerTag Rtag;
        }BiThrNode,*BiThrTree;
    线索化的过程就是在遍历的过程中修改空指针的过程
    如果所用的二叉树需经常遍历或查找结点时需要某种遍历序列中的前驱和后继,那么就可以采用线索二叉链表的存储结构

### 6.10 树、森林与二叉树的转换

    树转换为二叉树
        1、加线.在所有兄弟结点之间加一条连线
        2、去线.对树中每个结点,只保留它与第一个孩子结点的连线,删除它与其他孩子结点之间的连线
        3、层次调整.以树的根结点为轴心,将整棵树顺时针旋转一定的角度,使之结构层次分明.注意第一个孩子是二叉树结点的左孩子,兄弟转换过来的孩子是结点的右孩子
    
    森林转换为二叉树
        1、把每个树转化为二叉树
        2、第一棵二叉树不动,从第二棵二叉树开始,依次把后一棵二叉树的根结点作为前一棵二叉树的根结点的右孩子,用线连接起来.当所有的二叉树连接起来后就得到了由森林转换来的二叉树
    
    二叉树转换为树
        1、加线.若某结点的左孩子结点存在,则将这个左孩子的右孩子结点、右孩子的右孩子结点、右孩子的右孩子的右孩子结点
        2、去线.删除原二叉树中所有结点与其右孩子结点的连线
        3、层次调整.使之结构层次分明

    二叉树转转为森林
        1、从根结点开始,若右孩子存在,则把与右孩子结点的连线删除,再查看分离后的二叉树,若右孩子存在,则连线删除...,直到所有右孩子连线都删除为止,得到分离的二叉树
        2、再将每棵分离后的二叉树转换为树即可
    
    树与森林的遍历
        树的遍历分为两种方式
            1、一种是先根遍历树,即先访问树的根结点,然后依次先根遍历树的每棵子树
            2、另一种是后根遍历,即先依次后根遍历每棵子树,然后再访问根结点
        森林的遍历也分为两种方式
            1、前序遍历:先访问森林中每一棵树的根结点,然后再依次先根遍历的每棵子树,再依次用同样方式遍历除去第一棵树的剩余树构成的森林
            2、后序遍历:是先访问森林中第一棵树,后根遍历的方式遍历每棵子树,然后再访问根结点,再依次用同样方式遍历除去第一棵树的剩余树构成的森林

### 6.11 霍夫曼树

    霍夫曼树定义与原理
        从树中一个结点到另一个结点之间的分支构成两个结点之间的路径,路径上的分支数目称作路径长度
        树的路径长度就是从树根到每一结点的路径长度之和
        带权路径长度WPL最小的二叉树称作霍夫曼树,也称为最优二叉树
            1、根据给定的n个权值(w1,w2,...wn)构成n棵二叉树的集合F={T1,T2,...,Tn},其中每棵二叉树Ti中只有一个带权为wi根结点,其左右子树均为空
            2、在F中选取两颗根结点的权值最小的树作为左右子树构造一棵新的二叉树,且置新的二叉树的根结点的权值为其左右子树上根结点的权值之和
            3、在F中删除这两棵树,同时将新得到的二叉树加入F中
            4、重复2和3步骤,直到F只含一棵树为止.这棵树便是霍夫曼树
    
    霍夫曼编码
        若要设计长短不等的编码,则必须任一字符的编码都不是另一个字符的编码的前缀,这种编码称为前缀编码
        一般地,设需要编码的字符集为{d1,d2,...,dn},各个字符在电文中出现的次数或频率集合为{w1,w2,...,w3},以d1,d2,...,dn作为叶子结点,以w1,w2,...,wn作为相应叶子结点的权值来构造一棵霍夫曼树.规定霍夫曼树的左分支代表0,右分支代表1,则从根结点到叶子结点所经过的路径分支组成的0和1的序列便为该结点对应字符的编码,这就是霍夫曼编码

## 第7章 图

### 7.1 图的定义

    图(Graph)是由顶点的有穷非空集合和顶点之间边的集合组成,通常表示为:G(V,E),其中,G表示一个图,V是图G中顶点的集合,E是图G中边的集合
        在图中数据元素,称之为顶点(Vertex)
        在图结构中,不允许没有顶点.在定义中,若V是顶点的集合,则强调了顶点集合V有穷非空
        图中,任意两个顶点之间都可能有关系,顶点之间的逻辑关系用边来表示,边集可以是空的
    
    各种图定义
        无向边:若顶点vi到vj之间的边没有方向,则称这两条边为无向边(Edge),用无序偶对(vi,vj)来表示.如果图中任意两个顶点之间的边都是无向边,则称该图为无向图(Undirected graphs)
        有向边:若顶点vi到vj的边有方向,则称这条边为有向边,也称为弧(Arc),用有序偶<vi,vj>来表示.vi称为弧尾(Tail),vj称为弧头(Head)
        如果图中任意两个顶点之间的边都是有向边,则称该图为有向图。连接顶点A到D的有向边就是弧,A是弧尾,D是弧头,<A,D>表示弧,注意不能写成<D,A>
        AT(TENTION):无向边(),有向边<>
        在图中,若不存在顶点到其自身的边,且同一条边不重复出现,则称这样的图为简单图
        在无向图中,如果任意两个顶点之间都存在边,则称该图为无向完全图。
        在无向图中,如果任意两个顶点之间都存在方向互为相反的两条弧,则称该图有向完全图
        有很多条边或弧的图称为稀疏图,反之称为稠密图
        与图的边或弧相关的数叫做权,这种带权的图通常称为网
        假设有两个图G=(V,{E})和G'=(V',{E'}),如果V'⊆V且E'⊆E,则称G'为G的子图
    
    图的顶点与边间关系
        对于无向图G=(V,{E}),如果边(v,v')∈E,则称顶点v和v'互为邻接点,即v和v'相邻接.边(v,v')依附于顶点v和v',或者说(v,v')与顶点v和v'相关联.顶点v的度是和v相关联的边的数目,记为TD(v),边数为个顶点度数和的一半
        对于有向图G=(V,{E}),如果弧<v,v'>∈E,则称顶点v邻接到顶点v',顶点v'邻接自顶点.弧<v,v'>和顶点v,v'相关联.以顶点v为头的弧的数目称为v的入度,记为ID(v);以v为尾的弧的数称为v的出度,记为OD(v);顶点v的度为TD(v)=ID(v)+OD(v)
        无向图G=(V,{E})中从顶点v到顶点v'的路径是一个顶点序列(v=vi,0,vi,1,...,vi,m=v'),其中(vi,j-1,vi,j)∈E,1≤j≤m
        路径的长度是路径上的边或弧的数目
        第一个顶点到最后一个顶点相同的路径称为回路或环.序列中顶点不重复出现的路径称为简单路径.除了第一个顶点和最后一个顶点之外,其余顶点不重复出现的回路,称为简单回路或简单环
    
    连通图相关术语
        在无向图G中,如果顶点v到顶点v'有路径,则称v和v'是连通的.如果对于图中任意两个顶点vi、vj∈E,vi和vj都是连通的,则称G是连通图
        无向图中的极大连通子图称为连通分量
        在有向图中G中,如果对于每一对vi、vj∈V、vi≠vj,从vi到vj和从vj到vi都存在路径,则称G是强连通图.有向图中的极大强连通子图称作有向图的强连通分量
        一个连通图的生成树是一个极小的连通子图,它含有图中全部的n个顶点,但只有足以构成一棵树的n-1条边
        如果一个有向图恰有一个顶点的入度为0,其余顶点的入度均为1,则是一颗有向树.一个有向图的生成森林有若干棵有向树组成,含有图中全部顶点,但只有足以构成若干棵不相交的有向树的弧

### 7.2 图的抽象数据类型

    ADT 图(Graph)
    Data
        顶点的有穷非空集合和边的集合
    
    Operation
        CreateGraph(*G,V,VR):按照顶点集V和边弧集VR的定义构造图G
        DestroyGraph(*G):图G存在则销毁
        LocateVex(G,u):若图G中存在顶点u,则返回图中的位置
        GetVex(G,v,value):将图G中顶点v赋值value
        FirstAdjvex(G,v,*w):返回顶点v相对于顶点w的下一个邻接顶点,若w是v的最后一个邻接点则返回"空"
        InsertVex(*G,v):在图G中增添新顶点v
        DeleteVex(*G,v):删除图G中顶点v及其相关的弧
        InsertArc(*G,v,w):在图G中增添弧<v,w>,若G是无向图,还需要增添对称弧<w,v>
        DeleteArc(*G,v,w):在图中删除弧<v,w>,若G是无向图,则还删除对称弧<w,v>
        DFSTraverse(G):对图G中进行深度优先遍历,在遍历过程对每个顶点调用
        HFSTraverse(G):对图G中进行广度优先遍历,在遍历过程中对每个顶点调用
    endADT

### 7.3 图的存储结构

    邻接矩阵
        图的邻接矩阵存储方式是用两个数组来表示图.一个一维数组存储图中顶点信息,一个二维数组(称为邻接矩阵)存储图中的边或弧的信息
        ∞表示权值中不可能的极限值，计算机允许的、大于所有边上权值的值
    
    图的邻接矩阵存储的结构
        typedef char VertexType;
        typedef int EdgeType;
        #define MAXVEX 100          /*最大顶点数*/
        #define INFINITY 65535      /*用xx来代表∞*/
        typeder struct{
            VertexType vexs[MAXVEX];
            EdgeType arc[MAXVEX][MAXVEX];
            int numVertexes,numEdges;
        }MGraph;
    
    邻接表
        数组与链表结合的存储方法
        无向图
            图中顶点用一个一维数组存储
            图中每个顶点vi的所有邻接点构成一个线性表
        有向图
            以顶点为弧尾来存储边表,建立有向图的逆邻接表,即对每个顶点vi都建立一个链接为vi为弧头的表
        typedef char VertexType;
        typedef int EdgeType;
        typedef struct EdgeNode{
            int adjvex;
            EdgeType weight;
            struct EdgeNode *next;
        }EdgeNode;
        typedef struct VertexNode{
            VertexType data;
            EdgeNode *firstedge;
        }VertexNode,AdjList[MAXVEX];
        typedef struct{
            AdjList adjList;
            int numVertexes,numEdges;
        }GraphAdjList;
    
    十字链表
        将邻接表与逆邻接表结合
        边表结点结构:tailvex headvex headlink taillink
            其中tailvex是指弧起点在顶点表的下标,headvex是指弧终点在顶点表中的下表,headlink是指入边表指针域,指向终点相同的下一条边,taillink是指边表指针域,指向起点相同的下一条边.如果是网,还可以再增加一个weight域来存储权值
    
    邻接多重表
        边表结点结构:ivex ilink jvex jlink
            其中ivex和jvex是与某条边依附的两个顶点在顶点表中下标.ilink指向依附顶点ivex的下一条边,jlink指向依附顶点jvex的下一条边
    
    边集数组
        边集数组是由两个一维数组构成.一个是存储顶点的信息;另一个是存储边的信息,这个边数组每个数据元素由一条边的起点下标(begin)、终点下标(end)和权(weight)组成

### 7.4 图的遍历

    从图中某一顶点出发访遍图中其余顶点,且使每一个顶点仅被访问一次,这一过程就叫做图的遍历(Traversing Graph)

    深度优先遍历,也有称为深度优先搜索,简称为DFS
        从图中某个顶点v出发,访问此顶点,然后从v的未被访问的邻接点出发深度优先遍历图,直至图中所有和v由路径相通的顶点都被访问到
        若图中尚有顶点未被访问,则另选图中一个未曾被访问的顶点作始起点,重复上述过程,直至图中所有顶点都被访问到为止
    广度优先遍历,又称为广度优先搜索,简称BFS

### 7.5 最小生成树

    把构造连通网的最小代价生成树称为最小生成树

    普里姆(Prim)算法
        假设N=(P,{E})是连通网,TE是N上最小生成树中边的集合.算法从U={u0}(u0∈V),TE={}开始.重复执行下述操作:在所有u∈U,v∈V-U的边(u,v)∈E中找一条代价最小的边(u0,v0)并入集合TE,同时v0并入U,直至U=V为止.此时TE中必有n-1条边,则T=(V,{TE})为N的最小生成树
        只基本实现最小生成树的构建,算法还可以优化,参见《算法导论》图算法
    
    克鲁斯卡尔(Kruskal)算法
        假设N=(V,{E})是连通网,则令最小生成树的初始状态为只有n个顶点而无边的非连通图T={V,{}},图中每个顶点自成一个连通分量.在E中选择代价最小的边,若该边依附的顶点落在T中不同的连通分量上,则将此边加入到T中,否则舍去此边而选择下一条代价最小的边.依次类推,直至T中所有顶点都在同一连通分量上为止
    
    前者对于稠密图,边数非常多的情况更好O(n2)顶点数
    后者对于稀疏图,边数少效率高,O(eloge)边数

### 7.6 最短路径

    对于网面来说,最短路径,是指两顶点之间经过的边上权值之和最少的路径,并且称路径上的第一个顶点是源点,最后一个顶点是终点

    迪杰斯特拉(Dijkstra)算法
        按路径长度递增的次序产生最短路径,基于已经求出的最短路径的基础上,求得更远顶点的最短路径

    弗洛伊德(Floyd)算法
        利用数组D(代表顶点到顶点的最短路径权值和的矩阵),数组P(代表对应顶点的最小路径的前驱矩阵),依次经过顶点中转,计算最短路径的变化
        需要求所有顶点至所有顶点的最短路径问题时,弗洛伊德算法是不错的选择

### 7.7 拓扑排序

    拓扑排序介绍
        在一个表示工程的有向图中,用顶点表示活动,用弧表示活动之间的优先关系,这样的有向图为顶点表示活动的网,我们称为AOV网(Activity On Vertex Network).
        设G=(V,E)是一个具有n个顶点的有向图,V中的顶点序列v1,v2,...,vn,满足若从顶点vi到vj有一条路径,则在顶点序列中顶点vi必在顶点vj之前.则称这样的顶点序列为一个拓扑序列
        拓扑排序,其实就是对一个有向图构造拓扑序列的过程
    
    拓扑排序算法
        从AOV网中选择一个入度为0的顶点输出,然后删去此顶点,并删除以此顶点为尾的弧,继续重复此步骤,直到输出全部顶点或者AOV网中不存在入度为0的顶点为止

### 7.8 关键路径

    在一个表示工程的带权有向图中,用顶点表示事件,用有向边表示活动,用边上的权值表示活动的持续时间,这种有向图的边表示活动的网,我们称之为AOE网(Activity On Edge Network)
    把路径上各个活动所持续的时间之和称为路径长度,从源点到汇点具有最大长度的路径叫关键路径,在关键路径上的活动叫关键活动

    关键路径算法原理
        定义参数
            事件的最早发生时间etv(earliest time of vertex):即顶点vk的最早发生时间
            事件的最晚发生时间ltv(latest time of vertex):即顶点vk的最晚发生时间,也就是每个顶点对应的事件最晚需要开始的时间,超出此时间将会延误整个工期
            活动的最早开工时间ete(earliest time of edge):即弧ak的最早发生时间
            活动的最晚开工时间lte(latest time of edge):即弧ak的最晚发生时间,也就是不推迟工期的最晚开工时间
        找到所有活动的最早开始时间和最晚开始时间,并比较,如果相等就意味着此活动是关键活动,活动间的路径为关键路径,意味着活动没有空闲

    关键路径算法
        求事件的最早发生时间etv的过程,就是从头至尾找拓扑序列的过程,在求关键路径之前,需要先调用一次拓扑序列算法的代码来计算etv和拓扑序列列表

## 第8章 查找

    查找就是根据给定的某个值,在查找表中确定一个其关键字等于给定值的数据元素(或记录)

### 8.1 查找概论

    查找表(Search Table)是由同一类型的数据元素(或记录)构成的集合
    关键字(Key)是数据元素中某个数据项的值,又称为键值,可以标识一个数据元素.也可以标记一个记录的某个数据项(字段),称为关键码
    若此关键字可以唯一地标识一个记录,则称此关键字为主关键字(Primary Key)
    对于那些可以识别多个数据元素(或记录)的关键字,我们称为次关键字(Secondary Key)
    静态查找表(Static Search Table):只作查找操作的查找表
        (1)查询某个"特定的"数据元素是否在查找表中
        (2)检索某个"特定的"数据元素和各种属性
    动态查找表(Dynamic Search Table):在查找过程中同时插入查找表中不存在的数据元素,或者从查找表中删除已经存在的某个数据元素
        (1)查找时插入数据元素
        (2)查找时删除数据元素

### 8.2 顺序表查找

    针对线性表进行查找操作,因此为静态查找表
    顺序查找(Sequential Search)又叫线性查找,是最基本的查找技术,它的查找过程是:从表中第一个(或最后一个)记录开始,逐个进行记录的关键字和给定值比较,若某个记录的关键字和给定值相等,则查找成功,找到所查的记录;如果直到最后一个(或第一个)记录,其关键字和给定值比较都不等时,则表中没有所查的记录,查找不成功

    顺序表查找算法
        在数组a中查看有没有关键字(key)
    顺序表查找优化
        每次循环时都需要对i是否越界,即是否小于等于n作判断.在数组的头或尾设置一个哨兵
        根据查找概率将容易查找的记录放在前面,也可以提高效率

### 8.3 有序表查找

    折半查找
        折半查找(Binary Search)技术,又称为二分查找.它的前提是线性表中的记录必须是关键码有序(通常从小到大有序),线性表必须采用顺序存储.折半查找的基本思想是:在有序表中,取中间记录作为比较对象,若给定值与中间记录的关键字相等,则查找成功;若给定值小于中间记录的关键字,则在中间记录的左半区继续查找;若给定值大于中间记录的关键字,则在中间记录的右半区继续查找.不断重复上述过程,直到查找成功,或所有查找区域无记录,查找失败为止

    插值查找
        根据要查找的关键字key与查找表中最大最小记录的关键字比较后的查找办法,其核心就在于插值的计算公式(key-a[low])/(a[high]-a[low])(将折半查找的1/2修改)
        对于表长较大,而关键字分布又比较均匀的查找表,平均性能更好

    斐波那契查找
        先根据查找表规模确定第一次查找位置
        同时要将第一次查找范围内的数组进行扩展赋值(空赋值为最大值)
            (1)当key=a[mid]时,查找就成功
            (2)当key<a[mid]时,新范围时第low个到第mid-1个,此时范围个数为F[k-1]-1个
            (3)当key>a[mid]时,新范围是第m+1个到第high个,此时范围个数为F[k-2]-1个
        平均性能优于折半查找,最坏情况下,始终处于左侧长半区,效率低于折半

### 8.4 线性索引查找

    把一个关键字与它对应的记录相关联的过程
    所谓线性索引就是将索引项集合组织为线性结构,也成为线性表

    稠密索引
        在线性索引中,将数据集中的每个记录对应一个索引项
        对于稠密索引这个索引项来说,索引项一定是按照关键码有序的排列

    分块索引
        分块有序,是把数据集的记录分成了若干块,并且这些块满足两个条件:
            块内无序、块间有序
        分块索引的索引项结构分三个数据项
            最大关键码,它存储每一块中的最大关键字,这样的好处就是可以使得在它之后的下一块中的最小关键字也能比这一块最大的关键字要大
            存储了块中的记录个数,以便于循环时使用
            用于指向块首数据元素的指针,便于开始对这一块中记录进行遍历
        在分块索引表中查找,就是分两步进行
            在分块索引表中查找要查关键字所在的块.由于分块索引表是块间有序的,因此很容易利用折半、插值等算法得到结果
            根据块手指针找到相应的快,并在块中顺序查找关键码

    倒排索引(inverted index)
        索引项的通用结构
            次关键码,记录号表
            其中记录号表存储具有相同次关键字的所有记录的记录号(可以是指向记录的指针或者是该记录的主关键字)

### 8.5 二叉排序树

    二叉排序树(Binary Sort Tree),又称为二叉查找树.他或者是一颗空树,或者是具有下列性质的二叉树
        若它的左子树不空,则左子树上所有结点的值均小于它的根结点的值
        若它的右子树不空,则右子树上所有结点的值均大于它的根结点的值
        它的左、右子树也分别为二叉排序树
    
    二叉排序树查找、插入操作
    二叉排序数删除操作
        三种情况
            叶子结点
            仅有左或右子树的结点
            左右子树都有的结点:用直接前驱或直接后继替换,替换时出现情况继续递归

### 8.6 平衡二叉树(AVL树)

    平衡二叉树(Self-Balancing Binary Search Tree或Height-Balanced Binary Search Tree),是一种二叉排序树,其中每一个结点的左子树和右子树的高度差至多等于1
    是一种高度平衡的二叉树,将二叉树上结点的左子树深度减去右子树深度的值称为平衡因子BF,平衡二叉树只能有-1,0,1
    距离插入结点最近的,而平衡因子的绝对值大于1的结点为根的子树,称为最小不平衡子树

    平衡二叉树实现原理
        基本思想:在构建二叉树排序树的过程中,每当插入一个结点时,先检查是否因插入而破坏了树的平衡性,若是,则找出最小不平衡树.在保持二叉排序树特性的前提下,调整最小不平衡子树中各结点之间的链接关系,进行响应的旋转,使之成为新的平衡子树
        BF>1,右旋;BF<1,左旋

    平衡二叉树实现算法
        右旋:当传入一个二叉排序树P,将它的左孩子结点定义为L,将L的右子树变成P的左子树,再将P改成L的右子树,最后将L替换P成为根结点

### 8.7 多路查找树(B树)

    多路查找树,其每一个结点的孩子数可以多于两个,且每一个结点处可以存储多个元素

    2-3树
        2-3树 其中的每个结点都具有两个孩子(称它为2结点)或三个孩子(称它为3结点)
        一个2结点包含一个元素和两个孩子(或没有孩子)
        一个3结点包含一小一大两个元素和三个孩子(或没有孩子)

        2-3树的插入实现
            (1)对于空树,插入一个2结点即可
            (2)插入结点到一个2结点的叶子上.由于本身就只有一个元素,只需要将其升级为3结点即可.
            (3)要往3结点中插入一个新元素.因为3结点本身已经是2-3树的结点最大容量(已经有两个元素),因此就需要将其拆分,且将树中两元素或插入元素的三者中选择其一向上移动一层
            2-3树插入的传播效应导致根结点的拆分,进而使得树的高度增加
        
        2-3树的删除实现
            (1)所删除元素位于一个3结点的叶子结点上,只需要在该结点处删除该元素
            (2)所删除的元素位于一个2结点上,即要删除的时一个只有一个元素的结点
                此结点的双亲也是2结点,且拥有一个3结点的右孩子,删除左子结点,只需要左旋
                此结点的双亲是2结点,它的右孩子也是2结点.删除左子结点,需要对整棵树变形,让比右孩子直接后继下来补上,同时也补上因为移位造成的缺位
                此结点的双亲是一个3结点.删除该结点,需要拆分双亲结点,并将其中一个与子结点合并为3结点
                当前树是一个满二叉树,"反向进行",将2-3的层数减少,利用3结点进行合并
            (3)所删除的元素位于非叶子的分支结点.将树按中序遍历后得到此元素的前驱或后继元素,让它们来补位
        
    2-3-4树
        是2-3树的概念扩展,包括了4结点的使用.一个4结点包含小中大三个元素和四个孩子(或没有孩子),一个结点要么没有孩子,要么具有4个孩子.左、第二、第三、右子树元素呈递增关系
    
    B树
        B树(B-tree)是一种平衡的多路查找树),2-3树和2-3-4树都是B树的特例.结点最大的孩子数目成为B树的阶
        一个m阶的B树属性
            如果根结点不是叶结点,则其至少有两颗子树
            每一个非根的分支结点都有k-1个元素和k个孩子,其中[m/2]≤k≤m.每一个叶子结点n都有k-1个元素,其中[m/2]≤k≤m
            所有叶子结点都位于同一层次
            所有分支结点包含下列信息数据(n,A0,K1,A1,K2,A2,...,Kn,An),其中:Ki(i=1,2,...,n)为关键字,且Ki<Ki+1(i=1,2,...,n-1);Ai(i=0,2,...,n)为指向子树根结点的指针,且指针Ai-1所指子树中所有结点的关键字均大于Kn,n([m/2]-1≤n≤m-1)为关键字的个数(或n+1为子树的个数)
        在B树上查找的过程是一个顺指针查找结点和在结点中查找关键字的交叉过程.B树的数据结构就是为内外存的数据交互准备的.在含有n个关键字的B树上查找时,从根结点到关键字结点的路径上涉及的结点数不超过log[m/2]((n+1)/2)+1
    
    B+树
        是应文件系统所需而出的一种B树的变形树,注意严格意义上讲,它其实已经不是前面所定义的树了.在B+树中,出现在分支结点中的元素会被当作它们在该分支结点位置的中序后继者(叶子结点)中再次列出.另外,每一个叶子都会保存一个指向后一叶子结点的指针
        一棵m阶的B+树和m阶的B树的差距在于
            有n棵子树的结点中包含有n个关键字
            所有的叶子结点包含全部关键字的信息,及指向含这些关键子记录的指针,叶子结点本身依关键字的大小自小而大顺序链接
            所有分支结点可以看成是索引,结点中仅含有其子树中的最大(或最小)关键字
        随机查找从根结点出发,顺序查找从最左侧的叶子结点出发

### 8.8 散列表查找(哈希表)概述

    散列表查找定义
        存储位置=f(关键字),f为函数
        散列技术是在记录的存储位置和它的关键字之间建立一个确定的对应关系f,使得每个关键字key对应一个存储位置f(key)
        f称为散列函数,又称为哈希(Hash)函数.采用散列技术将记录存储在一块连续的存储空间中,这块连续存储空间称为散列表或哈希表(Hash table)

    散列表查找步骤
        (1)在存储时,通过散列函数计算记录的散列地址,并按此散列地址存储该记录
        (2)在查找记录时,通过同样的散列函数计算记录的散列地址,按此散列地址访问该记录
        散列技术既是一种存储方法,也是一种查找方法
        散列技术最适合的求解问题是查找与给定值相等的记录
        关键问题:设计一个简单、均匀、存储利用率高的散列函数
        两个关键字key1≠key2,但是却有f(key1)=f(key2),这种现象称为冲突,并把key1和key2称为这个散列函数的同义词

### 8.9 散列函数的构造方法

    好的散列函数
        计算简单,散列函数的计算时间不应该超过其他查找技术与关键字比较的时间
        散列地址分布均匀,让散列地址均匀地分布在存储空间中,保证存储空间的有效利用,并减少为处理冲突而耗费的时间

    直接定址法
        f(key)=a*key+b(a、b为常数)
        适合查找表较小且连续的情况

    数字分析法
        使用关键字的一部分来计算散列存储位置,还可以对抽取出的关键字进行反转、左/右环位移、叠加等处理

    平方取中法
        适合于不知道关键字的分布,而位数又不是很大的情况

    折叠法
        将关键字从左到右分割成位数相等的几部分(注意最后一部分位数不够时可以短些),然后将这几部分叠加求和,并按散列表表长,取后几位作为散列地址
        有时可能这还不能够保证分布均匀,可以从一端向另一端来回折叠后对齐相加.
        折叠法事先不需要直到关键字的分布,适合关键字位数较多的情况

    除留余数法
        f(key)=key mod p (p≤m),mod是取模(求余数)的意思.还可以对关键字折叠、平方取中后再取模
        若散列表表长为m,通常p为小于或等于表长(最好接近m)的最小质数或不包含小于20质因子的合数

    随机数法
        选择一个随机数,其关键字的随机函数值为它的散列地址
        f(key)=random (key),random是随机函数
        当关键字的长度不等时,随机数法比较适合
        参考因素
            计算散列地址所需的时间
            关键字的长度
            散列表的大小
            关键字的分布情况
            记录查找的频率

### 8.10 处理散列冲突的方法

    开放定址法
        一旦发生了冲突,就去寻找下一个空的散列地址,只要散列表足够大,空的散列地址总能找到,并将记录存入
        fi (key)=(f (key) +di) MOD m (di=1,2,3,...,m-1)
        这种解决冲突的开放定址法称为线性探测法
        本来都不是同义词却需要争夺一个地址的情况,称为堆积.
        当发生较多堆积时,可以改进di=1^2,-1^2,2^2,-2^2,...,q^2,-q^2,(q≤m/2).增加平方运算的目的是为了不让关键字都聚集在某一块区域,这种方法称为二次探测法
        fi (key)=(f (key) +di) MOD m (di=1^2,-1^2,2^2,-2^2,...,q^2,-q^2,q≤m/2)
        在冲突时,对于位移量di采用随机函数计算得到,称为随机探测法
        fi (key)=(f (key) +di) MOD m (di是一个随机数列)
    
    再散列函数法
        事先准备多个散列函数
        fi (key)=RHi (key) (i=1,2,...,k)
    
    链地址法
        将所有关键字为同义词的记录存储在一个单链表中,称这种表为同义词子表,在散列表中只存储所有同义词子表的头指针

    公共溢出区法
        为所有冲突的关键字建立一个公共的溢出区来存放

### 8.11 散列表查找实现

    散列表查找算法实现
        定义一个散列表的结构以及一些相关的常数
        定义散列函数
        插入关键字前,计算散列地址,出现冲突开放定址重新寻址,或使用链地址

    散列查找性能分析
        散列查找的平均查找长度取决因素
            散列函数是否均匀
                不同的散列函数对同一组随机的关键字,产生冲突的可能性是相同的
            处理散列冲突的方法
                相同的关键字、散列函数,不同处理方法使平均查找长度不同,二次探测比线性探测更不易产生冲突,链地址法处理冲突不产生堆积,平均查找性能更佳
            散列表的装填因子
                装填因子α=填入表中的记录个数/散列表长度.α标志着散列表的装满的程度.
                选择一个合适的装填因子以便将平均查找长度限定在一个范围之内,可以让散列查找的时间复杂度接近O(1)

## 第9章 排序

### 9.1 排序的基本概念与分类

    假设含有n个记录的序列为{r1,r2,...,rn},其相应的关键字分别为{k1,k2,...,kn},需确定1,2,...,n的一种排列p1,p2,...,pn,使其相应的关键字满足kp1≤...≤kpn(非递减或非递增)关系,即使得序列成为一个按关键字有序的序列{rp1,rp2,...,rpn},这样的操作就称为排序
    在排序问题中,通常将数据元素称为记录.输入输出都是一个记录集合,可以将排序看成是线性表的一种操作

    排序的稳定性
        假设ki=kj(1≤i≤n,1≤j≤n,i≠j),且在排序前的序列中r1领先于rj(即i<j).如果排序后ri仍领先于rj,则称所用的排序方法是稳定的;反之,若可能使得排序后的序列中rj领先ri,则称所用的排序方法是不稳定的
    
    内排序与外排序
        内排序是在排序整个过程中,待排序的所有记录全部被放置在内存中.外排序是由于排序的记录个数太多,不能同时放置在内存,整个排序过程需要在内外存之间多次交换数据才能进行
        排序算法性能影响因素
            时间性能:最重要标志,内排序进行比较和移动两个操作
            辅助空间:主要标准,执行算法所需要的辅助存储空间
            算法的复杂性:算法本身的复杂度
                内排序:插入排序、交换排序、选择排序和归并排序
    
    排序用到的结构与函数
        排序顺序表结构、交换函数

### 9.2 冒泡排序

    最简单排序实现
        冒泡排序(Bubble Sort)是一种交换排序,它的基本思想是:两两比较相邻记录的关键字,如果反序则交换,直到没有反序的记录为止
        单纯地逐层地交换

    冒泡排序算法
        每层循环跟随单个上升气泡

    冒泡排序优化
        避免因已经有序的情况下进行无意义的循环判断

    冒泡排序复杂度  O(n2)

### 9.3 简单选择排序

    简单选择排序算法
        简单选择排序(Simple Selection Sort)就是通过n-i次关键字间的比较,从n-i+1个记录中选出关键字最小的记录,并和第i(1≤i≤n)个记录交换之
    
    简单选择排序复杂度 O(n2),但性能上略优于冒泡排序

### 9.4 直接插入排序

    直接插入排序算法
        直接插入排序(Straight Insertion Sort)的基本操作是将一个记录插入到已经排好序的有序表中,从而得到一个新的、记录数增1的有序表

    直接插入排序复杂度 O(n2),比冒泡和简单选择排序要好

### 9.5 希尔排序

    优秀排序算法的首要条件就是速度

    希尔排序原理
        将记录分割成若干个子序列,对子序列分别进行直接插入排序,当整个序列基本有序时,再对全体记录进行一次直接插入排序
        基本有序,就是小的关键字基本在前面,大的基本在后面,不大不小的基本在中间
        采取跳跃分割的策略:将相距某个"增量"的记录组成一个子序列,这样才能保证在子序列内分别进行直接插入排序后得到的结果是基本有序而不是局部有序

    希尔排序算法
        确定增量increment=f(increment),以增量为间隔进行简单排序

    希尔排序复杂度分析
        increment=f(increment),迄今为止还没有找到最好的增量序列
        Δ[k]=2^(t-k+1)-1(0≤k≤t≤[log[2](n+1)])时,时间复杂度O(n^(3/2))
        增量序列的最后一个增量值必须=1,不稳定

### 9.6 堆排序

    堆是具有下列性质的完全二叉树:每个结点的值都大于或等于其左右孩子结点的值,称为大顶堆;或者每个结点的值都小于或等于其左右孩子结点的值,称为小顶堆

    堆排序算法
        堆排序(Heap Sort)就是利用堆(假设利用大顶堆)进行排序的方法.将待排序的序列构造成一个大顶堆.此时,整个序列的最大值就是堆顶的根结点.将它移走(其实就是将其与堆数组的末尾元素交换,此时末尾元素就是最大值),然后将剩余的n-1个序列重新构造成一个堆,这样就会得到n个元素中的次小值.如此反复执行,便能得到一个有序序列

    堆排序复杂度分析
        主要运行时间:初始构建堆,重建堆时的反复筛选 O(n)+O(nlogn)=O(nlogn),时间复杂度稳定,排序不稳定
        不适合待排序序列个数较少的情况

### 9.7 归并排序

    归并排序算法
        归并排序(Merging Sort):假设初始序列含有n个记录,则可以看成是n个有序的子序列,每个子序列的长度为1,然后两两合并,得到[n/2]([x]表示不小于x的最小整数)个长度为2或1的有序子序列;再两两归并,...,如此重复,直至得到一个长度为n的有序序列为止,这种排序方法称为2路归并排序

    归并排序复杂度分析
        最好、最坏、平均时间性能O(nlogn),空间复杂度O(n+logn)
        是稳定的排序算法

    非递归实现归并排序
        在一个循环内实现归并出入
        使用归并排序时,尽量考虑用非递归方法,提升时间、空间性能

### 9.8 快速排序

    快速排序算法
        快速排序(Quick Sort)的基本思想是:通过一趟排序将待排记录分割成独立的两部分,其中一部分记录的关键字均比另一部分记录的关键字小,则可分别对这两部分记录继续进行排序,以达到整个序列有序的目的
        先选取当中的一个关键字,比如选择第一个关键字,然后想尽办法将它放到第一个位置,使得它左边的值都比它小,右边的值比它大,将这样的关键字称为枢轴

    快速排序复杂度分析
        最优和平均时间复杂度为O(nlogn),最差为O(n2),空间复杂度O(logn)
    
    快速排序优化
        优化选择枢轴
            随机选取,概率上无影响
            三数取中(median-of-three),取三个关键字先进行排序,将中间数作为枢轴,一般是取左端、右端和中间三个数,也可以随机选取
            九数取中,从数组中分三次取样,每次取三个数,三个样品中各取出中数,再取出中数作为枢轴

        优化不必要的交换
            找到枢轴的位置时,再进行赋值交换

        优化小数组
            当排序区间长度不大于某个常数时(有资料认为7或者50合适,实际应用可适当调整),就用直接插入排序

        优化递归操作
            减少递归次数,进行尾递归优化,用迭代替换递归

    了不起的排序算法
        至今经过多次优化后,整体性能上仍然是最好的

## 结尾

    数据结构和算法对于程序员的职业人生来说,那就是两个圆圈的交集部分(我觉得应该学习的知识,能够赚钱的知识),用心去掌握它,你的编程之路将会是坦途