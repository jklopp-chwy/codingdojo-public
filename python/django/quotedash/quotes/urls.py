from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('quotes', views.quotes),
    path('add_quote', views.add_quote),
    path('delete_all', views.delete_all),
    path('edit_account/<int:id>', views.edit_account),
    path('update_account', views.update_account),
    path('user/<int:id>', views.user),
    path('delete_quote/<int:id>', views.delete_quote),
    path('like_quote/<int:id>', views.like_quote)
]