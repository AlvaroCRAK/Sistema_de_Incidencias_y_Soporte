from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class UsuarioEmisor ( models.Model ):
    nombre = models.CharField ( max_length = 100 )
    def __str__ ( self ):
        return self.nombre

class Usuario ( AbstractUser ):
    email = models.EmailField ( unique = True )
    fecha_registro = models.DateTimeField ( auto_now_add = True )
    
    groups = models.ManyToManyField(
        Group,
        related_name='usuario_groups',
        blank=True,
        help_text='The groups this user belongs to.'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='usuario_permissions',
        blank=True,
        help_text='Specific permissions for this user.'
    )
    
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
    id_salon = models.AutoField ( primary_key = True )
    tipo_salon = models.CharField ( max_length = 25, null = False )
    codigo_salon = models.IntegerField ( null = False )
    pabellon_salon = models.CharField ( max_length = 25, null = False )

    def __str__ ( self ):
        return f"{self.tipo_salon} - {self.codigo_salon}"

class Incidencia ( models.Model ):
    emisor = models.CharField( max_length = 100, null = False)
    #emisor = models.ForeignKey ( UsuarioEmisor, related_name = "incidencias_enviadas", on_delete = models.CASCADE )
    receptor = models.ForeignKey ( Soporte, related_name = "incidencias_recibidas", on_delete = models.CASCADE )
    
    tipo_incidencia = models.ForeignKey ( TipoDeIncidencia, on_delete = models.CASCADE )
    dispositivo_afectado = models.ForeignKey ( DispositivoAfectado, on_delete = models.CASCADE )
    descripcion_estado = models.ForeignKey ( DescripcionDelEstado, on_delete = models.CASCADE )
    salon = models.ForeignKey ( Salon, on_delete = models.CASCADE )
    
    fecha = models.DateField ( auto_now_add = True )
    comentarios = models.TextField(blank=True, null=True)
    
    def __str__ ( self ):
        return f'Incidencia #{self.id} - {self.tipo_incidencia.tipo}'
