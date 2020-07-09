"""AGENDA COFFE URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView
from agenda_coffe import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('AgendaTOP/', views.Jorge),
    path('AgendaTOP/Etec/', views.Etec),
    path('AgendaTOP/Etec/Create/', views.Etec_create),
    path('AgendaTOP/Etec/Create/submit', views.Etec_subcreate),
    path('AgendaTOP/Create/', views.create),
    path('AgendaTOP/Create/submit', views.submit_evento),
    path('AgendaTOP/Notas/', views.Notas),
    path('AgendaTOP/Notas/Create/', views.Create_notas),
    path('AgendaTOP/Notas/Create/submit', views.Submit_notas),
    path('AgendaTOP/Estudos/', views.Studies),
    path('AgendaTOP/Estudos/Create', views.Create_studies),
    path('AgendaTOP/Estudos/Create/submit', views.Submit_studies),
    path('AgendaTOP/Estudos/submit', views.Submit_studies),
    path('', RedirectView.as_view(url='/AgendaTOP/')),
] 