from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    context = {}
    return render(request, "files/index.html", context)

def altaPersonas(request):
    context = {}
    return render(request, "files/registration.html", context)
