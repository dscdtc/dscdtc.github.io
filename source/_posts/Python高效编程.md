---
title: Python高效编程
copyright: false
date: 2018-01-20 17:17:52
---
# 记录实际编程和面试都会遇到的典型问题。

<!-- more -->

## 在列表,字典,集合中根据条件筛选数据

```py
from random import randint
from timeit import timeit
​
data = [randint(-10,10) for _ in range(10)]

filter(lambda x:x >= 0,data)
#首选列表解析 时间比filter少一半左右
[x for x in data if x >= 0]
​
data = {x:randint(60,100) for x in range(1,21)}
{k:v for k,v in data.items() if v > 90}
​
data = set(data)
{x for x in data if x%3==0}
```

## 为元组/列表中每个元素命名,提高程序的可读性

```py
#第一种
NAME,AGE,SEX,EMAIL = range(4)
student = ('Jan',14,'male','jan@jan.net')
print(student[NAME])

#第二种
from collections import namedtuple
Student = namedtuple('Student',['name','age','sex','email'])
student= Student('Jan',14,'male','jan@jan.net')
print(student[NAME])
student.age
isinstance(student,tuple)
```

## 统计序列中元素的出现频度

```py
from random import randint
data = [randint(1,10) for x in range(20)]
c = dict.fromkeys(data,0)

#第一种
for x in data:
    c[x]+=1

#第二种
from collections import Counter
c2 = Counter(data)
#出现频度最高的三个
c2.most_common(3)

#统计一篇文章中单词出现次数
import re
#导入Python之禅
import this
c3 = Counter(re.split('\W+',this.s))
```

## 根据字典中值的大小,对字典中的项排序

```py
from random import randint
data = {x:randint(60,100) for x in 'abcdefg'}
#sorted(data.values())

#第一种
t = zip(data.values(),data.keys())
sorted(t)

#第二种
sorted(data.items(),key=lambda x: x[1])
```

## 快速找到多个字典中的公共键(key)

```py
from random import randint,sample

s1 = {x: randint(1,4) for x in sample('abcdefgh',randint(3,6))}
s2 = {x: randint(1,4) for x in sample('abcdefgh',randint(3,6))}
s3 = {x: randint(1,4) for x in sample('abcdefgh',randint(3,6))}

#第一种
res = []
for k in s1:
    if k in s2 and k in s3:
        res.append(k)

#第二种
from functools import reduce

s1.keys()&s2.keys()&s3.keys()
map(dict.keys,[s1,s2,s3])
reduce(lambda a, b:a & b,map(dict.keys,[s1,s2,s3]))
```

## 实现用户的历史记录功能(最多n条)

```py
from collections import deque
from random import randint

N = randint(0,100)
# 一个容纳5个值的队列
history = deque([],5)

def guess(k):
    if k == N:
        print('right!')
        return True
    if k < N:
        print('%s is less than N'%k)
    else:
        print('%s is greater than N'%k)
    return False

while True:
    input_number = input('please input a number: ')
    if input_number.isdigit():
        k = int(input_number)
        history.append(k)
        if guess(k):
            break
    elif input_number == 'history':
        print(list(history))
```

## 将多个小字符串拼接成一个大字符串

```py
#第一种(拼接项少) +
#第二种(拼接项多) ''.join()
list1 = ['abc','123','23','sdsa','xyz']
''.join(list1)

list2 = ['abc',123,'23',4654,'xyz']
''.join(str(x) for x in list2)
```

## 对字符串进行左,右,居中对齐

```py
s = 'abc'
#第一种 ljust() rjust() center()
s.ljust(20)
s.rjust(20,'!')
s.center(20,"-")

#第二种 format
format(s,'<20')
format(s,'>20')
format(s,'^20')
```

## 设置文件的缓冲

```py
# 全缓冲
# 默认是4096
f = open('demo.txt','w',buffering=2048)
f.write('-' * 2048)
f.write('+')
# 行缓冲
f = open('demo1.txt','w',buffering=1)
# 无缓冲
f = open('demo2.txt','w',buffering=0)
```

## 为创建大量实例节省内存

```py
class Player(object):
    def __init__(self,uid,name,status=0,level=1):
        self.uid = uid
        self.name = name
        self.status = status
        self.level = level
        
class Player2(object):
    __slots__ = ['uid','name','status','level']
    def __init__(self,uid,name,status=0,level=1):
        self.uid = uid
        self.name = name
        self.status = status
        self.level = level       

p1 = Player('001','uu')
p2 = Player2('001','uu')
set(dir(p1)) - set(dir(p2))
# p1比p2多了{'__dict__', '__weakref__'}
# '__dict__'可以动态绑定
p1.x = 123
del p1.__dict__['x']

import sys
# 占用了320内存
sys.getsizeof(p1.__dict__)

# p2事先定义__slots__ 声明了实例属性名字的列表
# p2就无法动态绑定 从而节省了内存
# p2.x = 123
```

作者：dreamkong
链接：https://juejin.im/post/5a30ffa351882506fd588b3f
来源：掘金
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
