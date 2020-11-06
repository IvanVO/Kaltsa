from django.urls import path
from django.http import HttpResponse

from . import views

urlpatterns = [
    path('', views.home, name="homePage"),
    path('alta-de-personas/', views.altaPersonas, name="altaPersonas"),
    path('perfil/<str:pk>', views.perfil, name="perfil"),
]
