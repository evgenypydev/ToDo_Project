from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ToDo
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
def index(request):
    todos = ToDo.objects.all()
    return render(request, "todoapp/index.html", {"todolist": todos, "title": "Main page"})


@require_http_methods(["POST"])
@csrf_exempt
def add(request):
    title = request.POST["title"]
    description = request.POST["description"]
    todo = ToDo(title=title, description=description)
    todo.save()
    return redirect("index")


@require_http_methods(["POST"])
@csrf_exempt
def edit(request, todo_id):
    todo = ToDo.objects.get(id=todo_id)
    todo.title = request.POST["title"]
    todo.description = request.POST["description"]
    todo.save()
    return redirect("index")


def update(request, todo_id):
    todo = ToDo.objects.get(id=todo_id)
    todo.is_complete = not todo.is_complete
    todo.save()
    return redirect("index")


def delete(request, todo_id):
    todo = ToDo.objects.get(id=todo_id)
    todo.delete()
    return redirect("index")



