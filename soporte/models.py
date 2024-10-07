from django.db import models

class Soporte ( models.Model ):
    id_soporte = models.AutoField ( primary_key = True )
    nombre_soporte = models.CharField ( max_length = 100, null = False )
    contrasena_soporte = models.CharField ( max_length = 100, null = False )

    def __str__ ( self ):
        return self.nombre_soporte 
