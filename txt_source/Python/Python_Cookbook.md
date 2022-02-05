# Python Cookbook

## 第1章 数据结构和算法

    Python内置了许多非常有用的数据结构，比如列表、集合以及字典
    通常需要考虑比如搜索、排序、排列以及筛选这一类常见的问题。在collections模块中包含了针对各种数据结构的解决方案

### 1.1 将序列分解为单独的变量

    将序列(或可迭代对象)分解为单独的变量，可以用赋值的方式，但变量的总数和结构要与序列相吻合
    
    可以选一个用不到的变量名丢弃某些特定的值

### 1.2 从任意长度的可迭代对象中分解元素

    从某个可迭代对象中分解出N个元素，如果这个可迭代对象的长度可能超过N，会导致出现“分解的值过多”的异常
    对于多个值，用*修饰的变量可以将对应的变量变为新的列表
        *式的语法在迭代一个边长的元组序列时尤其有用
        同样可以用来丢弃多个特定的值
        一个赋值式只能有一个*式

    递归不是Python的强项，因为其内在的递归限制

### 1.3 保存最后N个元素

    collections.deque能够保存有限的历史记录
        q=deque(maxlen=n)保存固定长度的队列，默认不限制长度
        q.append(elem),队列右侧添加，q.appendleft(elem)队列左侧添加
        q.pop()、q.popleft()队列右侧、左侧弹出
        复杂度为O(1)，而列表为O(N)
    
    yield与return一样，都会返回值，但return意味着程序段的结束，而yield则只是交出CPU的使用权，并未结束程序段，send()和next()会继续中断的地方

### 1.4 找到最大或最小的N个元素

    heapq模块中有nlargest()和nsmallest()能从集合中找出最大或最小的N个元素，并接受参数key，工作在更加复杂的数据结构之上

    如果寻找的N个元素与集合中元素的总数目相比很小，heapq.heapify(heap)会将集合转化成列表，并以堆的顺序排列，而堆heap[0]总是最小的元素，而heapq.heappop(heap)则实现了堆排序(将最小的元素弹出，以第二小的元素替代)
    当所要找的元素数量相对较小时，nlargest()和nsmallest()才是最实用的.N=1时，min()和max()会更加快.如果N和集合本身的大小差不多，更快的方法是对集合排序，然后做切片操作.nlargest()和nsmallest()的实际实现会根据使用它们的方式而有所不同，可能会相应作出一些优化措施.

### 1.5 实现优先级队列

    同样是利用heapq heappush(queue,{-priority,index,item})，将priority作为堆排序主参考，index作为额外索引值，是唯一的，避免优先级相同对item进行比较，取负数是因为heappush从小到大排序
    再用heappop弹出优先级最高的元素

    这样是稳定的，即优先级相同的先进先出
    复杂度为O(logN)

### 1.6 在字典中将键映射到多个值上

    collections.defaultdict(type)自动初始化第一个值，只需要关注添加元素，type确定键映射到的值为列表还是集合
        会自动创建字典表项以待稍后访问(即使这些表项当前在字典中还没有找到).如果不想要这个功能，可以在普通的字典调用setdefault()方法来取代

    对自己第一个值做初始化操作，会变得杂乱

### 1.7 让字典保持有序

    控制字典中元素的顺序，可以使用collections OrderedDict类，当对字典做迭代时，会严格按照元素初始添加的顺序进行
    如果想在进行JSON编码时精确控制各字段的顺序，只要首先在OrderedDict中构建就可以
    json.dumps(OrderedDict类)

    OrderedDict内部维护了一个双向链表，会根据元素加入的顺序来排列键的位置.第一个新加入的元素被放置在链表的末尾.接下来对已存在的键做重新赋值不会改变键的顺序
    OrderedDict大小是普通字典的2倍多，这是由于它额外创建的链表所导致.如果涉及大量OrderedDict实例，需要认真对应用做需求分析，从而判断使用OrderedDict所带来的好处是否能超越因额外的内存开销所带来的缺点

### 1.8 与字典有关的计算问题

    为了能对字典内容做些有用的计算，通常会利用zip()将字典的键和值反转过来.
    注意zip()创建了一个迭代器，内容只能被消费一次

    如果尝试在字典上执行常见的数据操作，将会发现它们只会处理键，而不是值
    可以利用字典的values()方法来解决这个问题
    也可以通过key参数传递键值
    当涉及(value,key)对的比较时，如果碰巧有多个条目拥有相同的value值，那么此时key值将用来作为判定结果的依据

### 1.9 在两个字典中寻找相同点

    要找出这两个字典的相同之处，只需通过keys()或者items()方法执行常见的集合操作

    字典的keys()方法会返回keys-view对象，其中暴露了所有的键.字典的键支持常见的集合操作.
    字典的items()方法返回由(key,value)对组成的items-view对象.这个对象支持类似的集合操作.
    字典的values()方法并不支持集合操作，如果必须执行这样的操作，可以先将值转化为集合来实现

### 1.10 从序列中移除重复项且保持元素间顺序不变

    如果序列中的值是可哈希的，那么这个问题可以通过使用集合和生成器轻松解决
    如果一个对象是可哈希的，那么在它的生存期内必须是不可变的，它需要有一个__hash__()方法.整数、浮点数、字符串、元组都是不可变的
    如果在不可哈希的对象(比如列表)序列中去除重复项，需要一个参数key，用来指定一个函数用来将序列中的元素转换为可哈希的类型，这么做的目的是为了检测重复项

    如果只是去除重复项，构建一个集合足够简单
    但是这种方法不能保证元素间的顺序不变
    对生成器的使用，使得这个函数不必绑定在只能对列表进行处理

### 1.11 对切片命名

    假设有一些代码用来从字符串的固定位置中取出具体的数据(比如从一个平面文件或类似的格式)
        平面文件是一种包含设有相对关系结构的记录文件
    此时可对切片命名
        name=slice(start,stop,step)
        string[name] #引用

    内置的slice()函数会创建一个切片对象，可用在任何允许进行切片操作的地方
    如果有一个slice对象的实例s，可以分别通过s.start、s.stop、s.step属性来得到关于该对象的信息
    可以通过使用indices(size)方法将切片映射到特定大小的序列上.这会返回一个(start,stop,step)元组，所有的值都已经恰当地限制在边界以内(当作索引操作时可避免出现IndexError异常)

### 1.12 找出序列中出现次数最多的元素

    collections Counter类正是为此类问题设计的。它有一个非常方便的most_common()方法可以直接得到答案
        C=collections.Counter(序列)创建对象
        C.most_common(n)得到出现最为频繁的前n个

    可以给Counter对象提供任何可哈希的对象序列作为输入.在底层实现中,Counter是一个字典，在元素和它们出现的次数间做了映射
        所以可以通过字典的方式修改元素出现次数
        或者C.update(more)
    Counter对象可以同各种数学运算操作结合起来使用

### 1.13 通过公共键对字典列表排序

    可以利用operator模块中的itemgetter函数对这类结构进行排序
        result=sorted(dict,key=itemgetter(somekey))
    itemgetter()函数还可以接受多个键

    dict被传递给内建的sorted()函数，该函数接受一个关键字参数key，这个参数应该代表一个可调用对象。该对象从dict中接受一个单独的元素作为输入并返回一个用来做排序依据的值。itemgetter()函数创建的就是这样一个可调用对象
    函数operator.itemgetter()接受的参数可作为查询的标记。用来从dict的记录中提取出所需要的值。它可以是字典的键名称、用数字表示的列表元素或是任何可以传给对象的__getitem__()方法的值.如果传多个标记给itemgetter()，那么它产生的可调用对象将返回一个包含所有元素在内的元组，然后sorted()将根据对元组的排序结果来排列输出结果
    有时候会用lambda表达式来取代itemgetter()的功能
        sorted(dict,key=lambda r:(r['key1'],r['key2']))
        但是用itemgetter()通常会运行得更快一些

### 1.14 对不原生支持比较操作的对象排序

    内建的sorted()函数可接受一个用来传递可调用对象的参数key，而该可调用对象会返回待排序对象中的某些值，sorted则利用这些值来比较对象。

    要使用lambda表达式还是operator.attrgetter()只是一种个人喜好。但是通常来说，后者要更快一些，而且具有允许同时提取多个字段值的能力。这与1.13的针对字典的使用很类似
    涉及到lambda还是operator.*getter()得，也适用于min()和max()这样的函数

### 1.15 根据字段将记录分组

    itertools.groupby()函数在对数据进行分组时特别有用。
    可以先用operator.itemgetter()对数据进行排序，然后在使用itertools.groupby(data,key=itemgetter())
        会返回key和对应数据成对的序列

    函数groupby()通过扫描序列找出拥有相同值(或是由参数key指定的函数所返回的值)的序列项，并将它们分组。groupby()创建了一个迭代器，而在每次迭代时都会返回一个值和一个子迭代器，这个子迭代器可以产生所有在该分组内具有该值的项
    在这里重要的是首先要根据感兴趣的字段对数据进行排序。因为groupby()只能检查连续的项，不首先排序的话，得到的结果将是断续的
    如果只是简单地根据日期将数据分组到一起，放进一个大的数据结构中以允许进行随机访问，那么利用defaultditc()构建一个一键多值字典可能会更好
    如果不考虑内存方面的因素，这种方式会比前面先排序再迭代更快

### 1.16 筛选序列中的元素

    要筛选序列中的数据，通常最简单的方法是使用列表推导式
    使用列表推导式的一个潜在缺点是如果原始输入非常大的话，这么做可能会产生一个庞大的结果。如果需要考虑这个问题，可以使用生成器表达式通过迭代的方式产生筛选的结果
    有时候筛选的标准没法简单地表示在列表推导式或生成器表达式中。比如，假设筛选过程涉及异常处理或者其他一些复杂的细节。基于此，可以将处理筛选逻辑的代码放到单独的函数中，然后使用内建的filter()函数处理
        filter(fun,values)

    列表推导式和生成器表达式通常是用来筛选数据的最简单和最直接的方式。它们也具有同时对数据做转换的能力
    关于筛选数据，有一种情况是用新值替换不满足标准的值，而不是丢弃它们。
    另一个筛选工具是itertools.compress()，它接受一个可迭代对象以及一个布尔选择器序列作为输入。输出时，它会给出所有在相应的布尔选择器中为True的可迭代对象元素。如果想把对一个序列的筛选结果施加到另一个相关的序列上时，就会非常有用

### 1.17 从字典中提取子集

    利用字典推导式可以轻松解决

    大部分可以用字典推导式解决的问题也可以通过创建元组序列然后将它们传给dict()函数来完成
    但是字典推导式的方案更加清晰，而且实际运行起来也要快很多
    如果需要考虑性能因素，那么通常都需要花一点时间来研究它

### 1.18 将名称映射到序列的元素中

    相比普通的元组，collections.namedtuple()(命名元组)只增加了极小的开销就提供了这些便利。实际上collections.namedtuple()是一个工厂方法，它返回的是Python中标准元组类型的子类。提供给它一个类型名称以及相应的字段，就返回一个可实例化的类、已经定义好的字段传入值等
    ex: from collections import namedtuple
        Subscriber = namedtuple('Subscriber',['addr','joined'])
        sub = Subscriber('jonesy@example.com','2012-10-19')
        sub.addr    sub.joined
    尽管namedtuple的实例看起来就像一个普通的类实例，但它的实例与普通的元组是可互换的，而且支持所有普通元组所支持的操作，例如索引和分解
    命名元组的主要作用在于将代码同它所控制的元素位置间解耦。如果从数据库调用中得到一个大型的元组列表，而且通过元素的位置来访问数据，那么假如在表单中新增了一列数据，那么代码就会崩溃。但如果首先将返回的元组转型为命名元组，就不会出现问题
    通过位置来引用元素常常使得代码的表达力不够强，而且也很依赖于记录的数据结构。

    namedtuple的一种可能用法是作为字典的替代，后者需要更多的空间来存储。如果要构建涉及字典的大型数据结构，使用namedtuple会更加高效。但是namedtuple是不可变的
    如果需要修改任何属性，可以通过使用namedtuple实例的_replace()方法实现。该方法会创建一个全新的命名元组，并对相应的值做替换
    _replace()方法有一个微妙的用途，那就是它可以作为一种简便的方法填充具有可选或缺失字段的命名元组。首先创建一个包含默认值的“原型”元组，然后使用_replace()方法创建一个新的实例，把相应的值替换掉
    应该要注意如果我们的目标是定义一个高效的数据结构，而且将来会修改各种实例属性，那么使用namedtuple并不是最佳选择。可以考虑定义一个使用__slots___属性的类

### 1.19 同时对数据做转换和换算

    有一种非常优雅的方式能将数据换算和转换结合在一起——在函数参数中使用生成器表达式

    这种解决方案展示了当把生成器表达式作为函数的单独参数时在语法上的一些微妙之处(即，不必重复使用括号)
    比起首先创建一个临时的列表，使用生成器做参数通常是更为高效和优雅的方式
    前者也能工作，但引入了一个额外的步骤而且创建了额外的列表。如果数据源非常巨大，那么就会创建一个庞大的临时数据结构，而且只用一次就要丢弃。基于生成器的解决方案可以以迭代的方式转换数据，在内存使用上要高效得多
    某些特定的换算函数比如min()和max()都可接受一个key参数，当可能倾向于使用生成器时会很有帮助

### 1.20 将多个映射合并为单个映射

    假设有两个字典，现在假设想执行查找操作，需要检查这两个字典。一种简单的方法是利用collections.ChainMap类来解决这个问题
        c = collections.ChainMap

    ChainMap可接受多个映射然后在逻辑上使它们表现为一个单独的映射结构。但这些映射在字面上并不会合并在一起。相反，ChainMap只是简单地维护一个记录底层映射关系的列表，然后重定义常见的字典操作来扫描这个列表。大部分的操作都能正常工作
    如果有重复的键，那么这里会采用第一个映射中所对应的值。
    修改映射的操作总是会作用在列出的第一个映射结构上
    ChainMap与带有作用域的值，比如编程语言中的变量(即全局变量、局部变量等)一起工作时特别有用
        values = ChainMap()
        values = values.new_child()
        values['x']=1
        values=values.parents
    作为ChainMap的替代方案，可能会考虑利用字典的update()方法将多个字典和合并在一起
    但这需要单独构建一个完整的字典对象(或者修改其中现有的一个字典，这就破坏了原始数据)。此外，如果其中任何一个原始字典做了修改，这个改变都不会反应到合并后的字典中
    而ChianMap使用的就是原始的字典，因此不会产生这种行为

## 第2章 字符串和文本

    无论是解析数据还是产生输出，几乎每一个有实用价值的程序都会设计某种形式的文本处理。有关文本操作的常见问题，有拆分字符串、搜索、替换、词法分析以及解析。许多任务都可以通过内建的字符串方法轻松解决。但是，更复杂的操作可能会需要用到正则表达式或者创建完整的解析器才能得到解决。

### 2.1 针对任意多的分隔符拆分字符串

    字符串对象的split()方法只能处理非常简单的情况，而且不支持多个分隔符，对分隔符周围可能存在的空格也无能为力。当需要一些更为灵活的功能时，应该使用re.split()方法
        re.split("规则",string)

    re.split()是很有用的，因为可以为分隔符指定多个模式。例如，分隔符可以是逗号、分号或是空格符(后面可跟着任意数量的额外空格)。只要找到了对应的模式，无论匹配点的两端是什么字段，整个匹配的结果就成为那个分隔符。最终得到的结果是字段列表，同str.split()得到的结果一样
    当使用re.split()时，需要小心正则表达式模式中的捕获组是否包含在了括号中。如果用到了捕获组，那么匹配的文本也会包含在最终结果中。
        ex: re.split(r'(;|,|\s)\s*',line)
        (||)结构|用以间隔
    在特定的上下文中获取到分隔字符也可能是有用的。利用索引[start:end:step]选取分隔结果和分隔字符
    如果不想在结果中看到分隔字符，但仍想用括号来对正则表达式进行分组，请确保用的是非捕获组，以(?:...)的形式指定

### 2.2 在字符串的开头或结尾处做文本匹配

    有一种简单的方法可用来检查字符串的开头或结尾，只要使用str.startswith()和str.endswith()方法就可以了
    如果需要同时针对多个选项做检查，只需给startswith()和endswith()提供包含可能选项的元组即可
    这是python中需要把元组当成输入的一个地方。确保输入的是元组

    startswith()和endswith()方法提供了一种非常方便的方式来对字符串的前缀和后缀做基本的检查。类似的操作也可以用切片来完成，但这种方案不够优雅
    也可以使用正则表达式作为替代方案，但是大材小用了
    当startswith()和endswith()方法和其他操作(比如常见的数据整理操作)结合起来效果也很好

### 2.3 利用shell通配符做字符串匹配

    fnmatch模块提供了两个函数————fnmatch()和fnmatchcase()————可用来执行这样的匹配。
    from fnmatch import fnmatch,fnmatchcase
    fnmatch(被匹配str,partten)
        pattern:'*','?','[0-9]'
    一般来说，fnmatch()的匹配模式所采用的大小写区分规则和底层文件系统相同(根据操作系统的不同而有所不同)
        ex: OS X(Mac)区分大小写，而Windows不区分
    如果这个区别很重要，就应该使用fnmatchcase()。它完全根据我们提供的大小写来匹配
    关于这些函数，一个常被忽略的特性是它们在处理非文件名式的字符串时的潜在用途。

    fnmatch所完成的匹配操作有点介乎于简单的字符串方法和全功能的正则表达式之间。如果只是试着在处理数据时提供一种简单的机制以允许使用通配符，那么通常这都是个合理的解决方案。
    如果实际上是想编写匹配文件名的代码，那应该使用glob模块来完成

