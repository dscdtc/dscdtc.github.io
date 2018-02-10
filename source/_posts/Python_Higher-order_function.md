---
title: Python高阶函数
copyright: true
password: dscdtc
date: 2018-02-10 11:04:59
---

## `map()`

> `map(f, LIST)`把f(x)作用在list的每一个元素并把结果生成一个新的list

```py
# 求列表值平方
map(lambda x:x*x, [1, 2, 3]);
>>> [1, 4, 9]

# 数字转为字符串
map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> ['1', '2', '3', '4', '5', '6', '7', '8', '9']
```

## `reduce()`

> `reduce()`把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
`reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)`

```py
# [1, 3, 5, 7, 9] => 13579
reduce(lambda x, y: x * 10 + y, [1, 3, 5, 7, 9])
```

## `filter()`

> `filter()`函数用于过滤序列。和`map()``reduce()`类似，filter()也接收一个函数和一个序列。不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。

```py
# 删掉序列中的空字符串
list(filter(lambda x: x and x.strip(), ['A', '', 'B', None, 'C', '  ']))
```

## `sorted(LIST, key=func, reverse=False )`

`sorted()`函数就可以对list进行排序:

```py
sorted([36, 5, -12, 9, -21])
>>> [-21, -12, 5, 9, 36]

sorted([36, 5, -12, 9, -21], reverse=True)
>>> [36, 9, 5, -12, -21]
```

此外，sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，key指定的函数将作用于list的每一个元素上，并根据key函数返回的结果进行排序, 然后sorted()函数按照keys进行排序，并按照对应关系返回list相应的元素。

```py
# 按绝对值大小排序
sorted([36, 5, -12, 9, -21], key=abs)
>>> [5, 9, -12, -21, 36]

# 字符串排序,忽略大小写
sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)
>>> ['about', 'bob', 'Credit', 'Zoo']
```
