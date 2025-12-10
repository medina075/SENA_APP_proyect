from django.urls import path
from . import views

app_name = 'cursos'

urlpatterns = [
    path('', views.main, name='main'),
    path('cursos/', views.cursos, name='cursos'),
    path('cursos/details/<int:id>', views.details, name='details'),
    path('cursos/crear', views.CursoCreateView.as_view(), name='crear'),
    path('cursos/editar/<int:curso_id>', views.CursoUpdateView.as_view(), name='editar'),
    path('cursos/eliminar/<int:curso_id>', views.CursoDeleteView.as_view(), name='eliminar_curso'),
]