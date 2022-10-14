# 페어프로그래밍 가이드

```bash
# 브랜치 생성 & 전환
git checkout -b [브랜치명]

# git checkout [브랜치명] : 브랜치를 전환합니다.
# git checkout -b [브랜치명] : 브랜치를 생성하고 전환합니다. 동일한 브랜치가 있으면 오류가 발생합니다.
```

```bash
git add .

git commit -m '커밋 메세지'

git push origin [브랜치명]
```

```bash
# master 브랜치로 전환
git checkout master

# master 브랜치 Pull
git pull origin master

# 토픽 브랜치 삭제
git branch -d [토픽 브랜치명]
```

- 이렇게 반복적으로 개발



# Mirror 방법

## 1. 저장소 clone

```bash
git clone --mirror (1번 개발자 페어 프로그래밍 저장소 주소)
cd (1번개발자의저장소이름)

ex) git clone --mirror 깃주소
그럼 레포지토리명으로 폴더가 생성
cd 레포지토리명 폴더
```



## 2. 복사한 저장소의 원격 저장소 설정

```bash
git remote set-url --push origin (2번 개발자의 새롭게 생성한 저장소 주소)
```



## 3. push

```bash
git push --mirror
```

