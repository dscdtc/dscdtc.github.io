---
title: Python类的属性和方法
copyright: true
password: dscdtc
date: 2018-02-10 10:59:47
---
## Python 内置类属性

| 属性 | 描述 |
| :--: | ----------------------------------- |
| `__dict__` | 类的属性（包含一个字典，由类的数据属性组成） |
| `__doc__` | 类的文档字符串 |
| `__name__` | 类名 |
| `__module__` | 类定义所在的模块（类的全名是`__main__.className`，如果类位于一个导入模块mymod中，那么`className.__module__` == mymod） |
| `__bases__` | 返回一个所有父类组成的元组 |

DEMO:

```py
#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Employee:
    '所有员工的基类'
    empCount = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
    def displayCount(self):
        print "Total Employee %d" % Employee.empCount
    def displayEmployee(self):
        print "Name : ", self.name,  ", Salary: ", self.salary

print "Employee.__doc__:", Employee.__doc__
print "Employee.__name__:", Employee.__name__
print "Employee.__module__:", Employee.__module__
print "Employee.__bases__:", Employee.__bases__
print "Employee.__dict__:", Employee.__dict__
```

输出结果如下：

```py
Employee.__doc__: 所有员工的基类
Employee.__name__: Employee
Employee.__module__: __main__
Employee.__bases__: ()
Employee.__dict__: {'__module__': '__main__', 'displayCount': <function displayCount at 0x10a939c80>, 'empCount': 0, 'displayEmployee': <function displayEmployee at 0x10a93caa0>, '__doc__': '\xe6\x89\x80\xe6\x9c\x89\xe5\x91\x98\xe5\xb7\xa5\xe7\x9a\x84\xe5\x9f\xba\xe7\xb1\xbb', '__init__': <function __init__ at 0x10a939578>}
```

## 类的专用方法

| 方法 | 描述 | 调用 |
| :--: | -----------------|------------------ |
| `__init__(self [,args...])` | 构造函数| `obj = className(args)` |
| `__del__(self)` | 析构方法, 删除一个对象 | `del obj` |
| `__repr__(self)` | 转化为供解释器读取的形式 | `repr(obj)` |
| `__str__(self)` | 用于将值转化为适于人阅读的形式 | `str(obj)`或`print(obj)` |
| `__cmp__(self,other)` | 对象比较 | `cmp(obj, x)`或`obj >\<\== x` |
| `__getitem__(self,other)` | 重定向到字典，返回字典的值 | `obj['dog']` |
| `__setitem__(self,key)` | 重定向到字典，设置字典的值 | `obj['dog']='fuck'` |
| `__delitem__(self,key)` | 重定向到字典，删除字典的值 | `objA + objB` |

```py
#!/usr/bin/python

class Vector:
   def __init__(self, a, b):
      self.a = a
      self.b = b

   def __str__(self):
      return 'Vector (%d, %d)' % (self.a, self.b)

   def __add__(self,other):
      return Vector(self.a + other.a, self.b + other.b)

v1 = Vector(2,10)
v2 = Vector(5,-2)
print v1 + v2

>>> Vector(7,8)
```

## 单下划线、双下划线、头尾双下划线说明：

* `__foo__`: 定义的是特殊方法，一般是系统定义名字 ，类似 `__init__()` 之类的。
* `_foo`: 以单下划线开头的表示的是 `protected` 类型的变量，即保护类型只能允许其本身与子类进行访问，不能用于 `from module import *`
* `__foo`: 双下划线的表示的是私有类型(private)的变量, 只能是允许这个类本身进行访问了。
