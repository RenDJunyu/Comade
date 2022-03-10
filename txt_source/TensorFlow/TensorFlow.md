# TensorFlow深度学习

    谷歌第二代人工智能学习系统
    人工智能不可避免地需要使用正式化的数学符号推导，涉及到少量的概率与统计、线性代数、微积分等数学知识。
    随着Google的TensorFlow2.0正式版深度学习框架的发布，业界兴起了一股学习更易上手、开发效果更高、使用更灵活的TensorFlow2.0的热潮

## 一、人工智能绪论

    我们需要的是一台可以从经验中学习的机器。——Alan·Turing

### 1.1 人工智能

    通过编程的方式，人类可以将提前设计好的交互逻辑交给机器重复且快速地执行，从而将人类从简单枯燥的重复劳动工作中解脱出来。但是对于需要较高智能水平的任务，如人脸识别、聊天机器人、自动驾驶等任务，很难设计明确的逻辑规则，传统的编程方式显得力不从心，人工智能应运而生。
    目前能达到的智能水平离通用人工智能(Artificial General Intelligence)还有一段距离，但人工智能时代已经来临。

    人工智能
        人工智能最早在1956年召开的达特茅斯会议上提出。
        1970年代，科学家们尝试通过知识库加推理的方式解决人工智能，通过构建庞大复杂的专家系统来模拟人类庄家的智能水平。但问题是很多复杂抽象的概念无法用具体的代码实现，比如人类对图片的识别、对语言的理解过程。机器学习在1980年成为人工智能中的热门学科。
        在机器学习中，有一门通过神经网络来学习复杂、抽象逻辑的方向，称为神经网络。
        2012年开始，应用深层神经网络技术在计算机视觉、自然语言处理、机器人等领域取得了重大突破，部分任务上甚至超越了人类智能水平，开启了以深层神经网络为代表的人工职能的第三次复兴。深层神经网络又称为深度学习。二者本质区别并不大，深度学习特质基于深层神经网络实现的模型或算法。

    机器学习
        机器学习可以分为有监督学习(Supervised Learning)、无监督学习(Unsupervised Learning)和强化学习(Reinforcement Learning, RL)
        有监督学习：有监督学习的数据集包含了样本x与样本的标签y，算法模型需要学习到映射关系f_θ:x→y，其中f_θ代表模型函数，θ为模型的参数。在训练时，通过计算模型的预测值f_θ(x)和真实标签y之间的误差来优化网络参数θ，使得下一次能够预测更精准。常见的有监督学习有线性回归、逻辑回归、支持向量机、随机森林等
        无监督学习：收集带标签的数据往往代价较为昂贵，对于只有样本x的数据集，算法需要自行发现数据的模态。无监督学习中有一类算法将自身作为监督信号，即模型需要学习的映射为f_θ:x→x，成为自监督学习(Self-supervised Learning)。在训练时，通过计算模型的预测值f_θ与自身x之间的误差来优化网络参数θ。常见的无监督学习算法有自编码器、生成对抗网络等
        强化学习：也成为增强学习，通过与环境进行交互来学习解决问题的策略的一类算法。强化学习问题并没有明确的“正确的”动作监督信号，算法需要与环境进行交互，获取环境反馈的滞后的奖励信号，因此并不能通过计算动作与“正确动作”之间的误差来优化网络。常见的强化学习算法有DQN、PPO等

    神经网络与深度学习
        神经网络算法是一类基于神经网络从数据中学习的算法，仍然属于机器学习的范畴。受限于计算能力和数据量，早期的神经网络层数较浅，一般在1-4层左右，网络表达能力有限。
        
        省略
        以下主要为笔记，知识型介绍掠过
        
        tensorflow2完成加法运算
        ```
        import tensorflow as tf
        a=tf.constant(2.)
        b=tf.constant(4.)
        print('a+b=',a+b)
        ```python
        相对于tensorflow1简化较多，同时创建计算图和数值结果称为命令式编程，也成为动态图模式，开发效率高，但是运行效率可能不如静态图模式。也支持通过tf.function转化为静态图模式
        
        三大核心功能
            1利用gpu进行加速运算
                ```
                # cpu和gpu算力测试，1e6时gpu开始超过cpu
                n=100000
                with tf.device('/cpu:0'):
                    cpu_a=tf.random.normal([1,n])
                    cpu_b=tf.random.normal([n,1])
                    print(cpu_a.device,cpu_b.device)
                with tf.device('/gpu:0'):
                    gpu_a=tf.random.normal([1,n])
                    gpu_b=tf.random.normal([n,1])
                    print(gpu_a.device,gpu_b.device)
                def cpu_run():
                    with tf.device('/cpu:0'):
                        c=tf.matmul(cpu_a,cpu_b)
                    return c
                def gpu_run():
                    with tf.device('/gpu:0'):
                        c=tf.matmul(gpu_a,gpu_b)
                    return c
                cpu_time=timeit.timeit(cpu_run,number=10)
                gpu_time=timeit.timeit(gpu_run,number=10)
                print('warmup:',cpu_time,gpu_time)
                cpu_time=timeit.timeit(cpu_run,number=10)
                gpu_time=timeit.timeit(gpu_run,number=10)
                print('run_time:',cpu_time,gpu_time)
                ```python
            2自动梯度
                ```
                a=tf.constant(1.0)
                b=tf.constant(2.0)
                c=tf.constant(3.0)
                w=tf.constant(4.0)
                with tf.GradientTape() as tape:#构建梯度环境
                    tape.watch([w])#将w加入梯度跟踪列表
                    #构建计算过程，函数表达式
                    y=a*w**2+b*w+c
                [dy_dw]=tape.gradient(y,[w])
                print(dy_dw)
                ```python
            3常用神经网络接口
                内建了常用神经网络计算函数、常用网络层、网络训练、模型保存与加载、网络部署等一系列深度学习系统的便捷功能。

        cuda并不是针对于神经网络专门的GPU加速库，而是面向各种需要并行计算的应用设计。而cuDNN则是针对于神经网络应用加速
        
        ipython可以进入交互式终端
        使用tf.test.is_gpu_available()测试GPU是否可用

        TensorFlow在运行时，默认会占用所有的GPU显存资源，是非常不友好的行为，可以设置为增长式占用模式，根据实际模型大小申请显存资源
            gpus=tf.config.experimental.list_physical_devices('GPU')
            if gpus:
                try:
                    #设置GPU为增长式占用
                    for gpu in gpus:
                        tf.config.experimental.set_memory_growth(gpu,True)
                except RuntimeError as e:
                    print(e)

## 二、回归问题

    有些人担心人工智能会让人类觉得自卑，但是实际上，即使是看到一朵花，我们也应该或多或少感到一些自愧不如。——艾伦·凯

### 2.1 神经元模型

### 2.2 优化方法

    均方误差
    数值方法优化：暴力搜索、随机实验、梯度下降算法

### 2.3 线性模型

    以下为例子
    # y=1.477x+0.089+epsilon,N(0,0.01^2)
    # 采样数据
    data=[] #保存样本集
    for i in range (100):
        x=np.random.uniform(-10.,10.)
        eps=np.random.normal(0.,0.01)
        y=1.477*x+0.089+eps
        data.append([x,y])
    data=np.array(data)
    # 计算误差
    def  mse(b,w,points):
        totalError=0
        for i in range(0,len(points)):
            x=points[i,0]
            y=points[i,1]
            totalError+=(y-(w*x+b))**2
        return totalError/float(len(points))
    # 计算梯度
    def step_gradient(b_current,w_current,points,lr):
        b_gradient=0
        w_gradient=0
        M=float(len(points))
        for i in range(0,len(points)):
            x=points[i,0]
            y=points[i,1]
            b_gradient+=(2/M)*((w_current*x+b_current)-y)
            w_gradient+=(2/M)*x*((w_current*x+b_current)-y)
        new_b=b_current-(lr*b_gradient)
        new_w=w_current-(lr*w_gradient)
        return [new_b,new_w]
    # 梯度更新
    def gradient_decent(points,startint_b,starting_w,lr,num_iterations):
        b=startint_b
        w=starting_w
        for step in range(num_iterations):
            b,w=step_gradient(b,w,np.array(points),lr)
            loss=mse(b,w,points)
            if step%50 == 0:
                print(f"iteration:{step},loss:{loss},w:{w},b:{b}")
        return [b,w]
    def main():
        lr=0.01 #学习率
        initial_b=0
        initial_w=0
        num_iterations=1000
        [b,w]=gradient_decent(data,initial_b,initial_w,lr,num_iterations)
        loss=mse(b,w,data)
        print(f'Final loss:{loss},w:{w},b:{b}')
    if __name__=="__main__":
        main()

### 2.4 线性回归

## 三、分类问题

    在人工智能上花一年时间，这足以让人相信上帝的存在。——艾伦·佩利

### 3.1 手写数字图片数据集

    模型泛化能力：模型能够在新样本上也能具有良好的表现，应该尽可能多地增加数据集的规模和多样性。

    MINST数据集，并转化为Numpy数组
    from tensorflow import keras #导入TF子库keras
    from tensorflow.keras import layers,optimizers,datasets #导入TF子库

    gpus=tf.config.experimental.list_physical_devices('GPU')
    if gpus:
        try:
            #设置GPU为增长式占用
            for gpu in gpus:
                tf.config.experimental.set_memory_growth(gpu,True)
        except RuntimeError as e:
            print(e)

    (x,y),(x_val,y_val)=datasets.mnist.load_data()#加载MNIST数据集
    x=2*tf.convert_to_tensor(x,dtype=tf.float32)/255.-1#转化为浮点张量，并归一化
    y=tf.convert_to_tensor(y,dtype=tf.int32)
    y=tf.one_hot(y,depth=10)#ont hot编码
    print(x.shape,y.shape)
    train_dataset=tf.data.Dataset.from_tensor_slices((x,y))
    train_dataset=train_dataset.batch(512)
    load_data()函数返回两个tuple对象，一个是训练集，一个是测试集
    每一张图片的计算流程是通用的。用形状为[h,w]的矩阵来表示一张图片，添加一个数量维度，[b,h,w]，b代表Batch Size。彩色图片可用，[b,h,w,c] c for channel。tf的Dataset可以方便完成模型的批量训练，只需要调用batch()函数即可构建带batch功能的数据基对象

### 3.2 模型构建

    one-hot编码，避免数字编码模型主动学习输出结果数字大小关系。将输出设置为d_out个输出节点，每个节点值表示类别概率。但是会占用相对多的存储空间，所以可以在存储时使用数字编码，计算时转换即可。
        y=tf.constant([x1,x2,x3,x4])#数字编码
        tf.one_hot(y,depth=n)#转换为类别总数为n的onehot编码
    一般把输入经过一次(线性)变换称为一层网络

### 3.3 误差计算

    通过优化损失函数L来找到最优数值解
    但是线性模型较为简单，表达能力较弱

### 3.5 非线性模型

    可以给线性模型嵌套一个激活函数，例如Sigmoid、ReLU

### 3.6 表达能力

    通过重复堆叠多次变换，来增加表达能力
    深度学习框架，能够自动求导，完成梯度的自动计算和更新
    对数据集的所有样本迭代一遍叫做Epoch
    #网络搭建
    layers.Dense(256,activation='relu')
    model=keras.Sequential([
        layers.Dense(256,activation='relu'),
        layers.Dense(128,activation='relu'),
        layers.Dense(10),
    ])
    with tf.GradientTape() as tape:
        x=tf.reshape(x,(-1,28*28))#打平
        out=model(x)#模型输出
        y_onehot=tf.one_hot(y,depth=10)
        loss=tf.square(out-y_onehot)
        loss=tf.reduce_sum(loss)
    grads=tape.gradient(loss,model.trainabel_variables)
    optimizers.apply_gradients(zip(grads,model.trainable_variables))

## 四、TensorFlow基础

    我设想在未来，我们可能就相当于机器人的宠物狗，到那时我也会支持机器人的。——克劳德·香农

    TensorFlow是一个面向深度学习算法的科学计算库，内部数据保存在张量Tensor对象上，所有的运算操作(OP)也都是基于Tensor对象进行的。复杂的神经网络算法本质上就是各种张量相乘、相加等基本运算操作的组合。

### 4.1 数据类型

    数值类型
        数值类型的张量是TensorFlow的主要数据载体，根据维度来区分，可分为
            标量(Scalar)。单个的实数，维度数为0，shape为[]
            向量(Vector)。n个实数的有序集合，通过中括号包括，维度数为1，长度不定，shape为[n]
            矩阵(Matrix)。n行m列实数的有序集合，维度数为2，每个维度长度不定，shape为[n,m]
            张量(Tensor)。所有维度数dim>2的数组统称为张量。张量的每个维度也成为轴，一般维度代表了具体的物理含义。如果表示图片数据的话，每个维度/轴代表的含义为图片数量、图片高度和宽度的、图片通道数。张量的维度数和维度对应的物理意义需要由用户自行定义。
        TensorFlow为了表达方便，把标量、向量、矩阵统称为张量。
        TensorFlow创建标量
            a=1.2
            aa=tf.constant(1.2)
            print(type(a),type(aa),tf.is_tensor(aa))
            print(aa)
        通过print(x)可以输出张量x的相关信息
            id为TensorFlow中内部索引对象的编号，shape表示张量的形状，dtype表示张量的数值精度，张量numpy()方法可以返回Numpy.array类型的数据，方便导出数据到系统的其他模块。
        向量的定义必须通过List容器传给tf.constant()函数

    字符串类型
        a=tf.constant('string content')
        tf.strings模块提供了常见字符串类型的工具函数
            lower(a)小写化
            join(a)拼接
            length(a)长度
            split(a)切分

    布尔类型
        a=tf.constant(True)，同样可以创建向量，但是不能与Python的布尔类型等价

### 4.2 数值精度

    数值类型的张量，可以保存为不同字节长度的精度。常用的精度类型有tf.int16、tf.int32、tf.int64、tf.float16、tf.float32、tf.float64(即tf.double)'
    在创建张量时，可以指定张量的保存精度
        tf.constant(number,dtype=tf.numtype)
    对于大部分深度学习算法，一般使用tf.int32和tf.float32即可，部分对于精度要求较高的算法，如强化学习某些算法，可以使用64位
    读取精度
        通过访问张量的dtype属性可以判断保存精度
    类型转换
        tf.cast(a,tf.dtype)，需要注意转换操作的合法性，是否会发生溢出等
        布尔类型和整形之间转换也是合法的，非0即True

### 4.3 待优化张量

    区分需要计算梯度信息的张量和不需要计算梯度信息的张量，tf.Variable，增加了name,trainable等属性用以支持计算图的构建’
        a=tf.constant([-1,0,1,2])
        aa=tf.Variable(a)#转化为Variable类型
    name和trainable属性是Variable特有的属性，name属性用于命名计算图中的变量，这套命名体系是TensorFlow内部维护的。创建Variable对象默认启用优化标志
    待优化张量可视为普通张量的特殊类型，普通张量也可以通过GradientTape.watch()方法临时加入跟踪梯度信息的列表，从而支持自动求导功能

### 4.4 创建张量

    在TensorFlow中，可以通过多种方式来创建张量，如从Python列表对象创建，从Numpy数组创建，或者创建采样自某种已知分布的张量等
    从数组、列表对象创建
        tf.convert_to_tensor(list)
        tf.convert_to_tensor(np.array(list))
        Numpy浮点数数字默认使用64精度保存
        tf.constant()和tf.convert_to_tensor()等价，后者为tf1的命名习惯
    创建全0或全1张量
        tf.zeros(list),tf.ones(list)
        tf.zeros_like(a),tf.ones_like(a)#创建shape一致的，tf.zeros(a.shape)也可
        tf.*_like为一系列便捷函数
    创建自定义数组张量
        自定义数值初始化
            tf.fill(shape,value)#创建全为自定义数字value的张量，形状为shape
    创建已知分布的张量
        正态分布和均匀分布是最常见的分布
        tf.random.normal(shape,mean=0.,stddev=1.)#创建形状为shape，均值为mean，标准差为stddev的正态分布
        tf.random.uniform(shape,minval=0.,maxval=None,dtype=tf.float32)创建采样自[minval,maxval)的均匀分布的张量，数值类型为dtype
    创建序列
        tf.range(start=0,limit,delta=1)#创建[0,limit)之间，步长为delta的整型序列

### 4.5 张量的典型应用

    标量
        典型用途是误差值的表示、各种测量指标的表示，比如准确度、精度和召回率
        tf.keras.losses.mse(或tf.keras.lossed.MSE，功能相同)返回样本误差值，取平均作为batch误差
            out=tf.random.uniform([4,10])
            y=tf.constant([2,3,2,0])
            y=tf.one_hot(y,depth=10)
            loss=tf.keras.losses.mse(y,out)
            loss=tf.reduce_mean(loss)
            print(loss)
    向量
        例如在全连接层和卷积神经网络层中，偏置张量b使用向量表示
            z=tf.random.normal([4,2])
            b=tf.zeros([2])
            z=z+b
        z和b能够直接相加，与Broadcasting相关
        通过高层接口类Dense()方式创建的网络层， 张量w和b存储在类的内部，由类自动创建并管理。
            fc=layers.Dense(3)
            fc.build(input_shape=(2,4))
            fc.bias
    矩阵
        例如全连接层的批量输入张量X的形状为[b,d_in]，b为输入样本的个数，Batch Size，d_in表示输入特征的长度
            x=tf.random.normal([2,4])
            w=tf.ones([4,3])
            b=tf.zeros([3])
            o=x@w+b
        上述代码实现了线性变换的网络层，激活函数为空。TensorFlow可以通过Dense类直接实现σ(X@W+b)全连接层。
            fc=layers.Dense(3)
            fc.build(input_shape=(2,4))
            fc.kernel
    三维张量
        典型应用为表示序列信号
            X=[b,sequence len,feature len]
            b表示序列信号的数量，sequence len表示序列信号在时间维度上的采样点数或步数，feature len表示每个点的特征长度
        为了能够方便字符串被神经网络处理，一般将单词通过嵌入层编码为固定长度的向量。
            (x_train,y_train),(x_test,y_test)=keras.datasets.imdb.load_data(num_words=10000)#自动加载IMDB电影评价数据集
            x_train=keras.preprocessing.sequence.pad_sequences(x_train,maxlen=80)#将句子填充、截断为等长80个单词的句子
            x_train.shape
        通过layers.Embedding层将数字编码的单词转换为长度为100的词向量
            embedding=layers.Embedding(10000,100)
            out=embedding(x_train)
            out.shape
    四维张量
        大于四维的张量一般应用的比较少，如在元学习中会采用五维的张量表示方法。
        四维张量在卷积神经网络中应用非常广泛，用于保存特征图数据，[b,h,w,c]
            b表示输入样本的数量，h/w分别表示特征图的高/宽，c表示特征图的通道数，部分深度学习框架也会使用[b,c,h,w]格式的特征图张量，例如PyTorch。
        神经网络中一般并行计算多个输入以提高计算效率，b张图片的张量[b,h,w,3]
            x=tf.random.normal([4,32,32,3])#创建彩色图片输入
            layers=layers.Conv2D(16,kernel_size=3)#创建卷积神经王路平
            out=layers(x)
            out.shape
            layers.kernel.shape#此处环境搭建可能出现问题，需要安装zlib，并创建对应的环境变量

