from django.urls import path
from AppCarolina.views import carrera, profesores, carreras, estudiantes, inicio, carreraFormulario, profesorFormulario, estudianteFormulario, busquedaComision, buscar


urlpatterns = [
    path('carrera/', carrera, name='Carrera'),
    path('profesores/', profesores, name='Profesores'),
    path('carreras/', carreras, name='Carreras'),
    path('estudiantes/', estudiantes, name='Estudiantes'),
    path('inicio/', inicio, name='Inicio'),
    path('carreraFormulario/', carreraFormulario, name='CarreraFormulario'),
    path('profesorFormulario/', profesorFormulario, name='ProfesorFormulario'),
    path('estudianteFormulario/', estudianteFormulario, name='EstudianteFormulario'),
    path('busquedaComision/', busquedaComision, name='BusquedaComision'),
    path('buscar/', buscar, name='Buscar'),
]
