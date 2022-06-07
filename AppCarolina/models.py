from django.db import models

class Carrera(models.Model):

    nombre = models.CharField(max_length=40)
    comision = models.IntegerField()

    def __str__(self) -> str:
        return self.nombre+" "+str(self.comision)

class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self) -> str:
        return self.nombre+" "+str(self.apellido)

class Profesor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    profesion = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.nombre+" "+str(self.apellido)+" "+str(self.profesion)