### 4.6 索引与切片

    通过索引和切片操作可以提取张量的部分数据，使用频率较高
    索引
        TF支持基本的[i][j]...标准索引形式，也支持通过逗号分隔索引号的索引方式。
            [1][2][3]==[1,2,3]
    切片
        通过start:end:step切片方式可以提取一段数据，不含end，step默认为1
            [1:3]==[1:3:1],[0,::]==[0]==[0,:],::可以简写为:
        隔行隔列采样，相当于图片缩放
            start:读取后续所有元素
            :end读到end，不含end
            ::step,::,:
        start,end,step都可以为负数，实现逆序、快速框取
        ...用以避免[:,:,:]过多冒号，...左边的维度自动对齐到左边，右边亦然

### 4.7 维度变换

    神经网络运算过程中，维度变换是最核心的张量操作，通过维度变换可以将数据任意地切换形式。
    线性层的批量形式：Y=X@W+b
    算法的每个模块对于数据张量的格式有不同的逻辑要求，当现有的数据格式不满足算法要求时，需要通过维度变换将数据调整为正确的格式。
    维度变换操作函数包含了改变视图reshape、插入新维度expand_dims、删除维度squeeze、交换维度transpose、复制数据tile等函数
    改变视图
        张量的视图是理解张量形式的方式，张量的存储体现在张量在内存上保存为一段连续的内存区域。同一个存储，从不同的角度观察数据，可以产生不同的视图。
            tf.reshape(x,[dims])返回维度变换后的结果，维度为-1时表示该轴长度根据张量总元素不变的法则自动推导
        在存储数据时，内存不支持维度层级概念，只能以平铺方式按序写入内存
        数据在创建时按照初始的维度顺序写入，改变张量的视图仅仅改变了张量的理解方式，并不需要改变张量的存储顺序。改变视图操作的默认前提是存储不需要改变，否则改变视图操作就是非法的。
        从语法上说，视图变换只需要满足新视图的元素总量与存储区域大小相等，维度顺序和存储顺序不能冲突
        正确使用视图变换，可以跟踪存储的维度顺序。
        可以通过张量的ndim和shape成员属性获得张量的维度数和形状
    增、删维度
        增加维度：数据不需要改变，只是改变数据的理解方式，可以理解为改变视图的特殊方式
            tf.expand_dims(x,axis)在指定的轴前插入新的维度，axis为正表示在当前维度前插入，为负表示之后，即0和-(n+1)插入位置相同，n为维度数
        删除维度：增加维度的逆操作，
            tf.squeeze(x,axis)，不指定维度，将会删除所有长度为1的维度
    交换维度
        有时需要直接调整的存储顺序，即交换维度，改变存储顺序和张量视图
        tf.transpose(x,perm)，perm为维度顺序如[0,3,1,2]
    复制数据
        在指定维度上复制数据
            tf.tile(x,multiples)，multiples分别指定了每个维度的复制倍数，如[2,1]将维度0复制到维度1
        自动扩展也能实现插入维度和复制数据
        tf.tile不会使维度发生变化，只是使维度长度变化，并且x必须大于一个维度
        tf.tile会创建一个新的张量来保存复制后的张量，涉及大量数据的读写IO运算，计算代价较高

### 4.8 Broadcasting

    Broadcasting称为广播机制(或自动扩展机制)，一种轻量级的张量复制手段，在逻辑上扩展张量数据的形状，只会在需要时才执行实际存储复制操作。对于大部分场景，Broadcasting机制都能通过优化手段避免实际复制数据而完成逻辑运算。
    对于所有长度为1的维度，和tf.tile一样，在此维度上逻辑复制数据若干份，在逻辑上改变张量的形状，使得视图上变成了复制后的形状。Broadcasting会通过深度学习框架的优化手段避免实际复制数据而完成逻辑运算。
    不同shape的张量直接相加，就是自动调用Broadcasting函数tf.broadcast_to(x,new_shape)扩展为相同的shape，然后再调用tf.add完成张量相加运算
    该机制并不会扰乱正常的计算逻辑，只会针对最常见的场景自动完成增加维度并复制数据的功能。核心思想是普适性，即一份数据能普遍适合于其他位置。将张量shape向右对齐，长度为1的维度，默认数据普遍适合于当前维度的其他位置；不存在的维度，增加新维度后默认当前数据也普适于新维度，可以扩展为更多维度数、任意长度的张量形状
        tf.broadcast_to(x,new_shape)，显式执行自动扩展
    +-*/等能够自动调用该机制

### 4.9 数学运算

    加减乘除运算
        分别通过tf.add,tf.subtract,tf.multiply,tf.divide实现，TF已经重载了+-*/运算符
        整除//，余除%
    乘方运算
        tf.pow(x,a)可以完成y=x^a的乘方运算，重载到x**a
        指数为1/a则实现开a方根
        平方tf.square(x)，平方根tf.sqrt(x)
    指数和对数运算
        tf.pow(a,x)或a**x
        对于自然指数tf.exp(x)
        自然对数log_e(x)，tf.math.log(x)实现，利用换底公式能够计算其他底数的对数
    矩阵相乘运算
        @或tf.matmul(a,b)，矩阵相乘可以使用批量方式，即A和B的维度数可以大于2，TF会选择A和B最后两个维度进行矩阵相乘。
        A和B需要满足A最后一个维度长度于B倒数第二个维度长度相等
        矩阵相乘函数同样支持自动Broadcasting机制

### 4.10 前向传播实战

    实现三层神经网络
        out=ReLU{ReLU{ReLU[X@W1+b1]@W2+b2}@W3+b3}
        
        (x,y),(x_val,y_val)=datasets.mnist.load_data()#加载MNIST数据集
        x=2*tf.convert_to_tensor(x,dtype=tf.float32)/255.-1#转化为浮点张量，并归一化
        y=tf.convert_to_tensor(y,dtype=tf.int32)
        train_dataset=tf.data.Dataset.from_tensor_slices((x,y))
        train_dataset=train_dataset.batch(512)
        lr=0.01
        loss=1
        # 每层的张量都需要被优化，故使用Variable 类型，并使用截断的正太分布初始化权值张量 
        # 偏置向量初始化为0 即可 
        # 第一层的参数 
        w1 = tf.Variable(tf.random.truncated_normal([784, 256], stddev=0.1)) 
        b1 = tf.Variable(tf.zeros([256])) 
        # 第二层的参数 
        w2 = tf.Variable(tf.random.truncated_normal([256, 128], stddev=0.1)) 
        b2 = tf.Variable(tf.zeros([128])) 
        # 第三层的参数 
        w3 = tf.Variable(tf.random.truncated_normal([128, 10], stddev=0.1)) 
        b3 = tf.Variable(tf.zeros([10]))
        while loss>0.1:
            with tf.GradientTape() as tape:
                # 改变视图，[b, 28, 28] => [b, 28*28] 
                x = tf.reshape(x, [-1, 28*28])
                # 第一层计算，[b, 784]@[784, 256] + [256] => [b, 256] + [256] => [b, 256] + [b, 256] 
                h1 = x@w1 + tf.broadcast_to(b1, [x.shape[0], 256]) 
                h1 = tf.nn.relu(h1) # 通过激活函数
                # 第二层计算，[b, 256] => [b, 128] 
                h2 = h1@w2 + b2 
                h2 = tf.nn.relu(h2) 
                # 输出层计算，[b, 128] => [b, 10] 
                out = h2@w3 + b3 
                # 计算网络输出与标签之间的均方差，mse = mean(sum(y-out)^2) 
                # [b, 10] 
                y_onehot=tf.one_hot(y,depth=10)#ont hot编码
                loss = tf.square(y_onehot - out) 
                # 误差标量，mean: scalar 
                loss = tf.reduce_mean(loss)
                print(loss) 
            # 自动梯度，需要求梯度的张量有[w1, b1, w2, b2, w3, b3] 
            grads = tape.gradient(loss, [w1, b1, w2, b2, w3, b3])
            # 梯度更新，assign_sub 将当前值减去参数值，原地更新 
            w1.assign_sub(lr * grads[0]) 
            b1.assign_sub(lr * grads[1]) 
            w2.assign_sub(lr * grads[2]) 
            b2.assign_sub(lr * grads[3]) 
            w3.assign_sub(lr * grads[4]) 
            b3.assign_sub(lr * grads[5])
        # 改变视图，[b, 28, 28] => [b, 28*28] 
        x=2*tf.convert_to_tensor(x_val,dtype=tf.float32)/255.-1#转化为浮点张量，并归一化
        x = tf.reshape(x, [-1, 28*28])
        y=tf.convert_to_tensor(y_val,dtype=tf.int32)
        # 第一层计算，[b, 784]@[784, 256] + [256] => [b, 256] + [256] => [b, 256] + [b, 256] 
        h1 = x@w1 + tf.broadcast_to(b1, [x.shape[0], 256]) 
        h1 = tf.nn.relu(h1) # 通过激活函数
        # 第二层计算，[b, 256] => [b, 128] 
        h2 = h1@w2 + b2 
        h2 = tf.nn.relu(h2) 
        # 输出层计算，[b, 128] => [b, 10] 
        out = h2@w3 + b3 
        y=tf.one_hot(y_val,depth=10)
        print(y.shape)
        for i in range(y.shape[0]):
            print(out[i].array(),y[i].array())

## 五、TensorFlow进阶

    人工智能将是谷歌的最终版本。它将称为终极搜索引擎，可以理解网络上的一切信息。它会准确地理解你想要什么，给你需要的东西。——拉里·佩奇

### 5.1 合并与分割

    合并
        将多个张量在某个维度上合称为一个张量。
        张量的合并可以使用拼接和堆叠操作实现，拼接操作并不会产生新的维度，仅在现有的维度上合并，而堆叠会创建新维度。
        拼接：tf.concat(tensors,axis)，tensors保存了所有需要合并的张量List，axis参数指定需要合并的维度索引，不进行拼接的维度需要长度一致
        堆叠：tf.stack(tensors,axis)，axis指定插入的位置，与tf.expand_dims用法一致
        同样需要满足张量堆叠合并条件，否则出现InvalidArgumentError错误
    分割
        合并操作的逆过程，将一个张量拆分为多个
            tf.split(x,num_or_size_splits,axis)
                x为待分割张量，axis指定分割的维度索引
                num_or_size_splits为切割方案，为单个数值时表示等长切割，为List表示切割成对应份数和长度
            tf.unstack(x,axis)，能够在某个维度上全部分割为1

### 5.2 数据统计

    向量范数
        L0范数，向量x中非零元素的个数
        L1范数，向量x的所有元素绝对值之和
        L2范数，向量x的所有元素的平方和
        ∞-范数，向量x的所有元素绝对值的最大值
        矩阵和张量可以先打平成向量后再计算
            tf.norm(x,ord)，ord=1计算L1，=2计算L2，=np.inf计算∞
    最值、均值、和
        通过tf.reduce_max、tf.reduce_min、tf.reduce_mean、tf.reduce_sum函数可以求解张量在某个维度上或全局的最大、最小、均值、和
        不指定axis参数时，tf.reduce_*会求出全局元素的最大、最小、均值、和等数据
            tf.nn.softmax(x,axis)能够转化为概率值，可应用与求解最大值的索引号
            tf.argmax(x,axis)和tf.argmin(x,axis)可以求解在axis轴上，x的最大值、最小值所在的索引号

### 5.3 张量比较

    tf.equal(x,y)，相同维度和长度的张量比较，返回比尔类型
    tf.math.greater()
    tf.math.less()
    tf.math.greater_equal()
    tf.math.less_equal()
    tf.math.not_equal()
    tf.math.is_nan()

### 5.4 填充与复制

    填充
        对于图片数据的高和宽、序列信号的长度，维度长度可能各不相同。为了方便网络的并行计算，需要将不同长度的数据扩张为相同长度。重复复制数据会破坏原有的数据结构，在需要补充长度的数据开始或结束处填充足够数量的特定数值，一般代表无效意义，
            tf.pad(x,padding)，padding包含多个[left padding,right padding]的嵌套方案List，如[[0,2],[1,1]]表示第一个维度左侧不加、右侧加2，第二个维度左侧右侧加1
        对于IMDB数据集的处理
            x_train = keras.preprocessing.sequence.pad_sequences(x_train, 
maxlen=max_review_len,truncating='post',padding='post')
            设定了末尾填充和末尾截断方式
    复制
        tf.tile可以在任意维度将数据重复复制多份

### 5.5 数据限幅

    实现非线性激活函数ReLU，可以通过简单的数据限幅来实现，限制元素的范围在x[0,+∞)
        tf.maximum(x,a)实现数据的下限幅，tf.minimum(x,a)实现数据的上限幅
        tf.clip_by_value(x,min,max)同时实现上下限幅

### 5.6 高级操作

    tf.gather
        实现根据索引号收集数据
            tf.gather(x,[range],axis)在axis维度收集range范围的数据
        也可以通过切片实现，但gather能够对离散范围进行取样，适合索引号没有规则，索引号可以乱序排列
        可以手动提取数据，然后利用stack合并
    tf.gather_nd
        通过指定每次采样点的多维坐标来实现采样多个点的目的。
            tf.gather_nd([points])，如([[1,1],[2,2],[3,3]])
    tf.boolean_mask
        掩码采样
            tf.boolean_mask(x,mask=[...],axis)，掩码长度必须与对应维度的长度一样，如[True,False]或[[True,False],[True,False]]
    tf.where
        根据条件的真假从参数A或B中读取数据
            tf.where(cond,a,b),cond为真取a，cond为假取b
            不加ab时，返回cond中为True的元素索引
        可以用于提取张量中满足条件的数据和索引
    scatter_nd
        高效地刷新张量的部分数据，但只能在全0的白板张量上执行
            tf.scatter_nd(indices,updates,shape)，indices为updates中数据对应的插入位置
    meshgrid
        生成二维网格的采样点坐标
            tf.meshgrid(x,y)
        返回在axis=2维度切割后的两个张量A和B，分别对应x坐标和y坐标
        通过matplotlib库可绘制出3D曲面

### 5.7 经典数据集加载

    keras.datasets模块提供了常用经典数据集的自动下载、管理、加载与转换功能，并并且提供了tf.data.Dataset数据集对象，方便实现多线程、预处理、随机打散和批训练等常用数据集的功能
        Boston Housing，波士顿房价趋势数据集，用于回归模型训练与测试
        CIFAR10/100，真实图片数据集，用于图片分类任务
        MNIST/Fashion_MNIST，手写数字图片数据集，用于图片分类任务
        IMDB，情感分类任务数据集，用于文本分类任务
    对于新提出的算法，一般优先在经典的数据集上面测试，再尝试迁移到更大规模、更复杂的数据集上
        通过datasets.xxx.load_data()函数即可实现经典数据集的自动加载。TensorFlow会默认将数据缓存在用户目录下的.keras/datasets文件夹。如果数据集不在缓存中，会自动从网络下载、解压和加载数据集。所有的数据都用NUmpy数组容器保存
        数据加载进入内存后，需要转换为Dataset对象，才能利用TF。通过Dataset.from_tensor_slices将训练部分的数据图片x和标签y都转换成Dataset对象
            tf.data.Dataset.from_tensor_slices((x,y))
    随机打散
        设置Dataset对象随机打散数据之间的顺序，防止每次训练时数据按固定顺序产生，从而使得模型尝试"记忆"住标签信息
            train_db.shuffle(buffer_size)，不会打乱样本与标签之间的关系
    批训练
        为了利用显卡的并行计算能力，一般在网络的计算过程中会同时计算多个样本。
        一个批样本中的数量称为Batch Size。
            db.batch(batch_size)
            batch size一般根据用户的GPU现存资源来设置。
    预处理
        从keras.datasets中加载的数据集的格式大部分情况下不能直接满足模型的输入要求，需要根据用户的逻辑自行实现预处理步骤。Dataset对象通过提供map(func)工具函数，可以调用用户自定义的预处理逻辑。
            train_db.map(preprocess)
        对于MNIST图片数据，可以这样预处理
            def preprocess(x, y): # 自定义的预处理函数 
            # 调用此函数时会自动传入x,y 对象，shape 为[b, 28, 28], [b]  
                # 标准化到0~1 
                x = tf.cast(x, dtype=tf.float32) / 255. 
                x = tf.reshape(x, [-1, 28*28])     # 打平 
                y = tf.cast(y, dtype=tf.int32)    # 转成整型张量 
                y = tf.one_hot(y, depth=10)    # one-hot 编码 
                # 返回的x,y 将替换传入的x,y 参数，从而实现数据的预处理功能 
                return x,y
    循环训练
        对于Dataset对象，可以通过
            for step,(x,y) in enumerate(train_db):
        或  for x,y in train_db
        每次x和y对象为批量样本和标签
        通过多个step来完成整个训练集的一次迭代，称为一个Epoch。在实际训练时，通常需要对数据集迭代多个Epoch才能取得较好的训练效果
            for epoch in range(20):
                ...

