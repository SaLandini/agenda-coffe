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
    #Inicio
    path('', views.Init),
    # Semana
    path('AgendaCoffe/Semana/', views.semana),
    path('AgendaCoffe/Semana/Create/', views.create),
    path('AgendaCoffe/Semana/Create/submit', views.submit_evento),
    #Tarefas
    path('AgendaCoffe/Etec/', views.tarefas),
    path('AgendaCoffe/Etec/Create/', views.tarefas_create),
    path('AgendaCoffe/Etec/Create/submit', views.tarefas_subcreate),
    #Anotações
    path('AgendaCoffe/Notas/', views.notas),
    path('AgendaCoffe/Notas/Create/', views.create_notas),
    path('AgendaCoffe/Notas/Create/submit', views.submit_notas),
    #Cursos
    path('AgendaCoffe/Estudos/', views.studies),
    path('AgendaCoffe/Estudos/Create', views.create_studies),
    path('AgendaCoffe/Estudos/submit', views.submit_studies),
    #Remedios
    path('Remedios', views.drugs)
] 