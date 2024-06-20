from django.db import models
from django.contrib.auth.models import User

class Fabricantes(models.Model):
    fabricante = models.CharField(max_length=500)

class Videojuegos(models.Model):
    titulo = models.CharField(max_length=500)
    portada = models.CharField(max_length=500)
    fabricante = models.ForeignKey(Fabricantes, on_delete=models.CASCADE)
    puntuacion = models.CharField(max_length=500)
    descripcion = models.CharField(max_length=500)

class Favoritos(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    videojuegos = models.ForeignKey(Videojuegos, on_delete=models.CASCADE)