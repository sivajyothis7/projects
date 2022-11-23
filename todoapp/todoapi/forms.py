from django import forms
from django.contrib.auth.models import User
from todoapi.models import Todo
from django.contrib.auth.forms import UserCreationForm
# class RegistrationForm(forms.Form):
#     first_name=forms.CharField(max_length=100)
#     last_name=forms.CharField(max_length=150)
#     username=forms.CharField(max_length=50)
#     email=forms.EmailField()
#     password=forms.CharField(max_length=100)

class RegistrationForm(UserCreationForm):

    password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
    class Meta:
        model=User
        fields=["first_name","last_name","username","email","password1","password2"]
        widgets={

            "email":forms.TextInput(attrs={"class":"form-control"}),
            "first_name":forms.TextInput(attrs={"class":"form-control"}),
            "last_name":forms.TextInput(attrs={"class":"form-control"}),
            "username":forms.TextInput(attrs={"class":"form-control"}),
        }


class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))


class TodoForm(forms.ModelForm):
    class Meta:
        model=Todo
        fields=["task_name"]

        widgets={
            "task_name":forms.TextInput(attrs={"class":"form-control"})
        }

class TodoChangeForm(forms.ModelForm):
    class Meta:
        model=Todo
        exclude=("user",)