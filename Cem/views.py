from django.shortcuts import render, redirect
from .forms import RegistroAlumnoForm
from django.contrib.auth.hashers import make_password


def inicio(request):
    return render(request, 'html/inicio.html')

def registro_alumno(request):
    if request.method == 'POST':
        form = RegistroAlumnoForm(request.POST)
        if form.is_valid():
            alumno = form.save(commit=False)
            # Cifrar la contraseña
            alumno.contraseña = make_password(form.cleaned_data['contraseña'])
            alumno.save()
            return redirect('inicio')  # Cambia 'inicio' por la vista a donde quieras redirigir
    else:
        form = RegistroAlumnoForm()
    
    return render(request, 'html/registro.html', {'form': form})

