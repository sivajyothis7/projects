from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Todo(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    task_name=models.CharField(max_length=100)
    status=models.BooleanField(default=False)
    created_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task_name

#registration
  #get --> return registration template
  #post -->
#login
#addTodo
#listtodos
#updateTodo
#deleteTodo
