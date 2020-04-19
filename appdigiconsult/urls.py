from django.urls import include, path
from django.conf.urls import url
from django.contrib import admin
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('pacientes/', pacientes, name='pacientes'),
    path('pacientes/edit/<int:id>', pacientesedit, name='pacientesedit'),
    path('pacientes/delete/<int:id>', pacientesdel, name='pacientesdel'),
    path('pacientes/add/', pacientesadd, name='pacientesadd'),

    # login
    path('accounts/', include('django.contrib.auth.urls')),
]