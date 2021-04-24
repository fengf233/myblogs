---
layout:     post
title:      Git用法总结
subtitle:   
date:       2019-09-01
author:     Mehaei
header-img: img/home-bg-geek.jpg
catalog: true
tags:
    - python
---
### 本地仓库的操作

**配置用户名**:`git config --global user.name "你自己的用户名(github)"`

**配置邮箱**:`git config --globel user.email "你自己的邮箱"`

**创建版本库**:

<li class="md-list-item">
在项目路径下创建空目录
</li>
<li class="md-list-item">
cd进入目录
</li>
<li class="md-list-item">
使用`git init`命令把这个目录变成Git仓库，建议不要修改.git目录里面的文件
</li>

**把文件添加到版本库**:

<li class="md-list-item">
在仓库创建文件test，随意添加内容如first commit
</li>
<li class="md-list-item">
添加文件到仓库(实际添加到暂存区)`git add test`
</li>
<li class="md-list-item">
把文件提交到仓库`git commit -m "注释信息"`
</li>

**查看仓库状态**:`git status`

**查看修改内容**:`git diff`

**查看从最近到最远的提交log**:`git log` (只看版本信息log使用`git log --pretty=oneline`)

**回退到上一个版本**:`git reset --hard HEAD^`

**回退到上上版本**:`git reset --hard HEAD^^`

**回退3或n个版本**:`git reset --hard HEAD~3`

**回退到具体版本**:`git reset --hard 具体版本号`

回退版本实际就是将HEAD指针到具体版本，回退后`git log`只有你回退具体版本前的log，可以使用`git reflog`查看操作记录，然后使用`git reset --hard 具体版本号`会到你想要的版本，`reflog`的$1列就是对于的版本号

**工作区**:仓库所在目录，通过`git add`从工作区往缓存区里面添加

**版本库**: .git目录是Git的版本库，主要分为缓存区(state),自动创建的分支(master)，以及指向master的指针(HEAD)。通过`git commit`将缓存区添加到master分支中，并且HEAD指向此次提交版本

**撤销**: `git checkout -- fileName`撤销文件修改分为两种情况

<li class="md-list-item">
如果fileName没有`git add`到缓存区，则使用`git checkout -- fileName`会将fileName文件回退到与master分支中的一样
</li>
<li class="md-list-item">
如果fileName有`git add`到缓存区，则使用`git checkout -- fileName`会将fileName文件回退到与缓存区中的状态一致
</li>

***以上为本地库的操作**

### 远程仓库操作

#### 配置git连接远程库

***以GitHub为例**

**创建SSH Key**：git bash中输入`ssh-keygen -t rsa -C "Github注册邮箱"`，然后一直回车到出现密钥就行

```
Generating public/private rsa key pair.​Enter file in which to save the key (/c/Users/xxx/.ssh/id_rsa):   #Key保存路径，可以不填​Enter passphrase (empty for no passphrase):   #输入密码（可以为空）为使用密钥时的密码，不是登录GitHub密码​Enter same passphrase again:   #再次确认密码（可以为空）​Your identification has been saved in /c/Users/xxx/.ssh/id_rsa.   #id_rsa私钥​Your public key has been saved in /c/Users/xxx/.ssh/id_rsa.pub.  #id_rsa.pub公钥​The key fingerprint is:​xx:xx:xx:xx:xxx
```

**Github设置**:进入你的GitHub主页，进入settings / ssh and GPG keys，点击New SSH Key将上一步中的id_rsa.pub公钥内容复制到key中，然后bash中使用`ssh -T git@github.com`测试是否git连接上github

**git多用户连接gitee和GitHub**：参考[https://gitee.com/help/articles/4229#article-header1](https://gitee.com/help/articles/4229#article-header1)

 

#### git远程仓库操作

**关联远程仓库**：`git remote add <remote-name> <远程仓库URL地址>`，这个是当在本地`git init`创建了本地仓库后与远程关联时使用,远程库默认名字为`origin`

**删除关联**：`git remote rm <remote-name>`

**拉取远程库合并到本地**：`git pull <remote-name> <远程branch分支>:<本地branch分支>`，如一般用`git pull origin master`表示从远程库oringin的master分支拉取，`<本地branch分支>`没有默认表示当前分支，有则指定合并分支

**推送本地库内容到远程库**：`git push <remote-name> <本地branch分支>:<远程branch分支>`,如一般是`git push origin master`，表示将本地master分支上传到远程库origin，如果省略远程分支名，则判断有没有同名的分支

**克隆远程版本库**：`git clone <url>`，在没有使用`git init`时，直接从远程库复制，相当于`git init`与`git pull`

**查看远程版本库信息**：`git remote -v`

**.gitignore文件**：此文件中记录在push到远程库时忽略的文件

### 分支管理

**查看本地所有分支**：`git branch`

**查看所有远程分支**：`git branch -r`

**创建新的分支**：`git branch <new-branch>`

**删除本地分支**：`git branch -d <branch>`

**切换到指定分支**：`git checkout <branch>`

**合并分支到当前分支**：`git merge <branch>`

### 一般git工作流程

1.`git clone`or`git pull`将远程库master分支拉下来

2.本地`git branch <new-branch>`创建自己的分支如dev

3.在自己的分支dev上开发，`git add`或`git commit`

4.然后切换到master分支，`git merge`合并dev到master分支

5.再次`git pull`拉取远程master分支，查看有么有冲突，有就解决

6.最后将本地master分支push到远程master上

***但实际上master一般作为稳定的发版本分支，不常修改。一般可能会在远程库创建开发的分支，在此分支上工作**

** **

 
