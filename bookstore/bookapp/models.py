from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Books(models.Model):
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=100,null=True)
    publisher=models.CharField(max_length=190,null=True)
    price=models.PositiveIntegerField(default=100,null=True)
    quantity=models.PositiveIntegerField(default=1,null=True)


    def __str__(self):
        return self.title
