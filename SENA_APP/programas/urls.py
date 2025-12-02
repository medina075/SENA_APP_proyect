from django.urls import path
from . import views

app_name = 'programas'

urlpatterns = [
    path('', views.main, name='main'),
    
    path('programas/', views.programas, name='programas'),
    path('programas/details/<int:id>', views.details, name='details'),
]