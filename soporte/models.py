from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class Usuario(AbstractUser):
    email = models.EmailField(unique=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    def __str__(self): return self.username

class Soporte(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    especialidad = models.CharField(max_length=100)
    def __str__(self):
        return f'Soporte: {self.usuario.username}'

class DescripcionDelEstado ( models.Model ):
    descripcion = models.CharField ( max_length = 100 )
    def __str__ ( self ):
        return self.descripcion

class DispositivoAfectado ( models.Model ):
    dispositivo = models.CharField ( max_length = 100 )
    def __str__ ( self ):
        return self.dispositivo

class TipoDeIncidencia ( models.Model ):
    tipo = models.CharField ( max_length = 100 )
    def __str__ ( self ):
        return self.tipo

class Salon ( models.Model ):
    salon = models.CharField ( max_length = 25 )

    def __str__ ( self ):
        return self.salon

class Incidencia ( models.Model ):
    emisor = models.CharField ( max_length = 100, null = False )
    
    tipo_incidencia = models.ForeignKey ( TipoDeIncidencia, on_delete = models.CASCADE )
    dispositivo_afectado = models.ForeignKey ( DispositivoAfectado, on_delete = models.CASCADE )
    descripcion_estado = models.ForeignKey ( DescripcionDelEstado, on_delete = models.CASCADE )
    comentarios = models.TextField () 

    salon = models.ForeignKey ( Salon, on_delete = models.CASCADE )
    
    fecha = models.DateTimeField ( auto_now_add = True )
    
    def __str__ ( self ):
        return f'Incidencia #{self.id} - {self.tipo_incidencia.tipo}'
