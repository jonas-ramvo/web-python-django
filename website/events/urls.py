from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name="home"),
    path('videojuego/<str:genero>/<str:id>/<str:titulo>/', views.videojuego,name="videojuego"),
    path('user_favorito', views.user_favorito,name="user_favorito"),
    path('user_favorito_delete', views.user_favorito_delete,name="user_favorito_delete"),
]