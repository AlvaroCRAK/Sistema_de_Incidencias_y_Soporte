from django.contrib.auth.models import AbstractUser
from django.db import models

class UsuarioEmisor ( models.Model ):
    nombre = models.CharField ( max_length = 100 )
    def __str__ ( self ):
        return self.nombre

class Usuario ( AbstractUser ):
    email = models.EmailField ( unique = True )
    fecha_registro = models.DateTimeField ( auto_now_add = True )
    def __str__ ( self ):
        return self.username

class Soporte ( models.Model ):
    usuario = models.OneToOneField ( Usuario, on_delete = models.CASCADE )
    especialidad = models.CharField ( max_length = 100 )
    def __str__ ( self ):
        return f'Soporte: {self.usuario.username}'

class DescripcionDelEstado ( models.Model ):
    descripcion = models.TextField ()
    def __str__ ( self ):
        return self.descripcion[:50]

class DispositivoAfectado ( models.Model ):
    dispositivo = models.CharField ( max_length = 100 )
    def __str__ ( self ):
        return self.dispositivo

class TipoDeIncidencia ( models.Model ):
    tipo = models.CharField ( max_length = 100 )
    def __str__ ( self ):
        return self.tipo

class Salon ( models.Model ):
    tipo_salon = models.CharField ( max_length = 100 )
    codigo_salon = models.CharField ( max_length = 100 )
    pabellon_salon = models.CharField ( max_length = 100 )
    def __str__ ( self ) :
        return f"{self.tipo_salon} - {self.codigo_salon}"

class Incidencia ( models.Model ):
    emisor = models.ForeignKey ( UsuarioEmisor, related_name = "incidencias_enviadas", on_delete = models.CASCADE )
    receptor = models.ForeignKey ( Soporte, related_name = "incidencias_recibidas", on_delete = models.CASCADE )
    
    tipo_incidencia = models.ForeignKey ( TipoDeIncidencia, on_delete = models.CASCADE )
    dispositivo_afectado = models.ForeignKey ( DispositivoAfectado, on_delete = models.CASCADE )
    descripcion_estado = models.ForeignKey ( DescripcionDelEstado, on_delete = models.CASCADE )
    salon = models.ForeignKey ( Salon, on_delete = models.CASCADE )
    
    fecha = models.DateField ( auto_now_add = True )
    def __str__ ( self ):
        return f'Incidencia #{self.id} - {self.tipo_incidencia.tipo}'