### 2.4 文本模式的匹配和查找

    如果想要匹配的只是简单的文字，那么通常只需要用基本的字符串方法就可以了，比如str.find()、str.endswith()、str.startswith()或类似的函数
    对于更为复杂的匹配则需要使用正则表达式以及re模块。
    如果打算针对同一种模式做多次匹配，那么通常会先将正则表达式模式预编译成一个模式对象
        partten=re.compile(r'partten')
        partten.match(str)
    match()方法总是尝试在字符串的开头找到匹配项。如果想针对整个文本搜索出所有的匹配项，那么就应该使用findall()方法
    当定义正则表达式时，我们常会将部分模式用括号包起来的方式引入捕获组。
    捕获组通常能简化后续对匹配文本的处理，因为每个组的内容都可以单独提取出来
    findall()方法搜索整个文本并找出所有的匹配项然后将它们以列表的形式返回。如果想以迭代的方式找出匹配项，可以使用finditer()方法

    利用re模块来对文本做匹配和搜索的基础。基本功能是首先用re.compile()对模式进行编译，然后使用像,match()、findall()或finditer()这样的方法做匹配和搜索
    当指定模式时通常会使用原始字符串，比如r'(\d+)/(\d+)/(\d+)'。这样的字符串不会对反斜线字符转义，这在正则表达式上下文中会很有用。否则，需要用双反斜线来表示一个单独的'\'
    请注意match()方法只会检查字符串的开头
    如果想要精确匹配，请确保在模式中包含一个结束标记($)
    如果只是想执行简单的文本匹配和搜索工作，通常可以省略编译步骤，直接使用re模块中的函数即可
    请注意，如果打算执行很多匹配或查找操作的话，通常需要先将模式编译然后再重复使用。模块级的函数会对最近编译过的模式做缓存处理，所以并不会有巨大的性能差异。但使用自己编译过的模式会省下一些查找步骤和额外的处理

### 2.5 查找和替换文本

    对于简单的文本模式，使用str.replace()即可
    针对更为复杂的模式，可以使用re模块中的sub()函数/方法。
    sub()的第一个参数是匹配的模式，第二个参数是要替换上的模式。类似'\3'这样的反斜线加数字的符号代表着模式中捕获组的数量
    如果打算用相同的模式执行重复替换，可以考虑先将模式编译以获得更好的性能。
    对于更加复杂的情况，可以指定一个替换回调函数。
        ex: from calendar import month_abbr
            def change_date(m):
                mon_name=month_abbr[int(m.group(1))]
                return '{} {} {}'.format(m.group(2),mon_name,m.group(3))
            datepat.sub(change_date,text)
    替换回调函数的输入参数是一个匹配对象，由match()或find()返回。用.group()方法来提取匹配中特定的部分。这个函数应该返回替换后的文本
    除了得到替换后的文本外，如果还想知道一共完成了多少次替换，可以使用re.subn()
        newtext,n=datepat.subn(partten,text)

    关于正则表达式的查找和替换把并没有更多的内容了，最有技巧性的地方在于指定正则表达式模式

### 2.6 以不区分大小写的方式对文本做查找和替换

    要进行不区分大小写的文本操作，需要使用re模块并且对各种操作都要加上re.IGNORECASE或re.I
    这种方法有一种局限，即待替换的文本与匹配的文本大小写并不吻合。如果想修正这个问题，需要用到一个支撑函数
        ex: def matchcase(word):
                def replace(m):
                    text=m.group()
                    if text.isupper():
                        return word.upper()
                    elif text.islower():
                        return word.lower()
                    elif text[0].isupper():
                        return word.capitalize()
                    else:
                        return word
                return replace

    对于简单的情况，只需要加上re.IGNORECASE或re.I标记就足以进行不区分大小写的匹配操作了。但请注意的是这对于某些涉及大小写转换的Unicode匹配来说可能是不够的

### 2.7 定义实现最短匹配的正则表达式

    这个问题通常会在匹配的文本被一对开始和结束分隔符包起来的时候出现(例如带引号的字符串)
    模式'\"(.*)\"'尝试去匹配包含在引号中的文本。但是，*操作符在正则表达式中采用的是贪心策略，所以匹配过程是基于找出最长的可能匹配来进行的。
    要解决这个问题，只要在模式中的*操作符后加上?修饰符就可以了
    这么做使得匹配过程不会以贪心方式进行，也就会产生出最短的匹配了

    当编写含有句点(.)字符的正则表达式，在模式中，句点除了换行符之外可匹配任意字符。但是，如果以开始和结束文本(比如说引号)将句点括起来的话，在匹配过程中将尝试找出最长的可能匹配结果。这会导致匹配时跳过多个开始或结束文本，而将它们都包含在最长的匹配中。
    在*或+后添加一个?，会强制将匹配算法调整为寻找最短的可能匹配

### 2.8 编写多行模式的正则表达式

    这个问题一般出现在希望使用句点(.)来匹配任意字符，但是忘记了句点并不能匹配换行符时。
    要解决这个问题，可以添加对换行符的支持
    在这个模式中，(?:.|\n)指定了一个非捕获组(即，这个组只做匹配但不捕获结果，也不会分配组号)

    re.compile()函数可接受一个有用的标记————re.DOTALL或re.S。这使得正则表达式中的句点(.)可以匹配所有的字符，也包括换行符
    对于简单的情况，使用re.DOTALL或re.S标记就可以很好地完成工作。但是如果要处理极其复杂的模式，或者面对的是为了做分词而将单独的正则表达式合并在一起的情况，如果可以选择的话，通常更好的方法是定义自己的正则表达式，这样它无序额外的标记也能正确工作

### 2.9 将Unicode文本同一表示为规范形式

    在Unicode中，有些特定的字符可以被表示成多种合法的代码点序列。
        ex: '\u00f1' 'n\u0303'都能表示'ñ'，但是并不相等(==)，且字符串长度不同
    第一种使用的是字符'ñ'的全组成形式(U+00F1)。第二种使用的是拉丁字母"n"紧跟着一个"~"组合而成的字符(U+0303)
    对于一个比较字符串的程序来说，同一个文本拥有多种不同的表示形式是个大问题。为了解决这个问题，应该先将文本统一表示成规范形式，这可以通过unicodedata模块来完成
        unicodedata.normalize(sel,str)
        sel:'NFC','NFD','NFKC','NFKD'
    normalize()的第一个参数指定了字符串应该如何完成规范表示。NFC表示字符应该是全组成的(即，如果可能的话就使用单个代码点)。NFD表示应该使用组合字符，每个字符应该是能完全分开的
    Python还支持NFKC和NFKD的规范表示形式，它们为处理特定类型的字符增加了额外的兼容功能

    对于任何需要确保以规范和一致性的方式处理Unicode文本的程序员来说，规范化都是重要的一部分。尤其是在处理用户输入时接收到的字符串时，此时你无法控制字符串的编码形式，那么规范化文本的表示就显得更为重要了
    在对文本进行过滤和净化时，规范化同样也占据了重要的部分。例如，从某些文本中去除所有的音符标记(可能是为了进行搜索或匹配)
        t1=unicodedata.normalize('NFD',str)
        ''.join(c for c in t1 if not unicodedata.combining(c))
    这展示了unicodedata模块的另一个重要功能————用来检测字符是否属于某个字符类别。使用工具combining()函数可对字符做检查，判断它是否为一个组合型字符。这个模块中还有一些函数可用来查找字符类别、检测数字字符等
    很显然，Unicode是一个庞大的主题。要获得更多有关规范化文本方面的参考信息，详见http://www.unicode.org/faq/normalization.html 。Ned Batchelder也在他的网站http://nedbatchelder.com/text/unipain.html 上对Python中的Unicode处理给出了优秀的示例说明

### 2.10 用正则表达式处理Unicode字符

    默认情况下re模块已经对某些Unicode字符类型有了基本的认识。例如，\d已经可以匹配任意Unicode数字字符了
    如果需要在模式字符中包含指定的Unicode字符，可以针对Unicode字符使用转义序列(例如\uFFFF或\UFFFFFFF)。比如，这里有一个正则表达式能在多个不同的阿拉伯代码页中匹配所有的字符
        arabic=re.compile('[\u0600-\u06ff\u0750-\u077f\u08a0-\u08ff]+')
    当执行匹配和搜索操作时，一个好主意是首先将所有的文本都统一表示为标准形式。但是，同样重要的是需要注意一些特殊情况。例如，当不区分大小写的匹配和大写转换匹配联合起来时，考虑会出现什么行为
        ex: 'u00dfe'.upper()='SSE'
            s='stra遝'.upper()不与'stra\u00dfe',re.IGNORECASE匹配

    把Unicode和正则表达式混在一起使用绝对是个能让人头痛欲裂的办法。如果真的要这么做，应该考虑安装第三方的正则表达式库regex，这些第三方库针对Unicode大写转换提供了完整的支持，还包含其他各种有趣的特性，包括近似匹配

### 2.11 从字符串中去掉不需要的字符

    strip()方法可用来从字符串的开始和结尾处去掉字符。lstrip()和rstrip()可分别从左或从右测开始执行去除欺负的操作。默认情况下这些方法去除的是空格符，但也可以指定其他的字符
    如果要对里面的空格执行某些操作，应该使用其他技巧，比如使用replace()方法或正则表达式替换
    通常会遇到的情况是将去除字符的操作同某些迭代操作结合起来，比如说从文件中读取文本行。在这时生成器会非常有用
        ex: with open(filename) as f:
                lines = (line.strip() for line in f)
                for line in lines:
                    ...
    这里，表达式lines=(line.strip() for line in f)的作用是完成数据的转换(把原始数据中每一行开头和结尾处的空格符去掉，相当于一种转换处理)。这很高效，因为这里并没有先将数据读取到任何形式的临时列表中。它只是创建一个迭代器，在所有产生处的文本行上都会执行strip操作
    对于更高级的strip操作，应该转而使用translate()方法

### 2.12 文本过滤和清理

    文本过滤和清理所覆盖的范围非常广泛，涉及文本解析和数据处理方面的问题。在非常简单的层次上，可能会用基本的字符串函数(例如str.upper()和str.lower())将文本转换为标准形式。简单的替换操作可通过str.replace()或re.sub()来完成，它们把重点放在移除或修改特定的字符序列上。也可以利用unicodedata.normalize()来规范化文本
    如果想更进一步。比方说也许想清除整个范围内的字符，或者去掉音符标志。要完成这些任务，可以使用常被忽视的str.translate()方法。
    使用translate()方法前，需要建立转换表
    remap={ord{'\t'}:' ',ord{'\f'}:' ',ord{'\r'}:None}
    可以转换将\t和\f这样的空格符为一个单独的空格，而删除回车符
    可以利用这种重新映射的思想进一步构建出更庞大的转换表。
        cmb_chrs=dict.fromkeys(c for c in range(sys.maxunicode) if unicodedata.combining(chr(c)))
    使用dict.fromkeys()方法构建一个将每个Unicode组合字符都映射为None的字典
    另一种用来清理文本的技术涉及I/O解码和编码函数。大致思路是首先对文本做初步的清理，然后通过结合encode()和decode()操作来修改和清理文本

    文本过滤和清理的一个主要问题就是运行时的性能。一般来说操作越简单，运行得就越快。对于简单的替换操作，用str.replace()通常是最快的方式————即使必须多次调用它也是如此。
    另一方面，如果需要做任何高级的操作，比如字符到字符的重映射或删除，那么translate()方法还是非常快的
    从整体上来看，我们应该在具体的应用中去进一步揣摩性能方面的问题。
    类似的技术也同样适用于字节对象，包括简单的替换、翻译和正则表达式

### 2.13 对齐文本字符串

    对于基本的字符串对齐要求，可以使用字符串的ljust()、rjust()和center()方法
        str.ljust(n,char)、str.rjust(n,char)、str.center(n,char)，用char(默认空格)调整str位置
    所有这些方法都可接受一个可选的填充字符
    format()函数也可以用来轻松完成对齐的任务、需要做的就是合理利用'<'、'>'，或'^'字符以及一个期望的宽度值
        '>'表示右对齐,'<'表示左对齐,'^'表示居中对齐，这些字符称为对齐字符
    如果想包含空格之外的填充字符，可以在对齐字符之前指定
    当格式化多个值时，这些格式化代码也可以用在format()方法中
        ex: '{:>10s} {:>10s}'.format('Hello','World')
    format()的好处之一是它并不是特定于字符串的。它能作用于任何值，这使得它更加通用。

    在比较老的代码中，通常会发现%操作符来格式化文本
        ex: '%-20s'%str
    但是在新的代码中，使用format()函数或方法会更加顺手。format()比%操作符提供的功能更为强大。此外，format()可作用于任意类型的对象，比字符串的ljust()、rjust()以及center()方法要更加通用
    参考python的在线手册，会有更加详细format()的函数

### 2.14 字符串连接及合并

    如果想要合并的字符串在一个序列或可迭代对象中，那么将它们合并起来的最快方法就是使用join()方法
        "".join(list with str in)
    join()操作其实是字符串对象的一个方法。这么设计的部分原因是因为想要合并在一起的对象可能来自于各种不同的数据序列，比如列表、元组、字典、文件、集合或生成器，如果单独在每一种序列对象中实现一个join()方法就显得太冗余了。因此只需要指定想要的分隔字符串，然后在字符串对象上使用join()方法将文本片段粘合在一起就可以了
    如果只是想连接一些字符串，一般使用+操作符就足够了
    针对更加复杂的字符串格式化操作，+操作符同样可以作为format()的替代
    如果打算在源代码中将字符串字面值合并在一起，可以简单地将它们排列在一起，中间不加+操作符

    要意识到使用+操作符做大量的字符串连接是非常低效的，原因是由于内存拷贝和垃圾收集产生的影响。
    +=要比使用join()方法要满上许多。主要是因为每个+=操作都会创建一个新的字符串对象。最好先收集所有要连接分部分，最后再一次将它们连接起来
    一个相关而漂亮的技巧是利用生成器表达式在将数据转换为字符串的同时完成连接操作
    对于不必要的字符串连接操作也要引起重视。有时候在技术上并非必需的时候，不要忘乎所以地使用字符串连接操作
        print(a+':'+b+':'+c)        #Ugly
        print(':'.join([a,b,c]))    #Still ugly
        print(a,b,c,sep=':')        #Better
    将字符串连接同I/O操作混合起来的时候需要对应用做仔细的分析。
        # Version 1 (string concatenation)
        f.write(chunk1 + chunk2)
        # Version 2 (separate I/O operations)
        f.write(chunk1)
        f.write(chunk2)
    如果这两个字符串都很小，那么第一个版本的代码能带来更好的性能，这是因为执行一次I/O系统调用的固有开销就很高。另一方面，如果这两个字符串都很大，那么第二个版本的代码会更加高效。因为这里避免了创建大的临时结果，也没有对大块的内存进行拷贝。需要对数据做分析，以此才能判定哪一种方式可以获得更好的性能
    如果编写的代码要从许多短字符串中构建输出，则应该考虑编写生成器函数，通过yield关键字生成字符串片段
    关于这种方法，它不会假设产生的片段要如何组合在一起。可以用join()将它们简单连接，或者将片段重定向到I/O,以混合的方式将I/O操作智能化结合在一起
    关键在于这里的生成器函数并不需要知道精确的细节，只是产生片段

### 2.15 给字符串中的变量名做插值处理

    Python并不直接支持在字符串中对变量做简单的值替换。但这个功能可以通过字符串的format()方法近似模拟出来
        "{name}".format(name=str)
    另一种方式是，如果要被替换的值确实能在变量中找到，则可以将format_map()和vars()联合起来使用
        name=str
        "{name}".format_map(vars())
    有关vars()的一个微妙的特性是它也能作用于类实例上
        a.name=str
        vars(a)
    而format()和format_map()的一个缺点则是没法优雅地处理缺少某个值的情况
    避免出现这种情况的一个方法就是单独定义一个带有__missing__()方法的字典类
        class safesub(dict):
            def __missing__(self,key):
                 return '{'+key+'}'
    用这个类来包装传给format_map()的输入参数，此类能够返回访问不存在的键
    如果发现在代码中常常需要执行这些步骤，则可以将替换变量的过程隐藏在一个小型的功能函数内，这里要采用一种称之为"frame hack"的技巧(即需要同函数的栈帧打交道。sys.get_frame这个特殊的函数可以让我们获得调用函数的栈信息)
        def sub(text):
            return text.format_map(safesub(sys._getframe(1).f_locals))
        sys._getframe(n)返回上n层，.f_locals为变量字典

    由于Python缺乏真正的变量插值功能，由此产生了各种解决方案。作为已给出的解决方案的替代，有时候会有类似以下的字符串格式化操作
        '%(name)s'%vars()
    或者模板字符串的使用
        s=string.Template("$name")
        s.substitute(vars())
    但是，format()和format_map()方法比上面这些替代方案都要更加现代化。使用format()的一个好处是可以同时得到所有关于字符格式化方面的功能(对齐、填充、数值格式化等)，而这些功能在字符串模板对象上是不可能做到的
    字典类中鲜为人知的__missing__()方法可用来处理缺少值时的行为。
    sys.get_frame(1)来返回调用方的栈帧。通过访问属性f_locals来得到局部变量。在大部分的代码中都应该避免去和栈帧打交道。可以修改f_locals的内容，但是修改后并不会产生任何持续性的效果。
    尽管访问不同的栈帧可能看起来是很邪恶的，但是想意外地覆盖或修改调用方的本地环境也是不可能的

### 2.16 以固定的列数重新格式化文本

    可以使用textwrap模块来重新格式化文本的输出
        textwrap.fill(str,n,initial_indent='',subsequent_indent='')
        n表示列字符数,initial_indent设置首行缩进字符,subsequent_indent设置悬挂缩进字符

    textwrap模块能够以简单直接的方式对文本格式做整理使其适合于打印————尤其是当希望输出结果能很好地显示在终端上。关于终端的尺寸大小，可以通过os.get_terminal_size()来获取
        os.get_terminal_size().columns
    fill()方法还有一些额外的选项可以用来控制如何处理制表符、句号等

