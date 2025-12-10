from django.urls import path
from . import views

app_name = 'aprendices'

urlpatterns = [
    path('', views.main, name='main'),
    path('aprendices/', views.aprendices, name='aprendices'),
    path('aprendices/details/<int:id>', views.details, name='details'),
    path('aprendices/crear', views.AprendizCreateView.as_view(), name='crear'),
    path('aprendices/editar/<int:aprendiz_id>', views.AprendizUpdateView.as_view(), name='editar'),
    path('aprendices/eliminar/<int:aprendiz_id>', views.AprendizDeleteView.as_view(), name='eliminar_aprendiz'),
]