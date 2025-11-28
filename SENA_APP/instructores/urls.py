from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('instructores/', views.instructores, name='instructores'),
    path('instructores/details/<int:id>', views.details, name='details'),
]