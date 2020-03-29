from django.shortcuts import render

# Create your views here.

# view para retornar o index.html
def index(request):
    return render(request, 'index.html')

#view para retornar a página de login
def login(request):
    return render(request, 'login.html')