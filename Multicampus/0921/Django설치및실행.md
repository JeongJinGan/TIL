## 디렉토리(폴더) 생성

```bash
jj@DESKTOP-5N8TM5H MINGW64 ~/Desktop/hyper
$ mkdir server
```



## 디렉토리 이동

```bash
jj@DESKTOP-5N8TM5H MINGW64 ~/Desktop/hyper
$ cd server/

jj@DESKTOP-5N8TM5H MINGW64 ~/Desktop/hyper/server
$
```



## pip설치 리스트 확인

```bash
jj@DESKTOP-5N8TM5H MINGW64 ~/Desktop/hyper/server
$ pip list
Package            Version
------------------ ---------
certifi            2022.6.15
charset-normalizer 2.1.0
colorama           0.4.5
idna               3.3
numpy              1.23.2
pandas             1.4.4
pip                22.2.2
pyproj             3.3.1
python-dateutil    2.8.2
pytz               2022.2.1
requests           2.28.1
setuptools         58.1.0
six                1.16.0
tqdm               4.64.1
urllib3            1.26.10

```



## 가상환경 생성

> python -m venv [가상환경이름]

```bash
jj@DESKTOP-5N8TM5H MINGW64 ~/Desktop/hyper/server
$ python -m venv server-venv
```



## 가상환경 작동

> **❗경로 위치 확인!!**

```bash
jj@DESKTOP-5N8TM5H MINGW64 ~/Desktop/hyper/server
$ source server-venv/Scripts/activate
```



## 가상환경 종료

```bash
jj@DESKTOP-5N8TM5H MINGW64 ~/Desktop/hyper/server
$ deactivate
```



## 장고설치

> 최신버전을 사용하기에는 불안한 요소들이 있기 때문에 최신보다는 낮은 버전을 사용한다.
>
>  Long-term 유지보수된 버전이 상용하기 좋고, 안정적이다.
>
> $ pip install django // 제일 최신버전 다운

```bash
jj@DESKTOP-5N8TM5H MINGW64 ~/Desktop/hyper/server
$ pip install django==3.2.13
```



## SET-UP

>$ django-admin startproject [프로젝트이름] [시작경로]

```bash
jj@DESKTOP-5N8TM5H MINGW64 ~/Desktop/hyper/server
$ django-admin startproject firstpjt . 			// . => 현재폴더
```



## 실행

```bash
jj@DESKTOP-5N8TM5H MINGW64 ~/Desktop/hyper/server
$ python manage.py runserver

인터넷 브라우저 주소 => localhost:8000
```

