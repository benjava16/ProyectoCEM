from django.shortcuts import render, redirect
from .forms import RegistroAlumnoForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required



@login_required
def inicio(request):
    return render(request, 'html/inicio.html')

def registro_alumno(request):
    if request.method == 'POST':
        form = RegistroAlumnoForm(request.POST)
        if form.is_valid():
            alumno = form.save(commit=False)
            alumno.password = make_password(form.cleaned_data['password'])  # Cambié 'contraseña' por 'password'
            alumno.save()
            return redirect('inicio')
    else:
        form = RegistroAlumnoForm()
    
    return render(request, 'html/registro.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        correo = request.POST['correo_electronico']
        password = request.POST['password']  # Cambié 'contraseña' por 'password'
        
        # Usar authenticate para verificar las credenciales
        user = authenticate(request, username=correo, password=password)  # Cambié 'contraseña' por 'password'
        
        if user is not None:
            login(request, user)  # Iniciar sesión
            return redirect('inicio')  # O la página que desees
        else:
            return render(request, 'html/login.html', {'error': 'Credenciales inválidas'})
    
    return render(request, 'html/login.html')