### 5.8 MNIST测试实战

    def preprocess(x, y): # 自定义的预处理函数 
    # 调用此函数时会自动传入x,y 对象，shape 为[b, 28, 28], [b]  
        # 标准化到0~1 
        x = tf.cast(x, dtype=tf.float32) / 255. 
        x = tf.reshape(x, [-1, 28*28])     # 打平 
        y = tf.cast(y, dtype=tf.int32)    # 转成整型张量 
        y = tf.one_hot(y, depth=10)    # one-hot 编码 
        # 返回的x,y 将替换传入的x,y 参数，从而实现数据的预处理功能 
        return x,y 

    batch_size=128
    (x_tra,y_tra),(x_val,y_val)=datasets.mnist.load_data()#加载MNIST数据集
    train_db=tf.data.Dataset.from_tensor_slices((x_tra,y_tra))
    test_db=tf.data.Dataset.from_tensor_slices((x_val,y_val))
    train_db=train_db.shuffle(10000)
    train_db=train_db.batch(batch_size)
    test_db=test_db.batch(batch_size)
    train_db = train_db.map(preprocess)
    test_db = test_db.map(preprocess)

    lr=0.01
    loss=1
    # 每层的张量都需要被优化，故使用Variable 类型，并使用截断的正太分布初始化权值张量 
    # 偏置向量初始化为0 即可 
    # 第一层的参数 
    w1 = tf.Variable(tf.random.truncated_normal([784, 256], stddev=0.1)) 
    b1 = tf.Variable(tf.zeros([256])) 
    # 第二层的参数 
    w2 = tf.Variable(tf.random.truncated_normal([256, 128], stddev=0.1)) 
    b2 = tf.Variable(tf.zeros([128])) 
    # 第三层的参数 
    w3 = tf.Variable(tf.random.truncated_normal([128, 10], stddev=0.1)) 
    b3 = tf.Variable(tf.zeros([10]))
    for epoch in range(20): # 训练Epoch 数 
        for step, (x,y) in enumerate(train_db): # 迭代Step 数
            with tf.GradientTape() as tape:
                # 第一层计算，[b, 784]@[784, 256] + [256] => [b, 256] + [256] => [b, 256] + [b, 256] 
                h1 = x@w1 + b1 
                h1 = tf.nn.relu(h1) # 通过激活函数
                # 第二层计算，[b, 256] => [b, 128] 
                h2 = h1@w2 + b2 
                h2 = tf.nn.relu(h2) 
                # 输出层计算，[b, 128] => [b, 10] 
                out = h2@w3 + b3 
                # 计算网络输出与标签之间的均方差，mse = mean(sum(y-out)^2) 
                loss = tf.square(y - out) 
                # 误差标量，mean: scalar 
                loss = tf.reduce_mean(loss)
            if step % 100 == 0: 
                print(step, 'loss:', float(loss))
            # 自动梯度，需要求梯度的张量有[w1, b1, w2, b2, w3, b3] 
            grads = tape.gradient(loss, [w1, b1, w2, b2, w3, b3])
            # 梯度更新，assign_sub 将当前值减去参数值，原地更新 
            w1.assign_sub(lr * grads[0]) 
            b1.assign_sub(lr * grads[1]) 
            w2.assign_sub(lr * grads[2]) 
            b2.assign_sub(lr * grads[3]) 
            w3.assign_sub(lr * grads[4]) 
            b3.assign_sub(lr * grads[5])
            if step % 500 == 0:
                total_correct=0
                total=0
                for x, y in test_db: # 对测验集迭代一遍  
                    h1 = x @ w1 + b1 # 第一层 
                    h1 = tf.nn.relu(h1) # 激活函数 
                    h2 = h1 @ w2 + b2 # 第二层 
                    h2 = tf.nn.relu(h2) # 激活函数 
                    out = h2 @ w3 + b3 # 输出层
                    pred = tf.argmax(out, axis=1) # 选取概率最大的类别
                    y = tf.argmax(y, axis=1) # one-hot 编码逆过程
                    correct = tf.equal(pred, y) # 比较预测值与真实值
                    total_correct += tf.reduce_sum(tf.cast(correct, dtype=tf.int32)).numpy() # 统计预测正确的样本个数
                    total+=batch_size
                print(step, 'Evaluate Acc:%.4f'%(total_correct/total)) 

    代码中需要注意，训练和测试集都需要进行预处理、分批。所以测试机需要逆onehot
    可以增加数据增强环节、精调网络超参数等技巧，获得更高的模型性能

## 六、神经网络

    很难想象哪一个大行业不会被人工智能改变。人工智能会在这些行业里发挥重大作用，这个走向非常明显。——吴恩达
    机器学习的最终目的是找到一组良好的参数θ，使得θ表示的数学模型能够很好地从训练集中学到映射关系f_θ:x→y,x,y∈D^{train}。神经网络属于机器学习的一个研究分支，特指利用多个神经元去参数化映射函数f_θ的模型

### 6.1 感知机

    感知机模型，接受长度为m的一维向量x=[x1,x2,...,xn]，每个输入节点通过权值为wi,i∈[1,n]的连接汇集为变量z，并加上常数偏置b，z称为感知机的净活性值
    感知机为线性模型，不能处理线性不可分问题。通过在线性模型后添加激活函数后得到活性值a=σ(z)，激活函数可以是阶跃函数、符号函数
    添加激活函数后，感知机可以完成二分类任务。阶跃函数和符号函数在z=0处不连续，其他位置导数为0，无法利用梯度下降算法进行参数优化。
    感知训练算法
        初始化参数w=0，b=0
        repeat
            从训练集随机采集一个样本(xi,yi)
            计算感知机的输出a=sign(W^Txi+b)
            如果a≠yi:
                w'=w+η·yi·xi //η为学习率
                b'=b+η·yi
        until 训练次数达到要求
        输出：分类网络参数w和b
        感知据不能解决异或等线性不可分问题，但是可以通过嵌套多层神经网络解决

### 6.2 全连接层

    现代深度学习的核心结构与感知机并没有多大差别。它在感知机的基础上，将不连续的阶跃激活函数换成了其他平滑连续可导的激活函数，并通过堆叠多个网络层来增强网络的表达能力
    通过替换感知机的激活函数，同时并行堆叠多个神经元来实现多输入、多输出的网络层结构。
        O=X@W+b
    每个输出节点与全部的输入节点相连接，称为全连接层，或稠密连接层，W矩阵称为全连接层的权值矩阵，b向量为全连接层的偏置向量
    张量方式实现
        要实现全连接层，只需要定义好权值张量W和偏置张量b，并利用批量矩阵相乘函数tf.matmul()即可
    层方式实现
        全连接层本质上是矩阵的相乘和相加运算。作为最常用的网络层之一，TF有更高层、使用更方便的层实现方式
            layers.Dense(unit,activation)
        通过layer.Dense类，只需要指定输出节点数Units和激活函数类型activation。输入节点数会根据第一次运算时的输入shape确定，同时根据输入、输出节点数自动创建并初始化权值张量W和偏置张量b，因此在新建类Dense实例时，并不会立即创建张量W和偏置张量b，而是需要调用build函数或者直接进行一次前向计算，才能完成网络参数的创建。activation参数指定当前层的激活函数，可以为常见的激活函数或自定义激活函数，也可以指定为None
            # 创建全连接层，指定输出节点数和激活函数 
            fc = layers.Dense(512, activation=tf.nn.relu)  
            h1 = fc(x)  # 通过fc 类实例完成一次全连接层的计算，返回输出张量
        可以通过类内部的成员名kernel和bias来获取权值张量W和偏置张量b对象
        fc.trainable_variables可以获得网络的所有待优化的张量参数列表
        网络层除了保存待优化张量列表trainable_variables，还有部分层包含了不参与梯度优化的张量，例如Batch Normalization层，通过non_trainable_variables成员返回所有不需要优化的参数列表。variables成员返回所有内部张量列表，对于全连接层，内部张量都参与梯度优化。
        利用网络层类对象进行前向计算，只需要调用类的__call__方法，fc(x)会自动调用类的__call__方法，在__call__方法中会自动调用call方法。对于全连接层类，在call方法中实现σ(X@W+b)的运算逻辑。

### 6.3 神经网络

    通过层层堆叠全连接层，保证前一层的输出节点数与当前层的输入节点数匹配，即可堆叠出任意层数的网络，将由神经元相互连接而成的网络称为神经网络，每层均为全连接层的称为全连接网络。输入和输出层之间的层之间的层称为隐藏层，输出层不计入总层数。
    设计全连接网络时，网络的结构配置等超参数可以按照经验法则自由设置，只需要遵循少量的约束。例如，隐藏层1的输入节点数与数据的实际特征长度匹配，每层的输入层节点数与上一层输出节点数匹配，输出层的激活函数和节点数需要根据任务的具体设定进行设计。结构设计自由度较大，最优超参数需要领域经验知识和实验尝试，或者可以通过AutoML技术搜索出较优设定
    张量方式实现
        对于多层神经网络，需要分别定义各层的权值W和偏置向量b，还需要根据全连接层数目定义W和b，并且需要防止混淆
        计算时只需要按照网络层顺序进行输入输出。
        在使用TF自动求导功能计算梯度时，需要将前向计算过程放置在tf.GradientTape()环境中，从而利用GradientTape对象的gradient()方法自动求解参数的梯度，并利用optimizers对象更新参数
    层方式实现
        对于常规网络层，通过层方式实现起来更加简洁高效。建立各个网络层类，并指定各层的激活函数类型后，在前向计算时，依序通过各个网络层即可。
        对于数据依次向前传播的网络，也可以通过Sequential容器封装成一个网络大类对象，调用大类的前向计算函数一次即可完成所有层的前向计算
            from tensorflow.keras import layers,Sequential 
            #  通过Sequential 容器封装为一个网络类 
            model = Sequential([ 
                layers.Dense(256, activation=tf.nn.relu) , # 创建隐藏层1 
                layers.Dense(128, activation=tf.nn.relu) , # 创建隐藏层2 
                layers.Dense(64, activation=tf.nn.relu) , # 创建隐藏层3 
                layers.Dense(10, activation=None) , # 创建输出层 
            ])
            out = model(x) #  前向计算得到输出
    优化目标
        把神经网络从输入到输出的计算过程称为前向传播或前向计算。神经网络的前向传播过程，也是数据张量(Tensor)从第一层流动(Flow)到输出层的过程。
        前向传播的最后一个就是完成误差的计算
            L=g(f_θ(x),y),f_θ(·)代表θ参数化的神经网络模型，g(·)称为误差函数，可以是均方差误差函数。L为网络误差，一般为标量，目标是使L最小
        最小化优化问题一般采用误差反向传播(Backward Propagation,BP)算法来求解网络参数θ的梯度信息，并利用梯度下降(Gradient Descent,GD)算法迭代更新参数
            θ'=θ-η·▽_ΘL
        神经网络也可以理解成完成特征的维度变换的功能，得到的特征一般包含了任务强相关的高层抽象特征信息，通过对这些特征进行简单的逻辑判定即可完成特定的任务
        网络的参数量是衡量网络规模的重要指标，权值矩阵W=din·dout，偏置向量b=dout

### 6.4 激活函数

    神经网络中常见激活函数，都是平滑可导的
    Sigmoid
        也成为Logistic函数，Sigmoid(x)=1/(1+e^(-x))
        能够把实数输入压缩到(0,1)区间，该区间在机器学习中表示
            概率分布(0,1)区间的输出和概率的分布范围[0,1]契合，可以通过Sigmoid函数将输出转译为概率输出
            信号强度，可以将0~1理解为某种信号的强度，例如颜色、门控值
        tf.nn.sigmoid(x)实现函数
    ReLU
        Sigmoid在输入值较大或较小时容易出现梯度值接近于0的现象，称为梯度弥散，使得网络参数长时间得不到更i性能，导致训练不收敛或停滞不动，较深层次的网络模型更容易出现。
        ReLU(REctified Linear Unit,线性修正单元)，使得网络层数达到8层
            ReLU(x)=max(0,x)
        单边抑制特性，与脑神经元激活模型类似
        tf.nn.relu(x)实现函数
        除了使用函数接口，还可以像Dense层一样将ReLU函数作为一个网络层添加到网络中，对应layers.ReLU()类，激活函数类不计入网络层数。
    LeakyReLU
        ReLU函数在x<0时导数恒为0，也可能造成梯度弥散。
            LeakyReLU=x(x≥0)    px(x<0),p较小
        tf.nn.Leaky_relu(x,alpha)
        对应类为layers.LeakyReLU，可以通过LeakyReLU(alpha)创建网络层
    Tanh
        Tanh能够将实数输入压缩到(-1,1)
            tanh(x)=(e^x-e^(-x))/(e^x+e^(-x))=2·sigmoid(2x)-1
        tf.nn.tanh(x)实现函数

### 6.5 输出层设计

    输出层除了与隐藏层一样，完成维度变换、特征提取的功能，还作为输出层，根据具体任务场景决定使用激活函数
    根据输出值的区间范围来分类讨论
        输出属于整个实数空间，或某段普通实数空间，如函数值趋势、年龄的预测
        输出值特别地落在[0,1]区间，如图片生成、二分类
        输出值在[0,1]区间，且总和为1，如多分类
        输出值在[-1,1]
    普通实数空间
        如正弦函数曲线预测、年龄预测、股票走势预测等都属于整个或部分连续的实数空间，输出层可以不加激活函数。误差的计算直接基于最后一层的输出o和真实值y进行计算
    [0,1]区间
        在机器学习中，一般会将图片的像素值归一化到[0,1]区间，可以使用Sigmoid函数
        二分类问题可以在输出层只设置一个节点，或者可以分别预测A和非A，并满足概率和为1
    [0,1]区间，和为1
        可以使用Softmax(zi)=e^(zi)/Σe^(zj),j∈[1,dout]
        tf.nn.softmax(z)实现函数，通过layers.Softmax(axis=-1)添加，axis指定需要进行计算的维度
        在Softmax函数的数值计算过程中，容易因输入值偏大发生数值溢出现象，在计算交叉熵时，也会出现数值溢出。为了数值计算稳定性，TF提供了统一接口，将Softmax和交叉熵损失函数同时实现，同时处理了数值不稳定的异常，一般推荐使用这些接口函数
            tf.keras.losses.categorical_crossentropy(y_true,y_pred,from_logits=False)
                y_true为One-hot编码后的真实标签，y_pred表示网络预测值
                from_logits为True，y_pred表示未经过Softmax函数的变量z
                from_logits为False，y_pred表示经过Softmax函数的输出
            一般将from_logits设置为True，该接口函数将在内部进行Softmax计算
        同样能够用keras.losses.CategoricalCrossentropy(from_logits)同时实现Softmax与交叉熵损失函数的计算
    [-1,1]
        可以使用tanh激活函数

### 6.6 误差计算

    常见的误差函数有均方差、交叉熵、KL散度、Hinge Loss函数，均方差和交叉熵在深度学习中比较常见，前者用于回归，后者用于分类
    均方差误差函数
        均方差(Mean Squared Error,MSE) 误差函数把输出向量和真实向量映射到笛卡尔坐标系的两个点上，计算二者欧氏距离的平方，MSE误差函数值总是≥0，=0时达到最优
        分类问题也可应用均方误差函数。
        函数方式实现：keras.losses.MES(y_onehot,o)，需要再次平均得到平均样本均方差，tf.reduce_mean(loss)
        层方式实现：keras.losses.MeanSquaredError()，调用__call__函数即可
            criteon(y_onehot,x)
    交叉熵误差函数
        熵越大，不确定性越大，信息量越大，onehot编码的熵为0
            H(P)=-ΣP(i)log_2P(i)
        用tf.math.log来计算熵
        交叉熵：H(p||q)=-Σp(i)log_2q(i)，可以分解为p的熵加上p与q的KL散度
            D_KL(p||q)=Σp(i)log(p(i)/q(i))
        交叉熵和KL散度都不对称，如果p采用onehot编码，二者相等且
            H(p||q)=D_KL(p||q)=-logo_i
        最小化交叉熵损失函数的过程也是最大化正确类别的预测概率的过程

### 6.7 神经网络类型

    全连接层是神经网络最基本的网络类型，最大的缺陷是在处理较大特征长度的数据时，参数量较大，使得深层次的全连接网络参数量巨大，训练较为困难。
    卷积神经网络
        通过利用局部相关性和权值共享的思想，得到卷积神经网络，在计算机视觉中呈现统治态势。比较流行的模型有图片分类的AlexNet、VGG、GoogleNet、ResNet、DenseNet等，用于目标识别的RCNN、Fast RCNN、Faster RCNN、Mask RCNN、YOLO、SSD等
    循环神经网络
        除了具有空间结构的图片、视频等数据外，序列信号也是非常常见的一种数据类型，例如文本数据。卷积神经网络缺乏Memory机制和处理不定长序列信号的能力。循环神经网络(Recurrent Neural Network,RNN)擅长处理序列信号。LSTM是RNN的变种，克服了RNN缺乏长期记忆、不擅长处理长序列的问题。Google基于LSTM提出用于机器翻译的Seq2Seq模型，并商用与谷歌神经机器翻译系统GNMT。其他变种还有GRU、双向RNN等
    注意力(机制)网络
        注意力机制的提出，克服了RNN训练不稳定、难以并行化等缺陷。Google提出了第一个利用纯注意力机制实现的网络模型Transformer，随后提出了GPT、BERT、GPT-2。自注意力机制有BigGAN模型等
    图卷积神经网络
        图片、文本等数据具有规则的空间、时间结构，称为欧式数据。对于社交网络、通信网络、蛋白质分子结构等一系列的不规则空间拓扑结构的数据，图卷积网络(Graph Convolution Network,GCN)模型，在半监督任务上取得不错效果。后续的有GAT,EdgeConv,DeepGCN等

### 6.8 汽车油耗预测实战

    数据集
        采用Auto MPG数据集，需要从UCI服务器下载并读取到DataFrame对象中。并且对于原始表格中的数据可能含有空字段(缺失值)的数据项，需要进行清除
        对于一些无关字段，可以进行移除转换
        对数据集进行8:2切分训练集和测试集，并将关键字段抽出作为标签数据
        统计训练集各个字段数值的均值和标准差，完成数据的标准化，通过norm()函数实现。最后利用切分的数据集结构构建数据集对象
    创建网络
        将网络实现为一个自定义网络类，在初始化函数中创建各个子网络层，在前向计算函数中call中实现自定义网络类的计算逻辑。自定义网络类继承自keras.Model基类，是自定义网络类的标准写法，以便利用trainable_variables,save_weights等
    训练与测试
        实例化网络对象并创建优化器
        网络训练部分通过Epoch和Step组成双层循环训练网络
        对于回归问题，可以使用MSE均方差和MAE平均绝对误差
        如果训练效果随着Epoch变化不显著，可以提前结束训练。
    # 在线下载汽车效能数据集 
    dataset_path = keras.utils.get_file("auto-mpg.data", 
    "http://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data") 
    # 利用pandas 读取数据集，字段有效能（公里数每加仑），气缸数，排量，马力，重量
    # 加速度，型号年份，产地 
    column_names = ['MPG','Cylinders','Displacement','Horsepower','Weight', 
                    'Acceleration', 'Model Year', 'Origin'] 
    raw_dataset = pd.read_csv(dataset_path, names=column_names, 
                        na_values = "?", comment='\t', 
                        sep=" ", skipinitialspace=True) 
    dataset = raw_dataset.copy() 
    # 查看部分数据 
    # dataset.head()
    dataset.isna().sum() # 统计空白数据 
    dataset = dataset.dropna() # 删除空白数据项 
    dataset.isna().sum() # 再次统计空白数据
    # 处理类别型数据，其中origin 列代表了类别1,2,3,分布代表产地：美国、欧洲、日本 
    # 先弹出(删除并返回)origin 这一列 
    origin = dataset.pop('Origin') 
    # 根据origin 列来写入新的3 个列 
    dataset['USA'] = (origin == 1)*1.0 
    dataset['Europe'] = (origin == 2)*1.0 
    dataset['Japan'] = (origin == 3)*1.0 
    # dataset.tail() # 查看新表格的后几项
    #切分为训练集和测试集 
    train_dataset = dataset.sample(frac=0.8,random_state=0) 
    test_dataset = dataset.drop(train_dataset.index) 
    # 移动MPG 油耗效能这一列为真实标签Y 
    train_labels = train_dataset.pop('MPG') 
    test_labels = test_dataset.pop('MPG')
    # 查看训练集的输入X 的统计数据 
    train_stats = train_dataset.describe() 
    # train_stats.pop("MPG") # 仅保留输入X 
    train_stats = train_stats.transpose() # 转置 
    # 标准化数据 
    def norm(x): # 减去每个字段的均值，并除以标准差 
        return (x - train_stats['mean']) / train_stats['std'] 
    normed_train_data = norm(train_dataset) # 标准化训练集 
    normed_test_data = norm(test_dataset) # 标准化测试集
    print(normed_train_data.shape,train_labels.shape) 
    print(normed_test_data.shape, test_labels.shape) 
    train_db = tf.data.Dataset.from_tensor_slices((normed_train_data.values, 
    train_labels.values)) # 构建Dataset 对象 
    train_db = train_db.shuffle(100).batch(32) # 随机打散，批量化
    class Network(keras.Model): 
        # 回归网络模型 
        def __init__(self): 
            super(Network, self).__init__() 
            # 创建3 个全连接层 
            self.fc1 = layers.Dense(64, activation='relu') 
            self.fc2 = layers.Dense(64, activation='relu') 
            self.fc3 = layers.Dense(1) 
    
        def call(self, inputs, training=None, mask=None): 
            # 依次通过3 个全连接层 
            x = self.fc1(inputs) 
            x = self.fc2(x) 
            x = self.fc3(x) 
            return x
    model = Network() # 创建网络类实例 
    # 通过build 函数完成内部张量的创建，其中4 为任意设置的batch 数量，9 为输入特征长度 
    model.build(input_shape=(4, 9))  
    model.summary() # 打印网络信息 
    optimizer = tf.keras.optimizers.RMSprop(0.0002) # 创建优化器，指定学习率

    for epoch in range(200): # 200 个Epoch 
        for step, (x,y) in enumerate(train_db): # 遍历一次训练集 
            # 梯度记录器，训练时需要使用它 
            with tf.GradientTape() as tape: 
                out = model(x) # 通过网络获得输出 
                loss = tf.reduce_mean(losses.MSE(y, out)) # 计算MSE 
                mae_loss = tf.reduce_mean(losses.MAE(y, out)) # 计算MAE 
    
            if step % 10 == 0: # 间隔性地打印训练误差 
                print(epoch, step, float(loss)) 
            # 计算梯度，并更新 
            grads = tape.gradient(loss, model.trainable_variables) 
            optimizer.apply_gradients(zip(grads, model.trainable_variables))

