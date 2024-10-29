from django.urls import path 
# from .views import RegisterView,LoginView
from . import views

urlpatterns = [
    path("register/", views.RegisterView, name="register"),
    path("login/", views.LoginView, name="login")
]
