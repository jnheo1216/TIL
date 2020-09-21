# Git 기초

> Git은 분산형 버전관리시스템(DVCS)

Git을 윈도우에 활용하기 위해서는 [git bash](http://gitforwindows.org/)를 설치해야한다

## 1. 저장소초기화

```bash
$ git init
Initialized empty Git repository in C:/Users/hjeio/Desktop/TIL/.git/

```

* 로컬저장소를 만들고 나면 `.git/` 폴더가 생성되고, bash에 `(master)` 라고 표시된다.
* 반드시 저장소를 만들기 전에 원하는 디렉토리인지 확인하는 습관을 가지고, 저장소 안에 저장소는 하지말자.
  * 예) Desktop -> 저장소 TIL -> 또 저장소

## 2. add

작업한 내용을 커밋 대상 목록에 추가한다.

```bash
# 작업 후 상태
$ git status
On branch master

No commits yet
# untracked files => git으로 관리된적없는 파일
Untracked files:
# 커밋될것들을 포함시키기위해 add 명령어 필요
  (use "git add <file>..." to include in what will be committed)
        markdown-images/
        markdown.md
# 커밋될 곳이 없다(nothing)
# 하지만 새로 생성한 파일은 존재 (untracked files)
nothing added to commit but untracked files present (use "git add" to track)
```

```bash
$ git add .
# add 명령 후 상태
$ git status
On branch master

No commits yet
# 커밋이 될 변경사항들
# working directory (x)
# staging area (o)
Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   "markdown-images/\354\272\241\354\262\230.PNG"
        new file:   markdown.md
```

```bash
$ git add .
$ git add a.html
$ git add b.html c.html
$ git add blog/
```



## 3. commit

```bash
$ git commit -m 'Add markdown.md'
[master (root-commit) 28ce67b] Add markdown.md
 2 files changed, 83 insertions(+)
 create mode 100644 "markdown-images/\354\272\241\354\262\230.PNG"
 create mode 100644 markdown.md
```

* 커밋은 버전(이력)을 기록하는 명령어이다.
* 커밋메세지는 해당하는 이력을 나타낼 수 있도록 작성해야 한다.
* 커밋이력을 확인하는 명령어

```bash
$ git log
commit 28ce67bb3869373c8e792864be5e0c5dfe57e226 (HEAD -> master)
Author: jnheo1216 <hjeionyng94@gmail.com>
Date:   Thu Aug 20 14:59:19 2020 +0900

    Add markdown.md
$ git log -1
$ git log --oneline
$ git log --oneline -1
```

## 4. 기타명령어

 ### `restore`

작업공간(working directory)의 변경사항을 버린다.

```bash
$ git status
On branch master
Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   README.md
        deleted:    blog.html

no changes added to commit (use "git add" and/or "git commit -a")
$ git restore blog.html
```

* `--staged` 옵션을 활용하면, staging area를 취소(add명령어의 반대)

```bash
$ git restore --staged README.md
$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   README.md

no changes added to commit (use "git add" and/or "git commit -a")
```

### 커밋메세지 변경

```bash
$ git commit --amend
```

### reset, revert





