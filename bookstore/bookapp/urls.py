from bookapp import views
from django.urls import path

urlpatterns=[
    path("signup",views.SignUpView.as_view(),name="register"),
    path("login",views.LoginView.as_view(),name="signin"),
    path("home",views.HomePageView.as_view(),name="index"),
    path("home/add",views.AddBookView.as_view(),name="add-book"),
    path("home/all",views.BookListView.as_view(),name="list-book"),
]




