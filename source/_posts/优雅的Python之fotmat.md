---
title: Python 优雅编程之 str.format()
date: 2017-12-21 09:18:50
tags: [Python]
categories: Python
---
# Python 优雅编程之 str.format()

![Python format()](https://dn-mhke0kuv.qbox.me/cff238212709802d1a16.png?imageView2/1/w/1304/h/734/q/85/format/webp/interlace/1)
<!--more-->

## 1 str.format 的引入

在 Python 中，我们可以使用 + 来连接字符串，在简单情况下这种方式能够很好的工作。但是当我们需要进行复杂的字符串连接时，如果依然使用 + 来完成，不仅会使代码变得晦涩难懂，还会让代码变得难以维护，此时这种方式就显得力不从心了。

例如，我们想打印这样一条记录：

`User:John has completed Action:payment at Time:13:30:00`
如果使用加号实现，会是下面这种形式：

```py
print "User:" + user_name + " has completed Action:" + \
            action_name + " at Time:" + current_time
```

如果以后回过头来阅读这段代码，我们很难直观看出它的输出格式，且修改起来也相对麻烦。

我们可以换用 % 来实现：

```py
print "User:%s has completed Action:%s at Time:%s" % \
        (user_name, action_name, current_time)
```

这回代码变得清晰简洁多了。

不过，Python 为我们提供了另一种简洁优雅的实现方式，也是官方更加推荐的方式：使用 str.format() 来实现字符串的格式化：

```py
print "User:{} has completed Action:{} at Time:{}".format(
        user_name, action_name, current_time)
```

`str.format()` 既能够用于简单的场景，也能够胜任复杂的字符串替换，而无需繁琐的字符串连接操作。Python 的内置类型 str 和 unicode 均支持使用 str.format() 来格式化字符串。

我们接下来就详细地讨论 str.format() 的具体用法。

## 2 str.format 基本语法

格式化字符串使用花括号 &#123;&#125; 来包围替换字段，也就是待替换的字符串。而未被花括号包围的字符会原封不动地出现在结果中。

### 2.1 使用位置索引

以下两种写法是等价的：

```py
"Hello, {} and {}!".format("John", "Mary")

"Hello, {0} and {1}!".format("John", "Mary")
```

花括号内部可以写上目标字符串的索引，也可以省略。如果省略，则按 format 括号里的目标字符串顺序依次替换。

### 2.2 使用关键字索引

除了通过位置来指定目标字符串，我们还可以通过关键字来指定它。

例如：

`"Hello, {boy} and {girl}!".format(boy="John", girl="Mary")`
使用关键字索引的好处是，我们无需关心参数的位置，且字符串的最终结果能够一目了然。在以后的代码维护中，我们能够快速地修改对应的参数，而不用对照字符串挨个去寻找相应的参数。

注意：如果字符串本身含有花括号，则需要将其重复两次来转义。例如，字符串本身含有 {，为了让 Python 知道这是一个普通字符，而不是用于包围替换字段的花括号，我们只需将它改写成 &#123;&#123; 即可。

## 3 str.format 高级语法

str.format 非常强大，足以完成日常工作中遇到的格式化输出。熟练掌握该方法，能够为以后的字符串处理打好基础，还能节省不少时间。

### 3.1 访问参数的属性或元素

在使用 str.format 来格式化字符串时，我们通常将目标字符串作为参数传递给 format 方法。实际上，我们还可以在格式化字符串中访问参数的某个属性或某个元素：

```py
"My car is {0.color}.".format(black_car)
"The first student is {student[0]}.".format(student=stu_list)
"John is {d[john]} years old.".format(d=age_dict)
```

### 3.2 参数输出转换

参数的字符串输出，默认是由其自身的 __format__ 方法来实现的。也就是说，Python 使用参数的 __format__ 输出来取代替换字段。如果我们想调用 str() 或 repr() 来转换参数，可以通过添加 转换标志 来实现：

```py
#call str() on argument
"It's a {0!s}."

#call repr() on argument
"We can get info from {name!r}."
```

## 4 str.format 一般形式

格式化字符串的一般形式如下：

`"... {field_name!conversion:format_spec} ..."`
从上面的代码可以看到，格式化字符串可分为 field_name、conversion、format_spec 三部分，分别对应替换字段名称（索引）、转换标志、格式描述。其中，字段名称是必选的，而后两者是可选的。转换标志紧跟在英文感叹号后面，而格式描述紧跟在英文冒号后面。

前面已经提到过，字段名称既可是位置索引，也可是关键字索引。字段名称后面可以通过点来访问属性，或通过方括号来访问元素。

在这里，我们重点看一下格式描述（format_spec）这一项。

格式描述中含有6个选项，分别是 fill、align、sign、width、precision、type。
它们的位置关系如下：

`[[fill]align][sign][#][0][width][,][.precision][type]`

> fill

可以是任意字符，默认为空格。

> align

仅当指定最小宽度时有效。

* < 左对齐(默认选项)
* \> 右对齐
* = 仅对数字有效；将填充字符放到符号与数字间，例如 +0001234
* ^ 居中对齐

> sign 仅对数字有效

* \+ 所有数字均带有符号
* \- 仅负数带有符号（默认选项）
* 空格；正数前面带空格，负数前面带符号
* \'#' 只对整数有效,自动在二进制、八进制、十六进制数值前添加对应的 0b、0o、 0x。
* ',' 自动在每三个数字之间添加 , 分隔符。

* width 十进制数字，定义最小宽度。如果未指定，则由内容的宽度来决定。

* 如果没有指定对齐方式（align），那么可以在 width 前面添加一个0来实现自动填充0，等价于 fill 设为 0 并且 align 设为 =。

> precision
用于确定浮点数的精度，或字符串的最大长度。不可用于整型数值。
> type
确定参数类型，默认为 s ，即字符串。
> 整数输出类型：
* b：以二进制格式输出
* c：将整数转换成对应的 unicode 字符
* d：以十进制输出（默认选项）
* o：以八进制输出
* x：以十六进制小写输出
* X：以十六进制大写输出
* n：与 d 相同，但使用当前环境的分隔符来分隔每3位数字

> 十进制浮点数输出类型：

* e：指数标记；使用科学计数法输出，用e来表示指数部分，默认 precision 为6
* E：与 e 相同，但使用大写 E 来表示指数部分
* f：以定点形式输出数值，默认 precision 为6
* F：与 f 相同
* g：通用格式；对于给定的 precision p >= 1，取数值的p位有效数字，并以定点或科学计数法输出（默认选项）
* G：通用格式；与 g 相同，当数值过大时使用 E 来表示指数部分
* n：与 g 相同，但使用当前环境的分隔符来分隔每3位数字
* %：百分比标记；使用百分比的形式输出数值，同时设定 f 标记

## 举个栗子>>>

　　它通过&#123;&#125;和:来代替传统%方式

> 1、使用位置参数

要点：从以下例子可以看出位置参数不受顺序约束，且可以为{},只要format里有相对应的参数值即可,参数索引从0开，传入位置参数列表可用*列表

```py
>>> li = ['hoho',18]
>>> 'my name is {} ,age {}'.format('hoho',18)
'my name is hoho ,age 18'
>>> 'my name is {1} ,age {0}'.format(10,'hoho')
'my name is hoho ,age 10'
>>> 'my name is {1} ,age {0} {1}'.format(10,'hoho')
'my name is hoho ,age 10 hoho'
>>> 'my name is {} ,age {}'.format(*li)
'my name is hoho ,age 18'
```

> 2、使用关键字参数

要点：关键字参数值要对得上，可用字典当关键字参数传入值，字典前加**即可

```py
>>> hash = {'name':'hoho','age':18}
>>> 'my name is {name},age is {age}'.format(name='hoho',age=19)
'my name is hoho,age is 19'
>>> 'my name is {name},age is {age}'.format(**hash)
'my name is hoho,age is 18'
```

> 3、填充与格式化

`:[填充字符][对齐方式 <^>][宽度]`

```py
>>> '{0:*>10}'.format(10)  ##右对齐
'********10'
>>> '{0:*<10}'.format(10)  ##左对齐
'10********'
>>> '{0:*^10}'.format(10)  ##居中对齐
'****10****'
```

> 4、精度与进制

```py
>>> '{0:.2f}'.format(1/3)
'0.33'
>>> '{0:b}'.format(10)    #二进制
'1010'
>>> '{0:o}'.format(10)     #八进制
'12'
>>> '{0:x}'.format(10)     #16进制
'a'
>>> '{:,}'.format(12369132698)  #千分位格式化
'12,369,132,698'
```

> 5、使用索引

```py
>>> li
['hoho', 18]
>>> 'name is {0[0]} age is {0[1]}'.format(li)
'name is hoho age is 18
```
