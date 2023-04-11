from django.urls import path
from .views import index, add, update, delete, edit

urlpatterns = [
    path("", index, name="index"),
    path("add", add, name="add"),
    path("update/<int:todo_id>", update, name="update"),
    path("edit/<int:todo_id>", edit, name="edit"),
    path("delete/<int:todo_id>", delete, name="delete"),
]