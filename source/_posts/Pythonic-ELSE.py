---
title: Pythonic ELSE
tags: [Python]
categories: Python
copyright: true
date: 2018-02-09 16:11:39
---

> 我们都知道 Python 中 else 的基本用法是在条件控制语句中的 `if...elif...else...`，但是 else 还有两个其它的用途，一是用于循环的结尾，另一个是用在错误处理的 try 中。

<!-- more -->

# 循环中的 else -- `for/while...else`

> 跟在循环后面的 else 语句只有在当循环内没出现 break，也就是正常循环完成时才会执行。

先看一个可能遇到的小坑~ 猜猜看会输出啥。

```py
for i in range(10):
    if i == 5:
        print 'found it! i = %s' % i
else:
    print 'not found it ...'
```
打印出来的结果为：

```py
found it! i = 5
not found it ...
```

显然这不是我们期望的结果。应改为:

```py
for i in range(10):
    if i == 5:
        print 'found it! i = %s' % i
        break  # 在for循环中含有break时则直接终止循环，不会执行else子句
else:
    print 'not found it ...';
```

再来看一个插入排序法的例子：

```py
from random import randrange
def insertion_sort(seq):
  if len(seq) <= 1:
    return seq
  _sorted = seq[:1]
  for i in seq[1:]:
    inserted = False
    for j in range(len(_sorted)):
      if i < _sorted[j]:
        _sorted = [*_sorted[:j], i, *_sorted[j:]]
        inserted = True
        break
    if not inserted:
      _sorted.append(i)
return _sorted
print(insertion_sort([randrange(1, 100) for i in range(10)]))

>>> [8, 12, 12, 34, 38, 68, 72, 78, 84, 90]
```

在这个例子中，对已排序的 _sorted 元素逐个与 i 进行比较，若 i 比已排序的所有元素都大，则只能排在已排序列表的最后。这时我们就需要一个额外的状态变量 inserted 来标记完成遍历循环还是中途被 break，在这种情况下，我们可以用 else 来取代这一状态变量：

```py
from random import randrange
def insertion_sort(seq):
  if len(seq) <= 1:
    return seq
  _sorted = seq[:1]
  for i in seq[1:]:
    for j in range(len(_sorted)):
      if i < _sorted[j]:
        _sorted = [*_sorted[:j], i, *_sorted[j:]]
        break
    else:
      _sorted.append(i)
  return _sorted
print(insertion_sort([randrange(1, 100) for i in range(10)]))

>>> [1, 10, 27, 32, 32, 43, 50, 55, 80, 94]
```

`while...else`

```py
while False:
  print("Will never print!")
else:
  print("Loop failed!")

>>> Loop failed!
```

# 错误捕捉中的 else -- `try...except...else...finally`

> 流程控制语法用于捕捉可能出现的异常并进行相应的处理，其中 except 用于捕捉 try 语句中出现的错误；而 else 则用于处理没有出现错误的情况；finally 负责 try 语句的”善后工作“ ，无论如何都会执行。

```py
def divide(x, y):try:
    result = x / y
  except ZeroDivisionError:
    print("division by 0!")
  else:
    print("result = {}".format(result))    
  finally:
    print("divide finished!")
divide(5,2)
print("*"*20)
divide(5,0)
result = 2.5

>>>
divide finished!
********************
division by 0!
divide finished!
```

当然，也可以用状态变量的做法来替代 else：

```py
def divide(x, y):
  result = None
  try:
    result = x / y
  except ZeroDivisionError:
    print("division by 0!")    
  if result is not None:
    print("result = {}".format(result))
  print("divide finished!")
divide(5,2)
print("*"*20)
>>>
divide(5,0)
result = 2.5
divide finished!
********************
division by 0!
divide finished!
```
