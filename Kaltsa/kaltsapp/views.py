from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import *
from .forms import MissingPersonForm, giveClueForm, CreateUserForm, UserProfileForm


def home(request):
    personsData = MissingPerson.objects.all()
    context = {'personsData': personsData}

    return render(request, "files/index.html", context)

def crearCuenta(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        # profileForm = CreateUserProfile()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()

                return redirect('iniciarSesion')
        context = {'form':form}

        return render(request, "files/createAccount.html", context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, "files/login.html", context)

def logoutUser(request):
    logout(request)

    return redirect('iniciarSesion')

@login_required(login_url="iniciarSesion")
def altaPersonas(request):
    form = MissingPersonForm()

    if request.method == 'POST':
        form = MissingPersonForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            # missing_person = form.cleaned_data.get('full_name')

            return redirect('home')
    context = {'form': form}

    return render(request, "files/registration.html", context)

@login_required(login_url="iniciarSesion")
def perfilUsuario(request):

    context = {}

    return render(request, "files/userProfile.html", context)

def perfil(request, pk):
    profile = MissingPerson.objects.get(id=pk)
    context = {'profile': profile}

    return render(request, "files/profile.html", context)

def proporcionarPista(request, full_name, pk):
    pista = MissingPerson.objects.get(full_name=full_name, id=pk)
    # clue_of = MissingPerson.objects.all()
    form = giveClueForm()

    if request.method == 'POST':
        form = giveClueForm(request.POST)
        if form.is_valid():
            form.save()
            Clue.objects.create(
                clue_of=pista,
            )

            return redirect('home')

    context = {'form':form, 'pista':pista}

    return render(request, "files/giveClue.html", context)
