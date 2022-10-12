## 복습 & 실습

[참고]

- Django Auth 기본
    - [https://docs.djangoproject.com/en/4.1/topics/auth/default/](https://docs.djangoproject.com/en/4.1/topics/auth/default/)
- Django User Model
    - [https://docs.djangoproject.com/en/4.1/ref/contrib/auth/](https://docs.djangoproject.com/en/4.1/ref/contrib/auth/)
- Custominzing
    - [https://docs.djangoproject.com/en/4.1/topics/auth/customizing/](https://docs.djangoproject.com/en/4.1/topics/auth/customizing/)
- 비밀번호 암호화
    - [https://docs.djangoproject.com/en/3.2/topics/auth/passwords/](https://docs.djangoproject.com/en/3.2/topics/auth/passwords/)
    - [https://d2.naver.com/helloworld/318732](https://d2.naver.com/helloworld/318732)



## Django Auth

* Django authentication system(인증 시스템)은 인증과 권한 부여를 함께 제공하고 있음
  * User
  * 권한 및 그룹
  * 암호 해시 시스템
  * Form 및 View 도구
  * 기타 적용가능한 시스템
* 필수 구성은 settings.py의 INSTALLED_APPS에서 확인 가능
  * django.contrib.auth
* Authentication(인증)
  * 신원 확인
  * 사용자가 자신이 누구인지 확인하는 것
* Authorization(권한, 허가)
  * 권한 부여
  * 인증된 사용자가 수행할 수 있는 작업을 결정



## 사전 설정

### 프로젝트 생성



### 가상환경 생성

```python
# 가상환경 생성
python -m venv venv
```



### 가상환경 실행

```python
# 가상환경 실행
. venv/scripts/activate
```



### 패키지 설치

```python
# 미리 준비된 패키지 일괄 설치
pip instrall -r requirements.txt
```



### 프로젝트 생성 및 앱 생성

```python
django-admin startproject pjt . #pjt는 프로젝트명
```

```python
python manage.py startapp {app name} # 프로젝트 내부 각 앱마다 생성
```



### 모델 마이그레이션

> **주의: 마이그레이션은 마지막에 실행 할 것!**
>
> - 프로젝트 도중 모델을 수정하게 될 경우 에러가 발생한다.

```bash
python manage.py makemigrations

python manage.py migrate
```



### 데이터베이스 초기화

> - migrations 파일 삭제
> - migrations 폴더 및 __init__.py는 삭제하지 않음
> - 번호가 붙은 파일만 삭제
> - db.sqlite3 삭제



### 서버 실행

```bash
python manage.py runserver
```



### 앱설정

``` python
# settings.py

INSTALLED_APPS = [
 'accounts',
  ...
]

```



## url설정

``` python
# 프로젝트 폴더 urls.py

urlpatterns = [
  path('accounts/', include('accounts.urls')),
]
```



## 각각의 애플리케이션의 url설정

``` python
# 애플리케이션 폴더 urls.py

# url을 변수화해서 사용하기 위해 app_name 사용 
app_name = 'accounts'

urlpatterns = [
	pass
]
```



## 커스텀 유저 Auth 설정

``` python
# settings.py에 추가
AUTH_USER_MODEL = 'accounts.User'
```



## 데이터 형식 설정

``` python
# models.py

# Django에서는 User모델을 기본적으로 제공한다.
# Django는 새 프로젝트를 시작하는 경우 비록 기본 User모델이 충분 하더라도 커스텀 모델을 성정하는 것을 강력하게 권장한다. 
# -> 커스텀 User모델은 기본 User 모델과 동일하게 작동 하면서도 필요한 경우 나중에 맞춤 설정할 수 있기 때문
from django.db import models
from django.contrib.auth.models import AbstractUser 

# Abstract User를 상속받아서 사용
class User(AbstractUser):
  pass
```



## 실습

#### User 객체 활용

* User 객체는 인증 시스템의 가장 기본
* 기본 속성
  * username
  * password 
    * 여기서 암호는 저장이 필수적이며 별도의 해시 처리(SHA256, secure hash algoritm)가 필요하다.
  * email
  * first_name
  * last_name



``` python
# User 생성
user = User.objects.create_user('hong', 'hong@gmail.com', '1q2w3e4r')
# User 비밀번호 변경
user = User.objects.get(pk=2)
User.set_password("new password")
User.save()
# User 인증(비밀번호 확인)
from django.contrib.auth import authenticate
user = authenticate(username='john', password='secret')
```



## 회원가입 구현해보기

#### urls.py

``` python
# 애플리케이션 폴더 urls.py
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
  path('signup/', views.signup, name='signup'),
]
```



#### views.py

``` python
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from accounts.models import User

def signup(request):
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('articles:index')
  else:
  	form = UserCreationForm()
  context = {
    'form': form
  }
  return render(request, 'accounts/signup.html', context)
```



#### templates > accounts > signup.html 생성

``` html
{% raw %}{% extends 'base.html' %}
{% load django_bootstrap5 %}
{% block body %}
<h1>회원가입</h1>
<form action="" method="POST">
 {% csrf_token %}
 {% bootstrap_form form %}
 {% bootstrap_button button %}
</form>
{% endblock body %}{% endraw %}
```



#### 어플리케이션 폴더 > forms.py 생성

``` python
from django.contrib.auth.forms import UserCreationForm
# from .models import User
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
  class Meta:
    model = get_user_model()
    fields = ('username', 'password')
```



#### views.py

``` python
from django.shortcuts import render
# from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm # 추가

from accounts.models import User

def signup(request):
  if request.method == 'POST':
    # CustomUserCreationForm을 가져옴
    form = CustomUserCreationForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('articles:index')
  else:
  	form = CustomUserCreationForm()
  context = {
    'form': form
  }
  return render(request, 'accounts/signup.html', context)
```



## 프로필 페이지 만들기

#### urls.py

``` python
# 애플리케이션 폴더 urls.py
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
  path('signup/', views.signup, name='signup'),
  path('<int:pk>/', views.detail, name='detail'),
]
```



#### views.py

``` python
from django.shortcuts import render
# from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm # 추가
# from .models import User
from django.contrib.auth import get_user_model
  
def signup(request):
  if request.method == 'POST':
    # CustomUserCreationForm을 가져옴
    form = CustomUserCreationForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('articles:index')
  else:
  	form = CustomUserCreationForm()
  context = {
    'form': form
  }
  return render(request, 'accounts/signup.html', context)

def detail(request, pk):
  # 유저를 참조할땐 상속을 받고있기때문에 get_user_model을 import 해서 함수로 참조
	user = get_user_model().objects.get(pk=pk)
  context = {
    'user': user
  }
  return render(request, 'accounts/detail.html', context)
```



#### detail.html

``` python
{% raw %}{% extends 'base.html' %}

{% block body %}
<h1>{{ user.username }}님의 프로필</h1>

{% endblock body %}
{% endraw %}
```