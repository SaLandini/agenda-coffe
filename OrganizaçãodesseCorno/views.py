from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from datetime import datetime, timedelta
from OrganizaçãodesseCorno.models import what_I_need_to_do, etec_tarefas, Anotas

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

def Etec(request):
    usuario = request.user
    materia = etec_tarefas.materia
    dia = etec_tarefas.dia_entrega
    tarefas = etec_tarefas.objects.filter()
    dados_etec = {'etec': tarefas}

    return render(request,'pageEtec.html', dados_etec)

def Etec_create(request):
    id_materia = request.GET.get('id')
    dados_etec = {}
    if id_materia:
        dados_etec['etec'] = etec_tarefas.objects.get(id=id_materia)
    return render(request,'CreateEtec.html', dados_etec)

def Etec_subcreate(request):
    if request.POST:
        materia = request.POST.get("materia")
        dia_entrega = request.POST.get('dia_entrega')
        usuario = request.user
        id_materia = request.POST.get("id_materia")
        if id_materia:
            etec_tarefas.objects.filter(id=id_materia).update(materia=materia,
                                                        dia_entrega = dia_entrega,)
        else:
            etec_tarefas.objects.create(materia=materia,
                                dia_entrega = dia_entrega)
    return redirect('/AgendaTOP/Etec/')

def Notas(request):
    usuario = request.user
    anotação = Anotas.notas
    descri = Anotas.descri
    notas = Anotas.objects.filter()
    dados_notas = {'nota':notas}

    return  render(request,'pageNotes.html',dados_notas)

def Create_notas(request):
    id_notas = request.GET.get('id')
    dados_notas = {}
    if id_notas:
        dados_notas['nota'] = Anotas.objects.get(id=id_notas)
    return render(request, 'CreateNotes.html', dados_notas)

def Submit_notas(request):
    if request.POST:
        anotação = request.POST.get('anotação')
        descri = request.POST.get('descri')
        user = request.user
        id_notas = request.POST.get('id_notas')

        if id_notas:
            Anotas.objects.filter(id=id_notas).update(notas=anotação,
                                                        descri = descri)
        else:
            Anotas.objects.create(notas=anotação,
                                descri=descri)
        return redirect('/AgendaTOP/Notas')

