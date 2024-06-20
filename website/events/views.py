from django.shortcuts import render, redirect
from events.models import Videojuegos,Favoritos
from django.contrib.auth.models import User

def home(request):
    videojuegos = Videojuegos.objects.all()
    return render(request,'index.html',{'videojuegos':videojuegos})

def videojuego(request,genero,id,titulo):
    videojuego =  Videojuegos.objects.get(id=id)
    return render(request,'videojuego.html',{'videojuego':videojuego})

def user_favorito(request):
    videojuego_id = request.POST["favorito_id"]
    user_id = request.user.id
    if Favoritos.objects.filter(user_id=user_id).filter(videojuegos_id=videojuego_id):
        return redirect('home')
    else:
        favorito = Favoritos.objects.create(videojuegos_id=videojuego_id, user_id=user_id)
        favorito.save()
    return redirect('home')

def user_favorito_delete(request):
    videojuego_id = request.POST["favorito_id"]
    user_id = request.user.id
    if Favoritos.objects.filter(user_id=user_id).filter(videojuegos_id=videojuego_id):
        favorito = Favoritos.objects.filter(user_id=user_id).filter(videojuegos_id=videojuego_id)
        favorito.delete()
    return redirect('micuenta')