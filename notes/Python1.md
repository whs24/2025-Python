

# <center>Python程序设计
##### <center>五毫升

> &emsp;&emsp;Python 作为当下极具影响力的编程语言，其重要性体现在语法简洁易读，新手能快速入门，且拥有庞大的库生态，像 numpy、tensorflow 等库覆盖数据处理、机器学习等多领域，大幅提升开发效率；它具备跨平台兼容性，代码可在不同系统部署，动态类型特性也让编程更灵活。
> &emsp;&emsp;从应用看，它深度渗透数据分析、人工智能、Web 开发、自动化运维、网络爬虫等众多行业，是数据科学家处理科研与企业数据的利器，也是 AI 领域主流框架的核心接口，还能通过 Django 等框架构建各类 Web 应用，更可用于编写脚本实现系统自动化任务，堪称连接技术与行业需求的 “万能工具”，在技术演进和产业实践中都占据着不可替代的关键地位。
## 一、Python基础及语法

### 1.为什么介绍Python？
- 掌握接受其他新语言的能力
- 熟悉其他类型语言
- 增强解决问题的能力
- **解释型语言（代码 → Python解释器 → 执行）**

### 2.什么是Python？
- 创始人 Guido van Rossum
- 大蟒蛇
- *Python 3.0 与之前的版本不兼容*

### 3.Python优点
**为什么用Python？**
- 简单易学
- 代码优美
- 轻量级开发工具
- 类库丰富

**强类型**：除了强制转换，数据类型不可改变
**动态类型**：运行期间数据类型检查
**解释性**：边翻译边执行，运行速度慢
**脚本语言**

**框架与类使用**：网页框架（Flask），数据计算（numpy），普通框架（Requests）
**IDE**:Pycharm、IDLE、Ulipad、Vim、Emacs


### 4.Python语法

>- 数据类型
>- 变量
>- 函数
>- 控制流语句
>- 类库、包

#### (1) 数据类型
**①数值类型**
- 整数
- 长整数（2.0）
- 浮点数
- 复数
- 布尔类型
*运算符同 C++*  
*eval用来计算表达式结果*



**②字符类型**
- 字符串：三种引号赋值均可
 *str() 与 repr()*
&emsp;  str() ——人可以读懂的字符串
&emsp; &emsp;&emsp;  &emsp; *一般用于整数和浮点数*
&emsp;  repr() ——解释器识别的字符串
&emsp; &emsp; &emsp; &emsp; *一般用于对象*


*操作：*

可以用加法和乘法
从0开始，开括号
-1代表最后一个字符
不可修改
```
s[0]
s[0:4]
s[5:]
s[6:-1]
```
*函数*：
- count （实例化）出现次数
- len 字符串长度
- rjust 右对齐填充
- ljust 左对齐填充
- upper/lower 大小写
- split 切分
- join 连接
- find rfind index rindex 查找（子串匹配算法）
- replace 替换
- isdigit(),islower(),isupper() 检测是否只有数字/小写/大写
- strip(),lstrip(),rstrip() 处理头尾、头、尾 去除空白字符
- title() 首字母大写
- encode,decode 转换为unicode
```
s.count('word') // 实例化（成员函数）
```
*格式化方法*：
- %s: string (uses function 'str')
- %r: string (uses function 'repr')
- %i: int
- %f, %e, %g: float


**③列表类型**：

**List**
```
shoplist = ['apple', 'mango', 'carrot', 'banana']
shoplist[1] -> 'mango'
shoplist*2 -> ['apple', 'mango', 'carrot', 'banana', 'apple', 'mango', 'carrot', 'banana']
shoplist+['papaya'] -> ['apple', 'mango', 'carrot', 'banana', 'papaya']

for item in shoplist:
    print (item)    //遍历
```
*列表方法：*
- append(value), extend
- insert(index, value)
- remove (value) 删除 
- index(value) 搜索
- reverse() 倒转
- sort () 排序
```
r.append(['1', '2'])     [r, ['1', '2']]

```
对于列表、字典等类型（不包含数值类型和字符串类型）:
_**赋值代表引用，而不是拷贝!**_
```
>>> a = [1, 3, 2]
>>> b = a     //引用
>>> c = b[0:2]
>>> d = b[:]  //赋值
```
相等性比较
```
>>> a = [1, 2]
>>> b = [1, 2]
>>> a == b        # test whether values are equal
True
>>> a is b        # is用于判断两个变量引用对象是否为同一个，就是所引用的对象的内存地址是否一致
False
```


**④元组类型:**
**tuple**
和list 类似，但是不能修改
zoo = ('wolf', 'elephant', 'penguin')
可以嵌套定义：
       new_zoo = ('monkey', 'dolphin', zoo)
元组没有方法
List转换为tuple：
```
l=[1,2,3]
t=tuple(l)  ->  (1,2,3)
l=list(t)   ->  [1,2,3]
```

**⑤字典类型：**
**Dictionary**
Key/value对
```
d = {  'Swaroop'  : 'swaroopch@byteofpython.info',
                'Larry' : 'larry@wall.org',
                'Matsumoto' :'matz@ruby-lang.org',
                'Spammer':'spammer@hotmail.com'}
```

查找key值     ```d['Larry' ]=  'larry@wall.org'```
查找key       ``` d.has_key('Larry') = True```
添加           ```   d['lucy']='lucy@gmail.com'```
删除            ```  del d['Larry' ]```

*常用方法：*
- len()
- Keys()
- Values()
- Items()
- clear()
- copy()
- deepcopy()

