---
title: Python中的天坑--dict
copyright: true
password:
date: 2018-01-17 17:22:34
---

> Python中的字典是无序的(不能人为重新排序):</br>
>（1）键值的哈希碰撞，hash(key1) == hash(key2)时，向字典里连续添加的这个两个键的顺序是不可以控制的，也是无法做到连续的，后来的键会按算法调整到其它位置。</br>
>（2）字典空间扩容，当键的数量超过字典默认开的空间时，字典会做空间扩容，扩容后的键顺和创建顺序就会发生变化，不受人为控制。
<!-- more -->

# 有序字典实现方案

## 1 采取对list/tuple内部元素命名的方法来代替dict

```py
# Method1[推荐写法]
NAME,AGE,SEX,EMAIL = xrange(4) # py3中使用range(4)
student = ('Jan',14,'male','jan@jan.net')
#student = ['Jan',14,'male','jan@jan.net']
print(student[NAME])

# Method2
from collections import namedtuple
Student = namedtuple('Student',['name','age','sex','email'])
student= Student('Jan',14,'male','jan@jan.net')
print(student[NAME])
student.age
isinstance(student,tuple)
```

## 2 sorted()函数排序

```py
my_dict={"cc":100,"aa":200,"bb":10}

# 按key升序, 返回元组列表
print(sorted(my_dict.items(),key=lambda x:x[0]))
>>>[('aa', 200), ('bb', 10), ('cc', 100)]

# 按value降序, 返回元组列表
print(sorted(my_dict.items(),key=lambda x:x[1], reverse=True))
>>>[('aa', 200), ('cc', 100), ('bb', 10)]
```

## 3 使用标准库collections中的`OrderedDict()`

```py
from collections import OrderedDict
orderDict=OrderedDict()
orderDict['a']=1
orderDict['b']=2
orderDict['c']=3
print(orderDict)

>>>OrderedDict([('a', 1), ('b', 2), ('c', 3)])
# 原生dict:如果让orderDict=dict(),则会输出
# >>>{'a': 1, 'c': 3, 'b': 2}
```

> *OrderedDict()虽然是好东西，但是它内部维护了一个双向链表,若数据量很大的话，会非常消耗内存.*

# 字典的Pythonic技巧

* 提取部分子集

```py
#提取分数超过90分的学生信息，并变成字典
students_score={'jack':80, 'james':91, 'leo':100, 'sam':60}
good_score={name:score for name,score in students_score.items() if score>90}
print(good_score)
>>>{'james': 91, 'leo': 100}
```

* 字典中的最值

```py
stocks={'wanke':25.6,'wuliangye':32.3,'maotai':299.5,'huatai':18.6}
print(min(stocks.values()))
>>> 18.6
print(max(stocks.values()))
>>> 299.5
```

使用`zip()`进行翻转

```py
stocks = {'wanke':25.6,'wuliangye':32.3,'maotai':299.5,'huatai':18.6}
new_stocks = zip(stocks.values(), stocks.keys())
```

# 字典的方法们

* `get()`
  > 字典的取值: 一种是使用直接key的方式来进行读取，也就是dict[key]，当key不存在的时候，会发生KeyError的异常(良好的代码，一定是要考虑健壮性,切记)。另外一种则使用get的方式，当使用get方法的时候，默认情况下返回的None，如果key存在，那么就会返回这个key对应的值。</br>
  > **[建议]:尽量用dict.get()来代替dict[key]**

  ```py
  print(prices.get('peach'))
  >>> None
  print(prices.get('apple'), 'Not Found')
  >>> 10
  print(prices.get('peach'), 'Not Found')
  >>> Not Found
  ```

* `pop()`
  > 获取并删除键值对

  ```py
  d = {'name': 'kel'}
  d.pop('name')
  >>> 'kel'
  d.pop('kel')
  >>> Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    KeyError: 'kel'
  # 使用默认值，则不会在键不存在的时候出现异常
  d.pop('kel','key is not exist')
  >>> 'key is not exist'
  ```

* `setdefault()`
  > setdefault方法主要是用来设置字典的键值，当一个键存在的时候，直接使用已经存在的值，当键不存在的时候，那么就添加一个值。

  ```py
  d = {'name': 'kel'}
  d.setdefault('kel','person')
  >>> 'person'
  d
  >>> {'kel': 'person', 'name': 'kel'}

  d.setdefault('kel','animal')
  >>> 'person'
  d
  >>> {'kel': 'person', 'name': 'kel'}
  ```

  > 当字典中的值是列表的时候，那么就可以使用方法`d.setdefault('key',[]).append(somevalue)`
  ```py
  d.setdefault('abc',[]).append('123')
  d
  >>> {'kel': 'person', 'name': 'kel', 'abc': ['123']}
  ```
  > 当值不能重复的时候，可以使用set集合`d3.setdefault('key',set()).add(somevalue)`

* `fromkeys()`
  > 创建具有默认值的字典
  ```py
  dict.fromkeys(('age','name'), None)
  >>> {'age': None, 'name': None}
  ```

  > 创建字典的另外两种方式:
  ```py
  d = dict(name='kel',age=32) # 键名不能是关键字且必须符合变量命名
  d = {'name':'kel','age':32}
  ```

* `dict1.update(dict2)`
  > 把字典dict2的键/值对更新到dict1里
  ```py
  dict1 = {'Name': 'Zara', 'Age': 7}
  dict2 = {'Sex': 'female', 'Age': 666}
  dict1.update(dict2)
  dict1
  >>> {'Age': 666, 'Name': 'Zara', 'Sex': 'female'}
  ```

  ```py
  >>> dict1 = {'Name': 'Zara', 'Age': 7}
  >>> dict2 = {'Sex': 'female', 'Age':65536}
  >>> dict1.update(dict2)
  >>> dict1
  {'Age': 65536, 'Name': 'Zara', 'Sex': 'female'}
  ```

* `dict.has_key(key)`
  > 如果键在字典dict里返回true，否则返回false

* `values()`
  > 返回包含字典中所有值的列表

* `keys()`
  > 返回包含字典中所有键的列表
