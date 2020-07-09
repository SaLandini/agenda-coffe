from django.contrib import admin
from agenda_coffe.models import what_I_need_to_do, etec_tarefas, Anotas, Estudos
# Register your models here.

class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo','id','descrição','time')

class EtecAdmin(admin.ModelAdmin):
    list_display = ('materia', 'dia_entrega')

class NotaAdmin(admin.ModelAdmin):
    list_display = ('notas', 'descri')

class StudiesAdmin(admin.ModelAdmin):
    list_display = ('curso_name', 'curso_site_name','curso_link','youtube')

admin.site.register(what_I_need_to_do, EventoAdmin)
admin.site.register(etec_tarefas, EtecAdmin)
admin.site.register(Anotas, NotaAdmin)
admin.site.register(Estudos, StudiesAdmin)
