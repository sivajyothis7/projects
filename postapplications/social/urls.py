from django.urls import path
from social import views

urlpatterns=[
    path("register",views.RegisterView.as_view(),name="register"),
    path("login",views.LoginView.as_view(),name="signin"),

]