from django.urls import path
from . import views

# app_name은 왜 쓸까요?
# 우리는 기본적으로 URL을 모두 변수화해서 쓰고 있다
# Template, View에서 직접 '/accounts/' X
# app_name과 path 이름으로
urlpatterns = [
    path("", views.main, name="main"),
]

app_name = "accounts"

urlpatterns = [
    path("", views.index, name="index"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("detail/<int:pk>/", views.detail, name="detail"),
    path("update/", views.update, name="update"),
    path("password/", views.change_password, name="change_password"),
    path("delete/", views.delete, name="delete"),
    path("<int:pk>/follow/", views.follow, name="follow"),
]