## 七、反向传播算法

    回首得越久，你会看得越远。——温斯顿·丘吉尔
    误差反向传播算法(Backpropagation,BP)是神经网络中的核心算法之一。

### 7.1 导数与梯度

    导数被定义为变化量的极限。导数本身是标量，但表征了函数值在某个方向上的变化率。沿着坐标轴方向的导数称为偏导数。
    神经网络中x一般用来表示输入，网络的自变量是网络参数集θ={w1,b1,w2,b2,...}。关心的是误差函数输出L沿着自变量θi方向上的导数。
        ▽_θL=(𝜕L/𝜕Θ1,𝜕L/𝜕Θ2,...,𝜕L/𝜕Θn)
    梯度下降算法可以按着向量形式进行更新：Θ'=θ-η·▽_θL，求解最大值(如强化学习求最大化回报函数)时，-变为+，称为梯度上升算法
    通过梯度下降算法不能保证得到全局最优解，主要由目标函数的非凸性造成。
    深度学习框架主要实现的算法就是反向传播算法和梯度下降算法

### 7.2 导数常见性质

    基本函数的导数
        常数函数c，导数为0
        线性函数y=ax+c，导数为a
        幂函数x^a，导数为ax^(a-1)
        指数函数a^x，导数为a^xlna
        对数函数log_ax，导数为1/(xlna)
    常用导数性质
        线性运算，导数的加减=加减的导数
        乘法，(fg)'=f'g+fg'
        除法，(f/g)'=(f'g-fg')/g^2,g≠0
        复合函数的导数，df(g(x))/dx=f'(u)g'(x),u=g(x)

### 7.3 激活函数导数

    Sigmoid函数导数
        σ(x)=1/(1+e^(-x))
        dσ(x)/dx=σ(1-σ)
    ReLU函数导数
        ReLU(x)=max(0,x)
        dReLU/dx=1(x≥0) 0(x<0)
        在反向传播时，不会放大梯度造成梯度爆炸；也不会缩小梯度，造成梯度弥散
        AlexNet中采用ReLU激活函数，层数达到了8层，后续上百层的也多采用ReLU
    LeakyReLU函数导数
        LeakyReLU=x(x≥0) px(x<0)
        dLeakyReLU/dx=1(x≥0) p(x<0)
    Tanh函数梯度
        tanh(x)=2·sigmoid(2x)-1
        dtanh(x)/dx=1-tanh^2(x)

### 7.4 损失函数梯度

    均方误差函数梯度
        L=1/2·Σ(yk-ok)^2
        𝜕L/𝜕oi=oi-yi
    交叉熵函数梯度
        Softmax梯度
            pi=e^(zi)/Σe^(zj)
            𝜕pi/𝜕zj=pi(1-pj)(i=j) -pi·pj(i≠j)
        交叉熵梯度
            L=-Σyklog(pk)
            𝜕L/𝜕zi=pi(yi+Σyk(k≠i))-yi
            对于y经过Onehot编码，𝜕L/𝜕zi=pi-yi

### 7.5 全连接层梯度

    单神经元梯度
        采用Sigmoid激活函数的神经元模型，数学模型σ^(1)=σ(w^(1)^Tx+b^(1))
            𝜕L/𝜕wj1=(o1-t)o1(1-o1)xj
        误差对权值wj1的偏导数至于输出值o1、真实值t以及当前权值连接的输入xj有关
    全连接层梯度
        𝜕L/𝜕wjk=(ok-tk)ok(1-ok)xj，j为输入，k为输出
        δk=(ok-tk)ok(1-ok)，表征连接线的终止节点处的误差梯度传播的某种特性，偏导只与起始节点xj，终止节点处δk有关

### 7.6 链式法则

    在不显式推导神经网络的数学表达式的情况下，逐层推导梯度的核心公式
        dz/dt=𝜕z/𝜕x·dx/dt+𝜕z/𝜕y·dy/dt
        # 构建梯度记录器 
        with tf.GradientTape(persistent=True) as tape:
        # 非tf.Variable 类型的张量需要人为设置记录梯度信息 
            tape.watch([w1, b1, w2, b2]) 
            # 构建2 层线性网络 
            y1 = x * w1 + b1     
            y2 = y1 * w2 + b2
        # 独立求解出各个偏导数 
        dy2_dy1 = tape.gradient(y2, [y1])[0] 
        dy1_dw1 = tape.gradient(y1, [w1])[0] 
        dy2_dw1 = tape.gradient(y2, [w1])[0]

### 7.7 反向传播算法

    𝜕L/𝜕wij=oj(1-oj)Σδk^(K)wjk·oi,δj^J=oj(1-oj)Σδk^(K)wjk
    输出层𝜕L/𝜕wjk=δkoj,δk^(K)=(ok-tk)ok(1-ok)
    倒数第二层𝜕L/𝜕wij=δj^(J)·oi,δj^(J)=oj(1-oj)Σδk^(K)wjk
    导数第三层𝜕L/𝜕wni=δi^(I)·on,δi^(I)=oi(1-oi)Σδj^(J)wij
    通过循环迭代计算每一层每个节点的参数，即可求得当前层的偏导数，从而得到每层权值矩阵W的梯度，再通过梯度下降算法迭代优化网络参数

### 7.8 Himmelblau函数优化实战

    Himmelblau函数是用来测试优化算法的常用样例函数之一
        f(x,y)=(x^2+y-11)^2+(x+y^2-7)^2
    以下代码可以得到Himmelblau函数的图像
        def himmelblau(x): 
            return (x[0] ** 2 + x[1] - 11) ** 2 + (x[0] + x[1] ** 2 - 7) ** 2
        x = np.arange(-6, 6, 0.1) # 可视化的x 坐标范围为-6~6 
        y = np.arange(-6, 6, 0.1) # 可视化的y 坐标范围为-6~6 
        print('x,y range:', x.shape, y.shape) 
        # 生成x-y 平面采样网格点，方便可视化 
        X, Y = np.meshgrid(x, y) 
        print('X,Y maps:', X.shape, Y.shape) 
        Z = himmelblau([X, Y]) # 计算网格点上的函数值 
        # 绘制himmelblau 函数曲面 
        fig = plt.figure('himmelblau') 
        ax = fig.gca(projection='3d') # 设置3D 坐标轴 
        ax.plot_surface(X, Y, Z) # 3D 曲面图 
        ax.view_init(60, -30) 
        ax.set_xlabel('x') 
        ax.set_ylabel('y') 
        plt.show()
    Himmelblau函数有四个局部最小值点，且局部最小值都是0
    利用TF自动求导，不同的初始值得到的极小值数值解不同，即搜索轨迹不同
        # 参数的初始化值对优化的影响不容忽视，可以通过尝试不同的初始化值， 
        # 检验函数优化的极小值情况 
        # [1., 0.], [-4, 0.], [4, 0.], [-2,2]
        x = tf.constant([4., 0.]) # 初始化参数 
        
        for step in range(200):# 循环优化200 次 
            with tf.GradientTape() as tape: #梯度跟踪 
                tape.watch([x]) # 加入梯度跟踪列表 
                y = himmelblau(x) # 前向传播 
            # 反向传播 
            grads = tape.gradient(y, [x])[0]  
            # 更新参数,0.01 为学习率 
            x -= 0.01*grads 
            # 打印优化的极小值 
            if step % 20 == 19: 
                print ('step {}: x = {}, f(x) = {}' 
                    .format(step, x.numpy(), y.numpy()))

### 7.9 反向传播算法实战

    不同的激活函数、损失函数，梯度传播表达式不同，更多是利用自动求导工具计算
    scikit-learn库的工具make_moons能够生成多个线性不可分的2分类数据集
    数据集
        N_SAMPLES = 2000 # 采样点数  
        TEST_SIZE = 0.3 # 测试数量比率 
        # 利用工具函数直接生成数据集 
        X, y = make_moons(n_samples = N_SAMPLES, noise=0.2, random_state=100)  
        # 将2000 个点按着7:3 分割为训练集和测试集 
        X_train, X_test, y_train, y_test = train_test_split(X, y, 
        test_size=TEST_SIZE, random_state=42) 
        print(X.shape, y.shape)
        # 绘制数据集的分布，X 为2D 坐标，y 为数据点的标签 
        def make_plot(X, y, plot_name, file_name=None, XX=None, YY=None, preds=None, 
        dark=False): 
            if (dark): 
                plt.style.use('dark_background') 
            else: 
                sns.set_style("whitegrid") 
            plt.figure(figsize=(16,12)) 
            axes = plt.gca() 
            axes.set(xlabel="$x_1$", ylabel="$x_2$") 
            plt.title(plot_name, fontsize=30) 
            plt.subplots_adjust(left=0.20) 
            plt.subplots_adjust(right=0.80) 
            if(XX is not None and YY is not None and preds is not None): 
                plt.contourf(XX, YY, preds.reshape(XX.shape), 25, alpha = 1, 
        cmap=plt.cm.Spectral) 
                plt.contour(XX, YY, preds.reshape(XX.shape), levels=[.5], 
        cmap="Greys", vmin=0, vmax=.6) 
            # 绘制散点图，根据标签区分颜色 
            plt.scatter(X[:, 0], X[:, 1], c=y.ravel(), s=40, cmap=plt.cm.Spectral, 
        edgecolors='none') 
            
            plt.savefig('dataset.svg') 
            plt.close() 
        # 调用make_plot 函数绘制数据的分布，其中X 为2D 坐标，y 为标签 
        make_plot(X, y, "Classification Dataset Visualization ") 
        plt.show()
    网络层
        
        class Layer: 
            # 全连接网络层 
            def __init__(self, n_input, n_neurons, activation=None, weights=None, 
        bias=None): 
                """ 
                :param int n_input: 输入节点数 
                :param int n_neurons: 输出节点数 
                :param str activation: 激活函数类型 
                :param weights: 权值张量，默认类内部生成 
                :param bias: 偏置，默认类内部生成 
                """  
                # 通过正态分布初始化网络权值，初始化非常重要，不合适的初始化将导致网络不收敛 
                self.weights = weights if weights is not None else np.random.randn(n_input, n_neurons) * np.sqrt(1 / n_neurons) 
                self.bias = bias if bias is not None else np.random.rand(n_neurons) * 0.1 
                self.activation = activation # 激活函数类型，如’sigmoid’ 
                self.last_activation = None # 激活函数的输出值o 
                self.error = None # 用于计算当前层的delta 变量的中间变量 
                self.delta = None  # 记录当前层的delta 变量，用于计算梯度 
            def activate(self, x): 
                # 前向传播函数 
                r = np.dot(x, self.weights) + self.bias  # X@W+b 
                # 通过激活函数，得到全连接层的输出o 
                self.last_activation = self._apply_activation(r) 
                return self.last_activation
            def _apply_activation(self, r): 
                # 计算激活函数的输出 
                if self.activation is None: 
                    return r # 无激活函数，直接返回 
                # ReLU 激活函数 
                elif self.activation == 'relu': 
                    return np.maximum(r, 0) 
                # tanh 激活函数 
                elif self.activation == 'tanh': 
                    return np.tanh(r) 
                # sigmoid 激活函数 
                elif self.activation == 'sigmoid': 
                    return 1 / (1 + np.exp(-r)) 
                return r 
            def apply_activation_derivative(self, r): 
                # 计算激活函数的导数 
                # 无激活函数，导数为1 
                if self.activation is None: 
                    return np.ones_like(r) 
                # ReLU 函数的导数实现 
                elif self.activation == 'relu': 
                    grad = np.array(r, copy=True) 
                    grad[r > 0] = 1. 
                    grad[r <= 0] = 0. 
                    return grad 
                # tanh 函数的导数实现 
                elif self.activation == 'tanh': 
                    return 1 - r ** 2 
                # Sigmoid 函数的导数实现 
                elif self.activation == 'sigmoid': 
                    return r * (1 - r) 
                return r
    网络模型
        class NeuralNetwork: 
            # 神经网络模型大类 
            def __init__(self): 
                self._layers = []  # 网络层对象列表 
        
            def add_layer(self, layer): 
                # 追加网络层 
                self._layers.append(layer)
            def feed_forward(self, X): 
                # 前向传播 
                for layer in self._layers: 
                    # 依次通过各个网络层 
                    X = layer.activate(X) 
                return X
            def backpropagation(self, X, y, learning_rate): 
                # 反向传播算法实现 
                # 前向计算，得到输出值 
                output = self.feed_forward(X) 
                for i in reversed(range(len(self._layers))):  # 反向循环 
                    layer = self._layers[i]  # 得到当前层对象 
                    # 如果是输出层 
                    if layer == self._layers[-1]:  # 对于输出层 
                        layer.error = y - output  # 计算2 分类任务的均方差的导数 
                        # 关键步骤：计算最后一层的delta，参考输出层的梯度公式 
                        layer.delta = layer.error * layer.apply_activation_derivative(output) 
                    else:  # 如果是隐藏层 
                        next_layer = self._layers[i + 1]  # 得到下一层对象 
                        layer.error = np.dot(next_layer.weights, next_layer.delta) 
                        # 关键步骤：计算隐藏层的delta，参考隐藏层的梯度公式 
                        layer.delta = layer.error * layer.apply_activation_derivative(layer.last_activation) 
                for i in range(len(self._layers)): 
                    layer = self._layers[i] 
                    # o_i 为上一网络层的输出  
                    o_i = np.atleast_2d(X if i == 0 else self._layers[i - 1].last_activation) 
                    # 梯度下降算法，delta 是公式中的负数，故这里用加号 
                    layer.weights += layer.delta * o_i.T * learning_rate
    网络训练
            def train(self, X_train, X_test, y_train, y_test, learning_rate, max_epochs): 
                # 网络训练函数 
                # one-hot 编码 
                y_onehot = np.zeros((y_train.shape[0], 2)) 
                y_onehot[np.arange(y_train.shape[0]), y_train] = 1
                mses = [] 
                for i in range(max_epochs):  # 训练1000 个epoch 
                    for j in range(len(X_train)):  # 一次训练一个样本 
                        self.backpropagation(X_train[j], y_onehot[j], learning_rate) 
                    if i % 10 == 0: 
                        # 打印出MSE Loss 
                        mse = np.mean(np.square(y_onehot - self.feed_forward(X_train))) 
                        mses.append(mse) 
                        print('Epoch: #%s, MSE: %f' % (i, float(mse))) 

                        # 统计并打印准确率
                        accuracy=0
                        y_test_flat=y_test.flatten()
                        for order,n in enumerate(self.feed_forward(X_test)):
                            accuracy+=(n[0]<0.5)==y_test_flat[order]
                        accuracy/=len(y_test_flat)
                        print('Accuracy: %.2f%%' % (accuracy*100)) 
                return mses 

        nn = NeuralNetwork() # 实例化网络类 
        nn.add_layer(Layer(2, 25, 'sigmoid'))  # 隐藏层1, 2=>25 
        nn.add_layer(Layer(25, 50, 'sigmoid')) # 隐藏层2, 25=>50 
        nn.add_layer(Layer(50, 25, 'sigmoid')) # 隐藏层3, 50=>25 
        nn.add_layer(Layer(25, 2, 'sigmoid'))  # 输出层, 25=>2
        nn.train(X_train, X_test, y_train, y_test,lrate,epoch)
        需要注意网络权值初始化，可以使用正态分布

### 八、Keras高层接口

    人工智能难题不仅是计算机科学问题，更是数学、认知科学和哲学问题。——Francois Chollet
    Keras是一个主要由Python语言开发的开源神经网络计算库，被设计为高度模块化和易扩展的高层神经网络接口。Keras库分为前端和后端，后端一般是调用现有的深度学习框架实现底层运算，如Theano、CNTK、TensorFlow等，前端接口是Keras抽象过的一组统一接口函数。用户通过Keras编写的代码可以轻松的切换不同的后端运行。
    TF2中，Keras被正式确定为TF的高层唯一接口API，只能使用Keras的接口来完成TF层方式的模型搭建与训练。Keras被实现在tf.keras子模块中
    Keras可以理解为一套搭建与训练神经网络的高层API协议，安装标准的Keras库就可以方便调用，TF中也实现了Keras协议

### 8.1 常见功能模块

    Keras提供了一系类高层的神经网络相关类和函数，如经典数据集加载函数、网络层类、模型容器、损失函数类、优化函数、经典模型类等
    常见网络类
        常见的神经网络层，可以使用张量方式的底层接口函数来实现，这些接口函数一般在tf.nn中。更常用的，对于常见的网络层，一般直接使用层方式来完成模型搭建，在tf.keras.layers命名空间中提供了大量常见网络层的类，例如全连接层、激活函数层、池化层、卷积层、循环神经网络层等。对于这些网络层类，只需要在创建时指定网络层的相关参数，并调用__call__方法即可，Keras会自动调用每个层的前向传播逻辑，这些逻辑一般实现在类的call函数中
            x = tf.constant([2.,1.,0.1])  # 创建输入张量 
            layer = layers.Softmax(axis=-1)  # 创建Softmax 层 
            out = layer(x)  # 调用softmax 前向计算，输出为out
        与  out = tf.nn.softmax(x)  # 调用softmax 函数完成前向计算
        结果相同
    网络容器
        通过Keras提供的网络容器Sequential将多个网络层封装成一个大网络模型，只需要调用网络模型的实例一次
            network = Sequential([ # 封装为一个网络 
                layers.Dense(3, activation=None), # 全连接层，此处不使用激活函数 
                layers.ReLU(),#激活函数层 
                layers.Dense(2, activation=None), # 全连接层，此处不使用激活函数 
                layers.ReLU() #激活函数层 
            ]) 
            x = tf.random.normal([4,3])
            out=network(x)
        Sequential容器也可以通过add()方法继续追加新的网络层
            network.add(layer.Dense(3))
            ...
            network.build(input_shape=(4,4))
            network.summary()
        参数个数计算，上一层输入个数*本层权重数+本层权重数，以此类推相加
        Sequential对象的trainable_variables和variables包含了所有层的待优化张量列表和全部张量列表

