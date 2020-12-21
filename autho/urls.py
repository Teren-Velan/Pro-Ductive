from django.urls import path
from django.contrib.auth import views

from django.contrib import admin
from . import views

app_name = "autho"

urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('signin/', views.signin, name="signin"),
    path('logout/', views.signout, name="logout"),
]
