from django.shortcuts import render,redirect
from bookapp.models import Books
from django.contrib.auth.models import User
from django.views.generic import View,CreateView,TemplateView,DetailView,ListView
from django.contrib.auth import authenticate,login,logout
from bookapp import forms
from django.urls import reverse_lazy
from django.contrib import messages
# Create your views here.

# class SignUpView(View):
#     def get(self,request,*args,**kwargs):
#         form=forms.RegistrationForm()
#         return render(request,"registration.html",{"form":form})
#
#     def post(self,request,*args,**kwargs):
#         form=forms.RegistrationForm(request.POST)
#         if form.is_valid():
#             User.objects.create_user(**form.cleaned_data)
#             return redirect("signin")
#         else:
#             return render(request, "registration.html", {"form": form})

class SignUpView(CreateView):
    model = User
    form_class = forms.RegistrationForm
    template_name = "registration.html"
    success_url =reverse_lazy("signin")

    def form_valid(self, form):
        messages.success(self.request, "account has been created")
        return super().form_valid(form)




class LoginView(View):
    def get(self,request,*args,**kwargs):
        form=forms.LogInForm()
        return render(request,"login.html",{"form":form})

    def post(self,request,*args,**kwargs):
        form=forms.LogInForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            user=authenticate(request,username=uname,password=pwd)
            if user:
                login(request,user)
                return redirect("index")
            else:
                return render(request,"login.html",{"form":form})


class HomePageView(TemplateView):
    template_name = "home.html"


class AddBookView(CreateView):
    model = Books
    form_class = forms.AddBookForm
    template_name ="add-book.html"
    success_url = reverse_lazy("list-book")

    def form_valid(self, form):
        form.instance.user=self.request.user
        messages.success(self.request,"book added successfully")
        return super().form_valid(form)

class BookListView(ListView):
    model = Books
    context_object_name ="books"
    template_name ="booklist.html"
