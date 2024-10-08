from django.db import models
from soporte.models import Soporte

class Usuario ( models.Model ):
    id_usuario = models.AutoField ( primary_key = True );
    nombre_usuario = models.CharField ( max_length = 100, null = False )

    def __str__ ( self ):
        return self.nombre_usuario 

class Incidencia ( models.Model ):
    id_incidencia = models.AutoField ( primary_key = True )
    fecha_incidencia = models.DateField ( auto_now_add = True )
    estado_incidencia = models.CharField ( max_length = 25, default = 'por atender' )
    id_emisor = models.ForeignKey ( Usuario, related_name = 'incidencias_enviadas',
                                    on_delete = models.CASCADE )
    id_receptor = models.ForeignKey ( Soporte, related_name = 'incidencias_recibidas', 
                                     on_delete = models.CASCADE)
    id_salon = models.ForeignKey ( 'Salon', on_delete = models.CASCADE )
    id_categoria = models.ForeignKey ( 'Categoria', on_delete = models.CASCADE )
    detalles_categoria = models.TextField ()

    def __str__ ( self ):
        return f"Incidencia {self.id_incidencia} - {self.estado_incidencia}"

class Salon ( models.Model ):
    id_salon = models.AutoField ( primary_key = True )
    tipo_salon = models.CharField ( max_length = 25, null = False )
    codigo_salon = models.IntegerField ( null = False )
    pabellon_salon = models.CharField ( max_length = 25, null = False )

    def __str__ ( self ):
        return f"{self.tipo_salon} - {self.codigo_salon}"

class Categoria ( models.Model ):
    id_categoria = models.AutoField ( primary_key = True )
    nombre_categoria = models.CharField ( max_length = 100, null = False )
    id_subcategoria = models.ForeignKey ( 'Subcategoria', null = True, 
                                         on_delete = models.CASCADE )
    
    def __str__ ( self ):
        return self.nombre_categoria 

class Subcategoria ( models.Model ):
    id_subcategoria = models.AutoField ( primary_key = True )
    nombre_subcategoria = models.CharField ( max_length = 100, null = False )
    id_categoria = models.ForeignKey ( Categoria, related_name = 'subcategoria', on_delete = models.CASCADE )

    def __str__ ( self ):
        return self.nombre_subcategoria 

class Descripcion ( models.Model ):
    id_descripcion = models.AutoField ( primary_key = True )
    nombre_descripcion = models.CharField ( max_length = 100, null = False )

    def __str__ ( self ):
        return self.nombre_descripcion 
