from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.
from .models import *
from .forms import MissingPersonForm


def home(request):
    personsData = MissingPerson.objects.all()
    context = {'personsData': personsData}

    return render(request, "files/index.html", context)

def altaPersonas(request):

    form = MissingPersonForm()
    if request.method == 'POST':
        form = MissingPersonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            missing_person = form.cleaned_data.get('full_name')

            return redirect('homePage')
    context = {'form': form}

    return render(request, "files/registration.html", context)


def perfil(request, pk):
    profile = MissingPerson.objects.get(id=pk)

    context = {'profile': profile}

    return render(request, "files/profile.html", context)
