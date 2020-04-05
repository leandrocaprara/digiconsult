from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

# view para retornar o index.html
@login_required(login_url="accounts/login/")
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
            return redirect('home')
        else:
            form = AuthenticationForm(data = request.POST)

    return render(request, 'accounts/login.html', {'form': form})