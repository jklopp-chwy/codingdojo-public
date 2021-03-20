from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home),
    path('profile', views.profile),
    path('register', views.register),
    path('logout', views.logout),
    path('login',views.login),
    path('post', views.post),
    path('comment/<int:id>', views.comment),
    path('delete_all', views.delete_all)
]