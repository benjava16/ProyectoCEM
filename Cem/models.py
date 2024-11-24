from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class AlumnoManager(BaseUserManager):
    def create_user(self, correo_electronico, password=None, **extra_fields):  # Cambié 'contraseña' por 'password'
        if not correo_electronico:
            raise ValueError('El correo electrónico debe ser proporcionado')
        correo_electronico = self.normalize_email(correo_electronico)
        user = self.model(correo_electronico=correo_electronico, **extra_fields)
        user.set_password(password)  # Cambié 'contraseña' por 'password'
        user.save(using=self._db)
        return user

    def create_superuser(self, correo_electronico, password=None, **extra_fields):  # Cambié 'contraseña' por 'password'
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(correo_electronico, password, **extra_fields)

class Alumno(AbstractBaseUser):
    correo_electronico = models.EmailField(unique=True)
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    apellido_paterno = models.CharField(max_length=100, blank=True, null=True)
    apellido_materno = models.CharField(max_length=100, blank=True, null=True)
    edad = models.IntegerField(null=True, blank=True)
    pais = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=255, default='default_password')  # El campo de la contraseña ya está actualizado a 'password'
    last_login = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = AlumnoManager()

    USERNAME_FIELD = 'correo_electronico'
    REQUIRED_FIELDS = ['nombre']

    def __str__(self):
        return self.correo_electronico