from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.shows),
    path('shows', views.shows),
    path('shows/<int:id>', views.get_shows),
    path('shows/<int:id>/delete', views.delete_shows),
    path('shows/new_show', views.new_shows),
    path('shows/create_show', views.create_shows),
    path('shows/<int:id>/edit_show', views.edit_shows),
    path('shows/<int:id>/edit', views.edit)
]