### 8.2 模型装配、训练与测试

    在训练网络时，一般的流程是通过前向计算获得网络的输出值，再通过损失函数计算网络误差，然后通过自动求导工具计算梯度并更新，同时间隔性地测试网络的性能。
    模型装配
        在Keras中有两个比较特殊的类：keras.Model和keras.layers.Layer类，Layer类是网络层的母类，定义了网络层的一些常见功能，如添加权值、管理权值列表等。Model类是网络的母类，除了具有Layer类的功能，还添加了保存模型、加载模型、训练与测试模型等便捷功能。Sequential也是Model的子类。
        创建网络后，正常的流程是循环迭代数据集多个Epoch，每次按批产生训练数据、前向计算，然后通过损失函数计算误差值，并反向传播自动计算梯度、更新网络参数。在Keras中提供了compile()和fit()函数。通过compile()函数指定网络使用的优化器对象、损失函数类型、评价指标等设定，这一步称为装配
            network.compile(optimizer=optimizers.Adam(lr=0.01), 
                loss=losses.CategoricalCrossentropy(from_logits=True), 
                metrics=['accuracy'] # 设置测量指标为准确率 
            )
    模型训练
        模型装配王城后，通过fit()函数送入带训练的数据集和验证用的数据集，这一步称为模型训练
            # 指定训练集为train_db，验证集为val_db,训练5 个epochs，每2 个epoch 验证一次 
            # 返回训练轨迹信息保存在history 对象中 
            history = network.fit(train_db, epochs=5, validation_data=val_db, validation_freq=2)
        train_db为tf.data.Dataset对象，也可以传入Numpy Array类型
            history.history查看训练记录
        fit()函数的运行代表了网络的训练过程，训练中产生的历史数据可以通过返回值对象取得
    模型测试
        Model类可以方便地预测和测试。验证和测试有所不同
            out = network.predict(x)
        简单测试模型的性能，Model.evaluate(db)循环测试完db数据集上所有样本，并输出性能指标

### 8.3 模型保存与加载

    模型训练完成后，需要将模型保存到文件系统上，方便后续的模型测试与部署工作。在训练时间隔性地保存模型状态是好习惯，尤其对于大规模网络。一般大规模的网络需要训练数天乃至数周的时长，定时保存能够避免浪费大量的训练时间和计算资源
    Keras有三种常用的模型保存与加载方法
    张量方式
        网络的状态主要体现在网络的结构以及网络层内部张量数据上，在拥有网络结构源文件的条件下，直接保存网络张量参数到文件系统上是最轻量级的一种方式。
            Model.save_weight(path),'weights.ckpt'
        在需要的时候，先创建好网络对象，然后调用网络对象的load_weight(path)即可将指定的模型文件中保存的张量数值写入到当前网络参数中
            del Model#删除网络对象
            network = Sequential([layers.Dense(256, activation='relu'), 
                layers.Dense(128, activation='relu'), 
                layers.Dense(64, activation='relu'), 
                layers.Dense(32, activation='relu'), 
                layers.Dense(10)]) 
            network.compile(optimizer=optimizers.Adam(lr=0.01), 
                loss=tf.losses.CategoricalCrossentropy(from_logits=True), 
                metrics=['accuracy'] 
            )
            network.build(input_shape=())
            # 从参数文件中读取数据并写入当前网络 
            network.load_weights('weights.ckpt')
        仅仅保存张量参数的数值，不包含其他的结构参数，但是需要使用相同的网络结构才能正确恢复网络状态，一般在拥有网络源文件的情况下使用
    网络方式
        仅需要模型参数文件即可恢复出网络模型。
            Model.save(path)将模型的结构以及模型的参数保存到path
            kera.models.load_model(path)即可恢复网络结构和网络参数
                network.save('model.h5')
                network = keras.models.load_model('model.h5')
    SavedModel方式
        当需要将模型部署到其他平台时，SavedModel方式更具有平台无关性，会新建一个目录
            tf.saved_model.save(network,path),"any"
            tf.saved_model.load(path)
        acc=metrics.CategoricalAccuracy()
        acc.update_state(y_true,y_pred)用于更新准确率

### 8.4 自定义网络

    科研工作者一般是自行实现了较为新颖的网络层，经过大量实验验证有效后，深度学习框架才会跟进，内置对这些网络层的支持。
    对于需要创建自定义逻辑的网络层，可以通过自定义类来实现。创建自定义网络层类时，需要继承自layers.Layer基类；创建自定义的网络类时，需要继承自keras.Model基类，从而方便利用Layer/Model基类提供的参数管理等功能。并与其他标准网络层类交互使用
    自定义网络层
        至少需要实现初始化__init__方法和前向传播逻辑call方法。
            class MyDense(layers.Layer): 
                # 自定义网络层 
                def __init__(self, inp_dim, outp_dim): 
                    super(MyDense, self).__init__() 
                    # 创建权值张量并添加到类管理列表中，设置为需要优化 
                    self.kernel = self.add_variable('w', [inp_dim, outp_dim],trainable=True)#返回张量W的Python引用，变量名由TF内部维护，使用较少
                def call(self, inputs, training=None): 
                    # 实现自定义类的前向计算逻辑 
                    # X@W 
                    out = inputs @ self.kernel 
                    # 执行激活函数运算 
                    out = tf.nn.relu(out) 
                    return out
            net=MyDense(4,3)
        training参数用于指定模型的状态，True为训练模式，False为测试模式(默认,None)。全连接层的训练模式和测试模式逻辑一致
    自定义网络
        同样可以使用Sequential容器封装，适合数据按序在层间传播。对于复杂的网络结构，自定义网络更加灵活
            class MyModel(keras.Model): 
                # 自定义网络类，继承自Model 基类 
                def __init__(self): 
                    super(MyModel, self).__init__() 
                    # 完成网络内需要的网络层的创建工作 
                    self.fc1 = MyDense(28*28, 256) 
                    self.fc2 = MyDense(256, 128) 
                    self.fc3 = MyDense(128, 64) 
                    self.fc4 = MyDense(64, 32) 
                    self.fc5 = MyDense(32, 10)
                def call(self, inputs, training=None): 
                    # 自定义前向运算逻辑 
                    x = self.fc1(inputs)  
                    x = self.fc2(x)  
                    x = self.fc3(x)  
                    x = self.fc4(x)  
                    x = self.fc5(x)  
                    return x

### 8.5 模型乐园

    对于常用的网络模型如ResNet,VGG等，直接从keras.applications子模块中创建并使用，还可以通过设置weights参数加载预训练的网络参数
    加载模型
        对于ResNet50网络模型，一般去除最后一层后的网络作为新任务的特征提取自网络，即利用在ImageNet数据集上预训练好的网络参数初始化，并根据自定义任务的类别追加一个对应数据类别的全连接分类层或子网络，从而可以在预训练网络的基础上快速、高效地学习新任务
            # 加载ImageNet 预训练网络模型，并去掉最后一层 
            resnet = keras.applications.ResNet50(weights='imagenet',include_top=False) 
            resnet.summary() 
            # 测试网络的输出 
            x = tf.random.normal([4,224,224,3]) 
            out = resnet(x) # 获得子网络的输出 
        将自动从服务器下载模型结构和在ImageNet数据集上预训练好的网络参数。
            # 新建池化层 ，理解为高、宽维度下采样的功能
            global_average_layer = layers.GlobalAveragePooling2D() 
            # 利用上一层的输出作为本层的输入，测试其输出 
            x = tf.random.normal([4,7,7,2048]) 
            # 池化层降维，形状由[4,7,7,2048]变为[4,1,1,2048],删减维度后变为[4,2048] 
            out = global_average_layer(x)
            # 新建全连接层 
            fc = layers.Dense(100) 
            # 利用上一层的输出[4,2048]作为本层的输入，测试其输出 
            x = tf.random.normal([4,2048]) 
            out = fc(x) # 输出层的输出为样本属于100 类别的概率分布
            # 重新包裹成我们的网络模型 
            mynet = Sequential([resnet, global_average_layer, fc]) 
            mynet.summary()
        resnet.trainable=False可以选择冻结ResNet部分的网络参数，只训练新建的网络层

### 8.6 测量工具

    在网络的训练过程中，经常需要统计准确率、召回率等测量指标，Keras提供了一些常用的测量工具，位于keras.metrics模块中。
    使用的主要步骤：新建测量器、写入数据、读取统计数据和清零测量器
    新建测量器
        有较多的常用测量器类，如统计平均值的Mean类、统计准确率的Accuracy类、统计余弦相似度的CosineSimilarity类
            # 新建平均测量器，适合Loss 数据 
            loss_meter = metrics.Mean()
    写入数据
        通过测量器的update_state函数可以写入新的数据，测量器会根据自身逻辑记录并处理采样数据
            # 记录采样的数据，通过float()函数将张量转换为普通数值 
            loss_meter.update_state(float(loss))
    读取统计信息
        在需要的地方调用测量器的result()函数，来获取统计值
            loss_meter.result()
    清除状态
        在启动新一轮统计时，需要清除历史状态。通过reset_states()即可实现
            loss_meter.reset_states()

### 8.7 可视化

    在网络训练的过程中，通过Web端远程监控网络的训练进度，可视化网络的训练结果。TF提供了可视化工具，TensorBoard，将监控数据写入到文件系统。TensorBoard的使用需要模型代码和浏览器相互配合，且需要先安装TensorBoard库。
    模型端
        需要创建写入监控数据的Summary类，并在需要的时候写入监控数据。首先通过tf.summary.create_file_writer创建监控对象类实例，并指定监控数据的写入目录
            # 创建监控类，监控数据将写入log_dir 目录 
            summary_writer = tf.summary.create_file_writer(log_dir) 
        在前向计算完成后，对于误差这种标量数据，通过tf.summary.scalar函数记录监控数据，并指定时间戳step参数，类似于每个数据对应的时间刻度信息，不宜重复。每类数据通过字符串名区分，同类的数据需要写入相同名字的数据库中。
            with summary_writer.as_default(): # 写入环境 
                # 当前时间戳step 上的数据为loss，写入到名为train-loss 数据库中 
                tf.summary.scalar('train-loss', float(loss), step=step)
        对于图片类型的数据，通过tf.summary.image函数写入监控图片数据，接收多个图片的张量数据，通过设置max_outputs参数来选择最多显示的图片数量
            with summary_writer.as_default():# 写入环境 
                # 写入测试准确率 
                tf.summary.scalar('test-acc', float(total_correct/total), step=step) 
                # 可视化测试用的图片，设置最多可视化9 张图片 
                tf.summary.image("val-onebyone-images:", val_images, max_outputs=9, step=step)
        浏览器端
            打开Web后端，通过在cmd终端运行tensorboard --logdir path指定web后端监控的文件目录path
            输入网址http://localhost:6006(端口号可能会变，可查看命令提示)
            监控页面上端可以选择不同类型数据的监控页面。
            TensorBoard还支持通过tf.summary.histogram查看张量数据的直方图分布，以及通过tf.summary.text打印文本信息等功能
                with summary_writer.as_default():  
                    # 当前时间戳step 上的数据为loss，写入到ID 位train-loss 对象中 
                    tf.summary.scalar('train-loss', float(loss), step=step)  
                    # 可视化真实标签的直方图分布 
                    tf.summary.histogram('y-hist',y, step=step) 
                    # 查看文本信息 
                    tf.summary.text('loss-text',str(float(loss)))
            Facebook开发的Visdom工具也可以方便可视化数据，可以接受PyTorch的张量类型的数据，对于TF的需要转换为Nummpy数组

## 九、过拟合

    一切都应该尽可能地简单，但不能过于简单。——Albert·Einstein
    机器学习的主要目的是从训练集上学习到数据的真实模型，从而获得泛化能力。通常训练集和测试集都采样自某个相同的数据分布，采样到的样本是互相独立的，但来自相同的分布，这种假设称为独立同分布假设(i.i.d.)
    模型的表达能力，称为模型的容量。当模型的表达能力过强时，可能把训练集的噪声模态也学到，导致在测试集上表现不佳(泛化能力偏弱)

### 9.1 模型的容量

    模型的容量或表达能力，是指模型拟合复杂函数的能力。一种体现模型容量的指标为模型的假设空间(Hypothesis Space)大小，即模型可以表示的函数集的大小。假设空间越大越完备，从假设空间中搜索出逼近真实模型的函数也就越有可能。
    过大的假设空间会增加搜索难度和计算代价。在有限的计算资源约束下，较大的假设空间并不一定能搜索出更好的函数模型。由于观测误差的存在，较大的约束空间中可能包含了大量表达能力过强的函数，能够将训练样本的观测误差也学习进来。

### 9.2 过拟合与欠拟合

    模型的容量过大出现的模型泛化能力偏弱，在测试集上表现不佳，称为过拟合；模型的容量过小，在所有样本上表现不佳，称为欠拟合
    统计学习理论中，VC(Vapnik-Chervonenkis维度)是一个应用比较广泛的度量函数容量的方法。这些方法给机器学习提供了一定程度的理论保证，但很少应用到深度学习中去，一部分是因为神经网络过于复杂，难以确定网络结构背后的数学模型的VC维度
    可以根据奥卡姆剃刀原理来指导神经网络的设计和训练。优先选择使用更见的神经网络
    欠拟合
        当模型在训练集上误差维持较高、难以优化减少，同时在测试集上表现不佳，可能出现欠拟合。通过增加神经网络层数、增大中间维度的大小等方法，比较好的解决。在实际使用过程中，更多的是出现过拟合
    过拟合
        现代深度神经网络中过拟合现象非常容易出现，主要是因为神经网络的表达能力非常强，训练集样本数不够

### 9.3 数据集划分

    为了挑选模型超参数和检测过拟合现象，一般需要将原来的训练集再次切分为新的训练集和验证集(Valiation set)
    验证集与超参数
        当数据集规模偏小时，为了测试集能够比较准确地测试出模型的泛化能力，可以适当增加测试机的比例。
        由于测试机的性能不能作为模拟训练的反馈，而需要在模型训练时能够挑选出叫合适的模型超参数，判断模型是否过拟合等，从而将训练集再次切分为训练集D^train和验证集D^val。验证集用于选择模型的超参数，功能包括
            根据验证集的性质表现来调整学习率、权值衰减系数、训练次数等
            根据验证集的性能表现来重新调整网络拓扑结构
            根据验证集的性能表现判断是否过拟合和欠拟合
        三者的常见划分比例可以为6:2:2
        验证集与测试集的区别在于，算法设计人员可以根据验证机的表现来调整模型的各种超参数的设置，提升模型的泛化能力，但测试机的表现却不能用来反馈模型的调整，否则二者的功能重合。
        可以选择生成多个测试集，即使开发人员使用了其中一个测试集来挑选模型，还可以使用其他测试集来评价，也是Kaggle竞赛常用的做法
    提前停止
        一般把对训练集中的一个Batch运算更新一次叫做一个Step，对训练集的所有样本循环迭代一次称为Epoch。验证集可以在数次Step或数次Epoch后使用，计算模型的验证性能。验证过于频繁会引入额外的计算代价，建议几个Epoch后进行一次验证
        分类任务中，训练/验证/测试关注的指标有训练/验证/测试误差、准确率等。通过观测训练准确率和验证准确率可以大致推断模型是否出现过拟合和欠拟合。如果训练效果好但验证效果差，可能是过拟合；训练、验证效果都差，可能是欠拟合
        当观测到过拟合，可以重新设计网络模型的容量，如降低网络的层数、较低网络的参数量、添加正则化手段、添加假设空间的约束等，使得模型的实际容量降低；当观测到欠拟合，可以尝试增大网络的容量，如加深网络的层数、增加网络的参数量，尝试更加复杂的网络结构
        由于网络的实际容量可以随着训练的进行发生改变，对于神经网络，即使网络结构超参数保持不变(网络最大容量固定)，模型依然可能会出现过拟合。随着训练Epoch数增加，过拟合程度越来越严重
        对于分类问题，当发现验证准确率连续n个Epoch没有下降时，可能已经达到了最适合的Epoch附近，而提前停止训练

### 9.4 模型设计

    通过验证集可以判断网络模型是否过拟合或者欠拟合，从而为调整网络模型的容量提供判断依据

### 9.5 正则化

    通过设计不同层数、大小的网络模型可以为优化算法提供初始的函数假设空间，模型的实际容量可以随着网络参数的优化更新而产生变化。如果高阶网络参数均为0，可以退化到非零阶参数。通过限制网络参数的稀疏性，可以来约束网络的实际容量
    这种约束一般通过在损失函数上添加额外的参数稀疏性惩罚项实现，在未加约束之前的优化目标为  min L(f_θ(x),y),(x,y)∈D^train 
    对模型的参数添加额外的约束后，优化的目标变为
        min L(f_θ(x),y)+λ·Ω(θ),(x,y)∈D^train
    Ω(θ)为对网络参数θ的稀疏性约束函数，一般参数θ的稀疏性约束通过约束参数θ的L范数来实现。新的优化目标除了要最小化原来的损失函数外，还要约束网络参数的稀疏性，尽可能地迫使网络参数变得稀疏，它们之间的权重关系通过超参数λ来平衡。
    常用的正则化方式有L0、L1、L2正则化
    L0正则化
        采用L0范数作为稀疏性惩罚项的正则化计算方式
            Ω(θ)=Σ||θi||_0
        L0范数定义为非零元素的个数。通过约束惩罚项的大小可以迫使网络中的连接权值大部分为0，从而降低网络的实际参数量和网络容量。但是L0范数并不可导，不能利用梯度下降算法进行优化，在神经网络中使用的并不多
    L1正则化
        Ω(θ)=Σ||θi||_1，L1范数定义为所有元素的绝对值之和，也称为Lasso Regularization，是连续可导的，在神经网络中使用广泛
            tf.reduce_sum(tf.math.abs(w1))
    L2正则化
        Ω(θ)=Σ||θi||_2，L2范数定义为所有元素的平方和，也称为Ridge Regularization，也连续可导，使用广泛
            f.reduce_sum(tf.square(w1))
    正则化效果
        实际训练时，一般有限尝试较小的正则化系数，观察网络是否出现过拟合现象，然后尝试逐渐增大λ参数来增加网络参数稀疏性，提高泛化能力。过大的λ可能导致网络不收敛

