from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User
from events.models import Videojuegos,Favoritos

def micuenta(request):
    videojuegos = Videojuegos.objects.all()
    favoritos = Favoritos.objects.filter(user_id=request.user.id)
    return render(request,'login.html',{'videojuegos':videojuegos,'favoritos':favoritos})

def user_login(request):
    if request.method == "POST":
        intentos = request.session.get('intentos', 0)
        if intentos < 5 :
            if request.POST["username"] == '' or request.POST["password"] == '':
                messages.success(request,("Hay campos en blanco."))
                return redirect('micuenta')
            else:
                username = request.POST["username"]
                password = request.POST["password"]
                user = authenticate(request, username=username, password=password)
                request.session['intentos'] = intentos + 1
                if user:
                    login(request, user)
                    request.session['intentos'] = 0
                    messages.success(request,("Has iniciado sesion correctamente."))
                    return redirect('micuenta')
                else:
                    messages.success(request,("Error de autentificacion, vuelve a intentarlo."))
                    return redirect('micuenta')
        else:
            messages.success(request,("Has superado los intentos permitidos."))
            return redirect('micuenta')
    else:
        return redirect('micuenta')

def user_logout(request):
    logout(request)
    messages.success(request,("Has cerrado la session correctamente."))
    return redirect('micuenta')

def user_register(request):
    if request.method == "POST":
        form_registro = UserCreationForm(request.POST)
        if form_registro.is_valid():
            form_registro.save()
            username = form_registro.cleaned_data['username']
            password1 = form_registro.cleaned_data['password1']
            user = authenticate(request, username=username, password=password1)
            if user:
                login(request, user)
                messages.success(request,("Cuenta creada con exito."))
                return redirect('micuenta')
            else:
                messages.success(request,('Se produjo un error,vuelve a intentarlo.'))
                return redirect('user_register')
        else:
            messages.success(request,('Se produjo un error,vuelve a intentarlo.'))
            return redirect('user_register')
    else:
        return render(request, 'registro.html')