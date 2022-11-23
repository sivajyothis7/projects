from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView
from todoapi import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from todoapi.models import Todo
from django.contrib import messages
from todoapi.decorators import signin_required
from django.utils.decorators import method_decorator

# Create your views here.

# class SignUpView(View):
#     def get(self,request,*args,**kwargs):
#         form=forms.RegistrationForm()
#         return render(request,"registration.html",{"form":form})
#
#     def post(self,request,*args,**kwargs):
#         # print(request.POST.get("firstname"))
#         # print(request.POST.get("lastname"))
#         form=forms.RegistrationForm(request.POST)
#         if form.is_valid():
#             User.objects.create_user(**form.cleaned_data)
#             messages.success(request,"account has been created")
#             return redirect("signin")
#             # print("saved")
#         else:
#             messages.error(request,"registration failed")
#             return render(request,"registration.html",{"form":form})

class SignUpView(CreateView):
    model = User
    form_class = forms.RegistrationForm
    template_name = "registration.html"
    success_url = reverse_lazy("signin")

    def form_valid(self, form):
        messages.success(self.request,"account has been created")
        return super().form_valid(form)

class LoginView(View):
    def get(self,request,*args,**kwargs):
        form=forms.LoginForm()
        return render(request,"login.html",{"form":form})

    def post(self,request,*args,**kwargs):
        form=forms.LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            user=authenticate(request,username=uname,password=pwd)
            if user:
                login(request,user)
                messages.success(request,"login successful")
                return redirect("index")
            else:
                messages.error(request,"invalid credentials")
                return render(request,"login.html",{"form":form})



# class HomePageView(View):
#     def get(self,request,*args,**kwargs):
#         return render(request,"home.html")

@method_decorator(signin_required,name="dispatch")
class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["todos"]=Todo.objects.filter(user=self.request.user,status=False)
        return context

@method_decorator(signin_required,name="dispatch")
class SignOutView(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("signin")


# class TodoAddView(View):
#     def get(self,request,*args,**kwargs):
#         form=forms.TodoForm()
#         return render(request,"add-todo.html",{"form":form})
#
#     def post(self,request,*args,**kwargs):
#         form=forms.TodoForm(request.POST)
#         if form.is_valid():
#
#             form.instance.user=request.user #for modelform
#             form.save()
#             # Todos.objects.create(**form.cleaned_data,user=request.user)  #for normalform
#             messages.success(request,"todo is added")
#             return redirect("index")
#         else:
#             messages.error(request,"failed to add todo")
#             return render(request,"add-todo.html",{"form":form})

@method_decorator(signin_required,name="dispatch")
class TodoAddView(CreateView):
    model = Todo
    form_class = forms.TodoForm
    template_name = "add-todo.html"
    success_url = reverse_lazy("todos-list")

    def form_valid(self, form):
        form.instance.user=self.request.user
        messages.success(self.request,"todo has been added")
        return super().form_valid(form)

# class TodoListView(View):
#
#     def get(self,request,*args,**kwargs):
#         all_todos=Todo.objects.filter(user=request.user)
#         return render(request,"todolist.html",{"todos":all_todos})

@method_decorator(signin_required,name="dispatch")
class TodoListView(ListView):
    model = Todo
    context_object_name = "todos"
    template_name = "todolist.html"

    def get_queryset(self): #to customise queryset
        return Todo.objects.filter(user=self.request.user)

@signin_required
def delete_todo(request,*args,**kwargs):
    id=kwargs.get("id")
    Todo.objects.get(id=id).delete()
    messages.success(request,"todo deleted successfully")
    return redirect("todos-list")

# class TodoDetailView(View):
#     def get(self,request,*args,**kwargs):
#         id=kwargs.get("id")
#         todos=Todo.objects.get(id=id)
#         return render(request,"todo-detail.html",{"todos":todos})

@method_decorator(signin_required,name="dispatch")
class TodoDetailView(DetailView):
    model = Todo
    context_object_name = "todos"
    template_name = "todo-detail.html"
    pk_url_kwarg = "id" #or change "id" to "pk" in url

# class TodoEditView(View):
#     def get(self,request,*args,**kwargs):
#         id=kwargs.get("id")
#         todo=Todo.objects.get(id=id)
#         form=forms.TodoChangeForm(instance=todo)
#         return render(request,"todo-edit.html",{"form":form})
#
#     def post(self,request,*args,**kwargs):
#         id=kwargs.get("id")
#         todo=Todo.objects.get(id=id)
#         form=forms.TodoChangeForm(request.POST,instance=todo)
#         if form.is_valid():
#             form.save()
#             msg="todo has been changed"
#             messages.success(request,msg)
#             return redirect("todos-list")
#         else:
#             msg="todo update failed"
#             messages.error(request,msg)
#             return render(request,"todo-edit.html",{"form":form})

@method_decorator(signin_required,name="dispatch")
class TodoEditView(UpdateView):
    model = Todo
    form_class = forms.TodoChangeForm
    template_name = "todo-edit.html"
    success_url = reverse_lazy("todos-list")
    pk_url_kwarg = "id"

    def form_valid(self, form):
        messages.success(self.request,"todo has been updated")
        return super().form_valid(form)