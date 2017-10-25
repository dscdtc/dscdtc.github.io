---
title: 对js逻辑运算符的总结
date: 2017-03-30 12:21:30
tags: [Javascript]
categories: js
---
### 对js运算符“||”和“&&”的总结

**首先出个题：**

![img](http://dl.iteye.com/upload/attachment/143005/1ec269a5-d45f-37a3-ab50-6eaaee73e835.jpg)
假设对成长速度显示规定如下：
成长速度为5显示1个箭头；
成长速度为10显示2个箭头；
成长速度为12显示3个箭头；
成长速度为15显示4个箭头；
其他都显示都显示0各箭头。
用代码怎么实现？
<!--more-->

差一点的if，else：
``` Javascript
var add_level = 0; 
  
if(add_step == 5){
    add_level = 1;
}
else if(add_step == 10){
    add_level = 2;
}
else if(add_step == 12){
    add_level = 3;
}
else if(add_step == 15){
    add_level = 4;
}
else {
    add_level = 0;
}
```
稍好些的switch：
```javascript
var add_level = 0;
  
switch(add_step){
    case 5 : add_level = 1;
        break;  
    case 10 : add_level = 2;
        break;  
    case 12 : add_level = 3;
        break;  
    case 15 : add_level = 4;
        break;  
    default : add_level = 0;
        break;  
}
```
如果需求改成：
成长速度为>12显示4个箭头；
成长速度为>10显示3个箭头；
成长速度为>5显示2个箭头；
成长速度为>0显示1个箭头；
成长速度为<=0显示0个箭头。
 
那么用switch实现起来也很麻烦了。
 
那么你有没有想过用一行就代码实现呢？
ok，让我们来看看js强大的表现力吧：
```js
var add_level = (add_step==5 && 1) || (add_step==10 && 2) || (add_step==12 && 3) || (add_step==15 && 4) || 0;
```
更强大的，也更优的：
```js
var add_level={'5':1,'10':2,'12':3,'15':4}[add_step] || 0;
```
第二个需求：
```js
var add_level = (add_step>12 && 4) || (add_step>10 && 3) || (add_step>5 && 2) || (add_step>0 && 1) || 0;
```
首先我们来梳理一下一个概念，请你一定要记住：在js逻辑运算中，0、""、null、false、undefined、NaN都会判为false，其他都为true（好像没有遗漏了吧，请各位确认下）。这个一定要记住，不然应用||和&&就会出现问题。

这里顺便提下：经常有人问我，看到很多代码if(!!attr)，为什么不直接写if(attr)；
其实这是一种更严谨的写法：
请测试 typeof 5和typeof !!5的区别。!!的作用是把一个其他类型的变量转成的bool类型。

下面主要讨论下逻辑运算符&&和||。

几乎所有语言中||和&&都遵循“短路”原理，如&&中第一个表达式为假就不会去处理第二个表达式，而||正好相反。
js也遵循上述原则。但是比较有意思的是它们返回的值。
代码：var attr = true && 4 && “aaa”;
那么运行的结果attr就不是简单的true或这false，而是”aaa”
再来看看||：
代码：var attr = attr || “”;这个运算经常用来判断一个变量是否已定义，如果没有定义就给他一个初始值，这在给函数的参数定义一个默认值的时候比较有用。因为js不像php可以直接在型参数上定义func($attr=5)。再次提醒你记住上面的原则：如果实参需要是0、""、null、false、undefined、NaN的时候也会当false来处理。

if(a >=5){
    alert("你好");
}
可以写成：
a >= 5 && alert("你好");

这样只需一行代码就搞定。但是需要注意的一点就是：js中||和&&的特性帮我们精简了代码的同时，也带来了代码可读性的降低。这就需要我们自己来权衡了。
一方面精简js代码，能实质性的减少网络流量，尤其是大量应用的js公用库。个人比较推荐的做法是：如果是相对复杂的应用，请适当地写一些注释。这个和正在表达式一样，能够精简代码，但是可读性会降低，对读代码的人要求会高些，最好的办法就是写注释。
 
我们可以不使用这些技巧，但是我们一定要能看懂，因为这些技巧已经广泛应用，尤其是像JQuery等js框里的代码，不理解这些你就很难看懂别人的代码。
像var Yahoo = Yahoo || {};这种是非常广泛应用的。
 
ok,最后让我们来看一段jQuery中的代码吧：
 
```javascript
var wrap =
    // option or optgroup
    !tags.indexOf("<opt") &&
    [ 1, "<select multiple='multiple'>", "</select>" ] ||
      
    !tags.indexOf("<leg") &&
    [ 1, "<fieldset>", "</fieldset>" ] ||
      
    tags.match(/^<(thead|tbody|tfoot|colg|cap)/) &&
    [ 1, "<table>", "</table>" ] ||
      
    !tags.indexOf("<tr") &&
    [ 2, "<table><tbody>", "</tbody></table>" ] ||
      
    // <thead> matched above
    (!tags.indexOf("<td") || !tags.indexOf("<th")) &&
    [ 3, "<table><tbody><tr>", "</tr></tbody></table>" ] ||
      
    !tags.indexOf("<col") &&
    [ 2, "<table><tbody></tbody><colgroup>", "</colgroup></table>" ] ||
      
    // IE can't serialize <link> and <script> tags normally
    !jQuery.support.htmlSerialize &&
    [ 1, "div<div>", "</div>" ] ||
      
    [ 0, "", "" ];
      
    // Go to html and back, then peel off extra wrappers  
    div.innerHTML = wrap[1] + elem + wrap[2];
      
    // Move to the right depth  
    while ( wrap[0]-- )
        div = div.lastChild;  
```

这段代码是作者用来处理 $(html) 时，有些标签必须要约束的，如`<option>`必须在`<select></select>`之内的。
可能你也发现了作者还有一个很巧的地方就是 `!tags.indexOf(”<opt“)`，作者很巧很简单的就实现了startWith的功能了，没有一点多余的代码。jquery源代码中还有很多如此精妙的代码，大家可以去学习学习。