### 2.17 在文本中处理HTML和XML实体

    如果要生成文本，使用html.escape()函数来完成替换<or>这样的特殊字符相对来说是比较容易的
        ex: s='Elements are written as "<tag>text</tag>".'
            html.escape(s,<quote=False>,<errors='xmlcharrefreplace'>)
    如果要生成ASCII文本，并且想针对非ASCII字符将它们对应的字符编码实体嵌入到文本中，可以在各种同I/O相关的函数中使用errors='xmlcharrefreplace'参数来实现
    要替换文本中的实体，那就需要不同的方法。如果实际上是在处理HTML或XML，首先应该尝试使用一个合适的HTML或XML解析器。一般来说，这些工具在解析的过程中会自动处理相关值的替换。
    如果由于某种原因在得到的文本中带有一些实体，而想手工将它们替换掉，通常可以利用各种HTML或XML解析器自带的功能函数和方法来完成
        ex: 'Spicy &quot;Jalape&#241;o&quot.'
            from html.parser import HTMLParser
            p=HTMLParser()
            p.unescape('Spicy &quot;Jalape&#241;o&quot.')
            或html.unescape('Spicy &quot;Jalape&#241;o&quot.')
            from xml.sax.saxutils import unescape
            unescape('The prompt is &gt;&gt;&gt;')

    在生成HTML或XML文档时，适当地对特殊字符做转义处理常常是个容易被忽视的细节。尤其是当自己用print()或其他一些基本的字符串格式化函数来产生这类输出时更是如此。简单的解决方案是使用像html.escape()这样的工具函数
    如果需要反过来处理文本(即,将HTML或XML实体转换成对应的字符)，有许多像xml.sax.saxutils.unescape()这样的工具函数能帮上忙。但是，我们需要仔细考察一个合适的解析器应该如何使用。例如，如果是处理HTML或XML，像html.parser或xml.etree.ElementTree这样的解析模块应该已经解决了有关替换文本中实体的细节问题

### 2.18 文本分词

    需要将字符串从左到右解析为标记流
    要对字符串做分词处理，需要做的不仅仅只是匹配模式。还需要有某种方法来识别出模式的类型。
        ex: text = 'foo = 23 + 42 * 10'
            tokens = [('NAME','foo'),('EQ','='),('NUM','23'),('PLUS','+'),('NUM','42'),('TIMES','*'),('NUM','10')]
    要完成这样的分词处理，第一步是定义出所有可能的标记，包括空格。这可以通过正则表达式中的命名捕获组来实现
        ex: NAME=r'(?P<NAME>[a-zA-Z_][a-zA-z_0-9]*)'
            master_pat=re.compile('|'.join([NAME,...]))
    在这种正则表达式模式中，形如?P<TOKENNAME>这样的约定是用来将名称分配给该模式的。
    接下来使用模式对象的scanner()方法来完成分词操作。该方法会创建一个扫描对象，在给定的文本中重复调用math(),一次匹配一个模式
        scanner=master_pat.scanner('foo = 42')
        a=scanner.match()
        a.lastgroup,a.group()
    要利用这项技术并将其转换为代码，可以做些清理工作然后将其包含在一个生成器函数中
        from collections import namedtuple
        Token = namedtuple('Token',['type','value'])
        def generate_tokens(pat,text):
            scanner = pat.scanner(text)
            for m in iter(scanner.match,None):
                yield Token(m.lastgroup,m.group())
        for tok in generate_tokens(master_pat,'foo = 42'):
            print(tok)
    如果想以某种方式对标记流做过滤处理，要么定义更多的生成器函数，要么就用生成器表达式

    对于更加高级的文本解析，第一步往往是分词处理。要使用上面展示的扫描技术，有几个重要的细节需要牢记于心。第一，对于每个可能出现在输出文本中的文本序列，都要确保有一个对应的正则表达式模式可以将其识别出来。如果发现有任何不能匹配的文本，扫描过程就会停止。
    这些标记在正则表达式(即re.compile('|'.join([NAME,NUM,PLUS,TIMES,EQ,WS])))中的顺序同样也很重要。当进行匹配时，re模块会按照指定的顺序来对模式做匹配。因此，如果碰巧某个模式是另一个较长模式的子串时，就必须确保较长的那个模式要先做匹配
    最后也最重要的是，对于有可能形成子串的模式要多加小心
    对于更加高级的分词处理，可以使用PyParsing或PLY这样的包

### 2.19 编写一个简单的递归下降解析器

    需要根据一组语法规则来解析文本，以此执行相应的操作或构建一个抽象语法树来表示输入。
    在这个问题中，把重点放在根据特定的语法来解析文本上。要做到这些，应该以BNF或EBNF的形式定义出语法的正式规格。比如对于简单的算数运算表达式，语法：
        expr ::= expr + term
            | expr - term
            | term
        term ::= term * factor
            | term / factor
            | factor
        factor ::= (expr)
            | NUM
    又或者以ENBF的形式定义为如下形式
        expr ::= term { (+|-) term }*
        term ::= factor { {*|/} factor }*
        factor ::= ( expr )
            |NUM
    在EBNF中，部分包括在{...}*中的规则是可选的。*意味着零个或更多重复项(和在正则表达式中的意义相同)
    可以把BNF看作是规则替换或取代的一种规范形式，左侧的符号可以被右侧的符号所取代(反之亦然)。一般来说，在解析的过程中会尝试将输入的文本同语法做匹配，通过BNF来完成各种替换和扩展。假设正在解析形如3 + 4 * 5的表达式，这个表达式首先应该被分解为标记流。NUM + NUM * NUM
    在此基础上，解析过程就通过替换的方式将语法匹配到输入标记上
        expr
        expr ::= term {(+|-) term }*
        expr ::= factor {(*|/) factor }*{(+|-) term }*
        expr ::= NUM {(*|/) factor }*{(+|-) term }*
        expr ::= NUM {(+|-) term }*
        expr ::= NUM + term {(+|-) term }*
        expr ::= NUM + factor {(*|/) factor }*{(+|-) term }*
        expr ::= NUM + NUM {(*|/) factor}*{(+|-) term }*
        expr ::= NUM + NUM * factor {(*|/) factor }*{(+|-) term }*
        expr ::= NUM + NUM * NUM {(*|/) factor }*{(+|-) term }*
        expr ::= NUM + NUM * NUM {(+|-) term }*
        expr ::= NUM + NUM * NUM
    完成所有的替换需要花上一段时间，这是由输入的规模和尝试去匹配的语法规则所决定的。第一个输入标记是一个NUM，因此替换操作首先会把重点放在匹配这一部分上。一旦匹配上了，重点就转移到下一个标记+上，如此往复。当发现无法匹配下一个标记时，右手侧的特定部分({*/)factor}*)就会消失。在一个成功的解析过程中，整个右手侧部分会完全根据匹配到的输入标记流来相应地扩展。

    ```Python
    import re
    import collections
    # Token specification
    NUM = r'(?P<NUM>\d+)'
    PLUS = r'(?P<PLUS>\+)'
    MINUS = r'(?P<MINUS>-)'
    TIMES = r'(?P<TIMES>\*)'
    DIVIDE = r'(?P<DIVIDE>/)'
    LPAREN = r'(?P<LPAREN>\()'
    RPAREN = r'(?P<RPAREN>\))'
    WS = r'(?P<WS>\s+)'
    master_pat = re.compile('|'.join([NUM, PLUS, MINUS, TIMES,DIVIDE, LPAREN, RPAREN, WS]))
    # Tokenizer
    Token = collections.namedtuple('Token', ['type', 'value'])
    def generate_tokens(text):
        scanner = master_pat.scanner(text)
        for m in iter(scanner.match, None):
            tok = Token(m.lastgroup, m.group())
            if tok.type != 'WS':
                yield tok
    # Parser
    class ExpressionEvaluator:
        '''
        Implementation of a recursive descent parser. Each method
        implements a single grammar rule. Use the ._accept() method
        to test and accept the current lookahead token. Use the ._expect()
        method to exactly match and discard the next token on on the input
        (or raise a SyntaxError if it doesn't match).
        '''
        def parse(self, text):
            self.tokens = generate_tokens(text)
            self.tok = None # Last symbol consumed
            self.nexttok = None # Next symbol tokenized
            self._advance() # Load first lookahead token
            return self.expr()
        def _advance(self):
            'Advance one token ahead'
            self.tok, self.nexttok = self.nexttok, next(self.tokens, None)
        def _accept(self, toktype):
            'Test and consume the next token if it matches toktype'
            if self.nexttok and self.nexttok.type == toktype:
                self._advance()
                return True
            else:
                return False
        def _expect(self, toktype):
            'Consume next token if it matches toktype or raise SyntaxError'
            if not self._accept(toktype):
                raise SyntaxError('Expected ' + toktype)
        # Grammar rules follow
        def expr(self):
            "expression ::= term { ('+'|'-') term }*"
            exprval = self.term()
            while self._accept('PLUS') or self._accept('MINUS'):
                op = self.tok.type
                right = self.term()
                if op == 'PLUS':
                    exprval += right
                elif op == 'MINUS':
                    exprval -= right
            return exprval
        def term(self):
            "term ::= factor { ('*'|'/') factor }*"
            termval = self.factor()
            while self._accept('TIMES') or self._accept('DIVIDE'):
                op = self.tok.type
                right = self.factor()
                if op == 'TIMES':
                    termval *= right
                elif op == 'DIVIDE':
                    termval /= right
            return termval
        def factor(self):
            "factor ::= NUM | ( expr )"
            if self._accept('NUM'):
                return int(self.tok.value)
            elif self._accept('LPAREN'):
                exprval = self.expr()
                self._expect('RPAREN')
                return exprval
            else:
                raise SyntaxError('Expected NUMBER or LPAREN')
    e = ExpressionEvaluator()
    print(e.parse('2 + (3 + 4) * 5'))
    ```
        基本的思路是，对放置在栈中的标记流进行匹配，如果对应就进行运算，同时推向下一个标记
    如果想做的不只是纯粹的计算，就需要修改ExpressionEvaluuator类来实现。则可以实现对计算式的解析输出

    文本解析是一个庞大的主题。
    要编写一个递归下降的解析器，总体思路较为简单。将每一条语法规则变为一个函数或方法
    每个方法的任务很简单————必须针对语法规则的每个部分从左到右扫描，在扫描过程中处理符号标记。从某种意义上说，这些方法的目的就是顺利地将规则消化掉，如果卡住了就产生一个语法错误。要做到这点，需要应用以下实现技术
        如果规则中的下一个符号标记是另一个语法规则的名称(例如,term或factor)，就需要调用同名的方法。这就是算法中的下降部分————控制其下降到另一个语法规则中。有时候规则会涉及调用已经在执行的方法(例如，在规则factor::='('expr')'中对expr的调用)。这就是算法中的"递归"部分
        如果规则中的下一个符号标记是一个特殊的符号(例如'(')，需要检查下一个标记，看它们是否能完全匹配。如果不能匹配，这就是语法错误。_expect()方法就是用来处理这些步骤的
        如果规则中的下一个符号标记存在多种可能的选择(例如+或-)，则必须针对每种可能性对下一个标记做检查，只有在有匹配满足时才前进到下一步。_accept()方法的功能即是如此。在_accept()中如果有匹配错误，就前进到下一步，但如果没有匹配，它只是简单的回退而不会引发一个错误(这样检查才可以继续进行下去)
        对于语法规则中出现的重复部分(例如expr::=term{('+'|'-')term}*)，这是通过while循环来实现的。一般在循环体中收集或处理所有的重复项，直到无法找到更多的重复项为止。
        一旦整个语法规则都已经处理完，每个方法就返回一些结果给调用者。这就是在解析过程中将值进行传递的方法。比如，在计算器表达式中，表达式解析的部分结果会作为值来返回。最终它们会结合在一起，在最顶层的语法规则方法中得到执行
    递归下降解析器可以用来实现相当复杂的解析器。例如，Python代码本身也是通过一个递归下降解析器来解释的，可以通过检查Python源代码中的Grammar/Grammar文件来查看。要自己手写一个解析器时仍然需要面对各种陷阱和局限
    局限之一就是对于任何涉及左递归形式的语法规则，都没法用递归下降解析器来解决。假设需要解释如下的规则:
        item ::=items ',' item
            |item
    则一定会产生无穷递归的错误
    也可能会陷入到语法规则自身的麻烦中。比如考虑标准算数中关于计算顺序的约定
    对于真正复杂的语法解析，最好还是使用像PyParsing或PLY这样的解析工具。如果使用PLY，解析计算器表达式代码如下:

    ```Python
    from ply.lex import lex
    from ply.yacc import yacc
    # Token list
    tokens = [ 'NUM', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'LPAREN', 'RPAREN' ]
    # Ignored characters
    t_ignore = ' \t\n'
    # Token specifications (as regexs)
    t_PLUS = r'\+'
    t_MINUS = r'-'
    t_TIMES = r'\*'
    t_DIVIDE = r'/'
    t_LPAREN = r'\('
    t_RPAREN = r'\)'
    # Token processing functions
    def t_NUM(t):
        r'\d+'
        t.value = int(t.value)
        return t
    # Error handler
    def t_error(t):
        print('Bad character: {!r}'.format(t.value[0]))
        t.skip(1)
    # Build the lexer
    lexer = lex()
    # Grammar rules and handler functions
    def p_expr(p):
        '''
        expr : expr PLUS term
            | expr MINUS term
        '''
        if p[2] == '+':
            p[0] = p[1] + p[3]
        elif p[2] == '-':
            p[0] = p[1] - p[3]
    def p_expr_term(p):
        '''
        expr : term
        '''
        p[0] = p[1]
    def p_term(p):
        '''
        term : term TIMES factor
        | term DIVIDE factor
        '''
        if p[2] == '*':
            p[0] = p[1] * p[3]
        elif p[2] == '/':
            p[0] = p[1] / p[3]
    def p_term_factor(p):
        '''
        term : factor
        '''
        p[0] = p[1]
    def p_factor(p):
        '''
        factor : NUM
        '''
        p[0] = p[1]
    def p_factor_group(p):
        '''
        factor : LPAREN expr RPAREN
        '''
        p[0] = p[2]
    def p_error(p):
        print('Syntax error')
    parser = yacc()
    print(parser.parse('2+(3+4)*5)')
    ```
    在这份代码中会发现所有的东西都是以一种更高层的方式定义的。我们只需编写匹配标记符号的正则表达式，以及当各种匹配语法规则时所需要的高层处理函数就行了。而实际的运行解析器、接受符号标记等都完全由库来实现
    Python自带的ast模块也值得学习

### 2.20 在字节串上执行文本操作

    字节串已经支持大多数和文本字符串一样的内建操作
        data=b'hello world'
        data[0:5]
        data.startswith(b'hello')
        data.split()
        data.replace(b'hello',b'hello cruel')
    类似的操作在字节数组上也能完成
    可以在字节串上执行正则表达式的模式匹配操作，但是模式本身需要以字节串的形式来指定

    就绝大部分情况而言，几乎所有能在文本字符串上执行的操作同样也可以在字节串上进行
    但是单独访问字节串的某个元素时，返回的是字符对应的值。这种语义上的差异会对试图按照字符的方式处理面向字节流数据的程序带来影响
    其次，字节串并没有提供一个漂亮的字符串表示，因此打印结果并不干净利落，除非首先将其解码为文本字符串
    同样道理，在字节串上是没有普通字符串那样的格式化操作的
    如果想在字节串上做任何形式的格式化操作，应该使用普通的文本字符串然后再做编码
    最后，需要注意的是使用字节串会改变某些特定操作的语义————尤其是那些与文件系统相关的操作。如果提供一个以字节而不是文本字符串来编码的文件名，文件系统通常都会禁止对文件名的编码/解码
    以字节串作为目录名从而导致产生的名称以未经编码的原始字节形式返回。在显示目录内容时，文件名包含了原始的UTF-8编码。
    可能会因为性能上有可能得到略微提升而倾向于将字节串作为文本字符串的替代来使用。尽管操纵字节确实要比文本来的略微高效一些(由于同Unicode相关的固有开销较高)，但这么做通常会导致非常混乱和不符合语言习惯的代码。常会发现字节串和Python中许多其他部分并不能很好地相容，这样为了保证结果的正确性，只能手动去执行各种各样的编码/解码操作。

## 第3章 数值、日期和时间

    在Python中使用整数和浮点数进行数值计算较为简单。但是，如果需要使用分数、矩阵或者日期时间，就需要额外的工作

### 3.1 数值近似

    需要将浮点数近似到固定位数的小数
    对于简单的近似，使用Python自带的round(value,ndigits)函数
    当数值刚好为近似选择的中间值，将会被近似到最近的偶数。例如1.5和2.5都会被近似到2
    round()参数ndigits可以为负数，-1、-2、-3将会使数值近似到十、百、千位，以此类推

    不要将近似与格式化数值输出混淆。如果目的是简单输出一个指定位数的数值，一般不需要使用round()。只需要在格式化时指定精度即可
    而且，不必通过对浮点数近似来"解决"可见的精度问题
        ex: a,b=2.1,4.2
            c=a+b #6.300000000000001
            c = round(c, 2)
    对于绝大多数涉及浮点数的程序，这样做是不必要也不推荐的。尽管计算中会引入微小错误，但这些错误行为是可以被理解和忍受的。如果一定要避免这样的错误(例如在金融程序中)，可以考虑使用decimal模块

