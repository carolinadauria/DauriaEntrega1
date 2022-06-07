from django.contrib import admin

from AppCarolina.views import carreras, estudiantes, profesores
from .models import *


admin.site.register(Carrera)
admin.site.register(Profesor)
admin.site.register(Estudiante)
