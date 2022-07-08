# Git 실습

## 0. 사전 설정 (PC 최초 한번)

```bash
$ git config --global user.name 'GitHub ID'
$ git config --global user.email 'GitHub Email'
```



## 1. 바탕화면에 TIL폴더를 만든다.

- TIL폴더를 열어서 마크다운 정리 파일을 옮긴다.
- VS Code를 연다.



## 2. TIL 폴더에 git 저장소를 만들어준다.

```bash
$ git init
설정 후 뒤에 master가 되었는지 확인
```



## 3. 커밋을 만든다.

```bash
$ git add .
$ git commit -m '마크다운 정리'
```

```bash
$ git log
```





# ✔Git 실습 해보기

```bash
jj@DESKTOP-5N8TM5H MINGW64 ~/Desktop/TIL
$ git init 
Initialized empty Git repository in C:/Users/jj/Desktop/TIL/.git/
jj@DESKTOP-5N8TM5H MINGW64 ~/Desktop/TIL (master) # $ git init 명령어로 master로 바뀜
$ git add
Nothing specified, nothing added.
hint: Maybe you wanted to say 'git add .'?      
hint: Turn this message off by running
hint: "git config advice.addEmptyPathspec false"

jj@DESKTOP-5N8TM5H MINGW64 ~/Desktop/TIL (master)  
$ git add . # $ git add . 명령어로 TIL디렉토리에 있는 모든 파일들을 add 시킨다

jj@DESKTOP-5N8TM5H MINGW64 ~/Desktop/TIL (master)  
$ git commit -m '마크다운 정리' #커밋 할때 '마크다운 정리'라는 메시지가 나오게 설정
Author identity unknown

*** Please tell me who you are.

Run
######Git 실습 0. 참고######
  git config --global user.email "you@example.com" #너가 누구인지 이메일 설정해라
  git config --global user.name "Your Name"   #너가 누구인지 이름을 설정해라 

to set your account's default identity.
Omit --global to set the identity only in this repository.

fatal: unable to auto-detect email address (got 'jj@DESKTOP-5N8TM5H.(none)')

jj@DESKTOP-5N8TM5H MINGW64 ~/Desktop/TIL (master)  
$ git config --global user.email 'rksaudwls123@naver.com' #내가 누구인지 이메일 설정

jj@DESKTOP-5N8TM5H MINGW64 ~/Desktop/TIL (master)  
$ git config --global user.name 'JeongJinGan' #내가 누구인지 이름 설정

jj@DESKTOP-5N8TM5H MINGW64 ~/Desktop/TIL (master)  
$ git log	#커밋 조회
fatal: your current branch 'master' does not have any commits yet

jj@DESKTOP-5N8TM5H MINGW64 ~/Desktop/TIL (master)  
$ git commit -m '마크다운 정리'
[master (root-commit) 4971ba0] 마크다운 정리
 4 files changed, 203 insertions(+)
 create mode 100644 Markdown.assets/bono.png       
 create mode 100644 Markdown.assets/pyhonlogo.png  
 create mode 100644 Markdown.md
 create mode 100644 markdown_practice.md

jj@DESKTOP-5N8TM5H MINGW64 ~/Desktop/TIL (master)
$ git log	#커밋 조회하였더니 위에서 커밋할때 메시지 출력되게 설정해주어서 '마크다운 정리' 메시지가 함께 출력됨
commit 4971ba0b9e443eee8a45ebdf1d99032f90298064 (HEAD -> master)
Author: JeongJinGan <rksaudwls123@naver.com>
Date:   Tue Jul 5 16:25:13 2022 +0900

    마크다운 정리

jj@DESKTOP-5N8TM5H MINGW64 ~/Desktop/TIL (master)
$ git status
On branch master
nothing to commit, working tree clean
```



# 로컬 저장소 만들기(연습)

### 1. 프로젝트 폴더만들기

- **바탕화면**에0706폴더 생성

### 2. 해당 폴더에서 Git 버전 관리 시작하기

```bash
$ git init
```

- 주의! (master)라고 되어 있으면 상위 폴더 확인하자
- 명령어를 입력하게 되면 `.git`폴더가 생성된다.

### 3. 작업

- 별도의 빈 파일 하나 생성
- status도 확인하기!

### 4. 작업이 완료되면 커밋하기

- 커밋하고, log도 확인하기

### 5. 자유롭게 파일 만들고 수정하고 삭제하면서 커밋 3개 더 쌓아보기





# ❌원격저장소 경로 설정 및 커밋❌

```bash
$ git remote add origin https://github.com/JeongJinGan/test.git
#    원격저장소 추가해 Origin으로              GitHub Username/ 저장소이름
# => 깃아 원격저장소 추가해줘 오리진이라는 이름으로 URL을
```

```bash
$ git remote -v
#원격 저장소의 정보를 확인함
```

```bash
$ git push <원격저장소이름><브랜치이름>
#원격 저장소로 로컬 저장소 변경 사항(커밋)을 올린 push
#로컬 폴더의 파일/폴더가 아닌 저장소의 버전(커밋)이 올라감
```









