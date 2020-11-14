from django.urls import path
from django.http import HttpResponse

from . import views

urlpatterns = [
    path('', views.home, name="homePage"),
    path('iniciar-sesion/', views.login, name="iniciarSesion"),
    path('crear-cuenta/', views.crearCuenta, name="crearCuenta"),
    path('alta-de-personas/', views.altaPersonas, name="altaPersonas"),
    path('perfil/<str:pk>', views.perfil, name="perfil"),
    path('proporcionar-pista/<str:pk>', views.proporcionarPista, name="pista"),
]