**⑥集合类型：**
**Set**
set类似是数学里的集合概念
可以具有任意数量的项目，并且可以具有不同的类型（整数，浮点数，元组，字符串等）
与list，tuple不同的地方是，set更加强调的是一种“*从属关系*”，
跟顺序无关，所以**有重复的元素会先排除**
set类型的创建：集合创建用花括号 { } 或者 set() 函数

*方法：*
- **set.add(元素)**   向set集合中添加元素
- **set1.update(set2)** 将集合set2更新到集合set1中
- **set.pop()** 随机选一个元素删除并将这个值返回。
pop()不能有参数，否则报错。如果set是空的了,也报错 
- **set.remove(obj)** 删除指定元素obj,该元素必须是set中的元素,否则就报错
- **set.discard(obj)** 删除指定元素obj，obj如果是set中的元素,就删除,如果不是,就什么也不做 
- **set.clear()** 清空集合中的所有元素，得到空集合

**⑦类型转换**：
```
typename(x) 
```



#### (2) 变量与语句

#### 1. 变量：

**标识符的第一个字符**
- 必须是字母表中的字母（大写或小写）
- 或者一个下划线（‘ _ ’）
  
**标识符名称的其他部分**
- 可以由字母（大写或小写）
- 下划线（‘ _ ’）
- 数字（0-9）组成
  
**标识符名称是对大小写敏感的**
- 例如，myname和myName不是一个标识符。
- 有效标识符：I  _my_name name_23  a1b2_c3
- 无效标识符：2things、this is spaced out my-name

#### 2. 语句：

**逻辑行与物理行**
i = 5         &emsp;&emsp;&emsp;&emsp;&emsp;  *逻辑行*
print (i) 

i = 5； print (i) ;   *物理行*

**缩进**

同一层次的语句必须相同的缩进
i=5
&emsp; j=6  *错误*
*建议一致TAB或者SPACE*


#### 3. 控制流:

**If 语句**
```
if a==b:
elif a>=b:
else:
```
**While语句**
```
while i<2:
```
**For语句**
```
for i in [1,2,3,4,5]:
for c in ‘hello python':
```
**Break语句**
```
while true:
If s==2: 
break
```
**Continue语句**
```while true:
If s==2: 
continue
```
**断行**
```
使用\
if a_complicated_expression and \
 another_complicated_expression:
    print ('this is valid syntax')
使用()
if (a_complicated_expression and 
another_complicated_expression):
    print ('this is valid syntax')

```


#### (3) 函数
**函数定义**
```		
                  def sum(a,b) :
   			return a+b
```
**函数调用**
```
		func = sum （函数也可以赋值）
		r = func(5,6)
```
**传参**

###### 参数个数固定：
```
  def add(a,b): 
     return a+b 

  r=add(1,5)
  print (r) -> 6
  ```
###### 默认参数：
```
def say(message, times = 1):
    print (message * times)

say('World', 5) -> 'WorldWorldWorldWorldWorld'
```
###### 关键参数：
*根据参数的名字进行参数传递*
```
def func(a, b=5, c=10)：
    print ('a is', a, 'and b is', b, 'and c is', c)

func(3, 7) -> a=3, b=7, c=10
func(25, c=24) -> a=25, b=5, c=24
func(c=50, a=100) ->  a=100, b=5, c=50
```
###### 元组参数：
*args可以代表多个参数*
```
def noargs(a, *args):
	print ("a=%s, others=%s" % (a, args))

noargs("hello", 1, 2, 3, "python", "good")
输出:
            a=hello, others=(1, 2, 3, 'python', 'good')
```
###### 字典参数：
```
def keyword_args(a, b='bla', **kwargs):
    return "a=%s, b=%s, kwargs=%s" % (a, b, str(kwargs))

keyword_args(c='call', d=12, a='gr')
输出：
		    a=gr, b=bla, kwargs={'c': 'call', 'd': 12}

```
###### 规则：
- 默认参数必须在非默认参数之后
- 只能用一个元组参数和一个字典参数
- 元组参数必须在默认参数之后（*arg）
- 字典参数必须在最后（**arg）

**Lambda函数**

Lambda 定义单行最小函数
作用类似于宏定义
```
g = lambda x: x*2
g(3) = 6

(lambda x,y:x+y)(2,3) -> 5
```
**局部变量**
局部变量作用域 – 函数体内部

*不可变对象：Number ,String , Tuple，bool*
*可变对象： List , Set , Dictionary是可以改变内部的元素*
```
def test_local(a, r):
    print ('local original ', a, r)
    a = 12
    r[1] = 999
    print ('local changed  ', a, r)

a = -5
r = [0, 1, 2]
print ('global original', a, r)
test_local(a, r)
print ('global changed ', a, r)

输出结果:
global original -5 [0, 1, 2]
local original  -5 [0, 1, 2]
local changed   12 [0, 999, 2]
global changed  -5 [0, 999, 2]
```
**全局变量**
```
def func():
	global x
	print ('x is', x)
	x = 2
	print ('Changed local x to', x)
x = 50
func()
print( 'Value of x is', x )
```
**Return语句**
def maximum(x, y):
    if x > y:
        return x
    else:
        return y
print (maximum(2, 3) )

#### (4) 包

**包机制**
```
a.py
def sum(a,b):
    return a+b;


b.py
from a import sum
Print ("3+2=",sum(3,2))
```
*DocStrings-文档字符串*
使得程序更加易懂：函数的第一逻辑行字符串是该函数的文档字符串DocStrings
调用：help(printMax)，或print (printMax.__doc__ )

创建自己的包
```
def sayhi():
	print ('Hi, this is mymodule speaking. ’)
version = '0.1'

from mymodule import sayhi, version
	sayhi()
	print ('Version', version )
```