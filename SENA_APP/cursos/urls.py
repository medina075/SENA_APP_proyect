from django.urls import path
from . import views

app_name = 'cursos'

urlpatterns = [
    path('', views.main, name='main'),
    path('cursos/', views.cursos, name='cursos'),
    path('cursos/details/<int:id>', views.details, name='details'),
]