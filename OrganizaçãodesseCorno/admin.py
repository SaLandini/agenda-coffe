from django.contrib import admin
from OrganizaçãodesseCorno.models import what_I_need_to_do, etec_tarefas
# Register your models here.

class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo','id','descrição','time')

class EtecAdmin(admin.ModelAdmin):
    list_display = ('materia', 'dia_entrega')

admin.site.register(what_I_need_to_do, EventoAdmin)
admin.site.register(etec_tarefas, EtecAdmin)