### 3.2 进行精确的小数运算

    承接上节最后，需要避免浮点运算中自然生成的误差
    众所周知，浮点数不能精确地表示十进制数。而且，即使是简单的数值运算都会引入细微误差
    这些误差是由底层CPU的浮点单元按照IEEE 754(IEEE二进制浮点数算数标准)所带来的"特性"
    既然Python的浮点数据类型使用原始表示方式储存数据，因此当代码中使用浮点数时，误差无可避免
    如果需要更高的精度(并愿意放弃一部分性能)，可以使用decimal模块
        ex: from decimal import Decimal
            a=Decimal('4.2')
            b=Decimal('2.1')
            a+b # Decimal('6.3')
    初次接触，这样可能会有点奇怪(例如用字符串表示数值)。但是，Decimal对象能够实现你所期望的功能(包括支持常规数学操作在内)。在字符格式函数中输出或使用它们与常规数字无异
    decimal的一个主要特性是，它允许控制计算的不同方面，包括数字位数和近似。为了实现这个功能，需要创建localcontext并修改设置
        ex: from decimal import localcontext
            a = Decimal('1.3')
            b = Decimal('1.7')
            print(a / b)
            with localcontext() as ctx:
                ctx.prec = 3
                print(a / b)

    decimal模块实现了IBM的通用小数算术规范。显而易见，会有超出本书范围的配置选项
    Python的新手可能会倾向于使用decimal模块来处理浮点数类型的显式精确问题。但理解程序的作用域非常重要。如果是处理科学或工程问题、计算机图形、或大多数科学自然中的事物，使用常规浮点类型是极其常见的。对于一个人来说，真实世界中很少有被测量到由浮点数提供的17位精度的事物。因此，由计算引入的微小错误并不重要。使用原始浮点数进行计算明显更快————这在进行大量数字运算时非常重要
    即便如此，并不能完全忽略错误。数学家在算法上花了大量时间，有些算法在处理误差上更加优越。同样也需要注意减法对消和大小数相加所带来的影响
        ex: nums=[1.23e18,1,-1.23e+18]
            sum(nums) #0
    可以通过使用math.fsum()来进行更加精准的实现
    对于其他算法，需要研究其中的算法并理解误差产生原因
    decimal模块的使用主要是涉及例如金融的事务。在这些程序中，在计算中产生细微的误差是相当麻烦的。decimal能够解决这一问题。当Python涉及数据库时Decimal对象便非常常见，还是特别在接触金融数据时

### 3.3 格式化输出数字

    需要格式化输出数字，控制数字位数，对齐，包括千分位符以及其他细节
    格式化输出单个数字，可以使用内置的format()函数
        ex: x=1234.56789
            format(x,'0.2f') # 两位小数
            format(x,'>10.1f') # 右对齐10位，一位小数
            format(x,'<10.1f')
            format(x,'^10.1f')
            format(x,',') # 千分位分隔符
    用'e'或'E'代替'f'以用科学计数法表示，根据希望采用的指数规格来指定
    指定宽度和精度的一般格式为'[<>^]?width[,]?(.digits)?',width和digits为整数，?代表可选的部分。同样的格式也可以用于字符串的.format()方法中

    对数值做格式化输出通常都是很直接的。这既能用于浮点型数，也能适用于decimal模块中的Decimal对象
    当需要限制数值的位数时，数值会根据round()函数的规则来进行取整
    对数值加上千位分隔符的格式化操作并不是特定于本地环境的。如果需要将这个需求纳入考虑，应该考察一下local模块中的函数。还可以利用字符串的translate()方法交换不同的分隔字符
        ex: swap_separators ={ ord('.'):',',ord(','):'.'}
        format(x,',').translate(swap_separators)
    在很多Python代码中，常用%操作符来对数值做格式化处理
    这种格式化操作是仍然是可接受的，但是比起更加现代化得format()方法，这种方法就显得不是那么强大了。比如当使用%操作符来格式化数值时，有些功能就没法得到支持了(例如添加千位分隔符)

### 3.4 同二进制、八进制和十六进制数打交道

    要将一个整数转换为二进制、八进制或十六进制的文本字符串形式，只要分别使用内建的bin()、oct()和hex()函数即可(输出会带有前缀0b,0o,0x)
    如果不希望出现0b、0o或者0x这样的前缀，可以使用format()函数。
        format(x,'b'/'o'/'x')
    整数是有符号的，因此如果要处理负数的话，输出中也会带上一个符号
    相反，如果需要产生一个无符号的数值，需要加上最大值来设置比特位的长度。比如要展示一个32位数
        format(2**32+x,'b')
    要将字符串形式的整数转换为不同的进制，只需要使用int()函数再配合适当的进制即可
        int('4d2',16)
    
    对于大部分的情况，处理二进制、八进制和十六进制数都是非常直接的。只是这些转换只适用于转换整数的文本表示形式，实际在底层只有一种整数类型
    对于用到了八进制数的程序员来说需要注意。在Python中指定八进制的语法和许多其他的编程语言稍有不同。
        os.chmod('script.py',0755) # SyntaxError: invalid token
    确保在八进制数前添加Oo前缀 #0o755

### 3.5 从字节串中打包和解包大整数

    需要将字节串解包为一个整型数值、将一个大整数重新转换为一个字节串
    ��������将字节解释为整数，可以使用int.from_bytes()，然后指定字节序
        ex: int.from_bytes(data,'little'/'big') # 小端法，大端法
    要将一个大整数重新转换为字节串，可以使用int.to_bytes()方法，只要指定字节数和字节序即可

    在大整数和字节串之间互相转换并不算是常见的操作。有时候在特定的应用领域中却有这样的需求，例如加密技术或网络应用中。比方说IPv6网络地址就是由一个128位的整数来表示的。如果正在编写的代码需要将这样的值从数据记录中提取出来，就得面对这个问题
    作为替代方案，可能会倾向于使用struct模块来完成解包。这行得通，但是struct模块可解包的整数大小是有限制的。因此需要解包多个值，然后再将它们合并起来以得到最终的结果。
        ex: data=b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'
            hi,lo = struct.unpack('>QQ',data)
            
    字节数的规范(大端或小端)指定了组成整数的字节是从低位到高位排列还是从高位到低位排列。
    如果尝试将一个整数打包成字节串，但字节大小不合适的话就会得到一个错误信息。如果需要的话，可以使用int.bit_length()方法来确定需要用到多少位才能保存这个值
        x.bit_length()
        nbytes,rem=divmod(x.bit_length(),8)
        if rem:nbytes+=1
        x.to_bytes(nbytes,'little')

### 3.6 复数运算

    代码在同最新的Web认证方案交互时遇到了奇点问题，而唯一的解决方案是在复平面解决。或者也许只需要利用复数完成一些计算就可以了。
    复数可以通过complex(real,imag)函数来指定，或者通过浮点数再加上后缀j来指定也行
    实部、虚部以及共轭值可以很方便地提取出来
        a.real # 实部 a.imag # 虚部 a.conjugate() # 共轭复数
    如果要执行有关复数的函数操作，例如求正弦、余弦或平方根，可以使用cmath模块
        cmath.sin()、cos()、exp()

    Python中大部分和数学相关的模块都可适用于复数。例如，如果使用numpy模块，可以很直接地创建复数数组，并对它们执行操作
        a=numpy.array([])
        a+n,对应实部/虚部计算
            n为单个数，则每个数都加上n
            n也为numpy.array，则规格相同，相应位置单独计算
        numpy.sin()每个数单独计算
    Python中的标准数学函数默认情况下不会产生复数值。因此像这样的值不会意外地出现在代码里
    如果希望产生复数结果，那必须明确使用cmath模块或者在可以感知复数的库中声明对复数类型的使用。
        cmath.sqrt(-1)

### 3.7 处理无穷大和NAN

    需要对浮点数的无穷大、负无穷大或NaN(not a number)进行判断测试
    Python中并没有特殊的语法来表示这些特殊的浮点数值，但是它们可以通过float()来创建
        float('inf'/'-inf'/'nan')
    要检测是否出现了这些值，可以使用math.isinf()和math.isnan()函数

    要获得关于这些特殊的浮点数值的详细信息，应该参考IEEE 754规范。但是，这里有几个棘手的细节问题需要搞清楚，尤其是当涉及比较操作和操作符时可能出现的问题
    无穷大值在数学计算中会进行传播
    但是，某些特定的操作会导致未定义的行为并产生NaN的结果
    NaN会通过所有的操作进行传播，且不会引发任何异常
    有关NaN，一个微妙的特性时它们在做比较时从不会被判定为相等
    唯一安全检测NaN的方法是使用math.isnan()
    有时候程序员希望在出现无穷大或NaN结果时可以修改Python的行为，让它抛出异常。fpectl模块可以用来调整这个行为，但是在标准Python中它是没有开启的，而且这个模块是同平台相关的，只针对专家及的程序员使用。

### 3.8 分数的计算

    fractions模块可以用来处理涉及分数的数学计算问题
        a=fractions.Fraction(5,4)
        a.numerator # 分子
        a.denominator # 分母
        c.limit_denominator(n) # 限制最简分母大小
        a=fractions.Fraction(*n.as_integer_ratio())
            *是特殊语法，把元组扩展到单个参数中

        在大多数程序中，涉及分数的计算问题并不常见。允许程序接受以分数形式给出的单位计量并执行相应的计算，这样可以避免用户手动将数据转换为Decimal对象或浮点数

### 3.9 处理大型数组的计算

    需要对大型的数据集比如数组或网格进行计算
    对于任何涉及数组的计算密集型任务，可以使用Numpy库。Numpy的主要特性是为Python提供了数组对象，比标准Python中的列表有着更好的性能表现，因此更加适合于做数学计算。
        ex: x=[1,2,3,4]
            x*2 x+x
            ax=numpy.array([1,2,3,4])
            ax+n ax*ax ax*n
    有关数组的几个基本数学运算在行为上都有所不同。Numpy中的数组在进行标量运算(例如ax*2或ax+10)时是针对逐个元素进行计算的。当两个操作数都是数组时，Numpy数组在进行数学运算时会针对数组的所有元素进行计算，并产生出一个新的数组作为结果
    由于数学操作会同时施加于所有的元素之上，这一事实使得对整个数组的计算变得非常简单和迅速。
    Numpy提供了一些"通用函数"的集合，它们也能对数组进行操作。这些通用函数可以作为math模块中所对应函数的替代
        np.sqrt()   np.cos()
    使用Numpy中的通用函数，其效率要比对数组进行迭代然后使用math模块中的函数每次只处理一个元素要快上百倍。只要有可能就应该使用这些通用函数
    在底层,Numpy数组的内存分配方式和C或者Fortran一样。是大块的连续内存，由同一种类型的数据组成。所以Numpy创建比通常Python中的列表要大得多的数组。创建一个1e4*1e4的二维浮点数组:
        grid=np.zeros(shape=(10000,10000),dtype=float)
    关于Numpy,一个特别值得一提的是Numpy扩展了Python列表的索引功能————尤其是针对多维数组时更是如此
        a=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
        a[n] # select row
        a[:,n] # select column
        a[x1:x2,y1:y2] # select a subregion
        a[x1:x2,y1:y2] # change a subregion
        a+[x1,x2,x3,x4] # 对所有行操作
        np.where(a<n1,a,n2) # 条件赋值

    Python中大量的科学和工程类函数库都以Numpy为基础，它也是广泛使用中的最为庞大和复杂的模块之一。
    对于Python的用法，一个相对来说比较常见的导入方式是import numpy as np。方便每次在程序中输入
    Numpy:www.numpy.org

### 3.10 矩阵和线性代数的计算

    需要执行矩阵和线性代数方面的操作，比如矩阵乘法、求行列式、解线性方程等
    Numpy库中有一个matrix对象可用来处理这种情况。Matrix对象在计算时遵循线性代数原则。
        m=np.matrix([1,-2,3],[0,4,5],[7,8,9])
        m.T # 转置
        m.I # 矩阵求逆
        v=np.matrix([[2],[3],[4]])
        m*v
    更多的操作可在numpy.linalg子模块中找到
        numpy.linalg.det(m) # 求行列式
        numpy.linalg.eigvals(m) # 求特征值
        numpy.linalg.solve(m,v) # 解方程组

    如果需要处理矩阵和向量，Numpy是个很好的起点

### 3.11 随机选择

    从序列中随机挑选元素，或生成随机数
    random模块中有各种函数可用于需要随机数和随机选择的场景。从序列中随机挑选出元素，可以使用random.choice(values)
    如果想取样出N个元素，将选出的元素移除以作进一步的考察，可以使用random.sample(values,n)
    如果只是想在序列中原地打乱元素的顺序(洗牌),可以使用random.shuffle(values)
    要产生随机整数，可以使用random.randint(start,end)
    要产生0到1之间均匀分布的浮点数值，可以使用random.ranndom()
    如果要得到N个随机比特位所表示的整数，可以使用random.getrandbits(n)

    random模块采用马特赛特旋转算法(也成为梅森旋转算法)来计算随机数。这是一个确定性算法，但是可以通过random.seed()函数来修改初始的种子值
        random.seed() # default: system time or os.urandom()
            or based on integer given、byte data
    除了以上展示的功能外，random模块还包含有计算均匀分布、高斯分布和其他概率分布的函数。random.uniform()可以计算均匀分布值，而random.gauss()则可计算出正态分布值。
    random模块中的函数不应该用在与加密处理相关的程序中。如果需要这样的功能，考虑使用ssl模块中的函数来替代。ssl.RAND_bytes()可以用来产生加密安全的随机字节序列

### 3.12 时间换算

    进行简单的时间转换工作，比如将日转换为秒，将小时转化为分钟等
    可以利用datetime模块来完成不同时间单位间的换算。要表示一个时间间隔，可以创建一个timedelta实例
        from datetime import timedelta
        a=timedelta(days=2,hours=6)
        b=timedelta(hours=4.5)
        c=a+b
        c.days  c.seconds   c.total_seconds()
    如果需要表示特定的日期和时间，可以创建datetime实例并使用标准的数学运算来操纵
        from datetime import datetime
        a=datetime(2012,9,23)
        print(a+timedelta(days=10))
        b=datetime(2012,12,21)
        d=b-a
        d.days
    当执行计算时，应该要注意的是datetime模块是可正确处理闰年的

    对于大部分基本的日期和时间操控问题，datetime模块已足够满足要求了。如果需要处理更为复杂的日期问题，比如处理时区、模糊时间范围、计算节日的日期等，可以试试dateutil模块
    可以使用dateutil.relativedelta()函数完成许多同datetime模块相似的时间计算。dateutil的一个显著特点是在处理有关月份的问题时能填补一些datetime模块留下的空缺(可正确处理不同月份中的天数)
        from dateutil.relativedelta import relativedelta
            a+relativedelta(months=+1)

### 3.13 计算上周5的日期

    Python的datetime模块中有一些使用函数和类可以完成这样的运算
    通过datetime.today()、today对象的.weekday()属性来进行倒推

    将起始日期和目标日期映射到它们在一周之中的位置上。然后用取模运算计算上一次目标日期出现时到起始日期为止一共经过的天数。然后从起始日期中减去一个合适的timedalta实例
    如果需要执行大量类似的日期计算，最好安装python-dateutil包
        from datetime import datetime
        from dateutil.relativedelta import relativedelta
        from dateutil.rrule import *
        d=datetime.now()
        d+relativedelta(weekday=FR)
        d+relativedelta(weekday=FR(-1))

### 3.14 找出当月的日期范围

    对日期进行迭代循环并不需要事先构建一个包含所有日期的列表。只需计算出范围的开始和结束日期，然后在迭代时利用datetime.timedelta对象来递增日期就可以了
    calendar.monthrange函数可接受任意的datetime对象，并返回一个包含对应月份第一个工作日的日期和天数的元组
        calendar.monthrange(year,month)

    首先计算出相应月份中第一天的日期。一种快速求解的方法是利用date或者datetime对象的replace()方法，只要将属性days设为1就可以了。关于replace()方法，一个好的方面就是它创建出的对象和输入对象类型是一致的。
    用calendar.monthrange()函数来找出待求解的月份中有多少天。当需要得到有关日历方面的基本信息时，calendar模块都会非常有用。monthrange()是其中唯一的一个可返回元组的函数，元组中包含当月第一个工作日的日期(0-6，依次代表周一到周日)以及当月的天数(28-31)
    一旦知道了这个月中有多少天，那么结束日期就可以通过在起始日期上加上一个合适的timedelta对象来表示。
    要循环日期范围，采用标准的算术以及比较操作符。timedelta实例可用来递增日期，而<操作符用来检查当前日期是否超过了结束日期
    最理想的方法是创建一个专门处理日期的函数，而且用法和Python内建的range()一样。可以用生成器的方式来实现

### 3.15 将字符串转换为日期

    Python中的标准模块datetime是用来处理这种问题的简单方案
        datetime.strptime(text,'%Y-%m-%d')

    datetime.strptime()方法支持许多格式化代码，比如%Y代表以4位数字表示的年份，%m代表以2位数字表示的月份。这些格式化占位符也可以反过来用在将datetime对象转换为字符串上。如果需要以字符串形式来表示datetime对象并且想让输出格式变得美观时，可以这样使用
        datetime.strftime(datetime,'%A %B %d, %Y')
    这里值得一提的是strptime()的性能通常比我们想象的还要糟糕许多，这是因为该函数是用纯Python代码实现的，而且需要处理各种各样的系统区域设定。如果要在代码中解析大量的日期，而且事先知道日期的准确格式，那么自行实现一个解决方案可能会获得巨大的性能提升。如果知道日期是以'YYYY-MM-DD'的形式表示的，可以利用str.split()
    比datetime.strptime()快了7倍多。如果需要处理大量涉及日期的数据时，这很可能就是需要考虑的问题

