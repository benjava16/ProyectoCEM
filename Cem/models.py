from django.db import models

# Create your models here.
class Alumno(models.Model):
    nombre = models.CharField(max_length=50)
    apellido_paterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50)
    edad = models.PositiveIntegerField()
    correo_electronico = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=128)
    pais = models.CharField(max_length=50)
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.nombre} {self.apellido_paterno}"
