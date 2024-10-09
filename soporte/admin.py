from django.contrib import admin
from .models import *


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id_usuario', 'nombre_usuario')
    search_fields = ('nombre_usuario',)


@admin.register(Soporte)
class SoporteAdmin(admin.ModelAdmin):
    list_display = ('id_soporte', 'nombre_soporte')
    search_fields = ('nombre_soporte',)


@admin.register(Incidencia)
class IncidenciaAdmin(admin.ModelAdmin):
    list_display = ('id_incidencia', 'fecha_incidencia', 'estado_incidencia', 'id_emisor', 'id_receptor', 'id_salon', 'id_categoria')
    list_filter = ('estado_incidencia', 'fecha_incidencia', 'id_receptor', 'id_categoria')
    search_fields = ('detalles_categoria',)
    raw_id_fields = ('id_emisor', 'id_receptor', 'id_salon', 'id_categoria')


@admin.register(Salon)
class SalonAdmin(admin.ModelAdmin):
    list_display = ('id_salon', 'tipo_salon', 'codigo_salon', 'pabellon_salon')
    search_fields = ('tipo_salon', 'codigo_salon')


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id_categoria', 'nombre_categoria')
    search_fields = ('nombre_categoria',)


@admin.register(Subcategoria)
class SubcategoriaAdmin(admin.ModelAdmin):
    list_display = ('id_subcategoria', 'nombre_subcategoria', 'id_categoria')
    search_fields = ('nombre_subcategoria',)
    list_filter = ('id_categoria',)


@admin.register(Descripcion)
class DescripcionAdmin(admin.ModelAdmin):
    list_display = ('id_descripcion', 'nombre_descripcion', 'id_subcategoria')
    search_fields = ('nombre_descripcion',)
    list_filter = ('id_subcategoria',)
