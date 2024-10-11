from rest_framework import serializers 
from .models import Incidencia 

class IncidenciaSerializer ( serializers.ModelSerializer ):
    class Meta:
        model = Incidencia 
        fields = '__all__'