### 9.6 Dropout

    Dropout通过随机断开神经网络的连接，减少每次训练时实际参与计算的模型的参数量；但是在测试时，会恢复所有的连接，保证模型测试时获得最好的性能
    在添加了Dropout功能的网路层中，每条连接是否断开符合某种预设的概率分布，如断开概率为p的伯努利分布。
    TF中可以通过tf.nn.dropout(x,rate)实现某条连接的Dropout功能，rate设置断开的概率值。也可以将Dropout作为一个网络层使用，在网络中间插入一个Dropout层
        model.add(layers.Dropout(rate=0.5))

### 9.7 数据增强

    增加数据集规模是解决过拟合最重要的途径。在有限的数据集上，通过数据增强技术可以增加训练的样本数量，获得一定程度上的性能提升。数据增强(Data Augmentation)是指在维持样本标签不变的条件下，根据先验知识改变样本的特征，使得新产生的样本也符合或近似符合数据的真实分布
    对于图片数据，为了方便神经网络处理，需要将图片缩放到某个固定的大小。旋转、缩放、平移、裁剪、改变视角、遮挡某局部区域都不会改变图片的主体类别标签
    tf.image子模块中有常用的图片处理函数。tf.image.resize能够进行图片缩放
        def preprocess(x,y): 
            # 预处理函数 
            # x: 图片的路径，y：图片的数字编码 
            x = tf.io.read_file(x) 
            x = tf.image.decode_jpeg(x, channels=3) # RGBA 
            # 图片缩放到244x244 大小，这个大小根据网络设定自行调整 
            x = tf.image.resize(x, [244, 244])
    旋转
        获得不同角度的新图片
            tf.image.rot90(x,k),旋转k个90度
    翻转
        图片的翻转分为沿水平轴和竖直轴翻转。
            tf.image.random_flip_left_right
            tf.image.random_flip_up_down
        在水平和竖直方向随机翻转
    裁剪
        在原图的左右和上下方向去掉部分边缘像素
            tf.image.resize(x,[l,w])#缩放
            tf.image.random_crop(x,[l,w])#随机裁剪
    生成数据
        通过生成模型在原有数据上进行训练，学习到真实数据的分布，利用生成模型获得新的样本，也可以提升网络性能。如通过条件生成对抗网络(Conditional GAN,CGAN)可以生成带标签的样本数据
    其他方式
        任意变换图片数据：叠加噪声、改变图片观察视角、随机遮挡部分区域

### 9.8 过拟合问题实战

    基于月牙形状的2分类数据集的过拟合与欠拟合模型
    构建数据集
        def load_dataset():
            # 采样点数
            N_SAMPLES = 1000
            # 测试数量比率
            TEST_SIZE = None

            # 从 moon 分布中随机采样 1000 个点，并切分为训练集-测试集
            X, y = make_moons(n_samples=N_SAMPLES, noise=0.25, random_state=100)
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=TEST_SIZE, random_state=42)
            return X, y, X_train, X_test, y_train, y_test
    探讨影响
        def network_layers_influence(X_train, y_train):
            # 构建 5 种不同层数的网络
            for n in range(5):
                # 创建容器
                model = Sequential()
                # 创建第一层
                model.add(layers.Dense(8, input_dim=2, activation='relu'))
                # 添加 n 层，共 n+2 层
                for _ in range(n):
                    model.add(layers.Dense(32, activation='relu'))
                # 创建最末层
                model.add(layers.Dense(1, activation='sigmoid'))
                # 模型装配与训练
                model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
                model.fit(X_train, y_train, epochs=N_EPOCHS, verbose=1)
                # 绘制不同层数的网络决策边界曲线
                # 可视化的 x 坐标范围为[-2, 3]
                xx = np.arange(-2, 3, 0.01)
                # 可视化的 y 坐标范围为[-1.5, 2]
                yy = np.arange(-1.5, 2, 0.01)
                # 生成 x-y 平面采样网格点，方便可视化
                XX, YY = np.meshgrid(xx, yy)
                preds = model.predict(np.c_[XX.ravel(), YY.ravel()])
                title = "网络层数：{0}".format(2 + n)
                file = "网络容量_%i.png" % (2 + n)
                make_plot(X_train, y_train, title, file, XX, YY, preds, output_dir=OUTPUT_DIR + '/')

## 十、卷积神经网络

    当前人工智能还未达到人类5岁水平，不过在感知方面进步飞快。未来在机器语音、视觉识别领域，五到十年内超越人类没有悬念。——沈向洋
    深度学习的深度是指网络层数较深，一般有5层以上。
    本质上深度学习和神经网络所指代的是同一类算法。基于生物神经元数学模型的多层感知机(MLP)实现的网络模型被称为神经网络。层数较少的神经网络被称为浅层神经网络。
    一种逐层预训练的算法，有效地初始化DBN网络，使得训练大规模、深层数的神经网络成为可能。深层的神经网络被称为深度学习。

### 10.1 全连接网络的问题

    网络的训练过程中，存储网络的参数、缓存计算图模型、梯度信息、输入和中间计算结果需要占用较多的资源
    局部相关性
        如果网络层的每个输出节点都与所有的输入节点相连接，用于提取所有输入节点的特征信息，这种稠密的连接方式是全连接层参数量大、计算代价高的根本原因。全连接层也称为稠密连接层，输入与输出的关系为
            o_j=σ(Σw_ij·x_i+bj)
        可以分析输入节点对输出节点的重要性分布，仅考虑较重要的一部分输入节点，而抛弃重要性较低的部分节点，从而减少权值连接数
        以实心网络所在的像素为参考点，周边欧式距离≤某个值的像素点以矩形网格表示，网格内的像素点重要性较高，之外的较低。该窗口便被称为感受野(Receptive field)。
        这种基于距离的重要性分布假设特性称为局部相关性，只关注和自己距离较近的节点。
    权值共享
        对于每个输出节点，均使用相同的权值矩阵，就能将网络层的参数量固定
        共享权值的"局部连接层"就是卷积神经网络
    卷积运算
        对于窗口内所有像素，采用权值相乘累加的方式提取特征信息，每个输出节点提取对应感受野区域的特征信息。这种运算其实是信号处理领域的一种标准运算：离散卷积运算。离散卷积运算为两个函数(其中一个经过翻转和平移)相乘的累加。在计算机视觉中，卷积运算基于2D图片函数和2D卷积核，都仅在各自窗口有效区域存在值，其他区域视为0。卷积的结果能够得到新的特征图
        权值相乘累加中的卷积核函数并没有经过旋转。在深度学习中统一称为卷积核，或Filter、Weight
        特定卷积核能够分别实现锐化、模糊效果、边缘提取效果

### 10.2 卷积神经网络

    卷积神经网络通过充分利用局部相关性和权值共享的思想，大大减少了网络的参数量，从而提高训练效率，更容易实现超大规模的深层网络。
    单通道输入和单卷积核
        ⨀表示哈达玛积，矩阵的对应元素相乘。
        卷积运算输出倦枕大小由卷积核的大小k，输入X的高度h/w，移动步长s，是否填充等因素共同决定。
    多通道输入和单卷积核
        多通道输入的卷积层更为常见，例如彩色图片的RGB三通道。
        在多通道输入的情况下，卷积核的通道数需要和输入X的通道数量相匹配，卷积核的第i个通道和X的第i个通道运算，得到第i个中间矩阵。
        一般来说，一个卷积核只能完成某种逻辑的特征提取，当需要同时提取多种逻辑特征时，可以通过增加多个卷积核来得到多种特征，提高神经网络的表达能力，便是多通道输入、多卷积核的情况
    多通道输入、多卷积核的情况
        当出现多卷积核时，第i个卷积核与输入X运算得到第i个输出矩阵(也称为输出张量O的通道i)，最后全部的输出矩阵在通道维度上进行拼接(Stack操作，创建输出通道数的新维度)，产生输出张量O，包含了n个通道数
        每个卷积核的大小k、步长s、填充设定等都是统一设置，才能保证输出的每个通道大小一致。
    步长
        感受野密度的控制手段一般是通过移动步长(Strides)实现的
        步长是指感受野窗口每次移动的长度单位。当步长较小时，有利于提取到更多的特征信息，输出张量的尺寸也更大；较大时，有利于减少计算代价，过滤冗余信息，输出张量的尺寸也更小。
    填充
        经过卷积运算后的输出O的高度一般会小于输入X的高宽，在网络模型设计时，有时希望输出O的高宽能够与输入X的高宽相同，从而方便网络参数的设计、残差连接等。一般通过在原输入X的高和宽维度上面进行填充若干无效元素操作：上下、左右填充
            h'=[(h+2p_h-k)/s]_下取整_1,p_h为上下填充
            w'=[(w+2p_w-k)/s]_下取整_1,p_w为左右填充
        在TF中，s=1时，只需要设置参数padding="SAME"，便可自动计算padding数量，使输入输出高宽相等

### 10.3 卷积层实现

    TF中，既可以通过自定义权值的底层实现方式搭建神经网络，也可以直接调用现成的卷积层类的高层方式快速搭建复杂网络。
    自定义权值
        tf.nn.conv2d函数可以方便实现2D卷积运算，基于输入X[b,h,w,c_in]和卷积核W[k,k,c_in,c_out]进行卷积运算，得到输出O[b,h',w',c_out]，c_in为输入通道数，c_out为卷积核数量即输出特征图的通道数
            out = tf.nn.conv2d(x,w,strides=1,padding=[[0,0],[0,0],[0,0],[0,0]])
            padding参数的设置格式为padding=[[0,0],[上,下],[左,右],[0,0]]
        自动计算并填充则用padding='SAME'，当s>1时，高、宽将/s，即先padding为可以被s整除3的最小整数，然后/s
        卷积神经网络层和全连接层一样，可以设置网络带偏置向量，tf.nn.conv2d函数是没有实现偏置向量计算的，添加偏置只需要手动累加张量。
    卷积层类
        通过卷积层类layers.Conv2D可以不需要手动定义卷积核W和偏置b张量，直接调用类实例即可完成卷积层的前向计算，实现更加高层和快捷。在TensorFlow中，API的命名有一定的规律，首字母大写的对象一般表示类，全部小写一般表示函数。使用类方式会(在创建类时或build时)自动创建需要的权值张量和偏置向量等，用户不需要记忆卷积核张量的定义格式，因此使用起来更加简单方便，灵活性也会略低。函数方式的接口需要自行定义权值和偏置等，更加灵活和底层。
        在新建卷积类时，只需要指定卷积核数量参数filters，卷积核大小kernel_size，步长strides，填充padding等即可。
            layer=layers.Conv2D(4,kernel_size=3,strides=1,padding='SAME')
        如果卷积核高宽不等，步长行列方向不等，需要将kernel_size设计为tuple格式(k_h,k_w)，strdes设计为(s_h,s_w)
        创建完成后，通过调用实例(__call__方法)完成前向计算
        通过类成员trainable_variable直接返回W和b的列表，layer.kernel、layer.bias分别访问W和b张量

### 10.4 LeNet-5实战

    同样基于MNIST手写数字图片数据集训练LeNet-5网络
        from tensorflow.keras import Sequential 
        network = Sequential([ # 网络容器 
            layers.Conv2D(6,kernel_size=3,strides=1), # 第一个卷积层, 6 个3x3 卷积核 
            layers.MaxPooling2D(pool_size=2,strides=2), # 高宽各减半的池化层 
            layers.ReLU(), # 激活函数 
            layers.Conv2D(16,kernel_size=3,strides=1), # 第二个卷积层, 16 个3x3 卷积核 
            layers.MaxPooling2D(pool_size=2,strides=2), # 高宽各减半的池化层 
            layers.ReLU(), # 激活函数 
            layers.Flatten(), # 打平层，方便全连接层处理 
        
            layers.Dense(120, activation='relu'), # 全连接层，120 个节点 
            layers.Dense(84, activation='relu'), # 全连接层，84 节点 
            layers.Dense(10) # 全连接层，10 个节点 
        ]) 
        # build 一次网络模型，给输入X 的形状，其中4 为随意给的batchsz 
    卷积网络可以显著降低网络参数量，同时增加网络深度
    损失函数可以通过交叉熵损失函数类新建，通过from_logits=True将softmax激活函数实现在损失函数中，不需要手动添加损失函数，提升数值计算稳定性
        # 导入误差计算，优化器模块 
        from tensorflow.keras import losses, optimizers 
        # 创建损失函数的类，在实际计算时直接调用类实例即可 
        criteon = losses.CategoricalCrossentropy(from_logits=True) 
        # 构建梯度记录环境 
        with tf.GradientTape() as tape:  
            # 插入通道维度，=>[b,28,28,1] 
            x = tf.expand_dims(x,axis=3) 
            # 前向计算，获得10 类别的概率分布，[b, 784] => [b, 10] 
            out = network(x) 
            # 真实标签one-hot 编码，[b] => [b, 10] 
            y_onehot = tf.one_hot(y, depth=10) 
            # 计算交叉熵损失函数，标量 
            loss = criteon(y_onehot, out)
    获得损失值后，通过Tensorflow的梯度记录器tf.GradientTape()来计算损失函数loss对网络参数network.trainabel_variables之间的梯度，并通过optimizer对象自动更新网络权值参数
        # 自动计算梯度 
        grads = tape.gradient(loss, network.trainable_variables) 
        # 自动更新参数 
        optimizer.apply_gradients(zip(grads, network.trainable_variables)) 
    在测试阶段，由于不需要记录梯度信息，代码一般不需要写在with tf.GradientTape() as tape环境中。前向计算得到的输出经过softmax函数后，代表了网络预测当前图片输入x属于i类别的概率P(x标签是i|x)。通过argmax函数选取概率最大的元素所在的索引，作为当前x的预测类别，与真实标注y比较，通过计算比较结果中间True的数量并求和来统计预测正确的样本个数，最后除以总样本的个数，得出网络的测试准确度。
        # 记录预测正确的数量，总样本数量 
        correct, total = 0,0 
        for x,y in db_test: # 遍历所有训练集样本 
            # 插入通道维度，=>[b,28,28,1] 
            x = tf.expand_dims(x,axis=3) 
            # 前向计算，获得10 类别的预测分布，[b, 784] => [b, 10] 
            out = network(x) 
            # 真实的流程时先经过softmax，再argmax 
            # 但是由于softmax 不改变元素的大小相对关系，故省去 
            pred = tf.argmax(out, axis=-1)   
            y = tf.cast(y, tf.int64) 
            # 统计预测正确数量 
            correct += float(tf.reduce_sum(tf.cast(tf.equal(pred, y),tf.float32))) 
            # 统计预测样本总数 
            total += x.shape[0] 
        # 计算准确率 
        print('test acc:', correct/total)

### 10.5 表示学习

    复杂的卷积神经网络模型也是基于卷积层的堆叠构成的。过去一段时间内，研究人员发现网络层数越深，模型的表达能力越强，也就越有可能取得更好的性能。
    图片数据的识别过程一般认为也是表示学习的(Representation Learning)的过程，从接受到的原始像素开始，逐渐提取边缘、角点等底层特征，再到纹理等中层特征，再到头部、物体部件等高层特征，最后的网络层基于这些学习到的抽象特征表示做分类逻辑的学习。学习到的特征越高层，越准确，越有利于分类器的分类。
    应用学习的思想，训练好的卷积神经网络往往能够学习到较好的特征，这种特征的提取方法一般是通用的。将在任务A上训练好的深层神经网络的前面数个特征提取层迁移到任务B上，只需要训练任务B
    的分类逻辑(表现为网络的最末数层)，即可取得非常好的效果，这种方式是迁移学习的一种，从神经网络角度也称为网络微调。

### 10.6 梯度传播

    卷积层通过移动感受野的方式实现离散卷积操作，通过循环移动感受野的方式并没有改变网络层的可导性，同时梯度的推导也没有变更复杂。

### 10.7 池化层

    在卷积层中，可以通过调节步长参数s实现特征图的高宽成倍缩小，从而降低了网络的参数量。实际上，除了通过设置步长，还有一种专门的网络层可以实现尺寸缩减功能，即为池化层(Pooling Layer)
    池化层同样基于局部相关性的思想，通过从局部相关的一组元素中进行采样或信息聚合，从而得到新的元素值。最大化池化层(Max Pooling)从局部相关元素中选取最大的一个元素值，平均池化层(Average Pooling)从局部相关元素集中计算平均值并返回。
    池化层没有需要学习的参数，计算简单，可以有效降低特征图的尺寸，非常适合图片这种类型的数据。
    通过精心设计池化层感受野的高宽k和步长s参数，可以实现各种降维运算。例如，感受野大小k=2、步长s=2，输出只有输入高宽一半的目的。

