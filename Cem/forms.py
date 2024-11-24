from django import forms
from .models import Alumno

class RegistroAlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ['correo_electronico', 'nombre', 'telefono', 'apellido_paterno', 'apellido_materno', 'edad', 'pais', 'password']  # Cambié 'contraseña' por 'password'
    
    def clean_correo_electronico(self):
        correo = self.cleaned_data.get('correo_electronico')
        if Alumno.objects.filter(correo_electronico=correo).exists():
            raise forms.ValidationError("El correo ya está registrado.")
        return correo
