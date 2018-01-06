---
title: re踩坑之旅
date: 2017-12-27 18:34:11
tags: [Python]
categories: Python
---
# re踩坑之旅

> 正则表达式(regular expression)描述了一种字符串匹配的模式（pattern）, 可以用来检查一个串是否含有某种子串、将匹配的子串替换或者从某个串中取出符合某个条件的子串等.
<!-- more -->

## re中的方法们

| 参数    | 描述 |
| :-----: | ----------------------------------- |
| pattern | 匹配的正则表达式(模式字符串) |
| string  | 要被查找替换的原始字符串 |
| flags   | 标志位, 控制正则表达式的匹配方式 |
| repl    | 替换的字符串, 也可为一个函数 |
| count   | 替换的最大次数, 默认0, 表示替换所有的匹配 |

| 修饰符(flag) | 全称 | 描述 |
| :----------: | :--------: | -------------------------------------- |
| re.I | IGNORECASE | 使匹配对大小写不敏感 |
| re.L | LOCALE | 本地化识别, 让\w, \W, \b, \B,取决于当前语言设置 |
| re.M | MULTILINE | 多行匹配, 影响 ^ 和 $ |
| re.S | DOTALL | 使 . 匹配包括换行在内的所有字符 |
| re.X | VERBOSE | 匹配时忽略pattern中的空白符, 使你可以为正则表达式添加注释 |
| re.U | UNICODE | 根据Unicode字符集解析字符, 这个标志影响 \w, \W, \b, \B |

* 字符串匹配

  * `re.match(pattern, string, flags=0)`
    > 如果在*字符串的开头*的零个或更多字符匹配正则表达式模式, 将返回相应的MatchObject实例.返回None则该字符串中与模式不匹配；**即使在多行模式下, re.match()将只匹配字符串的开头, 而不是在每个行的开头**.

  * `re.search(pattern, string, flags=0)`
    > 寻找的*第一个由该正则表达式模式产生匹配的位置*, 并返回相应的MatchObject实例.返回None则没有字符串中的位置匹配模式.

  * `re.sub(pattern, repl, string, count=0, flags=0)`
    > 按`pattern`匹配字符串`string`中的相应字符并替换为`repl` (*repl可以是返回字符串的函数*), 替换`count`次, 返回替换后的新字符串(不改变原字符串), 若未匹配到则返回原字符串.**`count`默认为0, 表示替换所有的匹配**.

  * `re.subn(pattern, repl, string, count=0, flags=0)`
    > 同上, 返回值为一个元组:**（替换后的新字符串, 替换次数）**.

  * `re.findall(pattern, string, flags=0)`
    > 返回字符串(string)中所有非重叠匹配的模式(pattern)组成的**列表**.
    ```py
      >>> re.findall('xx\dxx', 'xx1xx2xx3xx4xx5xx')
      ['xx1xx', 'xx3xx', 'xx5xx']
    ```

  * `re.split(pattern, string, maxsplit=0, flags=0)`
    > 按(pattern)匹配字符串(string)中的相应字符并替换为(repl), 替换(count)次, 返回替换后的新字符串.**count默认为0, 表示替换所有的匹配**.

* Match Objects方法
  * `group(num=0)`
    > 匹配的整个表达式的字符串, group() 可以一次输入多个组号, 在这种情况下它将返回一个包含那些组所对应值的元组.如果单个参数, 结果是一个单一的字符串 ；如果有多个参数, 其结果是参数每一项的元组.

  * `groups()`
    > 返回一个包含所有小组字符串的元组.

* pattern操作

  * `re.purge()`
    > 清除正则表达式缓存

  * `re.finditer(pattern, string, flags=0)`
    > 同`re.findall`, 返回迭代器

  * `re.compile(pattern, flags=0)`
    > 编译一个正则的模式(pattern), 返回模式对象

  * `re.template(pattern, flags=0)`
    > 编译一个用于正则模板的模式(pattern), 返回模式对象

  * `re.escape(pattern)`
    > 返回字符串, 转译`pattern`中所有非字母数字；如果你想匹配一个任意的文本字符串, 它可能包含正则表达式元字符.

