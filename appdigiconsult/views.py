from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import *

# Create your views here.

# toda vez que existir esse @login_required, o sistema irá exigir que o usuário esteja logado
# caso contrário, ele redirecionará para a página de login
@login_required(login_url="/accounts/login/")
# view para retornar o index.html
def home(request):
    # redireciona para a página principal
    return render(request, 'home.html')

# view para realizar o login
def login(request):
    # se o método for post
    if request.method == "POST":
        form = AuthenticationForm(data = request.POST)
        # se o form for válido
        if form.is_valid():
            email = form.get_user()
            # loga
            login(request, email)
            # pega o que houver de URL depois do domínio
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('home')
        else:
            form = AuthenticationForm(data = request.POST)
    return render(request, '/accounts/login.html', {'form': form})

@login_required(login_url="/accounts/login/")
def logout(request):
    # logout, sai do sistema
    logout(request)
    # redireciona para a página principal
    return render(request, 'login.html')

@login_required(login_url="/accounts/login/")
def pacientes(request):
    # pega todos os objetos da model Pacientes
    pacientes = Pacientes.objects.all()
    # redireciono para a página de pacientes enviando os dados da model pacientes
    return render(request, 'pacientes.html', {'pacientes': pacientes})

@login_required(login_url="/accounts/login/")
def pacientesadd(request):
    # informo que o form é um PacientesForm
    form = PacientesForm()
    if request.method == 'POST':
        form = PacientesForm(request.POST)
        if form.is_valid():
            # grava no banco de dados
            form.save()
            # e redireciono para a lista de pacientes
            return redirect('/pacientes/')
        else:
            # caso o form não seja válido, redireciona para o form
            form = PacientesForm()
    return render(request, 'pacientesadd.html', {'form': form})

@login_required(login_url="/accounts/login/")
def pacientesdel(request, id):
    # pesquiso no banco de dados (model Pacientes) o que vem na url
    paciente = get_object_or_404(Pacientes, pk = id)
    # deleto
    paciente.delete()
    return redirect('/pacientes/')

@login_required(login_url="/accounts/login/")
def pacientesedit(request, id):
    # pesquiso no banco de dados (model Pacientes) o que vem na url
    paciente = get_object_or_404(Pacientes, pk = id)
    # informo que form é um PacientesForm com os dados que foram buscados no banco com a linha acima
    form = PacientesForm(instance = paciente)
    if request.method == 'POST':
        form = PacientesForm(request.POST, instance = paciente)
        if form.is_valid():
            form.save()
            return redirect('/pacientes/')
        else:
            form = PacientesForm(instance = paciente)
    return render(request, 'pacientesadd.html', {'form': form})


