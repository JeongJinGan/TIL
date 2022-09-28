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
    content = request.GET.get("content___")
    priority = request.GET.get("priority___")
    deadline = request.GET.get("deadline___")

    Todo.objects.create(
        content=content,
        priority=priority,
        deadline=deadline,
    )
    return redirect("todos:index")


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
