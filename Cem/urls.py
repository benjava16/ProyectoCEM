from django.urls import path
from . import views
urlpatterns = [
    # Usar una cadena vacía para que sea la URL de inicio.
    path("", views.inicio, name="inicio"),
    path('registro/', views.registro_alumno, name='registro_alumno'),
    path('login/', views.login_view, name='login'),  # Nueva URL para inicio de sesión


]