from django.contrib import admin
from ordenamiento.models import *

class ParroquiaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ubicacion', 'tipo')
    search_fields = ('nombre',)
    list_filter = ('ubicacion', 'tipo')
    
class BarrioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'numero_viviendas', 'numero_parques', 'numero_edificios_residenciales', 'parroquia')
    search_fields = ('nombre',)
    list_filter = ('parroquia',)
    
admin.site.register(Parroquia, ParroquiaAdmin)
admin.site.register(Barrio, BarrioAdmin)
