from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from datetime import datetime, timedelta
from OrganizaçãodesseCorno.models import what_I_need_to_do

# Create your views here.
def Jorge(request):
     usuario = request.user
     horario = what_I_need_to_do.time
     evento = what_I_need_to_do.objects.filter(usuario=usuario)
     dados = {'need':evento}
     return render(request, 'pageJorge.html', dados)

def create(request):
    id_evento = request.GET.get('id')
    dados = {}
    if id_evento:
        dados['need'] = what_I_need_to_do.objects.get(id=id_evento)
    return render(request,'Create.html', dados)

def submit_evento(request):
    if request.POST:
        titulo = request.POST.get("titulo")
        time = request.POST.get('time')
        usuario = request.user
        id_evento = request.POST.get("id_evento")
        if id_evento:
            what_I_need_to_do.objects.filter(id=id_evento).update(titulo=titulo,
                                                        time = time,)
        else:
            what_I_need_to_do.objects.create(titulo=titulo,
                                   time = time,
                                   usuario=usuario)
    return redirect('/')

def delete_evento(request):
    evento = request.POST.get('titulo')
    evento.delete()
    return render(request,'/')