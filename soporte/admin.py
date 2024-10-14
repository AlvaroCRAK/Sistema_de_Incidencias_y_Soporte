from django.contrib import admin
from .models import Usuario, Soporte, DescripcionDelEstado, DispositivoAfectado, TipoDeIncidencia, Salon, Incidencia

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'fecha_registro']
    search_fields = ['username', 'email']

@admin.register(Soporte)
class SoporteAdmin(admin.ModelAdmin):
    list_display = ['id', 'usuario', 'especialidad']
    search_fields = ['usuario__username', 'especialidad']

@admin.register(DescripcionDelEstado)
class DescripcionDelEstadoAdmin(admin.ModelAdmin):
    list_display = ['id', 'descripcion']
    search_fields = ['descripcion']

@admin.register(DispositivoAfectado)
class DispositivoAfectadoAdmin(admin.ModelAdmin):
    list_display = ['id', 'dispositivo']
    search_fields = ['dispositivo']

@admin.register(TipoDeIncidencia)
class TipoDeIncidenciaAdmin(admin.ModelAdmin):
    list_display = ['id', 'tipo']
    search_fields = ['tipo']

@admin.register(Salon)
class SalonAdmin(admin.ModelAdmin):
    list_display = ['id', 'salon']
    search_fields = ['salon']

@admin.register(Incidencia)
class IncidenciaAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'ticket', 'emisor', 'estado_incidencia', 
        'tipo_incidencia', 'dispositivo_afectado', 
        'descripcion_estado', 'salon', 'fecha'
    ]
    list_filter = ['fecha', 'tipo_incidencia', 'salon', 'estado_incidencia']
    search_fields = ['emisor', 'ticket', 'tipo_incidencia__tipo', 'dispositivo_afectado__dispositivo']