## 正则表达式模式语法

| 定位符 | 描述 |
| :------: | ---- |
| ^ | 匹配字符串的开头, 若设置了re.M 还会与 \n 或 \r 之后的位置匹配 |
| $ | 匹配字符串的末尾 |
| \b | 匹配一个字边界, 即字与空格间的位置 |
| \B | 非字边界匹配 |
| \A | 匹配字符串开始|
| \Z | 匹配字符串结束, 如果是存在换行, 只匹配到换行前的结束字符串|
| \z | 匹配字符串结束|
| \G | 匹配最后匹配完成的位置|
| \1...\9 | 匹配第n个分组的内容 |
| \10 | 匹配第n个分组的内容, 如果它经匹配, 否则指的是八进制字符码的表达式 |

| 限定符 | 描述 |
| :------: | ---- |
| * | 匹配前面的子表达式零次或多次(默认贪婪greedy,尽可能多匹配) |
| + | 匹配前面的子表达式一次或多次(默认贪婪greedy,尽可能多匹配) |
| ? | 匹配前面的子表达式零次或一次, 或指明一个非贪婪限定符 |
| *?, +?, ?? | 限定符的非贪婪模式, 尽可能少的匹配 |
| {n} | 匹配前面的子表达式确定的 n 次 |
| {n,} | 匹配前面的子表达式至少 n 次 |
| {n,m} | 匹配前面的子表达式 n到m 次, **逗号和两个数之间不能有空格, 贪婪方式** |

| 非打印字符 | 描述 |
| :------: | ---- |
| \n | 匹配一个换行符 等价于 \x0a 和 \cJ |
| \r | 匹配一个回车符 等价于 \x0d 和 \cM |
| \s | 匹配任何空白字符, 包括空格、制表符、换页符等等 等价于 [ \f\n\r\t\v] |
| \S | 匹配任何非空白字符 等价于 [^ \f\n\r\t\v] |
| \t | 匹配一个制表符 等价于 \x09 和 \cI |
| \v | 匹配一个垂直制表符 等价于 \x0b 和 \cK |
| \f | 匹配一个换页符 等价于 \x0c 和 \cL |
| \cx | 匹配由x指明的控制字符 例如, \cM匹配一个`Control-M`或回车符x的值必须为A-Z或a-z之一否则,将c视为一个原义的'c'字符 |

| 特殊字符 | 描述 |
| :------: | ---- |
| . | 匹配任意单字符(除换行符), 当re.S标记被指定时, 可匹配换行符 |
| () | 标记一个子表达式的开始和结束位置, 子表达式可以获取供以后使用 |
| \ | 将下一个字符标记为或特殊字符, 或原义字符, 或向后引用, 或八进制转义符 |
| a&brvbar;b | 匹配a或b |
| (?imx: re) | 在括号中使用i, m, 或 x 可选标志 |
| (?-imx: re) | 在括号中不使用i, m, 或 x 可选标志 |
| (?#...) | 注释 |
| (?= re) | 前向肯定界定符。如果所含正则表达式, 在当前位置成功匹配时成功, 剩余部分还要尝试界定符的右边 |
| (?! re) | 前向否定界定符。当所含表达式不能在字符串当前位置匹配时成功 |

## 连续替换

```py
import re

my_str = "(condition1) and --condition2--"
print my_str.replace("condition1", "").replace("condition2", "text")

rep = {"condition1": "", "condition2": "text"}
rep = dict((re.escape(k), v) for k, v in rep.iteritems())
pattern = re.compile("|".join(rep.keys()))
my_str = pattern.sub(lambda m: rep[re.escape(m.group(0))], my_str)

print my_str

"""
Output:
() and --text--
"""
```

## 参考链接

[re源码](//Python27/Lib/re.py "//Python27/Lib/re.py"),
[菜鸟教程](http://www.runoob.com/regexp/regexp-syntax.html),
[CSDN博客1](http://blog.csdn.net/u014467169/article/details/51345657),
[CSDN博客2](http://blog.csdn.net/caroline_wendy/article/details/47065115)
