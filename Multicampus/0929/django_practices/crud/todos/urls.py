from django.urls import path
from . import views


# url namespace
# url을 이름으로 분류하는 기능

app_name = "todos"

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("detail/<int:pk_>", views.detail, name="detail"),
    path("change/<int:todo_pk>", views.change, name="change"),
    path("edit/<int:pk_>", views.edit, name="edit"),
    path("delete/<int:todo_pk>", views.delete, name="delete"),
    path("update/<int:pk_>", views.update, name="update"),
]
