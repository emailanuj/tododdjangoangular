from django.db import models
class ToDo(models.Model):
    todo_text=models.CharField(max_length=100)
    done=models.BooleanField()

    def __str__(self):
        return self.todo_text

