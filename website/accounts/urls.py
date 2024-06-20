from django.urls import path
from . import views

urlpatterns = [
    path('', views.micuenta,name="micuenta"),
    path('user_login', views.user_login,name="user_login"),
    path('user_logout', views.user_logout,name="user_logout"),
    path('user_register', views.user_register,name="user_register"),
]