### 1. 깃허브 새로운 저장소 생성

2번 개발자는 새로운 저장소를 생성합니다.

### 2. 1번 개발자 저장소 clone

2번 개발자는 1번 개발자의 저장소를 clone 합니다

```bash
git clone --mirror (1번 개발자 페어 프로그래밍 저장소 주소)
cd (1번개발자의저장소이름)

ex) git clone --mirror 깃주소
그럼 레포지토리명으로 폴더가 생성
cd 레포지토리명 폴더
```

### 3. 복사한 저장소의 원격 저장소 설정

2번 개발자는 새롭게 생성한 원격 저장소를 복사해온 프로젝트의 원격 저장소로 설정합니다.

```bash
git remote set-url --push origin (2번 개발자의 새롭게 생성한 저장소 주소)
```

### 4. push

2번 개발자는 프로젝트를 Push 합니다.

```bash
git push --mirror
```



## 페어프로그래밍 흐름

```bash
개발환경설정
1번.
1. 깃허브 저장소와 장고 프로젝트를 생성
- 2번 사람을 콜라보레이터로 초대

⊳ 그전에 반드시 
git init
git add .
git remote [저장소 주소]
git commit

2. 생성한 저장소에 장고 프로젝트를 push
- .gitignore : 가상환경을 ignore
- pip freeze > requirements.txt : 패키지 목록을 생성

2번.
3. 2번 사람이 clone
4. 2번사람만 가상환경 생성과 requirements.txt 설치
- pip install -r requirements.txt 

5. 2번사람만 앱을 생성
6. add / commit / push
7. 1번 pull
- git pull
--------------------------------

개발 진행
# 드라이버 <-> 네비게이터 전환할 때
드라이버 : add commit push
네비게이터 : pull

항상 두 사람이 같은 코드를 유지해야한다.
```

