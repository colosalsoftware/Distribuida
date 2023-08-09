# views.py
from django.shortcuts import render, redirect
from .models import Usuario
from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == 'POST':
        # Realizar autenticación personalizada aquí (por ejemplo, verificar en tu propia base de datos)
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Realizar la verificación del usuario en tu propia lógica
        if custom_authentication(email, password):
            # Aquí puedes establecer una sesión o token personalizado para el usuario
            return render(request, 'miapp/home.html')

    return render(request, 'miapp/login.html')

    
# views.py

def custom_authentication(email, password):
    try:
        # Intentar obtener un usuario con el correo electrónico proporcionado
        user = Usuario.objects.get(email=email)
        
        # Verificar la contraseña
        if user.password == password:
            return True
        else:
            return False
    except Usuario.DoesNotExist:
        return False

def register_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        # Verificar que las contraseñas coincidan
        if password == confirm_password:
            # Crear un nuevo usuario en la base de datos
            nuevo_usuario = Usuario(email=email, password=password)
            nuevo_usuario.save()
            return redirect('login')  # Redirigir a la página de inicio de sesión
    return render(request, 'miapp/register.html')
