from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ToDo
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.shortcuts import render
from django.contrib import messages


def edit(request, todo_id):
    todo = ToDo.objects.get(id=todo_id)
    if request.method == 'POST':
        todo.title = request.POST['title']
        todo.description = request.POST['description']
        todo.deadline = request.POST['deadline']
        todo.save()
        messages.success(request, 'Task successfully edited!')
        return redirect('index')
    context = {"todo": todo}
    return render(request, 'todoapp/edit.html', context)


def index(request):
    todos = ToDo.objects.all().order_by("deadline")
    return render(request, "todoapp/index.html", {"todolist": todos, "title": "Main page"})


@require_http_methods(["POST"])
@csrf_exempt
def add(request):
    title = request.POST["title"]
    description = request.POST["description"]
    deadline = request.POST["deadline"]
    todo = ToDo(title=title, description=description, deadline=deadline)
    todo.save()
    messages.success(request, 'Task successfully added!')
    return redirect("index")


def update(request, todo_id):
    todo = ToDo.objects.get(id=todo_id)
    todo.is_complete = not todo.is_complete
    todo.save()
    messages.success(request, 'Task successfully updated!')
    return redirect("index")


def delete(request, todo_id):
    todo = ToDo.objects.get(id=todo_id)
    todo.delete()
    messages.success(request, 'Task successfully deleted!')
    return redirect("index")



