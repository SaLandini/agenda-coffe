from django.contrib import admin
from agenda_coffe.models import Semana, Tarefas, Anotas, Estudos
# Register your models here.

class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo','id','descrição','time')

class TarefaAdmin(admin.ModelAdmin):
    list_display = ('materia', 'dia_entrega')

class NotaAdmin(admin.ModelAdmin):
    list_display = ('notas', 'descri')

class StudiesAdmin(admin.ModelAdmin):
    list_display = ('curso_name', 'curso_site_name','curso_link','youtube')

admin.site.register(Semana, EventoAdmin)
admin.site.register(Tarefas, TarefaAdmin)
admin.site.register(Anotas, NotaAdmin)
admin.site.register(Estudos, StudiesAdmin)
