from django.urls import path
from . import views
 
app_name = 'instructores'
 
urlpatterns = [
    path('', views.main, name='main'),
    path('instructores/', views.instructores, name='instructores'),
    path('instructores/details/<int:id>', views.details, name='details'),
    path('instructores/crear', views.InstructorCreateView.as_view(), name='crear'),
    path('instructores/editar/<int:Instructor_id>', views.InstructorUpdateView.as_view(), name='editar'),
    path('instructores/eliminar/<int:Instructor_id>', views.InstructorDeleteView.as_view(), name='eliminar_Instructor'),
]