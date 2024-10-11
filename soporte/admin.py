from django.contrib import admin
from .models import UsuarioEmisor, Usuario, Soporte, DescripcionDelEstado, DispositivoAfectado, TipoDeIncidencia, Salon, Incidencia

@admin.register(UsuarioEmisor)
class UsuarioEmisorAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'fecha_registro')
    search_fields = ('username', 'email')

@admin.register(Soporte)
class SoporteAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'especialidad')
    search_fields = ('usuario__username',)

@admin.register(DescripcionDelEstado)
class DescripcionDelEstadoAdmin(admin.ModelAdmin):
    list_display = ('descripcion',)
    search_fields = ('descripcion',)

@admin.register(DispositivoAfectado)
class DispositivoAfectadoAdmin(admin.ModelAdmin):
    list_display = ('dispositivo',)
    search_fields = ('dispositivo',)

@admin.register(TipoDeIncidencia)
class TipoDeIncidenciaAdmin(admin.ModelAdmin):
    list_display = ('tipo',)
    search_fields = ('tipo',)

@admin.register(Salon)
class SalonAdmin(admin.ModelAdmin):
    list_display = ('tipo_salon', 'codigo_salon', 'pabellon_salon')
    search_fields = ('tipo_salon', 'codigo_salon', 'pabellon_salon')

@admin.register(Incidencia)
class IncidenciaAdmin(admin.ModelAdmin):
    list_display = ('emisor', 'receptor', 'tipo_incidencia', 'fecha')
    search_fields = ('emisor__nombre', 'receptor__usuario__username', 'tipo_incidencia__tipo', 'fecha')

