from django.urls import path
from django.http import HttpResponse
from . import views

urlpatterns = [
    path('', views.home),
    path('alta-de-personas/', views.altaPersonas, name="altaPersonas"),
]
