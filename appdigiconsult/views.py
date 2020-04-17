from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import *
from .models import *

# Create your views here.

# view para retornar o index.html
@login_required(login_url="/accounts/login/")
def home(request):
    return render(request, 'home.html')

# view para realizar o login
def login(request):
    # se o método for post
    if request.method == "POST":
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            email = form.get_user()
            login(request, email)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('home')
        else:
            form = AuthenticationForm(data = request.POST)

    return render(request, '/accounts/login.html', {'form': form})

def logout(request):
    logout(request)
    return render(request, 'login.html')

@login_required(login_url="/accounts/login/")
def pacientes(request):
    pacientes = Pacientes.objects.all()
    return render(request, 'pacientes.html', {'pacientes': pacientes})

@login_required(login_url="/accounts/login/")
def pacientesadd(request):
    form = PacientesAdd(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/pacientes/')
        else:
            form = PacientesAdd()
    return render(request, 'pacientesadd.html', {'form': form})

