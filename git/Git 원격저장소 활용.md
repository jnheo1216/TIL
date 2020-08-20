# Git 원격저장소 활용

Git 원격저장소 기능을 제공하는 서비스 `gitlab`,`bitbucket`,`github`등등

## 0. 원격저장소 설정

```bash
$ git remote add origin {url}
$ git remote add origin https://github.com/jnheo1216/TIL.git
```

* git, 원격저장소를 추가(add)하고 `origin`이라는 이름으로 `url`으로 설정
* 설정된 저장소를 확인하기 위해서 아래의 명령어

```bash
$ git remote -v
origin  https://github.com/jnheo1216/TIL.git (fetch)
origin  https://github.com/jnheo1216/TIL.git (push)

```

## 원격저장소에 push

```bash
$ git push -u origin master
Enumerating objects: 18, done.
Counting objects: 100% (18/18), done.
Delta compression using up to 4 threads
Compressing objects: 100% (14/14), done.
Writing objects: 100% (18/18), 24.00 KiB | 2.67 MiB/s, done.
Total 18 (delta 4), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (4/4), done.
To https://github.com/jnheo1216/TIL.git
 * [new branch]      master -> master
Branch 'master' set up to track remote branch 'master' from 'origin'.
```