### 10.8 BatchNorm层

    卷积神经网络能够使网络参数量大大减少。但是在残差网络出现之前，网络的加深使得网络训练变得不稳定，甚至出现长时间不更新甚至不收敛的现象，同时网络对超参数比较敏感，超参数的微量扰动也会导致网络的训练轨迹完全改变。
    Google研究人员提出了一种参数标准化的手段，并基于此设计了Batch Normalization(BatchNorm,BN层)。使得网络的超参数的设定更加自由，比如更大的学习率、更随意的网络初始化等，同时网络的收敛速度更快，性能也更好。至此，卷积层、BN层、ReLU层、池化层一度成为网络模型的标配单元块。通过堆叠它们往往可以获得不错的模型性能
    数据标准化的其中一个好处，对于Sigmoid激活函数，当x<-2或x>2时，导数趋近于0，容易出现梯度弥散，所以可以将输入x标准化映射到0附近的一小段区间
    总之，网络层输入x分布相近，且在较小范围内时，更有利于函数的优化。可以通过数据标准化操作将数据x映射到x':x'=(x-μ_r)/sqrt(σ_r^2+ε)，μ_r为均值、σ_r^2为方差，ε是为防止出现分母为0错误而设置的较小数字，例如1e-8
    在基于Batch的训练阶段，获取每个网络层所有输入的统计数据u_r、σ_r^2，Batch内部的均值μ_B和方差σ_B^2可以近似为μ_r、σ_r^。在训练阶段，进行替换，通过标准化输入，并记录每个Batch的统计数据u_B、σ_B^2，用于统计真实的全局u_r、σ_r^2。测试阶段亦是如此
    标准化运算并没有引入额外的待优化变量，均通过统计得到，不需要参与梯度更新。实际上，为了提高BN层的表达能力，BN层作者引入了"scale and shift"技巧，将x'变量再次映射变换：x"=x'·γ+β
    γ参数实现对标准化后的x"再次进行缩放，β参数实现对标准化的x'进行平移，两个参数均通过反向传播算法自动优化，实现网络层"按需"缩放平移数据的分布的目的
    前向传播
        将BN层的输入记为x，输出记为x"
        训练阶段
            首先计算当前Batch的μ_B、σ_B^2，根据x_train"=(x_train-μ_B)·γ/sqrt(σ_B^2+ε)+β，计算BN层的输出
            同时按照
                μ_r←momentum·μ_r+(1-momentum)·μ_B
                σ_r^2←momentum·σ_r^2+(1-momentum)·σ_B^2
            迭代更新全局训练数据的统计值μ_r和σ_r^2，其中momentum是需要设置一个超参数，用于平衡更新幅度，默认为0.99
        测试阶段
            BN层根据x_test"=(x_test-u_r)·γ/sqrt(σ_r^2+ε)+β，计算输出x_test"，其中μ_r、σ_r^2、γ、β均来自训练阶段统计或优化的结果，在测试阶段直接使用，并不会更新这些参数
    反向更新
        在训练模式下的反向更新阶段，反向传播算法根据损失L求解梯度𝜕L/𝜕γ和𝜕L/𝜕β，并按着梯度更新法则自动优化γ、β参数
        需要注意的是，对于2D特征图输入X:[b,h,w,c]，BN层并不是计算每个点的μ_B、σ_B^2，而是在通道轴c上统计每个通道上面所有数据的μ_B、σ_B^2，μ_B、σ_B^2是每个通道上所有其他维度的均值和方差。
            # 构造输入 
            x=tf.random.normal([100,32,32,3]) 
            # 将其他维度合并，仅保留通道维度 
            x=tf.reshape(x,[-1,3]) 
            # 计算其他维度的均值 
            ub=tf.reduce_mean(x,axis=0) 
        在其他维度计算均值：
            Layer Norm，统计每个样本的所有特征的均值和方差
            Instance Norm，统计每个样本的每个通道上特征的均值和方差
            Group Norm，将c通道分成若干组，统计每个样本的通道组内的特征均值和方差
    BN层实现
        通过layers.BatchNormalization()类可以非常方便地实现BN层
        与全连接层、卷积层不同，BN层的训练阶段和测试阶段的行为不同，需要通过设置training标志位来区分训练模式还是测试模式
            network = Sequential([ # 网络容器 
                layers.Conv2D(6,kernel_size=3,strides=1), 
                # 插入BN 层 
                layers.BatchNormalization(), 
                layers.MaxPooling2D(pool_size=2,strides=2), 
                layers.ReLU(), 
                layers.Conv2D(16,kernel_size=3,strides=1), 
                # 插入BN 层 
                layers.BatchNormalization(), 
                layers.MaxPooling2D(pool_size=2,strides=2), 
                layers.ReLU(), 
                layers.Flatten(), 
                layers.Dense(120, activation='relu'), 
                # 此处也可以插入BN 层 
                layers.Dense(84, activation='relu'),  
                # 此处也可以插入BN 层 
                layers.Dense(10)])
        在训练阶段，需要设置网络的参数training=True以区分BN层是训练还是测试模型
            with tf.GradientTape() as tape:  
                # 插入通道维度 
                x = tf.expand_dims(x,axis=3) 
                # 前向计算，设置计算模式，[b, 784] => [b, 10] 
                out = network(x, training=True)
        在测试阶段，需要设置training=False，避免BN层采用错误的行为
            for x,y in db_test: # 遍历测试集 
                # 插入通道维度 
                x = tf.expand_dims(x,axis=3) 
                # 前向计算，测试模式 
                out = network(x, training=False) 

### 10.9 经典卷积网络

    在AlexNet出现之前的网络模型都是浅层的神经网络，Top-5错误率均在25%以上，AlexNet 8层的深层神经网络将Top-5错误率降低至16.4%，性能提升巨大，后续的VGG、GoogleNet模型继续将错误率降低，ResNet的出现首次将网络层数提升至152层
    AlexNet
        AlexNet接收224x224彩色图片数据为输入，经过5个卷积层和三个全连接层后得到样本属于1000个类别的概率分布。为了降低特征图的维度，AlexNet在第1、2、5个卷积层后添加了Max Pooling层，网络的参数量达到了6kw个。并且为了能够在当时的显卡设备上训练模型，还将卷积层、前2个全连接层等拆开在两块显卡上面分别训练，最后一层合并到一张显卡上面，进行反向传播更新。
        创新之处：层数达到了较深的8层；采用了ReLU激活函数，过去的神经网络大多采用Sigmoid激活函数，计算相对复杂，容易出现梯度弥散现象；引入Dropout层，提高了模型的泛化能力，防止过拟合
    VGG系列
        同样接收224x224大小的彩色图片数据，经过2个Conv-Conv-Pooling单元，和3个Conv-Conv-Conv-Pooling单元的堆叠，最后通过3层全连接层输出当前图片分别属于1000类别的概率分布。
        创新之处
            层数提升至19层；全部采用更小的3x3卷积核，相对于AlexNet中7x7的卷积核，参数量更少，计算代价更低；采用更小的池化层2x2窗口和步长s=2，而AlexNet中是步长s=2、3x3的池化窗口
    GoogleNet
        对于输入shape为[b,h,w,c_in]，1x1卷积层的输出为[b,h,w,c_out]，其中c_in为输入数据的通道数，c_out为输出数据的通道数，也是1x1卷积核的数量。1x1卷积核的一个特别之处在于，可以不改变特征图的宽高，而只对通道数c进行变换
        Google的层数为22，但是参数量只有AlexNet的1/12，性能远好于AlexNet
        采用模块化设计的思想，通过大量堆叠Inception模块，形成了复杂的网络结构。Inception模块的输入为X，通过4个子网络得到4个网络输出，在通道轴上面进行拼接合并，形成Inception模块的输出。这4个子网络是
            1x1卷积层；1x1卷积层，再通过一个3x3卷积层；1x1卷积层，再通过一个5x5卷积层；3x3最大池化层，再通过1x1卷积层

### 10.10 CIFAR10与VGG13实战

    MNIST是机器学习最常用的数据集之一，但由于手写数字图片非常简单，并且MNIST数据集只保存了图片灰度信息，并不适合输入设计为RGB三通道的网络模型。
    CIFAR10数据集由加拿大Canadian Institute For Advanced Research发布，包含了飞机、汽车、鸟、猫等共十大物体的彩色图片，每个种类收集了6000张32x32大小图片共6w张。其中5w作为训练数据集，1w作为测试数据集
        # 在线下载，加载CIFAR10 数据集 
        (x,y), (x_test, y_test) = datasets.cifar10.load_data() 
        # 删除y 的一个维度，[b,1] => [b] 
        y = tf.squeeze(y, axis=1) 
        y_test = tf.squeeze(y_test, axis=1) 
        # 打印训练集和测试集的形状
        print(x.shape, y.shape, x_test.shape, y_test.shape) 
        # 构建训练集对象，随机打乱，预处理，批量化 
        train_db = tf.data.Dataset.from_tensor_slices((x,y)) 
        train_db = train_db.shuffle(1000).map(preprocess).batch(128) 
        # 构建测试集对象，预处理，批量化 
        test_db = tf.data.Dataset.from_tensor_slices((x_test,y_test)) 
        test_db = test_db.map(preprocess).batch(128) 
        # 从训练集中采样一个Batch，并观察 
        sample = next(iter(train_db)) 
        print('sample:', sample[0].shape, sample[1].shape, 
            tf.reduce_min(sample[0]), tf.reduce_max(sample[0]))
    CIFAR10图片识别任务并不简单，主要是由于CIFAR10的图片内容需要大量细节才能呈现，而保存的图片分别率仅有32x32，使得主体部分信息较为模糊，甚至人眼都很难分辨。浅层的神经网络表达能力有限，很难训练优化到较好的性能。
    将网络实现为2个子网络：卷积子网络和全连接子网络。卷积自网络由5个子模块构成，每个子模块包含了Conv-Conv-MaxPooling单元结构
        conv_layers = [ # 先创建包含多网络层的列表 
            # Conv-Conv-Pooling 单元1 
            # 64 个3x3 卷积核, 输入输出同大小 
            layers.Conv2D(64, kernel_size=[3, 3], padding="same", activation=tf.nn.relu), 
            layers.Conv2D(64, kernel_size=[3, 3], padding="same", activation=tf.nn.relu), 
            # 高宽减半
            layers.MaxPool2D(pool_size=[2, 2], strides=2, padding='same'), 
            
            # Conv-Conv-Pooling 单元2,输出通道提升至128，高宽大小减半 
            layers.Conv2D(128, kernel_size=[3, 3], padding="same", activation=tf.nn.relu), 
            layers.Conv2D(128, kernel_size=[3, 3], padding="same", activation=tf.nn.relu), 
            layers.MaxPool2D(pool_size=[2, 2], strides=2, padding='same'), 
            
            # Conv-Conv-Pooling 单元3,输出通道提升至256，高宽大小减半 
            layers.Conv2D(256, kernel_size=[3, 3], padding="same", activation=tf.nn.relu), 
            layers.Conv2D(256, kernel_size=[3, 3], padding="same", activation=tf.nn.relu), 
            layers.MaxPool2D(pool_size=[2, 2], strides=2, padding='same'), 
        
            # Conv-Conv-Pooling 单元4,输出通道提升至512，高宽大小减半 
            layers.Conv2D(512, kernel_size=[3, 3], padding="same", activation=tf.nn.relu), 
            layers.Conv2D(512, kernel_size=[3, 3], padding="same", activation=tf.nn.relu), 
            layers.MaxPool2D(pool_size=[2, 2], strides=2, padding='same'), 
        
            # Conv-Conv-Pooling 单元5,输出通道提升至512，高宽大小减半 
            layers.Conv2D(512, kernel_size=[3, 3], padding="same", activation=tf.nn.relu), 
            layers.Conv2D(512, kernel_size=[3, 3], padding="same", activation=tf.nn.relu), 
            layers.MaxPool2D(pool_size=[2, 2], strides=2, padding='same') 
        ]
            # 利用前面创建的层列表构建网络容器 
        conv_net = Sequential(conv_layers)
    全连接子网络包含了3个全连接层，每层添加ReLU非线性激活函数，最后一层除外。
        # 创建3 层全连接层子网络 
        fc_net = Sequential([ 
            layers.Dense(256, activation=tf.nn.relu), 
            layers.Dense(128, activation=tf.nn.relu), 
            layers.Dense(10, activation=None), 
        ]) 
        # build2 个子网络，并打印网络参数信息 
        conv_net.build(input_shape=[4, 32, 32, 3]) 
        fc_net.build(input_shape=[4, 512]) 
        conv_net.summary()
        fc_net.summary()
    总参数量相对原始版本少很多。因为将网络实现为2个子网络，在进行梯度更新时，需要合并2个子网络的待优化参数
        # 列表合并，合并2 个子网络的参数 
        variables = conv_net.trainable_variables + fc_net.trainable_variables 
        # 对所有参数求梯度 
        grads = tape.gradient(loss, variables) 
        # 自动更新 
        optimizer.apply_gradients(zip(grads, variables)) 

