from django.contrib import admin
from ordenamiento.models import *


class BarrioInline(admin.TabularInline):
    model = Barrio
    extra = 1
    verbose_name = 'Barrio'
    verbose_name_plural = 'Barrios'
    

class ParroquiaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ubicacion', 'tipo')
    search_fields = ('nombre',)
    list_filter = ('ubicacion', 'tipo')
    inlines = [BarrioInline]
    
class BarrioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'numero_viviendas', 'numero_parques', 'numero_edificios_residenciales', 'parroquia')
    search_fields = ('nombre',)
    list_filter = ('parroquia',)
    
admin.site.register(Parroquia, ParroquiaAdmin)
admin.site.register(Barrio, BarrioAdmin)
