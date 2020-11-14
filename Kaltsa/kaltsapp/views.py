from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.
from .models import *
from .forms import MissingPersonForm, giveClueForm, CreateUserForm


def home(request):
    personsData = MissingPerson.objects.all()
    context = {'personsData': personsData}

    return render(request, "files/index.html", context)

def login(request):
    context = {}
    return render(request, "files/login.html", context)

def crearCuenta(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}

    return render(request, "files/createAccount.html", context)


def altaPersonas(request):
    form = MissingPersonForm()

    if request.method == 'POST':
        form = MissingPersonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # missing_person = form.cleaned_data.get('full_name')

            return redirect('homePage')
    context = {'form': form}

    return render(request, "files/registration.html", context)

def perfil(request, pk):
    profile = MissingPerson.objects.get(id=pk)
    context = {'profile': profile}

    return render(request, "files/profile.html", context)

def proporcionarPista(request, pk):
    pista = MissingPerson.objects.get(id=pk)

    form = giveClueForm()

    if request.method == 'POST':
        form = giveClueForm(request.POST)
        if form.is_valid():

            form.save()

            return redirect('homePage')

    context = {'form':form, 'pista':pista}

    return render(request, "files/giveClue.html", context)
