from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from .models import Alumno

class EmailBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            alumno = Alumno.objects.get(correo_electronico=username)
            if check_password(password, alumno.password):
                return alumno
        except Alumno.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Alumno.objects.get(pk=user_id)
        except Alumno.DoesNotExist:
            return None