from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from datetime import datetime, timedelta
from agenda_coffe.models import (
    Semana,
    Tarefas,
    Anotas,
    Estudos
)
"""
    Pagina Inicial
"""

def Init(request):
    return render(request, "Pages/pageInit.html")

"""
    Organização da semana
"""


def semana(request):
     usuario = request.user
     horario = Semana.time
     try:
        evento = Semana.objects.filter(usuario=usuario)
        dados = {'week':evento}
        return render(request, 'Pages/pageSemana.html', dados)
     except:
         return render(request, 'Pages/pageSemanaAnonymousUser.html')



def create(request):
    id_evento = request.GET.get('id')
    dados = {}
    if id_evento:
        dados['week'] = Semana.objects.get(id=id_evento)
    return render(request, 'Creates/Create.html', dados)


def submit_evento(request):
    if request.POST:
        titulo = request.POST.get("titulo")
        time = request.POST.get('time')
        usuario = request.user
        id_evento = request.POST.get("id_evento")
        if id_evento:
            Semana.objects.filter(id=id_evento).update(titulo=titulo,
                                                        time = time,)
        else:
            Semana.objects.create(titulo=titulo,
                                   time = time,
                                   usuario=usuario)
    return redirect('/')

"""
    Tarefas
"""


def tarefas(request):
    usuario = request.user
    materia = Tarefas.materia
    dia = Tarefas.dia_entrega
    try:
        tarefas = Tarefas.objects.filter(usuario=usuario)
        dados_etec = {'homework': tarefas}
        return render(request, 'Pages/pageTarefas.html', dados_etec)
    except:
        return render(request, 'Pages/pageTarefasAnonymousUser.html')


def tarefas_create(request):
    id_materia = request.GET.get('id')
    dados_etec = {}
    if id_materia:
        dados_etec['homework'] = Tarefas.objects.get(id=id_materia)
    return render(request,'Creates/CreateEtec.html', dados_etec)


def tarefas_subcreate(request):
    if request.POST:
        materia = request.POST.get("materia")
        dia_entrega = request.POST.get('dia_entrega')
        usuario = request.user
        id_materia = request.POST.get("id_materia")
        if id_materia:
            Tarefas.objects.filter(id=id_materia).update(materia=materia,
                                                        dia_entrega = dia_entrega,)
        else:
            Tarefas.objects.create(materia=materia,
                                dia_entrega = dia_entrega,
                                usuario = usuario)
    return redirect('/')

"""
    Notas
"""


def notas(request):
    usuario = request.user
    anotação = Anotas.notas
    descri = Anotas.descri
    try:
        notas = Anotas.objects.filter(usuario=usuario)
        dados_notas = {'nota':notas}
        return  render(request,'Pages/pageNotes.html',dados_notas)
    except:
        return render(request, 'Pages/pageNotesAnonymousUser.html')



def create_notas(request):
    id_notas = request.GET.get('id')
    dados_notas = {}
    if id_notas:
        dados_notas['nota'] = Anotas.objects.get(id=id_notas)
    return render(request, 'Creates/CreateNotes.html', dados_notas)


def submit_notas(request):
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
        return redirect('/')

"""
 Estudos
"""


def studies(request):
    usuario = request.user
    curso_name = Estudos.curso_name
    curso_link = Estudos.curso_link
    curso_site = Estudos.curso_site_name
    try:
        evento = Estudos.objects.filter(usuario=usuario)
        dados = {'studi':evento}
        return render(request, 'Pages/pageEstudos.html', dados)
    except:
        return render(request, 'Pages/pageEstudosAnonymousUser.html')



def create_studies(request):
    id_studies = request.GET.get('id')
    dados_study = {}
    if id_studies:
        dados_study['studi'] = Estudos.objects.get(id=id_studies)
    return render(request, 'Creates/CreateEstudos.html', dados_study)


def submit_studies(request):
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
        return redirect('/')


"""
    Remedios
"""

def drugs(request):
    return render(request, "Pages/pageDrugs.html")