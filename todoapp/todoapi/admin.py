from django.contrib import admin

# Register your models here.
from todoapi.models import Todo

admin.site.register(Todo)