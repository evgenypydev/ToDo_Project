from django.db import models

class ToDo(models.Model):
    title = models.CharField("Task name", max_length=100)
    description = models.CharField("Task description", max_length=200)
    is_complete = models.BooleanField("Complete", default=False)
    deadline = models.DateField()

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"

    def __str__(self):
        return f"{self.title} - {self.description}"