from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from datetime import datetime, timedelta
from agenda_coffe.models import (
    what_I_need_to_do,
    etec_tarefas,
    Anotas,
    Estudos
)
"""
    Pagina Inicial
"""

def Init(request):
    return render(request, 'pages/pageInit.html')

"""
    Organização da semana
"""


def Jorge(request):
     usuario = request.user
     horario = what_I_need_to_do.time
     evento = what_I_need_to_do.objects.filter(usuario=usuario)
     dados = {'need':evento}
     return render(request, 'pages/pageJorge.html', dados)


def create(request):
    id_evento = request.GET.get('id')
    dados = {}
    if id_evento:
        dados['need'] = what_I_need_to_do.objects.get(id=id_evento)
    return render(request, 'Creates/Create.html', dados)


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

"""
    Etec
"""


def Etec(request):
    usuario = request.user
    materia = etec_tarefas.materia
    dia = etec_tarefas.dia_entrega
    tarefas = etec_tarefas.objects.filter(usuario=usuario)
    dados_etec = {'etec': tarefas}

    return render(request,'pages/pageEtec.html', dados_etec)


def Etec_create(request):
    id_materia = request.GET.get('id')
    dados_etec = {}
    if id_materia:
        dados_etec['etec'] = etec_tarefas.objects.get(id=id_materia)
    return render(request,'Creates/CreateEtec.html', dados_etec)


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
                                dia_entrega = dia_entrega,
                                usuario = usuario)
    return redirect('/AgendaTOP/Etec/')

"""
    Notas
"""


def Notas(request):
    usuario = request.user
    anotação = Anotas.notas
    descri = Anotas.descri
    notas = Anotas.objects.filter(usuario=usuario)
    dados_notas = {'nota':notas}

    return  render(request,'pages/pageNotes.html',dados_notas)


def Create_notas(request):
    id_notas = request.GET.get('id')
    dados_notas = {}
    if id_notas:
        dados_notas['nota'] = Anotas.objects.get(id=id_notas)
    return render(request, 'Creates/CreateNotes.html', dados_notas)


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
                                descri=descri,
                                usuario = user)
        return redirect('/AgendaTOP/Notas')

"""
 Estudos
"""


def Studies(request):
    usuario = request.user
    youtube = Estudos.youtube
    curso_name = Estudos.curso_name
    curso_link = Estudos.curso_link
    curso_site = Estudos.curso_site_name
    evento = Estudos.objects.filter(usuario=usuario)
    dados = {'studi':evento}
    return render(request, 'pages/pageEstudos.html', dados)


def Create_studies(request):
    id_studies = request.GET.get('id')
    dados_study = {}
    if id_studies:
        dados_study['studi'] = Estudos.objects.get(id=id_studies)
    return render(request, 'Creates/CreateEstudos.html', dados_study)


def Submit_studies(request):
    if request.POST:
        curso_name = request.POST.get('curso_name')
        curso_link = request.POST.get('curso_link')
        curso_site = request.POST.get('curso_site')
        if 'checkbox' in request.GET:
            youtube = True
        else:
            youtube = False
        user = request.user
        id_studies = request.POST.get('id_studies')

        if id_studies:
            Estudos.objects.filter(id=id_studies).update(youtube = youtube,
                                                         curso_link = curso_link,
                                                         curso_site_name = curso_site,
                                                         curso_name = curso_name)
        else:
            Estudos.objects.create(youtube = youtube,
                                    curso_link = curso_link,
                                    curso_site_name = curso_site,
                                    curso_name = curso_name,
                                    usuario = user)
        return redirect('/AgendaTOP/Estudos/')