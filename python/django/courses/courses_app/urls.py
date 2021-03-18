from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.courses),
    path('shows', views.courses),
    path('courses/create_course', views.create_courses),
    path('courses/delete_course/<int:id>/', views.delete_courses)
]