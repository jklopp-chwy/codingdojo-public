from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('new', views.new),
    path('create', views.create),
    path('<int:number>', views.number),
    path('<int:number>/edit', views.edit),
    path('<int:number>/destroy', views.destroy)
]