### 3.16 处理涉及到时区的日期问题

    对于几乎涉及失去的问题，都应该使用pytz模块来解决。这个Python包提供了奥尔森时区数据，这也是许多语言和操作系统所使用的时区信息标准
    pyzt模块主要用来本地化由datetime库创建的日期。
        d=datetime(2012,12,21,9,30,0)
        loc_d=central.localize(d)
    一旦日期经过了本地化处理，它就可以转换为其他的时区。要知道同一时间在班加罗尔是几点
        bang_d=loc_d.astimezone(timezone('Asia/Kolkata'))
    如果打算对本地化的日期做算术计算，需要特别注意夏令时转换和其他方面的细节。2013年美国的标准夏令时于本地时间3月13日凌晨2点开始(此时时间要往前拨一个小时)。如果直接进行算术计算就会得到错误的结果
    因为上面的代码没有把本地时间中跳过的1小时给算上。要解决这个问题，可以使用timezone对象的normalize()方法。
        later = central.normalize(loc_d+timedelta(minutes=30))

    为了不让我们的头炸掉，通常用来处理本地时间的方法是将所有的日期都转换为UTC(世界统一时间)时间，然后在所有的内部存储和处理中都是用UTC时间
        utc_d=loc_d.astimezone(pytz.utc)
    一旦转换为UTC时间，就不用担心夏令时以及其他那些麻烦事了。因此，可以像之前那样对日期执行普通的算术运算。如果需要将日期以本地时间输出，只需将其转换为合适的时区即可。
    在同时区打交道时，一个常见的问题是如何知道时区的名称。要找出时区名称，可以考察一下pyzt.country_timezones，这是一个字典，可以使用ISO 3166国家代码作为key来查询
    根据PEP 431的描述，为了增强对时区的支持pyzt模块可能将不再建议使用。(但仍建议使用UTC时间等)

## 第4章 迭代器和生成器

    迭代是Python中最强有力的特性之一。从高层次看，可以简单地把迭代看作是一种处理序列中元素的方式。但还可以创建自己的可迭代对象，在itertools模块中选择实用的迭代模式、构建生成器等。

### 4.1 手动访问迭代器中的元素

    需要处理某个可迭代对象中的元素，但是基于某种原因不能也不想使用for循环
    要手动访问可迭代对象中的元素，可以使用next()函数，然后自己编写代码来捕获StopIteration异常。采用手工方式从文件中读取文本行
        with oprn('filename') as f:
            try:
                while True:
                    line =next(f)
                    print(line,end='')
            except StopIteration:
                pass
    一般来说，StopIteration异常是用来通知我们迭代结束的。但是，如果手动使用next()，也可以命令它返回一个结束值，比如说None   next(f,None)

    大多数情况下，会用for语句来访问可迭代对象中的元素。但偶尔也会碰到需要对底层迭代机制做更精细控制的情况。了解迭代时实际发生了些什么是很有帮助的
    以下对迭代时发生的基本过程做了解释说明
        items=[1,2,3]
        it = iter(items) # Invokes items.__iter__()
        next(it) # Invokes it.__next__()

### 4.2 委托迭代

    构建了一个自定义的容器对象，其内部持有一个列表、元组或其他的可迭代对象。要让新容器能够完成迭代操作
    一般来说，要做的就是定义一个__iter__()方法，将迭代请求委托到对象内部持有的容器上
        def __iter__(self):
            return iter(self.children)
    __iter__()方法只是简单地将迭代请求转发给对象内部持有的_children属性上

    Python的迭代协议要求__iter__()返回一个特殊的迭代器对象，由该对象实现的__next__()方法来完成实际的迭代。如果要做的只是迭代另一个容器中的内容，不必担心底层细节是如果工作的，所要作的就是转发迭代请求
    iter(s)通过调用s.__iter__()来简单地返回底层的迭代器，这和len(s)调用s.__len__()的方式是一样的

### 4.3 用生成器创建新的迭代模式

    实现一个自定义的迭代模式，使其区别于常见的内建函数(即range()、reversed()等)
    如果想实现一种新的迭代方式，可使用生成器函数来定义。产生某个范围内的浮点数的生成器：
        def frange(start,stop,increment):
            x=start
            while x<stop:
                yield x
                x+=increment
    要使用这个函数，可以使用for循环对其迭代，或者通过其他可以访问可迭代对象中元素的函数(例如sum()、list()等)来使用

    函数中只要出现了yield语句就会将其转变为一个生成器。与普通函数不同，生成器只会在响应迭代操作时才运行。
        def countdown(n):
            print('Starting to count from',n)
            while n>0:
                yield n
                n-=1
            print('Done!')
        c=countdown(3)
        next(c) next(c) next(c) next(c)
    核心特性是生成器函数只会在响应迭代过程中的"next"操作时才会运行。一旦生成器函数返回，迭代也就停止了。通常用来处理迭代的for语句替我们处理了这些细节，一般情况下不必为此操心

### 4.4 实现迭代协议

    要在对象上实现可迭代功能，最简单的方式就是使用生成器函数。用Node类来表示树结构。实现一个迭代器能够以深度优先的模式遍历树的节点:

    ```Python
        class Node:
            def __init__(self,value):
                self.value=value
                self.children=[]
            def __repr__(self):
                return 'Node({!r})'.format(self._value)
            def add_child(self,node):
                self._children.append(node)
            def __iter__(self):
                return iter(self._children)
            def depth_first(self):
                yield self
                for c in self:
                    yield from c.depth_first()
    ```
    depth_first()的实现非常易于阅读，描述起来也很方便。首先产生出自身，然后迭代每个子节点，利用子节点的depth_first()方法(通过yield from 语句)产生出其他元素

    Python的迭代协议要求__iter__()返回一个特殊的迭代器对象，该对象必须实现__next__()方法，并使用了StopIteration异常来通知迭代的完成。实现这样的对象常常会比较繁琐。

    ```Python
        class Node2:
            def __init__(self, value):
                self._value = value
                self._children = []
            def __repr__(self):
                return 'Node({!r})'.format(self._value)
            def add_child(self, node):
                self._children.append(node)
            def __iter__(self):
                return iter(self._children)
            def depth_first(self):
                return DepthFirstIterator(self)
        class DepthFirstIterator(object):
            '''
            Depth-first traversal
            '''
            def __init__(self, start_node):
                self._node = start_node
                self._children_iter = None
                self._child_iter = None
            def __iter__(self):
                return self
            def __next__(self):
            # Return myself if just started; create an iterator for children
                if self._children_iter is None:
                    self._children_iter = iter(self._node)
                    return self._node
            # If processing a child, return its next item
                elif self._child_iter:
                    try:
                        nextchild = next(self._child_iter)
                        return nextchild
                    except StopIteration:
                        self._child_iter = None
                        return next(self)
            # Advance to the next child and start its iteration
                else:
                    self._child_iter = next(self._children_iter).depth_first()
                    return next(self)
    ```
    DepthFirstIterator类的工作方式和生成器版本的实现相同但是却复杂了很多，因为迭代器必须维护迭代过程中许多复杂的状态，要记住当前迭代过程进行到哪里了。把迭代器以生成器的形式来定义就会很方便

### 4.5 反向迭代

    可以使用内建的reversed()函数实现反向迭代
    反向迭代只有在待处理的对象拥有可确定的大小，或者对象实现了__reversed__()特殊方法时，才能奏效。如果这两个条件都无法满足，则必须首先将这个对象转换为列表。
    将可迭代对象转换为列表可能会消耗大量的内存，尤其是当可迭代对象较大时更是如此

    如果实现了__reversed__()方法，就可以在自定义的类上实现反向迭代

    ```Python
        class Countdown:
            def __init__(self, start):
                self.start = start
            # Forward iterator
            def __iter__(self):
                n = self.start
                while n > 0:
                yield n
                n -= 1
    ```
    定义一个反向迭代器可使代码变得更加高效，因为这样就无需先把数据放到列表中，然后再反向去迭代列表

### 4.6 定义带有额外状态的生成器函数

    定义一个生成器函数，还涉及一些额外的状态，希望能够以某种形式将这些状态暴露给用户
    如果想让生成器将状态暴露给用户，可以将其实现为一个类，然后把生成器函数的代码放到__iter__()方法中

    ```Python
        from collections import deque
        class linehistory:
            def __init__(self,lines,histlen=3):
                self.lines=lines
                self.history = deque(maxlen=histlen)
            def __iter__(self):
                for lineno, line in enumerate(self.lines, 1):
                    self.history.append((lineno, line))
                    yield line
            def clear(self):
                self.history.clear()
    ```
    要使用这个类，可以将其看作是一个普通的生成函数。但由于它会创建一个实例，所以可以方位内部属性，比如history属性或clear()方法

    有了生成器之后很容易掉入陷阱，即试着只用函数来解决所有的问题。如果生成器函数需要以不寻常的方式同程序中其他部分交互的话(比如暴露属性，允许通过方法调用来获得控制等)，那就会导致出现相当复杂的代码。如果遇到了这种情况，就用类来定义。将生成器函数定义在__iter__()方法中并没有对算法做任何改变。由于状态只是类的一部分，这一事实使得我们可以很容易将其作为属性和方法来提供给用户交互
    如果打算用除了for循环之外的技术来驱动迭代过程的话，可能需要额外调用一次iter()

### 4.7 对迭代器做切片操作

    对由迭代器产生的数据做切片处理，但是普通的切片操作符在这里不管用
    要对迭代器和生成器做切片操作，itertools.islice()函数是完美的选择
        for x in itertools.islice(c,10,20):
            print(x)

    迭代器和生成器是没法执行普通的切片操作的，这是因为不知道它们的长度是多少(而且它们也没有实现索引)。islice()产生的结果是一个迭代器，它可以产生出所需要的切片元素，但这是通过访问并丢弃所有起始索引之前的元素来实现的。之后的元素会由islice()对象产生出来，直到到达结束索引为止
    islice()会消耗掉所提供的迭代器中的数据。由于迭代器中的元素只能访问一次，没法倒回去，需要引起注意。如果之后还需要倒回去访问前面的数据，那也许就应该先将数据转到列表中

### 4.8 跳过可迭代对象中的前一部分元素

    对某个可迭代对象做迭代处理，需要丢弃掉前面几个元素
    itertools模块中有一些函数可用来解决这个问题。第一个是itertools.dropwhile()函数。使用这个函数只需要提供一个函数和可迭代对象。该函数返回的迭代器会丢弃掉序列中的前面几个元素，只要它们在所提供的函数中返回True即可(提供的函数起一个筛子的作用，满足条件的都会丢弃直到有元素不满足为止)。这之后，序列中剩余的全部元素都会产生出来
    根据测试函数的结果来跳过前面的元素。如果恰好知道要跳过多少个元素，可以使用itertools.islice()
        islice(items,n,None)
    islice()的最后一个参数None用来表示想要前3个元素之外的所有元素，而不是只要前3个元素

    dropwhile()和islice()都是很方便实用的函数，可以利用它们来避免写出混乱代码
    dropwhile会丢弃开始部分的注释行，但同样会丢弃整个文件中出现的所有注释行。
    丢弃元素，直到有某个元素不满足测试函数为止。所有剩余元素全部会不经过筛选而直接返回
    适用于所有的可迭代对象，包括那些事先无法确定大小的对象也是如此。包括生成器、文件以及类似的对象。

### 4.9 迭代所有可能的组合或排列

    对一系列元素所有可能的组合或排列进行迭代
    itertools模块中提供了3个函数。第一个是itertools.permutations(items,n)————它接受一个元素集合，将其中所有的元素重排列为所有可能的情况，并以元组序列的形式返回(即将元素之间的顺序打乱成所有可能的情况)
    如果想得到较短长度的所有全排列，可以提供一个可选的长度参数
    使用itertools.combinations(items,n)可产生输入序列中所有元素的全部组合形式
    对于combinations()来说，元素之间的实际顺序是不予考虑的。
    当产生组合时，已经选择过的元素将从可能的候选元素(考虑范围)中移除掉。itertools.combinations_with_replacement(items,n)函数解除了这一限制，允许相同的元素得到多次选择

    面对看起来很复杂的迭代问题时，应该总是先去查看itertools模块

### 4.10 以索引-值对的形式迭代序列

    想记录迭代一个序列时序列中当前处理到的元素索引
    内建的enumerate(list,start)函数可以很好地解决这个问题
    如果要打印出规范的行号(这种情况下一般是从1开始而不是0)，可以传入一个start参数作为起始索引
    这种情况特别适合于跟踪记录文件中的行号，当想在错误信息中加上行号时就特别有用了。
    enumerate()可以方便地用来跟踪记录特定的值出现在列表中的偏移位置。如果想将文件中的单词和它们所出现的行之间建立映射关系，则可以通过使用enumerate()来将每个单词映射到文件行相应的偏移位置来实现

    对于那些可能想保存一个计数器的场景，enumerate()函数是个不错的替代选择，而且会更加便捷
    enumerate()的返回值是一个enumerate()对象实例，它是一个迭代器，可返回连续的元组。元组由一个索引值和对传入的序列调用next()而得到的值组成
    当在元组序列上应用enumerate()时，如果元组本身也被分解展开的话就会出错。要正确处理元组序列：
        data=[(x1,y1),(x2,y2)]
        for n,(x,y) in enumerate(data)

### 4.11 同时迭代多个序列

    可以使用zip()函数来同时迭代多个序列
    zip(a,b)的工作原理是创建出一个迭代器，该迭代器可产生出元组(x,y)，这里的x取自序列a，而y取自序列b。当其中某个输入序列中没有元素可以继续迭代时，整个迭代过程结束。因此整个迭代的长度和其中最短的输入序列长度相同
    如果这种行为不是所需要的，可以使用itertools.zip_longest()来替代，并使用None来补充

    zip()通常用在需要将不同的数据配对在一起时。
    尽管不常见，但是zip()可以接受多于2个序列作为输入。在这种情况下，得到的结果中元组里的元素数量和输入序列的数量相同
    zip()创建出的结果只是一个迭代器。如果需要将配对的数据保存为列表，需要使用list()函数

### 4.12 在不同的容器中进行迭代

    需要对许多对象执行相同的操作，但是这些对象包含在不同的容器内，希望可以避免写出嵌套的循环处理，保持代码的可读性
    itertools.chain()方法可以用来简化这个任务。它接受一系列可迭代对象作为输入并返回一个迭代器，这个迭代器能够有效地掩盖一个事实————实际上是在对多个容器进行迭代。
    在程序中，chain()常见的用途是想一次性对所有的元素执行某项特定的操作，但是这些元素分散在不同的集合中
    采用chain()的解决方案要更加优雅

    itertools.chain()可接受一个或多个可迭代对象作为参数，然后它会创建一个迭代器，该迭代器可连续访问并返回所提供的每个可迭代对象中的元素。尽管区别很小，但是chain()比首先将各个序列合并在一起然后再迭代要更加高效
    chain()并不会产生一个全新的序列，在内存上更加优化，而且也适用于可迭代对象不是同一种类型的情况

### 4.13 创建处理数据的管道

    想以流水线式的形式对数据进行迭代处理(类似Unix下的管道)。比如有海量的数据需要处理，但是没法完全将数据加载到内存中去
    生成器函数是一种实现管道机制的好方法。假设有一个超大的目录，其中都是想要处理的日志文件
    要处理这些文件，可以定义一系列小型的生成器函数，每个函数执行特定的独立任务

    ```Python
    import os
    import fnmatch
    import gzip
    import bz2
    import re
    def gen_find(filepat, top):
    '''
    Find all filenames in a directory tree that match a shell wildcard pattern
    '''
        for path, dirlist, filelist in os.walk(top):
            for name in fnmatch.filter(filelist, filepat):
                yield os.path.join(path,name)
    def gen_opener(filenames):
    '''
    Open a sequence of filenames one at a time producing a file object.
    The file is closed immediately when proceeding to the next iteration.
    '''
        for filename in filenames:
            if filename.endswith('.gz'):
                f = gzip.open(filename, 'rt')
            elif filename.endswith('.bz2'):
                f = bz2.open(filename, 'rt')
            else:
                f = open(filename, 'rt')
            yield f
            f.close()
    def gen_concatenate(iterators):
    '''
    Chain a sequence of iterators together into a single sequence.
    '''
        for it in iterators:
            yield from it
    def gen_grep(pattern, lines):
    '''
    Look for a regex pattern in a sequence of lines
    '''
        pat = re.compile(pattern)
        for line in lines:
            if pat.search(line):
                yield line
    ```
    然后简单地将这些函数堆叠起来形成一个数据处理的管道。如果要找出所有包含关键字的日志行：
        lognames = gen_find('access-log*','www')
        files = gen_opener(lognames)
        lines = gen_concatenate(files)
        pylines = gen_grep('(?i)python',lines)
    如果稍后想对管道进行扩展，甚至可以在生成器表达式中填充数据。找出传送的字节数并统计出总字节量
        bytecolumn = (line.rsplit(None,1)[1] for line in pylines)
        bytes = (int(x) for x in bytecolumn if x != '-')

    将数据以管道的形式进行处理可以很好地适用于其他广泛的问题，包括解析、读取实时的数据源、定期轮询等
    在这里yield语句表现为数据的生产者，而for循环表现为数据的消费者。当生成器被串联起来时，在迭代中每个yield语句都为管道中下个阶段的处理过程产生出数据。sum()函数实际上在驱动整个程序，每一次都从生成器管道中取出一份数据
    这种方法的优点在于每个生成器函数都比较短小而且功能独立，使得编写和维护都很容易。在许多情况下，其通用性使得它们可以在其他上下文中使用。
    这种方法在内存使用上也非常高效。由于处理过程的迭代特性，只会用到非常少的内存
    gen_concatenate()函数的目的是将输入序列连接为一个长序列行。itertools.chain()函数可以实现类似的功能，但是这需要将所有的可迭代对象指定为它的参数才行。这么做会使得gen_opener()生成器被完全耗尽。由于这个生成器产生的是打开的文件序列，在下一个迭代步骤中会被立刻关闭，因此不能用chain()
    gen_concatenate()函数中也出现了实现委托给一个子生成器的yield from语句，该句简单地使gen_concatenate()函数发射出所有由生成器it产生的值。
    管道方法并不会总是适用于每一个数据处理问题。有时候需要马上处理所有的数据。但使用生成器管道可以在逻辑上将问题分解成一种工作流程
    有关生成器可以参考David Beazley的"针对系统程序员之生成器技巧"

