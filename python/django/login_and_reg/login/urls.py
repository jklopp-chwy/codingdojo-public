from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home),
    path('register', views.register),
    path('logout', views.logout),
    path('login',views.login)
]