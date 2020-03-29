from django.urls import include, path
from .views import index, login

urlpatterns = [
    path('', index),
    path('login/', login),
]