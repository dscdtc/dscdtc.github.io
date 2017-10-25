---
title: JS简写技巧
date: 2017-10-25 10:44:23
tags: [Javascript]
categories: Javascript
---
本篇仅记录经常遗忘的方法, 更详细的内容[参见原文](https://www.sitepoint.com/shorthand-javascript-techniques/)
<!--more-->

### 1. 三目运算符

下面是一个很好的例子，将一个完整的 if 语句，简写为一行代码。
```js
const x = 20;
let answer;
if (x > 10) {
    answer = 'greater than 10';
} else {
    answer = 'less than 10';
}
```
简写为：

```js
const answer = x > 10 ? 'greater than 10' : 'less than 10';
```

### 2. 循环语句

当使用纯 JavaScript（不依赖外部库，如 jQuery 或 lodash）时，下面的简写会非常有用。
```js
for (let i = 0; i < allImgs.length; i++)
```
简写为：
```js
for (let index of allImgs)
```
下面是遍历数组 forEach 的简写示例：
```js
function logArrayElements(element, index, array) {
  console.log("a[" + index + "] = " + element);
}
[2, 5, 9].forEach(logArrayElements);
// logs:
// a[0] = 2
// a[1] = 5
// a[2] = 9
```

### 3. 声明变量

在函数开始之前，对变量进行赋值是一种很好的习惯。在申明多个变量时：
```js
let x;
let y;
let z = 3;
```
可以简写为：
```js
let x, y, z=3;
```

### 4.十进制数

可以使用科学计数法来代替较大的数据，如可以将 10000000 简写为 1e7。
xey = x*10^y
```js
for (let i = 0; i < 10000; i++) { }
```
简写为：
```js
for (let i = 0; i < 1e7; i++) { }
```

### 5.  变量赋值

当将一个变量的值赋给另一个变量时，首先需要确保原值不是 null、未定义的或空值。

可以通过编写一个包含多个条件的判断语句来实现：
```js
if (variable1 !== null || variable1 !== undefined || variable1 !== '') {
     let variable2 = variable1;
}
```
或者简写为以下的形式：
```js
const variable2 = variable1  || 'new';
```
可以将下面的代码粘贴到 es6console 中，自己测试：
```js
let variable1;
let variable2 = variable1  || '';
console.log(variable2 === ''); // prints true
variable1 = 'foo';
variable2 = variable1  || '';
console.log(variable2); // prints foo
```

### 6. 对象属性

ES6 提供了一个很简单的办法，来分配属性的对象。如果属性名与 key 名相同，则可以使用简写。
```js
const obj = { x:x, y:y };
```
简写为：
```js
const obj = { x, y };
```

### 7. 箭头函数

经典函数很容易读写，但是如果把它们嵌套在其它函数中进行调用时，整个函数就会变得有些冗长和混乱。这时候可以使用箭头函数来简写：
```js
function sayHello(name) {
  console.log('Hello', name);
}
 
setTimeout(function() {
  console.log('Loaded')
}, 2000);
 
list.forEach(function(item) {
  console.log(item);
});
```
简写为：
```js
sayHello = name => console.log('Hello', name);
setTimeout(() => console.log('Loaded'), 2000);
list.forEach(item => console.log(item));
```

### 8. 隐式返回值

返回值是我们通常用来返回函数最终结果的关键字。只有一个语句的箭头函数，可以隐式返回结果（函数必须省略括号（{ }），以便省略返回关键字）。

要返回多行语句（例如对象文本），需要使用（）而不是{ }来包裹函数体。这样可以确保代码以单个语句的形式进行求值。
```js
function calcCircumference(diameter) {
  return Math.PI * diameter
}
```
简写为：
```js
calcCircumference = diameter => (
  Math.PI * diameter;
)
```

### 9. 默认参数值

可以使用 if 语句来定义函数参数的默认值。ES6 中规定了可以在函数声明中定义默认值。
```js
function volume(l, w, h) {
  if (w === undefined)
    w = 3;
  if (h === undefined)
    h = 4;
  return l * w * h;
}
```
简写为：
```js
volume = (l, w = 3, h = 4 ) => (l * w * h);
volume(2) //output: 24
```

### 10. 解构赋值

解构赋值是一种表达式，用于从数组或对象中快速提取属性值，并赋给定义的变量。

在代码简写方面，解构赋值能达到很好的效果。
~~~js
	const observable = require('mobx/observable');
	const action = require('mobx/action');
	const runInAction = require('mobx/runInAction');
	const store = this.props.store;
	const form = this.props.form;
	const loading = this.props.loading;
	const errors = this.props.errors;
	const entity = this.props.entity;
~~~
简写为：
```js
	import { observable, action, runInAction } from 'mobx';
	const { store, form, loading, errors, entity } = this.props;
```
甚至可以指定自己的变量名：
```js
const { store, form, loading, errors, entity:contact } = this.props;
```

### 11. 展开运算符

展开运算符是在 ES6 中引入的，使用展开运算符能够让 JavaScript 代码更加有效和有趣。

使用展开运算符可以替换某些数组函数。
```js
	// joining arrays
	const odd = [1, 3, 5];
	const nums = [2 ,4 , 6].concat(odd);
	 
	// cloning arrays
	const arr = [1, 2, 3, 4];
	const arr2 = arr.slice( )
	简写为：

	// joining arrays
	const odd = [1, 3, 5 ];
	const nums = [2 ,4 , 6, ...odd];
	console.log(nums); // [ 2, 4, 6, 1, 3, 5 ]
	 
	// cloning arrays
	const arr = [1, 2, 3, 4];
	const arr2 = [...arr];
	和 concat( ) 功能不同的是，用户可以使用扩展运算符在任何一个数组中插入另一个数组。

	const odd = [1, 3, 5 ];
	const nums = [2, ...odd, 4 , 6];
	也可以将展开运算符和 ES6 解构符号结合使用：

	const { a, b, ...z } = { a: 1, b: 2, c: 3, d: 4 };
	console.log(a) // 1
	console.log(b) // 2
	console.log(z) // { c: 3, d: 4 }
```

### 12. 强制参数

默认情况下，如果不向函数参数传值，那么 JavaScript 会将函数参数设置为未定义。其它一些语言则会发出警告或错误。要执行参数分配，可以使用if语句抛出未定义的错误，或者可以利用“强制参数”。
```js
	function foo(bar) {
	  if(bar === undefined) {
	    throw new Error('Missing parameter!');
	  }
	  return bar;
	}
```
简写为：
```js
	mandatory = ( ) => {
	  throw new Error('Missing parameter!');
	}
	foo = (bar = mandatory( )) => {
	  return bar;
	}
```

### 13. Array.find

如果你曾经编写过普通 JavaScript 中的 find 函数，那么你可能使用了 for 循环。在 ES6 中，介绍了一种名为 find（）的新数组函数，可以实现 for 循环的简写。
```js
	const pets = [
	  { type: 'Dog', name: 'Max'},
	  { type: 'Cat', name: 'Karl'},
	  { type: 'Dog', name: 'Tommy'},
	]
	function findDog(name) {
	  for(let i = 0; i<pets.length; ++i) {
	    if(pets[i].type === 'Dog' && pets[i].name === name) {
	      return pets[i];
	    }
	  }
	}
```
简写为：
```js
	pet = pets.find(pet => pet.type ==='Dog' && pet.name === 'Tommy');
	console.log(pet); // { type: 'Dog', name: 'Tommy' }
```

### 14. Object [key]

虽然将 foo.bar 写成 foo ['bar'] 是一种常见的做法，但是这种做法构成了编写可重用代码的基础。

请考虑下面这个验证函数的简化示例：
```js
	function validate(values) {
	  if(!values.first)
	    return false;
	  if(!values.last)
	    return false;
	  return true;
	}
console.log(validate({first:'Bruce',last:'Wayne'})); // true
```
上面的函数完美的完成验证工作。但是当有很多表单，则需要应用验证，此时会有不同的字段和规则。如果可以构建一个在运行时配置的通用验证函数，会是一个好选择。
```js
	// object validation rules
	const schema = {
	  first: {
	    required:true
	  },
	  last: {
	    required:true
	  }
	}
	 
	// universal validation function
	const validate = (schema, values) => {
	  for(field in schema) {
	    if(schema[field].required) {
	      if(!values[field]) {
		return false;
	      }
	    }
	  }
	  return true;
	}
	console.log(validate(schema, {first:'Bruce'})); // false
	console.log(validate(schema, {first:'Bruce',last:'Wayne'})); // true
```
现在有了这个验证函数，我们就可以在所有窗体中重用，而无需为每个窗体编写自定义验证函数。

 

### 15. 双位操作符

位操作符是 JavaScript 初级教程的基本知识点，但是我们却不常使用位操作符。因为在不处理二进制的情况下，没有人愿意使用 1 和 0。

但是双位操作符却有一个很实用的案例。取值为正数时,可以使用双位操作符来替代`Math.floor( )`。双否定位操作符的优势在于它执行相同的操作运行速度更快。
[原理:浮点数不能进行位运算,在使用位操作符时js会将其转化为32位整形数]

```js
	Math.floor(4.9) === 4  //true
```
简写为：
```js
	~~4.9 === 4  //true
	**负数时`Math.floor(Num) != ~~Num`**
	~~-4.9 // -4
	Math.floor(-4.9) // -5
```
数值大于0时,效果等同于无符号位移:
```js
	4.9 >>> 0 // 4
```
