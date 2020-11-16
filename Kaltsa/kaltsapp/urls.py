from django.urls import path
from django.http import HttpResponse

from . import views

urlpatterns = [
    path('', views.home, name="home"),

    path('iniciar-sesion/', views.loginPage, name="iniciarSesion"),
    path('cerrar-sesion/', views.logoutUser, name="cerrarSesion"),

    path('crear-cuenta/', views.crearCuenta, name="crearCuenta"),

    path('alta-de-personas/', views.altaPersonas, name="altaPersonas"),

    path('perfil/', views.perfilUsuario, name="perfilUsuario"),

    path('perfil/<str:pk>', views.perfil, name="perfil"),
    path('proporcionar-pista/<str:full_name>/<str:pk>', views.proporcionarPista, name="pista"),
]