### 10.11 卷积层变种

    空洞卷积
        普通的卷积层为了减少网络的参数量，卷积核的设计通常选择较小的1x1和3x3感受野大小。小卷积核使得网络提取特征时的感受野区域有限，但是增大感受野的区域又会增加网络的参数量核计算代价，因此需要权衡设计
        空洞卷积(Dilated/Atrous Convolution)能够较好地解决这个问题，在普通卷积的感受野上增加一个Dilation Rate参数，用于控制感受野区域的采样步长。采样步长的增大会使得感受野区域增大，但是实际参与运算的点数仍然保持不变
        注意卷积核窗口的移动步长s和感受野区域的采样步长Dilation Rate不同
        在使用空洞卷积设置网络模型时，需要精心设计Dilation Rate参数来避免出现网格效应，同时较大的Dilation Rate参数并不利于小物体的检测、语义分割等任务
            layer = layers.Conv2D(1,kernel_size=3,strides=1,dilation_rate=2)
        dilation_rate默认为1，普通卷积
    转置卷积
        Transposed Convolution/Fractionally Strided Convolution，也称为反卷积/Deconvolution，实际上反卷积在数学上定义为卷积的逆过程，但转置卷积并不能恢复原卷积的输入；通过在输入之间填充大量的padding来实现输出高宽大于输入高宽的效果，从而实现向上采样的目的。
        o+2p-k为s倍数
            转置卷积与普通卷积并不互为逆过程，不能恢复出对方的输入内容，仅能恢复出等大小的张量。
                # 创建X 矩阵，高宽为5x5 
                x = tf.range(25)+1 
                # Reshape 为合法维度的张量 
                x = tf.reshape(x,[1,5,5,1]) 
                x = tf.cast(x, tf.float32) 
                # 创建固定内容的卷积核矩阵 
                w = tf.constant([[-1,2,-3.],[4,-5,6],[-7,8,-9]]) 
                # 调整为合法维度的张量 
                w = tf.expand_dims(w,axis=2) 
                w = tf.expand_dims(w,axis=3) 
                # 进行普通卷积运算 
                out = tf.nn.conv2d(x,w,strides=2,padding='VALID')
                # 普通卷积的输出作为转置卷积的输入，进行转置卷积运算 
                xx = tf.nn.conv2d_transpose(out, w, strides=2,  
                    padding='VALID', 
                    output_shape=[1,5,5,1])
        o+2p-k不为s倍数
            当步长s>1时，[(i+2*p-k)/s向下取整运算使得出现多种不同输入尺寸i对应到相同的输出尺寸o上
            在TF中，不需要手动指定a参数，只需要指定输出尺寸即可，TF会自动推导
        矩阵角度
            普通卷积进行的是串行计算，效率低；为了加速运算，可以将卷积核W根据步长重排成稀疏矩阵W'，再通过W'@X'一次性完成运算
            对于给定O，如果要生成与X同形状大小的张量，可以将W'转置后重排后的O'进行矩阵相乘
                X'=W'^T@O'，得到的X'通过reshape变为与原来的输入X尺寸一致，内容不同。
            转置卷积具有"放大特征图"的功能，在生成对抗网络、语义分割等中得到了广泛应用，如DCGAN中的生成器通过堆叠转置卷积层实现逐层"放大"特征图
        转置卷积实现
            tf.nn.conv2d_transpose进行转置卷积运算时，需要额外手动设置输出的高度，并不支持自定义padding设置，='VALID'输出大小o=(i-1)s+k，='SAME'输出大小o=i·s
            也可以通过layers.Conv2DTranspose类创建一个转置卷积层，然后调用实例完成前向计算
                layer = layers.Conv2DTranspose(1,kernel_size=3,strides=1,padding='VALID') 
                xx2 = layer(out) # 通过转置卷积层
    分离卷积
        普通卷积在对多通道输入进行运算时，卷积核的每个通道与输入的每个通道分别进行卷积运算，得到多通道的特征图，再对应元素相加产生单个卷积核的最终输出
        分离卷积的计算，卷积核的每个通道与输入的每个通道进行卷积运算，得到多个通道的中间特征。这个多通道的中间特征张量接下来进行多个1x1卷积核的普通卷积运算，得到多个高宽不变的输出，输出在通道轴上进行拼接，从而产生最终的分离卷积层的输出。分离卷积第一步卷积使用单个卷积核，第二个卷积使用多个卷积核
        分离卷积对于同样的输入和输出，参数量是普通卷积的1/3

### 10.12 深度残差网络

    研究人员发现网络的层数越深，越有可能获得更好的泛化能力，但是当模型加深以后，网络变得越来越难训练，主要是由于梯度弥散和梯度爆炸现象造成的。在较深层数的神经网络中，梯度信息由网络的末层逐层传向网络的首层时，传递的过程中会出现梯度接近于0或梯度值非常大的现象。网络层数越深，这种现象可能会越严重。
    既然浅层神经网络不容易出现这些梯度现象，可以尝试给深层神经网络添加一种回退到浅层神经网络的机制。
    通过在输入和输出之间添加一条直线连接的skip connect可以让神经网络具有回退的能力。通过这种方式，网络模型可以自动选择是否经由这两个卷积层完成特征变换，还是直接跳过这中间的卷积层而选择skip connection，亦或结合中间的卷积层和skip connect的输出
    基于skip connection的深度残差网络(Residual Neural Network,ResNet)算法，在ImageNet数据集上的分类、检测等任务上面均取得了最好性能。
    ResNet原理
        ResNet通过在卷积层的输入和输出之间添加skip connection实现层数回退机制，输入x通过两个卷积层，得到特征变换后的输出F(x)，与输入x进行对象元素的相加运算，得到最终输出H(x)
            H(x)=x+F(x)
        H(x)为残差模块(Residual Block)。由于被skip connection包围的卷积神经网络需要学习映射F(x)=H(x)-x，故称为残差网络。
        为了能够满足输入x与卷积层的输出F(x)能够相加运算，需要输入x的shape与F(x)的shape完全一致。
        当出现shape不一致时，一般通过在skip connection上添加额外的卷积运算环节将输入x变换到与F(x)相同的shape，identity(x)以1x1的卷积运算居多，主要用于调整输入的通道数
    ResBlock实现
        深度残差网络并没有增加新的网络层类型，只是在输入和输出之间添加一条skip connection，因此没有针对ResNet的底层实现。在TF中通过调用普通卷积层即可实现残差模块。
            class BasicBlock(layers.Layer): 
                # 残差模块类 
                def __init__(self, filter_num, stride=1): 
                    super(BasicBlock, self).__init__() 
                    # f(x)包含了2 个普通卷积层，创建卷积层1 
                    self.conv1 = layers.Conv2D(filter_num, (3, 3), strides=stride, padding='same') 
                    self.bn1 = layers.BatchNormalization() 
                    self.relu = layers.Activation('relu') 
                    # 创建卷积层2 
                    self.conv2 = layers.Conv2D(filter_num, (3, 3), strides=1, padding='same') 
                    self.bn2 = layers.BatchNormalization() 
        在前向传播，只需要将F(x)和identity(x)相加，并添加ReLU激活函数即可。
            def call(self, inputs, training=None): 
                # 前向传播函数 
                out = self.conv1(inputs) # 通过第一个卷积层 
                out = self.bn1(out) 
                out = self.relu(out) 
                out = self.conv2(out) # 通过第二个卷积层 
                out = self.bn2(out) 
                # 输入通过identity()转换 
                identity = self.downsample(inputs) 
                # f(x)+x 运算 
                output = layers.add([out, identity]) 
                # 再通过激活函数并返回 
                output = tf.nn.relu(output) 
                return output

### 10.13 DenseNet

    skip connection的思想在ResNet上取得巨大成功，研究人员开始尝试不同的skip connection方案，其中比较流行的是DenseNet。DenseNet将前面所有层的特征图信息通过skip connect与当前层输出进行聚合，与ResNet的对应位置相加不同，DenseNet采用在通道轴c维度进行拼接操作，聚合特征信息
    输入X0通过H1卷积层得到输出X1，X1与X0在通道轴上进行拼接，得到聚合后的特征张量，送入H2卷积层，得到输出X2，如此循环，直到最后一层的输出和前面所有层的特征信息进行聚合得到模块的最终输出。这种基于skip connection稠密连接的模块称为dense block

### 10.14 CIFAR10与ResNet18实战

        class BasicBlock(layers.Layer):
            # 残差模块
            def __init__(self, filter_num, stride=1):
                super(BasicBlock, self).__init__()
                # 第一个卷积单元
                self.conv1 = layers.Conv2D(filter_num, (3, 3), strides=stride, padding='same')
                self.bn1 = layers.BatchNormalization()
                self.relu = layers.Activation('relu')
                # 第二个卷积单元
                self.conv2 = layers.Conv2D(filter_num, (3, 3), strides=1, padding='same')
                self.bn2 = layers.BatchNormalization()

                if stride != 1:# 通过1x1卷积完成shape匹配
                    self.downsample = Sequential()
                    self.downsample.add(layers.Conv2D(filter_num, (1, 1), strides=stride))
                else:# shape匹配，直接短接
                    self.downsample = lambda x:x

            def call(self, inputs, training=None):

                # [b, h, w, c]，通过第一个卷积单元
                out = self.conv1(inputs)
                out = self.bn1(out)
                out = self.relu(out)
                # 通过第二个卷积单元
                out = self.conv2(out)
                out = self.bn2(out)
                # 通过identity模块
                identity = self.downsample(inputs)
                # 2条路径输出直接相加
                output = layers.add([out, identity])
                output = tf.nn.relu(output) # 激活函数

                return output

        class ResNet(keras.Model):
            # 通用的ResNet实现类
            def __init__(self, layer_dims, num_classes=10): # [2, 2, 2, 2]
                super(ResNet, self).__init__()
                # 根网络，预处理
                self.stem = Sequential([layers.Conv2D(64, (3, 3), strides=(1, 1)),
                                        layers.BatchNormalization(),
                                        layers.Activation('relu'),
                                        layers.MaxPool2D(pool_size=(2, 2), strides=(1, 1), padding='same')
                                        ])
                # 堆叠4个Block，每个block包含了多个BasicBlock,设置步长不一样
                self.layer1 = self.build_resblock(64,  layer_dims[0])
                self.layer2 = self.build_resblock(128, layer_dims[1], stride=2)
                self.layer3 = self.build_resblock(256, layer_dims[2], stride=2)
                self.layer4 = self.build_resblock(512, layer_dims[3], stride=2)

                # 通过Pooling层将高宽降低为1x1
                self.avgpool = layers.GlobalAveragePooling2D()
                # 最后连接一个全连接层分类
                self.fc = layers.Dense(num_classes)

            def call(self, inputs, training=None):
                # 通过根网络
                x = self.stem(inputs)
                # 一次通过4个模块
                x = self.layer1(x)
                x = self.layer2(x)
                x = self.layer3(x)
                x = self.layer4(x)

                # 通过池化层
                x = self.avgpool(x)
                # 通过全连接层
                x = self.fc(x)

                return x

            def build_resblock(self, filter_num, blocks, stride=1):
                # 辅助函数，堆叠filter_num个BasicBlock
                res_blocks = Sequential()
                # 只有第一个BasicBlock的步长可能不为1，实现下采样
                res_blocks.add(BasicBlock(filter_num, stride))

                for _ in range(1, blocks):#其他BasicBlock步长都为1
                    res_blocks.add(BasicBlock(filter_num, stride=1))

                return res_blocks

        def resnet18():
            # 通过调整模块内部BasicBlock的数量和配置实现不同的ResNet
            return ResNet([2, 2, 2, 2])

        def resnet34():
            # 通过调整模块内部BasicBlock的数量和配置实现不同的ResNet
            return ResNet([3, 4, 6, 3])
    在设计深度卷积神经网络时，一般按照特征图高宽h/w逐渐减少，通道数c逐渐增大的经验法则。可以通过堆叠通道数逐渐增大的Res Block来实现高层特征的提取，通过bulid_resblock可以一次完成多个残差模块的新建。
    通过调整每个Res Block的堆叠数量和通道数可以产生不同的ResNet
        tf.random.set_seed(2345)

        def preprocess(x, y):
            # 将数据映射到-1~1
            x = 2*tf.cast(x, dtype=tf.float32) / 255. - 1
            y = tf.cast(y, dtype=tf.int32) # 类型转换
            return x,y

        (x,y), (x_test, y_test) = datasets.cifar10.load_data() # 加载数据集
        y = tf.squeeze(y, axis=1) # 删除不必要的维度
        y_test = tf.squeeze(y_test, axis=1) # 删除不必要的维度
        print(x.shape, y.shape, x_test.shape, y_test.shape)

        train_db = tf.data.Dataset.from_tensor_slices((x,y)) # 构建训练集
        # 随机打散，预处理，批量化
        train_db = train_db.shuffle(1000).map(preprocess).batch(512)

        test_db = tf.data.Dataset.from_tensor_slices((x_test,y_test)) #构建测试集
        # 随机打散，预处理，批量化
        test_db = test_db.map(preprocess).batch(512)
        # 采样一个样本
        sample = next(iter(train_db))
        print('sample:', sample[0].shape, sample[1].shape,
            tf.reduce_min(sample[0]), tf.reduce_max(sample[0]))

        def main():

            # [b, 32, 32, 3] => [b, 1, 1, 512]
            model = resnet18() # ResNet18网络
            model.build(input_shape=(None, 32, 32, 3))
            model.summary() # 统计网络参数
            optimizer = optimizers.Adam(lr=1e-4) # 构建优化器

            for epoch in range(100): # 训练epoch

                for step, (x,y) in enumerate(train_db):

                    with tf.GradientTape() as tape:
                        # [b, 32, 32, 3] => [b, 10],前向传播
                        logits = model(x)
                        # [b] => [b, 10],one-hot编码
                        y_onehot = tf.one_hot(y, depth=10)
                        # 计算交叉熵
                        loss = tf.losses.categorical_crossentropy(y_onehot, logits, from_logits=True)
                        loss = tf.reduce_mean(loss)
                    # 计算梯度信息
                    grads = tape.gradient(loss, model.trainable_variables)
                    # 更新网络参数
                    optimizer.apply_gradients(zip(grads, model.trainable_variables))

                    if step %50 == 0:
                        print(epoch, step, 'loss:', float(loss))

                total_num = 0
                total_correct = 0
                for x,y in test_db:

                    logits = model(x)
                    prob = tf.nn.softmax(logits, axis=1)
                    pred = tf.argmax(prob, axis=1)
                    pred = tf.cast(pred, dtype=tf.int32)

                    correct = tf.cast(tf.equal(pred, y), dtype=tf.int32)
                    correct = tf.reduce_sum(correct)

                    total_num += x.shape[0]
                    total_correct += int(correct)

                acc = total_correct / total_num
                print(epoch, 'acc:', acc)
    ResNet18 的网络参数量共1100 万个，经过50 个Epoch 后，网络的准确率达到了79.3%。在精挑超参数、数据增强等手段加持下，准确率可以达到更高。

## 十一、循环神经网络

    人工智能的强力崛起，可能是人类历史上最好的事情，也可能是最糟糕的事情。——史蒂芬·霍金
    卷积神经网络利用数据的局部相关性和权值共享的思想大大减少了网络的参数量，非常适合于图片这种具有空间局部相关性的数据，已经被成功地一用到计算机领域的一系列任务上。自然界的信号除了具有空间维度外，还有一个时间维度。具有时间维度的信号非常常见，这类数据并不一定具有局部相关性，同时数据在时间维度上的长度也是可变的，卷积神经网络并不擅长处理此类数据。

### 11.1 序列表示方法

    具有先后顺序的数据一般称为序列，比如随时间而变化的商品价格数据就是非常典型的序列。
    对于很多信号并不能直接用一个标量数值表示，比如每个时间戳产生长度为n的特征向量。
    神经网络本质上是一系列的矩阵相乘、相加等数学运算，并不能直接处理字符串类型的数据。如果希望神经网络能够用于自然语言处理任务，则需要把单词或字符转化为数值。
    把文字编码位数值的过程称为word embedding。one-hot是一种方法，但是one-hot编码是高维度并且极其稀疏的，计算效率较低，并且忽略了单词先天具有的语义相关性。
    在自然语言处理领域，有专门的一个研究方向在探索如何学习到单词的表示向量(word vector)，使得语义层面的相关性能够很好地通过word vector体现出来。一个衡量词向量之间相关度的方法就是余弦相关度(cosine similarity)
        similarity(a,b)=cos(θ)=a·b/|a·b|，a和b为两个词向量
    embedding层
        在神经网络中，单词的表示向量可以直接通过训练的方式得到，将单词的表示层称为embedding层。embedding层负责把单词编码为某个词向量v，接受的是采用数字编码的单词编号i，系统总单词数量记为Nvocab，输出长度为n的向量v
            v=f_θ(i|Nvocab,n)
        embedding层实现起来非常简单，构建一个shape为[Nvocab,n]的查询表对象table，对于任意的单词编号i，只需要查询到对应位置上的向量并返回：v=table[i]
        embedding层是可训练的，它可放置在神经网络之前，完成单词到向量的转换，得到的表示向量可以继续通过神经网络完成后续任务，并计算误差L，采用梯度下降算法来实现端到端的训练
        在TF中，通过layers.Embedding(Nvocab,n)来定义一个word embedding层，其中Nvocab参数指定词汇数量，n指定单词向量的长度
            x = tf.range(10) # 生成10 个单词的数字编码 
            x = tf.random.shuffle(x) # 打散 
            # 创建共10 个单词，每个单词用长度为4 的向量表示的层 
            net = layers.Embedding(10, 4) 
            out = net(x) # 获取词向量
            net.embeddings #查看Embedding层内部的查询表table
            net.embeddings.trainable #张量的可优化属性，即可以通过梯度下降算法优化
    预训练的词向量
        Embedding层的查询表是随机初始化的，需要从0开始训练。实际上可以是用预训练的word embedding模型来得到单词的表示方法，基于预训练模型的词向量相当于迁移了整个语义空间的知识，往往能够得到更好的性能。
        目前应用的比较广泛的预训练模型有Word2Vec和Glove等。它们已经在海量语料库训练得到了较好的词向量表示方法，并可以直接导出学习到的词向量表，方便迁移到其他任务。比如GloVe模型Glove.6B.50d，词汇量为40万，每个单词是用长度为50的向量表示，用户只需要下载对应的模型文件即可。
            # 从预训练模型中加载词向量表 
            embed_glove = load_embed('glove.6B.50d.txt') 
            # 直接利用预训练的词向量表初始化Embedding 层 
            net.set_weights([embed_glove])
        经过预训练的词向量模型初始化的Embedding层可以设置为不参与训练：net.trainable=False。如果希望能够学到区别于预训练词向量模型不同的表示方法，可以把Embedding层包含进反向传播算法中去，利用梯度下降来微调单词表示方法

### 11.2 循环神经网络

    对于序列信号，例如文本序列
    全连接层
        网络参数量较多，内存占用和计算代价较高，网络结构动态变换
        每个全连接层子网络Wi和bi只能感受当前词向量的输入，并不能感受之前和之后的语境环境信息，导致句子整体语义的缺失，每个子网络只能根据自己的输入来提取高层特征。
        以下是解决方法
    共享权值
        卷积神经网络在处理局部相关数据时优于全连接网络，是因为充分利用了权值共享的思想，大大减少了网络的参数量。
        但是，这种网络结构并没有考虑序列之间的先后顺序，将词向量打乱次序后仍然能获得相同的输出，无法获取有效的全局语义信息
    全局语义
        让网络能够按序提取词向量的语义信息，并累积成整个句子的全局语义信息。可以利用内存机制，如果网络能够提供一个单独的内存变量，每次提取词向量的特征并刷新内存变量，直到最后一个输入完成，此时的内存变量，直到最后一个输入完成，此时的内存变量即存储了所有序列的语义特征，并且由于输入序列之间的先后顺序，使得内存变量内容与序列顺序紧密关联
        将内存机制实现为一个状态张量h，除了原来的Wxh参数共享外，额外增加了一个Whh参数，每个时间戳t上状态张量h刷新机制为
            ht=σ(Wxh·x_t+Whh·h_(t-1)+b)
        其中状态张量h0为出事的内存状态，可以初始化为全0，经过s个词向量的输入后得到网络最终的状态张量hs，hs较好地代表了句子的全局语义信息，基于hs通过某个全连接层分类器即可完成情感分类任务
    循环神经网络
        在每个时间戳t，网络层接受当前时间戳的输入xt和上一个时间戳的网络状态向量h_(t-1)，经过ht=f_θ(h_(t-1),xt)
        变换后得到当前时间戳的新状态向量ht，并写入内存状态中，其中f_θ代表了网络的运算逻辑，θ为网络参数集。在每个时间戳上，网络层均有输出产生ot，ot=gΦ(ht)，即将网络的状态向量变换后输出
        上述网络结构在时间戳上折叠，网络循环接受序列的每个特征向量xt，并刷新内部状态向量ht，同时形成输出ot，这种网络结构称为循环网络结构(RNN)。
        如果使用张量Wxh、Whh和偏置b来参数化f_θ网络，并按照ht=σ(Wxh·x_t+Whh·h_(t-1)+b)方式更新内存状态，把这种网络称为基本的循环神经网络，如果没有特别说明，一般说的循环神经网络即指这种实现。在循环神经网络中，激活函数更多地采用tanh函数，并且可以选择不使用偏置b来进一步减少参数量。状态向量ht可以直接用作输出，即ot=ht，也可以对ht做一个简单的线性变换ot=Whoht后得到每个时间戳上的网络输出ot

### 11.3 梯度传播

    通过循环神经网络的更新表达式可以看出输出对张量Wxh、Whh和偏置b均是可导的，可以利用自动梯度算法来求解网络的梯度。
    在推导𝜕ℒ/𝜕𝑾ℎℎ的过程中发现，𝜕h𝑡/𝜕hi的梯度包含了Whh的连乘运算，是导致循环神经网络训练困难的根本原因

### 11.4 RNN层使用方法

    在TF中，可以通过layers.SimpleRNNCell来完成ht=σ(Wxh·x_t+Whh·h_(t-1)+b)计算。在TF中，RNN表示通用意义上的循环神经网络，对于上述介绍的基础神经网络，一般称为SimpleRNN。SimpleRNN与SimpleRNNCell的区别在于，后者的层仅仅是完成了一个时间戳的前向运算，前者的层一般是基于Cell层实现的，它在内部已经完成了多个时间戳的循环运算，使用更为快捷
    SimpleRNNCell
            cell = layers.SimpleRNNCell(3) # 创建RNN Cell，内存向量长度为3 
            cell.build(input_shape=(None,4)) # 输出特征长度n=4 
            #cell.trainable_variables # 打印wxh, whh, b 张量
        SimpleRNNCell内部维护了3个张量，kernel变量即Wxh张量，recurrent_kernel变量即Whh张量，bias变量即偏置b向量。但是RNN的Memory向量并不由SimpleRNNCell维护，需要用户自行初始化向量h0并记录每个时间戳上的ht
        通过调用Cell实例即可完成前向运算：ot,[ht]=Cell(xt,[h_(t-1)])
        对于SimpleRNNCell来说，ot=ht，并没有经过额外的线性层转换，是同一个对象；[ht]通过一个List包裹起来，是为了与LSTM、GRU等RNN变种格式统一。在循环神经网络的初始化阶段，状态向量h0一般初始化为全0向量
            # 初始化状态向量，用列表包裹，统一格式 
            h0 = [tf.zeros([4, 64])] 
            x = tf.random.normal([4, 80, 100]) # 生成输入张量，4 个80 单词的句子 
            xt = x[:,0,:] # 所有句子的第1 个单词 
            # 构建输入特征n=100,序列长度s=80,状态长度=64 的Cell 
            cell = layers.SimpleRNNCell(64) 
            out, h1 = cell(xt, h0) # 前向计算
        可以通过id(name)查看变量的id，out和h1[0]一致。对于长度为s的训练，需要循环通过Cell类s次才算完成一次网络层的前向运算
            h = h0 # h 保存每个时间戳上的状态向量列表 
            # 在序列长度的维度解开输入，得到xt:[b,n] 
            for xt in tf.unstack(x, axis=1): 
                out, h = cell(xt, h) # 前向计算,out 和h 均被覆盖 
            # 最终输出可以聚合每个时间戳上的输出，也可以只取最后时间戳的输出
        最后一个时间戳的输出变量out将作为网络的最终输出。可以将每个时间戳上的输出保存，然后求和或者均值，将其作为网络的最终输出
    多层SimpleRNNCell网络
        与卷积神经网络一样，循环神经网络虽然在时间轴上面展开了多次，但只能算一个网络层。通过在深度方向堆叠多个Cell类来实现深层卷积神经网络一样的效果，从而大幅提升网路的表达能力。但是循环神经网络相对于卷积神经网络很容易出现梯度弥散和梯度爆炸，常见的RNN层数一般在十层以内
            x = tf.random.normal([4,80,100]) 
            xt = x[:,0,:] # 取第一个时间戳的输入x0 
            # 构建2 个Cell,先cell0,后cell1，内存状态向量长度都为64 
            cell0 = layers.SimpleRNNCell(64) 
            cell1 = layers.SimpleRNNCell(64) 
            h0 = [tf.zeros([4,64])] # cell0 的初始状态向量 
            h1 = [tf.zeros([4,64])] # cell1 的初始状态向量
        在时间轴上面循环计算多次来实现整个网络的前向运算，每个时间戳上的输入xt首先通过第一层，得到输出out0，再通过第二层，得到输出out1
            for xt in tf.unstack(x, axis=1): 
                # xt 作为输入，输出为out0 
                out0, h0 = cell0(xt, h0) 
                # 上一个cell 的输出out0 作为本cell 的输入 
                out1, h1 = cell1(out0, h1)
        实际上，可以先完成输入在第一层上所有时间戳的计算，并保存第一层在所有时间上的输出列表，再计算第二层、第三层等的传播。使用这种方式，需要一个额外的List来保存上一层所有时间戳上面的状态信息：middle_sequences.append(out0)
        需要注意的是，循环神经的每一层、每一个时间戳上面均有状态输出。一般来说，最末层Cell的状态有可能保存了高层的全局语义特征，因此一般使用最末层的输出作为后续任务网络的输入。每层最后一个时间戳上的状态输出包含了整个序列的全局信息，如果只希望选用一个状态变量来完成后续任务，比如情感分类问题，一般选用最末层、最末时间戳的状态输出最为合适
    SimpleRNN层
        通过SimpleRNNCell层高层接口可以非常方便地完成准备和计算过程
            layer=leyers.SimpleRNNCell(64)
            x=tf.random.normal([4,80,100])
            out=layer(x)
        可以看到，通过SimpleRNN可以仅需一行代码即可完成整个前向运算过程，默认返回最后一个时间戳上的输出
        如果希望返回所有时间戳上的输出列表，可以设置return_sequences=True参数
            #创建RNN层时，设置返回所有时间戳上的输出
            layer=layers.SimpleRNNCell(64,return_sequences=True)
            out=layer(x)
        同样可以堆叠多个SimpleRNN得到多层循环神经网络
            net = keras.Sequential([ # 构建2 层RNN 网络
                # 除最末层外，都需要返回所有时间戳的输出，用作下一层的输入 
                layers.SimpleRNN(64, return_sequences=True), 
                layers.SimpleRNN(64), 
            ]) 
            out = net(x) # 前向计算
        每层都需要要上一层在每个时间戳上面的状态输出，除了最末层以外，所有的RNN层都需要返回每个时间戳上面的状态输出，通过设置return_sequences=True来实现。

