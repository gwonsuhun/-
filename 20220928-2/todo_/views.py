from multiprocessing import context
from django.shortcuts import render, redirect
from .models import Todo


def index(request):
    check = Todo.objects.all()
    context = {"check": check}
    return render(request, "todo_/index.html", context)


def create(request):
    content = request.GET.get("content_")
    priority = request.GET.get("priority_")
    deadline = request.GET.get("deadline_")
    Todo.objects.create(
        content=content,
        priority=priority,
        deadline=deadline,
    )

    context = {
        "content": content,
        "priority": priority,
        "deadline": deadline,
    }
    return redirect("todo_:index")


def delete(request, pk):
    Todo.objects.get(id=pk).delete()
    return redirect("todo_:index")


def update(request, pk):
    Todo.completed = not Todo.completed
    <del>태그


# Create your views here.
