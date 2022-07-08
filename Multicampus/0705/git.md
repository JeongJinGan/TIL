# Git을 하기전에

## CLI(Comand Line Internet) 환경 

> 명령을 줄 단위로 조작

- cmd(명령프롬프트), bash, sh, ksh, csh, tcsh등


## GUI(Graphic User Interface)

> 그래픽을 유저가 조작



## 프롬프트 기본 인터페이스

- 컴퓨터 정보
- 디렉토리
- $

### 명령어

- pwd(print working directory) : 현재 디렉토리 출력
- cd(change directory) : 디렉토리 이동
  - . : 현재 디렉토리
  - .. : 상위 디렉토리
- ls(list) : 목록
- mkdir(make directory) : 디렉토리 생성
- touch : 파일의 날짜와 시간을 수정(0바이트 빈파일 생성)
- rm : 파일삭제
  - -r : 폴더 삭제시(폴더 안에 내용들을 계속 지워줘야 하기 때문)

- ctrl + L : 기록지우기

새 폴더로 경로 이동시

cd 새\ 폴더

=> 폴더 생성시 새_폴더로 만들면 편하다.





## 분산버전관리시스템(DVCS)

> 원경 저장소(remote repository)를 통하여 협업하고, 모든 히스토리를 클라이언트들이 공유
>
> (중앙집중식버전관리시스템은 중앙에서 버전을 관리하고 파일을 받아서 사용)

## 버전관리

버전 - 컴퓨터 소프트웨어의 특정 상태

일반적인 우리의 버전관리 방식 - 과제(최종, 진짜 최종, 교수님 피드백 후 진짜 최종) 등

=> 자료 간에 뭐가 바뀌었는지 차이를 알 수 없다.

> 컴퓨터 파일의 변경사항을 추적하고 여러 명의 사용자들 간에 해당 파일들의 작업을 조율



# Git 명령어

`$ git init`-> master로 바뀜

`$ git status` (추적)

- git 저장소에 있는 파일의 상태를 확인하기 위하여 활용

`$ git config --global user.email "자신의 이메일"`

`$ git config --global user.name "이름설정"`

`$ git log`

- 현재 저장소에 기록된 커밋(버전)을 조회
- 다양한 옵션을 통해 로그를 조회할 수 있음
  - $ git log -1(제일 최근 1개 가져오기)
  - $ git log --oneline(한줄로 보여줘)
  - $ git log -2 --oneline(최근 2개를 한줄로 보여줘)

`$ git add <file>`         ex) $git add b.txt

- working directory상의 변경 내용을 staging area에 추가하기 위해사용

  - ustracked 상태의 파일을 staged로 변경

  - modified 상태의 파일을 staged로 변경


`$ git commit -m '<커밋메시지>'`

- staged 상태의 파일들을 커밋을 통해 버전으로 기록

  

commit

- git은 데이터를 파일 시스템의 스냅샷으로 관리하고 매우 크기가 작음

- 파일이 달라지지 않으면 성능을 위해 파일을 새로 저장하지 않음

- 기존의 델타 기반 버전 관리시스템과 가장 큰 차이를 가짐

  

1. 작업을 하고
2. 변경된 파일을 모아(add) --> staging area 
   - 내가 버전 기록 파일들을 모아놓은 임시 공간
3. 버전으로 남긴다(commit) --> repository



Git은 파일을 modified, staged, committed로 관리

- modifeied : 파일이 수정된 상태 (add 명령어를 통하여 staging area로)

- staged : 수정한 파일을 곧 커밋할 것이라고 표시한 상태(commit 명령어로 저장소)

- committed : 커밋이 된 상태

  



```bash
1통 => Working Directory
2통 => Staging Area
3통 => .git directory
```

---

# Git Status(실제코드)

## a.txt 파일을 만든 직후

> 빨간 글씨 => 1통

```bash
$ git status
On branch master

# 트래킹이 되고 있지 않은 파일?
# => 1통 (working directory)
# => 한번도 git으로 관리되고 있지 않은 파일!
Untracked files:
# git add 사용해봐...
# 포함시키기 위해서 / 커밋이 될 것 => 2통에 넣으려면
  (use "git add <file>..." to include in what will be committed)
        a.txt

# 커밋할 것은 없어 => 2통이 비어있어
# 하지만(but) 트래킹되지 않은 파일은 존재한다. 
# (git add 사용해서 트래킹해)
nothing added to commit but untracked files present (use "git add" to track)
```

## b.txt 파일을 만들고 add한 이후

> 초록 글씨 => 2통

```bash
$ git status
On branch master
# (커밋될) 변경사항들 => 2통
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
  		# 새로운 파일: b.txt
        new file:   b.txt

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        a.txt

```

## a.txt 파일과 b.txt 파일을 모두 add한 이후 커밋까지

```bash
$ git status
On branch master
# 2통, 1통 모두 클린~!
nothing to commit, working tree clean
```



# ❗Git 주의사항❗

1. **(master) 있는 곳에서는 git init을 하지 않는다.**
2. **git 명령어를 입력할 때에는 항상 경로를 잘 보자**
3. **명령어의 결과 영어를 잘 읽자**

