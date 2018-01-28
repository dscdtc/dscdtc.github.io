---
title: github PullRequest 工作流程
date: 2017-10-23 15:22:34
tags: [git]
categories: Git
---

我们知道，如果你想为某个开源项目贡献代码，通用的流程是：

1.fork 项目到自己的仓库。
2.在新开的分支上提交。
3.提出 PR 请求维护者将你的新分支合并至原项目。

<!--more-->

下面是详细的命令:

* 项目clone & 新建分支

```shell
git clone <origin-git-address>  <project-name>
cd <project-name>
git remote add upstream <git-address>
git remote -v  // 查看链接情况
git checkout -b <local-branch-name>  // 新建并切换到分支
```

* 代码修改

OOXX...

* 项目提交

```shell
git fetch upstream
git rebase upstream/dev
git add . && git commit -m '<this-commit-info>'
git checkout <origin-git-branch> // 切换分支
git merge <local-branch-name> --squash
git commit -m '<this-commit-info>'
git push
```

* 提交PR

Pull Request -ing