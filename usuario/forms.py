from django import forms
from soporte.models import *


class IncidenciaForm(forms.ModelForm):
    class Meta:
        model = Incidencia
        fields = (  "id_incidencia", "estado_incidencia", "id_emisor", "id_receptor",
                    "id_salon", "id_categoria", "detalles_categoria"  )
        
    id_emisor = forms.ModelChoiceField(queryset=Usuario.objects.all())
    id_receptor = forms.ModelChoiceField(queryset=Soporte.objects.all())
    id_salon = forms.ModelChoiceField(queryset=Salon.objects.all())
    id_categoria = forms.ModelChoiceField(queryset=Categoria.objects.all())