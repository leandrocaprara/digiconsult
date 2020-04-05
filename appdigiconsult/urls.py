from django.urls import include, path
from django.conf.urls import url
from .views import *
from django.contrib import admin

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('login/', login, name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
]