### 4.14 扁平化处理嵌套型的序列

    可以通过带有yield from语句的递归生成器函数来实现

    ```Python
    from collections import Iterable
    def flatten(items, ignore_types=(str, bytes)):
        for x in items:
            if isinstance(x, Iterable) and not isinstance(x, ignore_types):
                yield from flatten(x)
            else:
                yield x
    ```
    isinstance(x,Iterable)简单地检查是否有某个元素是可迭代的。如果确实有，就用yield from将这个可迭代对象作为一种子例程进行递归，将它所有的值都产生出来。最后得到的结果就是一个没有嵌套的单值序列
    代码中额外的参数ignore_types和对not isinstance(x,ignore_types)的检查是为了避免将字符串和字节串解释为可迭代对象，进而将它们展开为单独的一个个字符。这使得嵌套型的字符串列表能够以大多数人所期望的方式工作

    如果想编写生成器用来把其他的生成器当作子例程调用，yield from是个不错的快捷方式。否则就需要编写有额外for循环的代码
    对字符串和字节串的额外检查是为了避免将这些类型的对象展开为单独的字符。如果还有其他类型是不想要展开的，可以为ignore_types参数提供不同的值来确定
    yield from在涉及协程和基于生成器的并发型高级程序中有着更加重要的作用

### 4.15 合并多个有序序列，再对整个有序序列进行迭代

    heapq.merge()函数则能够实现

    heapq.merge()的迭代性质意味着它对所有提供的序列都不会做一次性读取。这意味着可以用它处理非常长的序列，而开销非常小。
    heapq.merge()要求所有的输入序列都是有序的。它不会首先将所有的数据读取到堆中，或者预先做任何的排序操作。也不会对输入做任何验证，以检查它们是否满足有序的要求。只是简单地检查每个输入序列中的第一个元素，将最小的那个发送出去。然后再从之前选择的序列中读取一个新的元素，再重复执行这个步骤，直到所有的输入序列都耗尽为止

### 4.16 用迭代器取代while循环

    采用while循环来迭代处理数据，因为这其中涉及调用某个函数或有某种不常见的测试条件，而这些东西没法归类为常见的迭代模式
    在涉及I/O处理的程序中
        CHUNKSIZE = 8192
        def reader(s):
            while True:
                data = s.recv(CHUNKSIZE)
                if data == b'':
                    break
                process_data(data)
    这样的代码常常可以用iter()来替换

    关于内建函数iter()，它可以选择性接受一个无参的可调用对象以及一个哨兵(结束)值作为输入。当以这种方式使用时，iter()会创建一个迭代器。然后重复调用用户提供的可调用对象，直到它返回哨兵值为止
    这种特定的方式对于需要重复调用函数的情况，比如这些设计I/O的问题，有很好的效果。如果想从socket或文件中按块读取数据，通常会重复调用read()或者recv()，然后紧跟着检测是否到达文件末尾。通过将这两个功能合并为一个单独的iter()调用。

## 第5章 文件和I/O

    任何程序都需要处理输入和输出

### 5.1 读写文本数据

    需要对文本数据进行读写操作，但这个过程有可能针对不同的文本编码进行，比如ASCII、UTF-8或UTF-16编码
    可以使用open()函数配合rt模式来读取文本文件的内容
    要对文本文件执行写入操作，可以使用open()函数的wt模式来完成。如果待操作的文件已存在，那么这会清除并覆盖其原先的内容
    如果要在已存在文件的结尾处追加内容，可以使用open()函数的at模式
    默认情况下，文件的读取和写入采用的都是系统默认的文本编码方式，这可以通过sys.getdefaultencoding()来查询。在大多数机器上，这项设定都被设置为utf-8。如果知道正在读取或写入的文本采用的是另一种编码方式，那么可以为open()函数提供一个可选的编码参数
        open('filename','rt',encoding='latin-1')
    Python可以识别出几百种可能的文本编码。一些常见的编码方式不外乎是ascii、latin-1、utf-8以及utf-16。如果要同Web应用程序打交道，采用utf-8编码通常是比较保险的。ascii编码对应于范围U+000到U+007F中的7比特字符。latin-1编码则是字节0~255对Unicode字符U+0000到U+00FF的直接映射。关于latin-1编码，当读取到未知编码的文本时是不会产生解码错误的。以latin-1方式读取文件可能不会产生完全正确的解码文本，但是要从中提取出有用的数据仍然是足够的。如果稍后将数据重新写入到文件中，那么原始的输入数据将得到保留

    一般来说，读写文本文件都是非常简单直接的。需要注意：采用with语句会为使用的文件创建一个上下文环境(context)。当程序的控制流程离开with语句块后，文件将自动关闭。如果不用with语句，要记得手动关闭文件
    另一个细微的问题是关于换行符的识别，在UNIX和Windows上它们是不同的(即\n和\r\n之争)。默认情况下，Python工作在"通用型换行符"模式下。在该模式种，所有常见的换行格式都能识别出来。在读取时会将换行符转换成一个单独的\n字符
    同样的，在输出时换行符\n会被转换为当前系统默认的换行符。如果不需要这种"翻译"行为，可以给open()函数提供一个newline=''的参数
    关于文本文件中可能出现的编码错误，如果遇到这种错误，这通常表示没有以正确的编码方式来读取文件。应该仔细阅读要读取的文本的相关规范，并检查自己的操作是否正确(例如不要用latin-1编码方式读取，换成utf-8或者任何所需的编码方式)。如果还是有可能出现编码错误，则可以为open()函数提供一个可选的errors参数来处理错误
        errors='replace'/'ignore'
    如果常常在摆弄open()函数的encoding和errors参数，并为此做了大量的技巧性操作，那就适得其反了。关于文本，第一条守则就是只需要确保总是采用正确的文本编码形式即可。如果有疑问，就使用默认的编码设定

### 5.2 将输出重定向到文件中

    为print()函数加上关键字参数
        with open("filename",'rt') as f:
            print('Hello World!',file=f)
    
    需要确保文件是以文本模式打开的

### 5.3 以不同的分隔符或行结尾符完成打印

    在print()函数中使用sep和end关键字参数来根据需要修改输出
        sep默认为" ",end默认为"\n"

    除了空格之外，当还需要用其他字符来分隔文本时，通常在print()函数中通过sep关键字参数指定一个不同的分隔符。str.join也能实现同样的效果，但是只能处理字符串

