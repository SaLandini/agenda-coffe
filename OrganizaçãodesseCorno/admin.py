from django.contrib import admin
from OrganizaçãodesseCorno.models import what_I_need_to_do
# Register your models here.

class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo','id','descrição','time')


admin.site.register(what_I_need_to_do, EventoAdmin)