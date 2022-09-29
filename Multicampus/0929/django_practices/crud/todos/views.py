from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.


def index(request):
    todos = Todo.objects.all()
    context = {
        "todos": todos,
    }
    return render(request, "todos/index.html", context)


def create(request):
    title = request.GET.get("title___")
    content = request.GET.get("content___")
    priority = request.GET.get("priority___")
    deadline = request.GET.get("deadline___")

    Todo.objects.create(
        title=title,
        content=content,
        priority=priority,
        deadline=deadline,
    )
    return redirect("todos:index")


def update(request, pk_):
    # update할 특정 데이터를 불러온다 -> pk_를 사용해서
    todo = Todo.objects.get(pk=pk_)
    title_ = request.GET.get("title___")
    content_ = request.GET.get("content___")

    # 데이터를 수정
    todo.title = title_
    todo.content = content_

    # 데이터를 수정한 것을 반영(save)
    todo.save()

    # 데이터의 디테일 페이지로 리다이렉트
    return redirect("todos:detail", todo.pk)


def detail(request, pk_):
    # get() 메소드를 사용해서 특정 pk의 데이터를 불러온다.
    # 불러온 데이터를 변수에 할당
    todo = Todo.objects.get(pk=pk_)
    context = {
        "todo": todo,
    }
    return render(request, "todos/detail.html", context)


def edit(request, pk_):
    todo = Todo.objects.get(pk=pk_)
    context = {
        "todo": todo,
    }
    return render(request, "todos/edit.html", context)


def change(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    if todo.completed == False:
        todo.completed = True
    else:
        todo.completed = False

    todo.save()
    return redirect("todos:index")


def delete(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    todo.delete()

    return redirect("todos:index")
