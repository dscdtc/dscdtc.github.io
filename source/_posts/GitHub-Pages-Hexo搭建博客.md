---
title: GitHub Pages + Hexo搭建博客
date: 2017-10-18 10:00:54
tags: [github, blog]
categories: Git
---

***假设Git、Node等环境已配置完成，本文暂不赘述***
<!--more-->

# 0. hexo

```cmd
npm i -g hexo-cli
hexo init <folder>
cd <folder>
npm install

npm i hexo-deployer-git -S
```

# 1. 博客搭建流程

1. 创建仓库，`<username>.github.io`；

2. 创建两个分支：master 与 hexo；

3. 设置hexo为默认分支（因为我们只需要手动管理这个分支上的Hexo网站文件）；
4. 使用git clone git@github.com:CrazyMilk/CrazyMilk.github.io.git拷贝仓库；
5. 在本地CrazyMilk.github.io文件夹下通过Git bash依次执行npm install hexo、hexo init、npm install 和 npm install hexo-deployer-git（此时当前分支应显示为hexo）;
6. 修改_config.yml中的deploy参数，分支应为master；
依次执行git add .、git commit -m “…”、git push origin hexo提交网站相关的文件；
7. 执行hexo generate -d生成网站并部署到GitHub上。
这样一来，在GitHub上的CrazyMilk.github.io仓库就有两个分支，一个hexo分支用来存放网站的原始文件，一个master分支用来存放生成的静态网页。完美( •̀ ω •́ )y！

# 2. 博客管理流程

1. 日常修改

    在本地对博客进行修改（添加新博文、修改样式等等）后，通过下面的流程进行管理：

    依次执行git add .、git commit -m “…”、git push origin hexo指令将改动推送到GitHub（此时当前分支应为hexo）；
然后才执行hexo generate -d发布网站到master分支上。
虽然两个过程顺序调转一般不会有问题，不过逻辑上这样的顺序是绝对没问题的（例如突然死机要重装了，悲催….的情况，调转顺序就有问题了）。

2. 本地资料丢失

    当重装电脑之后，或者想在其他电脑上修改博客，可以使用下列步骤：

    使用git clone git@github.com:CrazyMilk/CrazyMilk.github.io.git拷贝仓库（默认分支为hexo）；
    在本地新拷贝的CrazyMilk.github.io文件夹下通过Git bash依次执行下列指令：npm install hexo、npm install、npm install hexo-deployer-git（记得，不需要hexo init这条指令）。

# 3. 博文压缩

在博客根目录下运行
`npm install gulp-clean-css gulp-uglify gulp-htmlmin gulp-htmlclean gulp --save`
新建gulpfile.js:

```js
    var gulp = require('gulp');
    var minifycss = require('gulp-clean-css');
    var uglify = require('gulp-uglify');
    var htmlmin = require('gulp-htmlmin');
    var htmlclean = require('gulp-htmlclean');
    // 压缩 public 目录 css
    gulp.task('minify-css', function() {
        return gulp.src('./public/**/*.css')
            .pipe(minifycss())
            .pipe(gulp.dest('./public'));
    });
    // 压缩 public 目录 html
    gulp.task('minify-html', function() {
    return gulp.src('./public/**/*.html')
        .pipe(htmlclean())
        .pipe(htmlmin({
            removeComments: true,
            minifyJS: true,
            minifyCSS: true,
            minifyURLs: true,
        }))
        .pipe(gulp.dest('./public'))
    });
    // 压缩 public/js 目录 js
    gulp.task('minify-js', function() {
        return gulp.src('./public/**/*.js')
            .pipe(uglify())
            .pipe(gulp.dest('./public'));
    });
    // 执行 gulp 命令时执行的任务
    gulp.task('default', [
        'minify-html','minify-css','minify-js'
]);
```

生成博文时执行`hexo g && gulp`就会根据`gulpfile.js`中的配置，对 public 目录中的静态资源文件进行压缩。
