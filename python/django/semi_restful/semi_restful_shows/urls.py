from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.shows),
    path('shows', views.shows),
    path('shows/<int:id>', views.get_shows),
    path('shows/<int:id>/delete', views.delete_shows)
]