### 5.4 读写二进制数据

    使用open()函数的rb或者wb模式就可以实现对二进制数据的读或写
    当读取二进制数据时，所有的数据将以字节串的形式返回，而不是文本字符串。当写入二进制数据时，数据必须是以对象的形式来提供，而且该对象可以将数据以字节形式暴露出来(即字节串、bytearray对象等)

    当读取二进制数据时，由于字节串和文本字符串之间存在微妙的语义差异，这可能会造成一些潜在的问题。在作索引和迭代操作时，字节串会返回代表该字节的整数值而不是字符串
    如果需要在二进制文件中读取或写入文本内容，请确保要进行编码或解码操作
    关于二进制I/O，像数组和C结构体这样的对象可以直接用来进行写操作，而不必先将其转换为byte对象
        nums=array.array('i',[1,2,3,4])
        with open('data.bin','wb) as f:
            f.write(nums)
    这种行为可适用于任何实现了所谓的"缓冲区接口"的对象。该接口直接将对象底层的内存缓冲区暴露给可用在其上进行的操作。写入二进制数据就是这样一种操作
    有许多对象还支持直接将二进制数据读入到它们底层的内存中，只要使用文件对象的readinto()方法就可以了
        a=array.array('i',[0,0,0,0,0,0,0,0])
        with open('data.bin','rb')
            f.readinto(a) #承接之前的操作
    使用这项技术要小心，因为这常常是与平台特性相关的，而且可能依赖于字的大小和字节序(即大端和小端)等属性。

### 5.5 对已不存在的文件执行写入操作

    可以通过使用open()函数中的x模式替代常见的w模式来解决，只有文件不存在才能通过x模式打开
    如果文件是二进制模式的，用xb模式替代xt

    这样以一种优雅的方式解决了一个常会在写文件时出现的问题(意外地覆盖了某个已存在的文件)。另一种解决方案是首先检查文件是否已存在
        if not os.path.exists('somefile'):
    很明显，使用x模式更加简单直接。x模式是Python3中对open()函数的扩展。在早期的Python版本或者在Python的实现中用到的底层C函数库里都不存在这样的模式

### 5.6 在字符串上执行I/O操作

    使用io.StringIO()和io.BytesIO()类来创建类似于文件的对象，这些对象可操作字符串数据
        s=io.StringIO()
        s.write('Hello World\n')
        print("This is test',file=s)
        s.getvalue()
        s.read(n)
    io.StringIO类只能用于对文本的处理。如果要操作二进制数据，则使用io.BytesIO()

    当出于某种原因需要模拟出一个普通文件时，这种情况下StringIO和BytesIO类是最为适用的。在单元测试中，可能会使用StringIO来创建一个文件型的对象，对象中包含了测试用的数据。之后可将这个对象发送给一个可以接受普通文件的函数
    StringIO和BytesIO实例是没有真正的文件描述符来对应的。没法工作在一个真正的系统级文件例如文件、管道或套接字的代码环境中。 

### 5.7 读写压缩的数据文件

    gzip和bz2模块使得同这类压缩型文件打交道变得非常简单。这两个模块都提供了open()的其他实现，可用于处理压缩文件。要将压缩文件以文本形式读取
        with gzip.open('somefile.gz','rt') as f:
        with bz2.open('somefile.ba2','rt') as f:
            text=f.read()
            f.write(text)
    以上所有的I/O操作都会采用文本形式并执行Unicode编码/解码操作。如果想处理二进制数据，则使用rb和wb形式

    大部分情况下读写压缩数据都是简单而直接的。选择正确的模式非常重要，如果没有指定模式，那么默认的模式是二进制，会使得期望接受文本的程序崩溃。gzip.open()和bz2.open()所接受的参数与内建的open()函数一样，也支持encoding、errors、newline等关键字参数
    当写入压缩数据时，压缩级别可通过compresslevel关键字参数来指定，这是可选的。
    默认级别是9，代表着最高的压缩等级。低等级的压缩可带来更好的性能表现，但压缩比就没有那么大
    gzip.open()和bz2.open()有一个较少提到的特性，即它们能够对已经以二进制模式打开的文件进行叠加操作
    这种行为使得gzip和bz2模块可以同各种类型的类文件对象比如套接字、管道和内存文件一起工作

### 5.8 对固定大小的记录进行迭代

    可以利用iter()和functools.partial()来完成这个巧妙的技巧。
        RECORD_SIZE = 32
        with open('somefile.data','rb') as f:
            records = iter(functools.partial(f.read,RECORD_SIZE),b'')
    示例中的records对象是可迭代的，它会产生出固定大小的数据块直到到达文件结尾。如果文件大小不是记录大小的整数倍的话，那么最后产生出的那个数据块可能比所期望的字节数要少

    关于iter()函数，如果传递一个可调用对象及一个哨兵值给他，那么它可以创建出一个迭代器。得到的迭代器会重复调用用户提供的可迭代对象，直到返回的值为哨兵值为止，此时迭代过程停止
    functools.partial用来创建可调用对象，每次调用它时都从文件中读取固定的字节数。b''在这里用作哨兵值，当读取到文件结尾时就会返回这个值，此时迭代过程结束
    对于读取固定大小的记录，几乎是最常见的情况。如果要针对二进制文件，按行读取(默认的迭代行为)更为普遍一些

### 5.9 将二进制数据读取到可变缓冲区中

    要将数据读取到可变数组中，使用文件对象的readinto()方法即可
        def read_into_buffer(filename):
            buf = bytearray(os.path.getsize(filename))
            with open(filename,'rb') as f:
                f.readinto(f)
            return buf

    文件对象的readinto()方法可用来将数据填充到任何预分配好的数组中，这包括array模块或者numpy这样的库所创建的数组。与普通的read()方法不同的是,readinto()是为已存在的缓冲区填充内容，而不是分配新的对象然后再将它们返回。可以用readinto()来避免产生额外的内存分配动作。读取一个由相同大小的记录所组成的二进制文件
        RECORD_SIZE = 32
        buf = bytearray(RECORD_SIZE)
        with open('somefile','rb') as f:
        while True:
            n = f.readinto(buf)
            if n < RECORD_SIZE:
                break
    这里用到的另一个有趣的特征应该就是内存映像了，它使得程序员可以对已存在的缓冲区做切片处理，但是中间不涉及任何拷贝动作，还可以修改它的内容
        m1 = memoryview(buf)
        m2 = m1[-5:]
        m2[:] = b'WORLD'
    使用f.readinto()需要注意的一点是，必须总是确保要检查它的返回值，即实际读取的字节数
    如果字节数小于所提供的缓冲区大小，这可能表示数据被截断或遭到了破坏(如期望督导一个准确的字节数时)
    可以在各种库模块找到那些带有'into'的函数(如recv_into()、pack_into()等)。Python中有许多模块都支持直接I/O访问，可用来填充或修改数组和缓冲区中的内容

### 5.10 对二进制文件做内存映射

    可以使用mmap模块实现对文件的内存映射操作。以可移植的方式打开一个文件并对它进行内存映射操作
        def memory_map(filename,access=mmap.ACCESS_WRITE):
            size = os.path.getsize(filename)
            fd = os.open(filename,os.O_RDWR)
            return mmap.mmap(fd,size,access=access)
    要使用这个函数，需要准备一个已经创建好的文件并为之填充一些数据。创建一个初始文件，并将其扩展为所需要的大小
        size = 1000000
        with open('data','wb') as f:
            f.seek(size-1)
            f.write(b'\x00')
    用memory_map()函数对文件内容做内存映射
        m = memory_map('data')
        len(m)
        m[0:10]
        m[0:11] = b'Hello World'
        m.close()
        with open('data','rb') as f:
            print(f.read(11))
    由mmap()返回的mmap对象也可以当作上下文管理器使用，在这种情况下，底层的文件会自动关闭
        with memory_map('data') as m:
            print(len(m))
            print(m[0:10])
        m.closed()
    默认情况下，memory_map()函数打开的文件既可以读也可以写。对数据的任何修改都会拷贝回原始的文件中。如果需要只读访问，可以为access参数提供mmap.ACCESS_READ值
    如果只想在本地修改数据，并不想将这些修改写回到原始文件中，可以使用mmap.ACCESS_COPY参数

    通过mmap将文件映射到内存中后，能够以高效和优雅的方式对文件的内容进行随机访问。与其打开文件后通过组合各种seek()、read()和write()调用来访问，不如简单地将文件映射到内存，然后通过切片操作来访问数据
    由mmap()暴露出的内存看起来就像一个bytearray对象。利用memoryview能够以不同的方式来解读数据
    对某个文件进行内存映射并不会导致将整个文件读到内存中。文件并不会拷贝到某种内存缓冲区或数组上。操作系统只是为文件内容保存一段虚拟内存而已。当访问文件的不同区域时，文件的这些区域将被读取并按照需要映射到内存区域中。文件中从未访问过的部分会简单地留在磁盘上。这些操作以透明的方式在后台完成
    如果有多个Python解释器对同一个文件做了内存映射，得到的mmap对象可用来在解释器之间交换数据。所有的解释器可以同时读写数据，在一个解释器中对数据做出的修改会自动反映到其他的解释器上。这里需要一些额外的步骤来处理同步问题，但是有时候可用这种方法作为通过管道或socket传输数据的替代方式
    对于mmap()的使用，不同的平台上会存在一些差异。还有选项可用来创建匿名的内存映射区域

### 5.11 处理路径名

    需要处理路径名以找出基文件名、目录名、绝对路径等相关的信息
    要操纵路径名，可以使用os.path模块中的函数。
        os.path.basename(path)
        os.path.dirname(path)
        os.path.join("","",os.path.basename(path))
        os.path.expanduser(path)
        os.path.splitext(path)

    对于任何需要处理文件名的问题，都应该使用os.path模块而不是通过使用标准的字符串操作来自己实现这部分功能。部分原因是为了考虑可移植性。os.path模块知道UNIX和Windows系统之间的一些差异，能够可靠地处理类似Data/data.csv和Data\data.csv这样的文件名。

### 5.12 检测文件是否存在

    可用通过os.path模块来检测某个文件或目录是否存在
        os.path.exists(dirname)
    之后可以执行进一步的测试来查明这个文件的类型。
        os.path.isfile(name)
        os.path.isdir(name)
        os.path.islink(name)
        os.path.realpath(name)
    如果需要得到元数据(即文件大小或修改日期)，这些功能在os.path模块中也有提供
        os.path.getsize(name)
        os.path.getmtime(name)
        time.ctime(os.path.getmtime(name))

    利用os.path模块来对文件做检测是简单而直接的。在编写脚本时唯一需要注意的事情就是关于权限的问题——尤其是获取元数据的操作

### 5.13 获取目录内容的列表

    可以使用os.listdir()函数来获取目录中的文件列表
        names = os.listdir(dirname)
    这么做会得到原始的目录文件列表，包括所有的文件、子目录、符号链接等。如果需要以某种方式来筛选数据，可以考虑利用列表推导式结合os.path模块中的各种函数来完成
        names = [name for name in os.listdir(dirname) if os.path.isfile(os.path.join(dirname,name))]
        names = [name for name in os.listdir(dirname) if os.path.isdir(os.path.join(dirname,name))]
    字符串的startswith()和endswith()方法对于筛选目录中的内容也同样有用
    至于文件名的匹配，可以用glob或者fnmatch模块
        pyfiles = glob.glob('somedir/*.py')
        pyfiles = [name for naem in os.listdir(dirname) if fnmatch(name,'*.py')]

    得到目录中内容的列表很简单，但只得到目录中每个条目的名称。如果想得到一些附加的元数据，比如文件大小、修订日期等，要么使用os.path模块中的其他函数，要么使用os.stat()函数。收集这些数据
        pyfiles = glob.glob('somedir/*.py')
        name_sz_date = [(name, os.path.getsize(name), os.path.getmtime(name)) for name in pyfiles]
        file_metadata = [(name, os.stat(name)) for name in pyfiles]

    请注意有关文件名编码时会出现一些微妙问题。一般来说，像os.listdir()这样的函数返回的条目都会根据系统默认的文件名编码方式来进行解码处理。有可能在特定的条件下会遇到无法解码的文件名

### 5.14 绕过文件名编码

    相对使用了原始文件名的文件执行I/O操作，这些文件名没有根据默认的文件名编码规则来解码或编码
    默认情况下，所有的文件名都会根据sys.getfilesystemencoding()返回的文本编码形式进行编码和解码
    如果基于某些原因想忽略这种编码，可以使用原始字节串来指定文件名
        with open('Jalape\x1o.txt','w') as f:
            f.write('Spicy')
        os.listdir('.')
        os.listdir(b'')
        with open(b'jalapen\xcc\x83o.txt') as f:
            print(f.read())
    当给同文件相关的函数比如open()和os.listdir()提供字节串参数时，对文件名的处理就发生了微小的改变

    一般情况下，不应该去担心有关文件名编码和解码的问题————普通的文件名操作应该能正常工作。有许多操作系统可能会允许用户通过意外或恶意的方式创建出文件名不遵守期望的编码规则的文件。这样a的文件名可能会使得处理大量文件的Python程序莫名其妙地崩溃
    在读取目录和同文件名打交道时，以原始的未编码的字节作为文件名就可以避免这样的问题

### 5.15 打印无法解码的文件名

    当打印来路不明的文件名时，可以使用下面的方式来避免出现错误
        def bad_filename(filename):
            return repr(filename)[1:-1]
        try:
            print(filename)
        except UnicodeEncodeError:
            print(bad_filename(filename))

    当程序必须去操纵文件系统时，默认情况下，Python假设所有的文件名都是根据sys.getfilesystemencoding()返回的编码形式进行编码的。某些文件系统不一定会强制执行这种编码约束，因此会允许文件以不恰当的编码方式来命名。某些用户可能会意外地创建出一个文件(如在某些有问题的代码中将不恰当的文件名传给open())
    当执行类似os.listdir()这样的命令时，错误的文件名会使Python陷入窘迫的境地。一方面Python不能直接丢弃错误的名字，而另一方面它也无法将文件名转为合适的文本字符串。对于这个问题，Python的解决方案是在文件名中取出一个无法解码的字节值\xhh，将其映射到一个所谓的"代理编码"中，代理编码由Unicode字符\udchh来表示。
    如果代码只是用来操纵文件名或者甚至是将文件名传递给函数(如open())，一切都能正常工作。只有当想把文件名输出时才会陷入麻烦(即打印到屏幕、记录到日志上等)。如果试着打印，程序就会崩溃
    崩溃的原因在于字符\udce4不是合法的Unicode字符。实际上是2字符组合的后半部分，这个组合称为代理对。由于前半部分丢失了，因此是非法的Unicode。唯一能成功产生输出的方式是，当遇到有问题的文件名时采取纠正措施。
    函数bad_filename()要实现什么功能很大程度取决于需求。
        def bad_filename(filename):
            temp = filename.encode(sys.getfilesystemencoding(),errors='surrogateescape')
            return temp.decode('latin-1')
    如果要编写完成关键任务的脚本，需要可靠地与文件名以及文件系统打交道。

### 5.16 为已经打开的文件添加或修改编码方式

    为一个已经打开的文件添加或修改Unicode编码，但不必首先将其关闭
    如果想为一个以二进制模式打开的文件对象添加Unicode编码/解码，可以用io.TextIOWrapper()对象将其包装
        u=urllib.request.urlopen('http://www.python.org')
        f=io.TextIOWrapper(u,encoding='utf-8')
        text=f.read()
    如果想修改一个已经以文本模式打开的文件的编码方式，可以在用新的编码替换之前的编码前，用detach()方法将已有的文本编码层移除。
        sys.stdout.encoding
        sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding='latin-1')
    这么做可能会破坏终端上的输出

    I/O系统是以一系列的层次来构建的。
        f=open('sample.txt','w')
        f #<_io.TextIOWrapper name='sample.txt' mode='w' encoding='cp936'>
        f.buffer #<_io.BufferedReader name='sample.txt'>
        f.buffer.raw #<_io.FileIO name='sample.txt' mode='wb' closefd=True>
    io.TextIOWrapper是一个文本处理层，它负责编码和解码Unicode。而io.BufferedWriter是一个缓冲I/O层，负责处理二进制数据。io.FileIO是一个原始文件，代表着操作系统底层的文件描述符。添加或修改文本的编码设计添加或修改最上层的io.TextIOWrapper层
    作为一般的规则，直接通过访问上面展示的属性来操作不同的层次是不安全的。如果用这种技术来修改编码
        f = io.TextIOWrapper(f.buffer,encoding='latin-1')
        f.write('Hello')
    这样的操作无效，因为f之前的值已经被销毁，在这个过程中导致底层的文件被关闭
    detach()方法将最上层的io.TextIOWrapper层同文件分离开来，并将下一个层次(io.BufferedWriter)返回。在这之后，最上层将不再起作用。
    一旦完成分离，就可以为返回的结果添加一个新的最上层
    同样可以利用这层技术来修改文本行的处理、错误处理机制以及其他有关处理方面的行为
        sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding='ascii',errors='xmlcharrefreplace')
        print('Jalape\u00f1o)
    非ASCII字符已经被替代了

### 5.17 将字节数据写入文本文件

    只需要简单地将字节数据写入到文件底层的buffer中就可以了
        sys.stdout.write(b'Hello\n')
        sys.stdout.buffer.write(b'Hello\b')
    同样也可以从文本文件中读取二进制数据，只要通过buffer属性来读取即可

    I/O系统是以不同的层次来构建的。文本文件是通过在缓冲的二进制模式文件之上添加一个Unicode编码/解码层来构建的。buffer属性简单地指向底层的文件。如果访问该属性，就可以绕过文本编码/解码层了
    默认情况下，sys.stdout总是以文本模式打开的。但如果要编写一个需要将二进制数据转储到标准输出的程序，就可以使用这种方法

### 5.18 将已有的文件描述符包装为文件对象

    有一个以整数值表示的文件描述符，已经同操作系统中已打开的I/O通道建立起了联系(即文件、管道、socket等)。而希望以高级的Python文件对象来包装这个文件描述符
    文件描述符与一般打开的文件相比是有区别的。文件描述符只是一个由操作系统分配的整数句柄，用来指代某种系统I/O通道。如果刚好有这样一个文件描述符，就可以通过open()函数用Python文件对象对其进行包装。只需要将整数形式的文件描述符作为第一个参数取代文件名就可以了。
        fd = os.open('somefile.txt',os.O_WRONLY | os.O_CREAT)
        f = open(fd,'wt')
        f.write('hello world\n')
        f.close()
    当高层的文件对象被关闭或销毁时，底层的文件描述符也会被关闭。如果不想要这种行为，只需给open()提供一个可选的closefd=False参数即可
        f = open(fd,'wt',closefd=False)

    在UNIX系统上，这种包装文件描述符的技术可以用来方便地对以不同方式打开的I/O通道(即管道、socket等)提供一个类似于文件的接口。

    ```Python
    from socket import socket,AF_INET,SOCK_STREAM
    def echo_client(client_sock,addr):
        print("Got Connection from",addr)
        client_in=open(client_sock.fileno(),'rt',encoding='latin-1',closefd=False)
        client_out=open(client_sock.fileno(),'wt',encoding='latin-1',closefd=False)
        for line in client_in:
            client_out.write(line)
            client_out.flush()
        client_sock.close()
    def echo_server(address):
        sock=socket(AF_INET,SOCK_STREAM)
        sock.bind(address)
        sock.listen(1)
        while True:
            client,addr=sock.accept()
            echo_client(client,addr)
    ```
    以上例子只是用来说明内建的open()函数的一种特性，而且只能工作在基于UNIX的系统之上。如果想在socket上加上一个类似文件的接口，并且需要做到跨平台，那么就应该使用socket的makefile()方法来替代。如果不需要考虑可移植性的话，就会发现上面给出的解决方案在性能上要比makefile()高出不少
    也可以利用这项技术为一个已经打开的文件创建一种别名，使得它的工作方式能够稍微区别于首次打开时的样子。以下代码创建一个文件对象，���得���能���在stdout上产生出二进制数据(通常stdout是以文本模式打开的)
        bstdout = open(sys.stdout.fileno(),'wb',closefd=False)
        bstdout.write(b'Hello World\n')
        bstdout.flush()
    尽管可以将一个已存在的文件描述符包装成一个合适的文件，但是并非所有的文件模式都可以得到支持，而且某些特定类型的文件描述符可能还带有有趣的副作用(尤其是在面对错误处理、文件结尾的情况时)。具体的行为也可能因为操作系统的不同而有所区别。以上代码只能在UNIX系统上工作。最基本的底线就是需要对自己的实现进行彻底的测试，确保代码能够按照期望的方式工作

### 5.19 创建临时文件和目录

    当程序运行时，需要创建临时文件或目录以便使用。在这之后进行销毁
    tempfile模块中有各种函数可以用来完成这个任务。要创建一个未命名的临时文件，可以使用tempfile.TemporaryFile
        from tempfile import TemporaryFile
        with TemporaryFile('w+t') as f:
            f.write('Hello World\n')
            f.write('Testing\n')
            f.seek(0)
            data=f.read()
    TemporaryFile()的第一个参数是文件模式，通常以w+t处理文本模式而以w+b处理二进制数据。这个模式可同时支持读写，在这里是很有用的，因为关闭文件后再来修改模式实际上会销毁文件对象。TemporaryFile()也可以接受和内建的open()函数一样的参数
    在大多数UNIX系统上，由TemporaFile()创建的文件都是未命名的，而且在目录中也没有对应的条目。如果想解放这种限制，可以使用NamedTemporaryFile()来替代。
        from tempfile import NamedTemporaryFile
        with NamedTemporaryFile('w+t') as f:
            print('filename is',f.name)
    要创建一个临时目录，可以使用tempfile.TemporaryDirectory()来实现
        from tempfile import TemporaryDirectory
        with TemporaryDirectory() as dirname:
            print('dirname is:',dirname)

    要和临时文件还有临时目录打交道，最方便的方式就是使用TemporaryFile()、NamedTemporaryFile()以及TemporaryDirectory()这三个函数。因为它们能自动处理有关创建和清除的所有步骤。从较低的层次看，也可以使用mkstemp()和msdtemp()来创建临时文件和目录
    但这些函数并不会进一步去处理文件管理的任务。mkstemp()函数只是简单地返回一个原始的操作系统文件描述符，然后自行转换为一个合适的文件。如果想将文件清理掉的话，这个任务也是自己完成
    一般情况下，临时文件都是在系统默认的区域中创建的，比如/var/tmp或者类似的地方。要找出实际的位置，可以使用tempfile.gettempdir()函数。
    所有同临时文件相关的函数都允许使用prefix、suffix和dir关键字参数来覆盖目录
    在可能的范围内，tempfile模块创建的临时文件都是以最安全的方式来进行的。这包括只为当前用户提供可访问的权限，并且在创建文件时采取了相应的步骤来避免出现竞态条件。在不同的平台下这可能会有一些区别。

### 5.20 同串口进行通信

    通过串口读取和写入数据，典型情况下是同某种硬件设备进行交互(即机器人或传感器)
    可以直接通过Python内建的I/O原语来完成这个任务，但对于串口通信来说，使用pySerial包比较好。这个包使用起来较为简单，打开一个串口
        ser = serial.Serial('COM3',baudrate=9600,bytesize=8,parity='N',stopbits=1)
    设备名称可能会根据设备的类型和操作系统而有所不同。在Windows上，可以使用0、1这样的数字代表设备来打开通信端口，比如"COM0"和"COM1"。一旦打开后，就可以通过read()、readline()和write()调用来写数据
        ser.write(b'G1 X50 Y50\r\n')
        resp = ser.readline()
    大部分情况下的串口通信任务应该是非常简单的

    但串口通信常常会变得相当混乱。应该使用一个像pySerial这样的包的原因就在于它对一些高级特性提供了支持(即超时处理、流控、刷新缓冲区、握手机制等)。比如，如果想开启RTS-CTS助手，只要简单地为Serial()提供一个rtscts=True关键字参数即可。
    所有涉及串口的I/O操作都是二进制的。确保在代码中使用的是字节而不是文本(或者根据需要执行适当的文本编码/解码操作)。当需要创建以二进制编码的命令或者数据包时，struct模块也会起到不少作用

### 5.21 序列化Python对象

    需要将Python对象序列化为字节流，便可将其保存到文件中、存储到数据库中或者通过网络连接进行传输
    序列化数据最常见的做法就是使用pickle模块。要将某个对象转储到文件中
        data = ... #some Python object
        f = open('somefile','wb')
        pickle.dump(data,f)
    要将对象转储为字符串，可以使用pickle.dumps()
        s=pickle.dumps(data)
    如果要从字节流中重新创建出对象，可以使用pickle.load()或者pickle.loads()函数
        f=open('somefile','rb')
        data=pickle.load(f)
        data=pickle.loads(s)

    对于大部分程序来说，只要掌握dump()和load()函数的用法就可以高效地利用pickle模块了。pickle模块能够兼容大部分Python数据类型和用户自定义的类实例。如果正在使用的库可以保存/恢复Python对象到数据库中，或者通过网络传输对象，很有可能就在使用pickle
    pickle是一种Python专有的自描述式的数据编码。称为自描述，是因为序列化的数据中包含有每个对象的开始和结束以及有关对象类型的信息。处理多个对象
        f=open('somedata','wb')
        pickle.dump([1,2,3,4],f)
        pickle.dump('hello',f)
        pickle.dump({'Apple','Pear','Banana'},f)
        f.close()
        f=open('somedata','rb')
        pickle.load(f) # for 4 times
    可以对函数、类以及实例进行pickle处理，但由此产生的数据只会对代码对象所关联的名称进行编码
        pickle.dumps(math.cos)
    当对数据做反序列化处理时，会假设所有所需的源文件都是可用的。模块、类以及函数会根据需要自动导入。对于需要在不同机器上的解释器之间共享Python数据的应用，这会成为一个潜在的维护性问题，因为所有的机器都必须能够访问到相同的源代码
    绝对不能对非受信任的数据使用pickle.load()。由于会产生副作用，pickle会自动加载模块并创建实例。了解pickle是如何运作的骇客可以故意创建出格式不正确的数据，使得Python解释器有机会去执行任意的系统命令。有必要将pickle限制为只在内部使用，解释器和数据之间要能够彼此验证对方
    某些特定类型的对象是无法进行pickle操作的。这些对象一般来说都会涉及某种外部系统状态，比如打开的文件、打开的网络连接、线程、进程、栈帧等。用户自定义的类有些时候可以通过__getstate__()和__setstate__()方法来规避这些规则。如果定义了这些方法，pickle.dump()就会调用__getstate__()来得到一个可以被pickle处理的对象。在unpickle的时候就会调用__setstate__()来得到一个可以被pickle处理的对象。在unpickle的时候就会调用__setstate__()了。下面这个类在内部定义了一个线程，但是仍然可以进行pickle/unpickle操作

    ```Python
    import time,threading
    class Countdown:
        def __init__(self,n):
            self.n=n
            self.thr=threading.Threading(target=self.run)
            self.thr.daemon=True
            self.thr.start()
        def run(self):
            while self.n>0:
                print('T-minus',self.n)
                self.n-=1
                time.sleep(5)
        def __getstate__(self):
            return self.n
        def __setstate__(self,n):
            self.__init___(n)
    c=countdown.Countdown(30)
    f=open('cstate.p','wb')
    import pickle
    pickle.dump(c,f)
    f.close()
    f=open('cstate.p','rb')
    pickle.load(f)
    ```
    这样线程从上次执行pickle操作时剩下的计数开始执行
    对于大型的数据结构，比如由array模块或numpy库创建的二进制数组，pickle就不是一种特别高效的编码。如果需要一定大量的数组型数据，那么最好简单地将数据按块保存在文件中，或者使用更加标准的编码，比如HDF5(由第三方库支持)
    由于pickle是Python的专有特性，而且同源代码的关联紧密，因此不应该把pickle作为长期存储的格式。如果源代码发生改变，那么存储的所有数据就会失效且变得无法读取。
    要将数据保存在数据库和归档存储中，最好使用一种更加标准的数据编码，比如XML、CSV或者JSON。这些编码格式的标准化程度更高，许多编程语言都支持，而且更能适应于源代码的修改
    pickle模块中有着大量的选项。对于大部分常见的用途，不必担心。如果要构建一个大型的应用，其中要用pickle来做序列化的话，就需要参考官方文档。

## 第6章 数据编码与处理

    利用Python来处理以各种常见编码形式所呈现出的数据，比如CSV文件、JSON、XML以及二进制形式的打包记录。与数据结构不同，将会着重处理数据在程序中的输入和输出问题

### 6.1 读写CSV数据

    对于大部分类型的CSV数据，都可以用csv库来处理。假设在名为stocks.csv的文件中包含有如下的股票市场数据
    Symbol,Price,Date,Time,Change,Volume
        "AA",39.48,"6/11/2007","9:36am",-0.18,181800
        ...
        import csv
        with open('stock.csv') as f:
            f_csv=csv.reader(f)
            headers=next(f_csv)
            for row in f_csv:
                # process row
    在上面的代码中，row将会是一个元组。要访问特定的字段就需要用到索引，比如row[0](表示Symbol)和row[4](表示Change)
    由于这样的索引常常容易引起混淆，可以考虑使用命名元组
        from collections import namedtuple
        import csv
        with open('stock.csv') as f:
            f_csv=csv.reader(f)
            headings=next(f_csv)
            Row=namedtuple('Row',headings)
            for r in f_csv:
                row=Row(*r)
                # process row
    这样就可以使用每一列的标头比如row.Symbol和row.Change来取代之前的索引了。应该要指出的是，这个方法只有在每一列的表头都是合法的Python标识符时才起作用
    如果不是的话，就必须调整原始的标头(如把非标识符字符用下划线或其他类似的符号取代)
    另一种可行的方式是将数据读取为字典序列
        import csv
        with open('stocks.csv') as f:
            f_csv=csv.DictReader(f)
            for row in f_csv:
                # process row
    在这个版本中，可以通过行表头来访问每行中的元素。比如row['Symbol']或者row['Change']
    要写入CSV数据，也可以使用csv模块来完成，但是要创建一个写入对象
        headers=['Symbol','Price','Date','Time','Change',Volume']
        rows=[("AA",39.48,"6/11/2007","9:36am",-0.18,181800)
            ...]
        with open('stocks.csv') as f:
            f_csv=csv.writer(f)
            f_csv.writerow(headers)
            f_csv.writerows(rows)
    如果数据是字典序列，处理方式则为
        with open('stocks.csv') as f:
            f_csv=csv.DictWriter(f,headers)
            f_csv.writeheader()
            f_csv.writerows(rows)

    应该总是选择使用csv模块来处理，而不是自己手动分解和解析CSV数据。
    手动通过spilt的方式，问题在于需要处理一些细节问题。如果有任何字段是被引号括起来的，就要继续去除引号。如果被引用的字段中恰好包含有一个逗号，产生出的那一行会因为大小错误而使得代码崩溃(因为原始数据也是用逗号分隔的)
    默认情况下,csv库被实现为能够识别微软Excel所采用的CSV编码规则。这也许是最为常见的CSV编码规则了，能够带来最佳的兼容性。如果查阅csv的文档，就会发现有几种方法可以将编码微调为其他的格式(如修改分隔字符等)。如果想读取以tab键分隔的数据
        with open('stocks.csv') as f:
            f_tsv=csv.reader(f,delimiter='\t')
            for row in f_tsv:
                # process row
    如果正在读取CSV数据并将其转换为命名元组，那么在验证列标题时要小心。某个CSV文件中可能在标题行中包含有非法的标识符字符，Num=Premises中的-不能用作Python的标识符字符
        Street Adress,Num-Premises,Latitude,Longitude
    这会使得创建命名元组的代码出现ValueError异常。要解决这个问题，应该首先整理标题。可以对非法的标识符字符进行正则替换
        import re
        with open('stocks.csv') as f:
            f_csv=csv.reader(f)
            headers=[re.sub('[^a-zA-Z_]','_',h) for in next(f_csv)]
            Row=namedtuple('Row',headers)
            for r in f_csv:
                row=Row(*r)
                # process row
    csv模块不会尝试去解释数据或者将数据转换为除字符串之外的类型。如果需要转换，则手动进行处理。
        col_types=[str,float,str,str,float,int]
        with open('stocks.csv') as f:
            f_csv=csv.reader(f)
            headers=next(f_csv)
            for row in f_csv:
                row=tuple(convert(value) for convert,value in zip(col_types,row))
    一般来说，对于这样的转换需要小心。CSV文件可能会缺少某些值，或者数据损坏，以及出现其他一些可能会使数据转换操作失败的情况，这都是很常见的。除非可以保证数据不会出错，否则需要考虑这些情况(可能需要加上适当的异常处理代码)
    如果目标是通过读取CSV数据来进行数据分析和统计，Pandas中有个方便的函数pandas.read_csv()，能够将CSV数据加载到DataFrame对象中。就可以生成各种各样的统计摘要，还可以对数据进行筛选并执行其他类型的高级操作。

### 6.2 读写JSON数据

    json模块中提供了一种简单的方法来编码和解码JSON格式的数据。这两个主要的函数就是json.dumps()以及json.loads()。这两个函数在命名上借鉴了其他序列化处理库的接口，比如pickle。将Python数据转换为JSON
        import json
        data={
            'name':'ACME',
            'shares':100,
            'price':542.23
        }
        json_str=json.dumps(data)
    把JSON编码的字符串转换回Python数据结构
        data=json.loads(json_str)
    如果要同文件而不是字符串打交道的话，可以选择使用json.dump()以及json.load()来编码和解码JSON数据
        with open('data.json','w') as f:
            json.dump(data,f)
        with open('data.json','w') as f:
            data=json.load(f)

    JSON编码支持的基本类型有None、bool、int、float和str，以及包含了这些基本类型的列表、元组以及字典。对于字典，JSON会假设键是字符串(字典中任何非字符串键都会在编码时转换为字符串)。要符合JSON规范，应该只对Python列表和字典进行编码。在Web应用中，把最顶层对象定义为字典是一种标准做法
    JSON编码的格式几乎与Python语法一致。True会被映射为true，False会被映射为false，而None会被映射为null。
    如果要检查从JSON中解码得到的数据，仅仅将其打印出来很困难确定数据的结构————尤其是如果数据中包含了深层次的嵌套结构或者有许多字段时。可以考虑使用pprint模块中的pprint()函数。这么做会把键按照字母顺序排列，并且将字典以更加合理的方式进行输出

    ```Python
    # 对网站上的搜索结果以漂亮的格式进行输出
    from urllib.request import urlopen
    import json
    u=urlopen('web')
    resp=json.loads(u.read(),decode('utf-8'))
    from pprint import pprint
    pprint(resp)
    ```
    一般来说，JSON解码时会从所提供的数据中创建出字典或者列表。如果想创建其他类型的对象，可以为json.loads()方法提供object_pairs_hook或者object_hook参数。将JSON数据解码为OrderedDict(有序字典)，这样可以保持数据的顺序不变
        s='{"name":"ACME","shares":50,"price":490.1}'
        from collections import OrderedDict
        data=json.loads(s,object_pairs_hook=OrderedDict)
        data
    将JSON字典转变为Python对象
        class JSONObject:
            def __init__(self,d):
                self.__dict__=d
        data=json.loads(s,object_hook=JSONObject)
        data.name,data.shares,data.price
    这部分代码，通过解析JSON数据而创建的字典作为单独的参数传递给了__init__()。之后可以根据需要使用，如直接将它当作对象的字典实例
    有几个选项对于编码JSON来说很有用。如果想让输出格式变得漂亮些，可以在json.dumps()函数中使用indent参数。这会使得数据能够像pprint()函数那样以漂亮的格式打印出来
        print(json.dumps(data,indent=4))
    如果想在输出中对键进行排序处理，可以使用sort_keys参数
        print(json.dumps(data,sort_keys=True))
    类实例一般是无法序列化为JSON的。
    如果想序列化实例，可以提供一个函数将类实例作为输入并返回一个可以被序列化处理的字典
        def serialize_instance(obj):
            d={'__classname__':type(obj).__name__}
            d.update(vars(obj))
            return d
    如果想取回一个实例

    ```Python
    class Point:
        def __init__(self,x,y):
            self.x=x
            self.y=y
    def unserialize_object(d):
        clsname=d.pop('__classname__',None)
        if clsname:
            cls=classes[clsname]
            obj=cls.__new__(cls)
            for key,value in d.items():
                setattr(obj,key,value)
            return obj
        else:
            return d
    classes={
        'Point':Point
    }
    p=Point(2,3)
    s=json.dumps(p,default=serialize_instance)
    a=json.loads(s,object_hook=unserialize_object)
    a,a.x,a.y
    ```
    json模块中还有许多其他的选项，这些选项可用来控制对数字、特殊值(比如NAN)等的底层解释行为

### 6.3 解析简单的XML文档

    xml.etree.ElementTree模块可用来从简单的XML文档中提取出数据。假设相对Planet Python上的RSS订阅做解析并生成一个总结报告
        from urllib.request import urlopen
        from xml.etree.ElementTree import parse
        u=urlopen('http://planet.python.org/rss20.xml')
        doc=parse(u)
        for item in doc.iterfind('channel/item'):
            title=item.findtext('title')
            date=item.findtext('pubDate')
            link=item.findtext('link')
            print(title)
            print(date)
            print(link)
            print()
    如果想要做更多的处理，就需要将print()函数替换为其他更加有趣的处理函数

    在许多应用中，同XML编码的数据打交道是很常见的事情。这儿不仅是因为XML作为一种数据交换格式在互联网中使用广泛，而且XML还是用来保存应用数据(例如文字处理、音乐库等)的常用格式。
    在许多情况下，XML如果只是简单地用来保存数据，那么文档结构就是紧凑而直接的。前面的RSS订阅源就类似于XML文档
    xml.etree.ElementTree.parse()函数将整个XML文档解析为一个文档对象。然后就可以利用find()、iterfind()以及findtext()方法查询特定的XML元素。这些函数的参数就是特定的标签名称
    当指定标签时，需要整体考虑文档的结构。每一个查找操作都是相对于一个起始元素来展开的。提供给每个操作的标签名也是相对于起始元素的。
    每个由ElementTree模块所表示的元素都有一些重要的属性和方法，它们对解析操作十分有用。tag属性中包含了标签的名称，text属性中包含有附着的文本，而get()方法可以用来提取出属性(如果有的话)
    xml.etree.ElementTree并不是解析XML的唯一选择。对于更加高级的应用，应该考虑使用lxml。lxml采用的编程接口和ElementTree一样。只需要将第一个导入语句修改为from lxml.etree import parse接口。lxml完全兼容于XML标准。lxml运行起来非常快速，还提供验证、XSLT以及XPath这样的功能支持

### 6.4 以增量方式解析大型XML我呢见

    从一个大型的XML文档中提取出数据，而且对内存的使用要尽可能少
    任何时候，当要面对以增量方式处理数据的问题时，都应该考虑使用迭代器和生成器。

    ```python
        from xml.etree.ElementTree import iterparse
        def parse_and_remove(filename,path):
            path_parts=path.split('/')
            doc=iterparse(filename,('start','end'))
            # Skip the root element
            next(doc)
            tag_stack=[]
            elem_stack=[]
            for event,elem in doc:
                if event == 'start':
                    tag_stack.append(elem.tag)
                    elem_stack.append(elem)
                elif event == 'end':
                    if tag_stack == path_parts:
                        yield elem
                        elem_stack[-2].remove(elem)
                    try:
                        tag_stack.pop()
                        elem_stack.pop()
                    except IndexError:
                        pass
    ```
    要测试这个函数，只需要找一个大型的XML文件来配合测试即可。这种大型的XML文件常常可以在政府以及数据公开的网站上找到。
    编写根据坑洞的数量对邮政编码(ZIP code)进行排序的脚本

    ```Python
    from xml.etree.ElementTree import parse
    from collections import Counter
    potholes_by_zip=Counter()
    doc=parse('potholes.xml')
    for pothole in doc.iterfind('row/row'):
        potholes_by_zip[pothole.findtext('zip')]+=1
    for zipcode,num in potholes_by_zip.most_common():
        print(zipcode,num)
    ```
    这个脚本唯一的问题就是它将整个XML文件都读取到内存中后再做解析。进行微小的修改

    ```Python
    from collections import Counter
    potholes_by_zip=Counter()
    data=parse_and_remove('potholes.xml','row/row')
    for pothole in data:
        potholes_by_zip[pothole.findtext('zip')]+=1
    for zipcode,num in potholes_by_zip.most_common():
        print(zipcode,num)
    ```

    示例依赖于ElementTree模块中的两个核心功能。iterparse()方法允许对XML文档做增量式的处理。要使用它，只需提供文件名以及一个事件列表即可。事件列表由1个或多个start/end，start-ns/end-ns组成。iterparse()创建出的迭代器产生出形式为(event,elem)的元组，这里的event是列出的事件，而elem是对应的XML元素
    当某个元素首次被创建但是还没有填入任何其他数据时(比如子元素)，会产生start事件，而end事件会在元素已经完成时产生。start-ns和end-ns事件是来处理XML命名空间声明的
    在实例中，start和end事件是用来管理元素和标签栈的。这里的栈代表着文档结构中被解析的当前层次(current hierarchical)，同时也用来判断元素是否匹配传递给parse_and_ramove()函数的请求路径。如果有匹配满足，就通过yield将其发送给调用者。紧跟在yield之后的语句就是使得ElementTree能够高效利用内存的关键所在
        elem_stack[-2].remove(elem)
    这将之前通过yield产生出的元素从它们的父节点中移除。可假设其再也没有任何其他的引用存在，因此该元素被销毁进而可以回收它所占用的内存
    这种迭代式的解析以及对节点的移除使得对整个文档的增量式扫描变得非常高效。在任何时刻都能构造出一颗完整的文档树。仍然可以编写代码以直接的方式来处理XML数据
    这种技术的主要缺点就是运行时的性能。运行速度会快一倍，但是使用的内存是60多倍

### 6.5 将字典转换为XML

    尽管xml.etree.ElementTree库通常用来解析XML文档，但它同样也可以用来创建XML文档

    ```Python
    from xml.etree.ElementTree import Element
    def dict_to_xml(tag,d):
        '''
        Turn a simple dict of key/value pairs into XML
        '''
        elem=Element(tag)
        for key,val in d.items():
            child=Element(key)
            child.text=str(val)
            elem.append(child)
        return elem
    s={'name':'GOOG','shares':100,'price':490.1}
    e=dict_to_xml('stock',s)
    from xml.etree.ElementTree import tostring
    tostring(e)
    ```
    如果想为元素附加上属性，可以使用set()方法实现
        e.set('_id','1234')
    如果需要考虑元素间的顺序，可以创建OrderedDict来取代普通的字典。

    当创建XML时，也许或倾向于只是用字符串来完成

    ```Python
    def dict_to_xml_str(tag,d):
        '''
        Turn a simple dict of key/value pairs into XML
        '''
        parts=['<{}>'.format(tag)]
        for key,val in d.items():
            parts.append('<{0}>{1}</{0}>'.format(key,val))
        parts.append('</{}>'.format(tag))
        return ''.join(parts)
    ```
    但如果有特殊字符，可能会被取代
    如果需要手工对这些字符做转义处理，可以使用xml.sax.saxutils中的escape()和unescape()函数
    创建Element实例要比使用字符串更为优越，除了可以产生出正确的输出外，可以更加方便地将Element实例组合在一起，创建出更大的XML文档。得到的Element实例也能够以各种方式进行处理。以更高的层面上对数据进行各种处理，最后只需要把结果作为字符串输出

### 6.6 解析、修改和重写XML

    xml.etree.ElementTree模块可以完成这样的任务。从本质上来说，开始时可以按照通常的方式来解析文档。
    采用ElementTree来读取XML文档，并对文档的结构做出修改
        from xml.etree.ElementTree import parse,Element
        doc=parse('pred.xml')
        root=doc.getroot()
        root.remove(root.find('sri'))
        root.remove(root.find('cr'))
        root.getchildren().index(root.find('nm'))
        e=Element('spam')
        e.text='This is a test'
        root.insert(2,e)
        doc.write('newpred.xml',xml_declaration=True)
    这些操作的结果产生了一个新的XML文档
    修改XML文档的结构是简单直接的，但是必须记住所有的修改主要是对父元素继续宁的，我们把它当作是一个列表一样对待。比如说，如果移除某个元素，那么就利用它的直接父结点的remove()方法来完成。如果插入或添加新的元素，同样要使用父结点的insert()和append()方法来完成。这些元素也可以使用索引和切片操作来进行操控，比如element[i]或者是element[i:j]
    如果需要创建新的元素，可以使用Element类来完成

### 6.7 用命名空间来解析XML文档

    如果解析一个使用了命名空间的XML文档，并尝试执行普通的查询操作，所有的步骤都会变得特别冗长啰嗦
        doc.findtext('author')
        doc.find('content')
        doc.find('content/html') #包含命名空间的查询(无效)
        doc.find('content/{http://www.w3.org/1999.xhtml}html')
        doc.findtext('content/{http://www.w3.org/1999.xhtml}html/head/title') #无效
        doc.findtext('content/{http://www.w3.org/1999.xhtml}html/{http://www.w3.org/1999.xhtml}head/{http://www.w3.org/1999.xhtml}title')
    通常可以将命名空间的处理包装到一个通用的类中，这样可以省去一些麻烦

    ```python
    class XMLNamespaces:
        def __init__(self,**kwargs):
            self.namespeces={}
            for name,uri in kwargs.items():
                self.register(name,uri)
        def register(self,name,uri):
            self.namespeces[name]='{'+uri+'}'
        def __call__(self,path):
            return path.format_map(self.namespeces)
    ```
    要使用这个类，可以按照如下方式进行
        ns=XMLNamespaces(html='http://www.w3.org/1999/xhtml')
        doc.find(ns('content/{html}html'))
        doc.findtext(ns('content/{html}html/{html}head/{html}title'))
    对包含有命名空间的XML文档进行解析会非常繁琐。XMLNamespaces类的功能只是用来稍微简化一下这个过程，它允许在后序的操作中使用缩短的命名空间名称，而不必去使用完全限定的URI
    在基本的ElementTree解析器中不存在什么机制能获得有关命名空间
