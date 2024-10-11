from django import forms
from soporte.models import Incidencia, Usuario, Soporte, Salon, Categoria, Subcategoria, Descripcion

class IncidenciaForm(forms.ModelForm):
    class Meta:
        model = Incidencia
        fields = [
            'nombre_emisor', 'id_receptor', 'id_salon', 'id_categoria', 'id_subcategoria',
            'id_descripcion', 'detalles_categoria'
        ]
        
        widgets = {
            'nombre_emisor': forms.TextInput(attrs={
                'class': 'block w-full p-2 border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500'
            }),
            'id_receptor': forms.Select(attrs={
                'class': 'block w-full p-2 border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500'
            }),
            'id_salon': forms.Select(attrs={
                'class': 'block w-full p-2 border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500'
            }),
            'id_categoria': forms.Select(attrs={
                'class': 'block w-full p-2 border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500'
            }),
            'id_subcategoria': forms.Select(attrs={
                'class': 'block w-full p-2 border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500'
            }),
            'id_descripcion': forms.Select(attrs={
                'class': 'block w-full p-2 border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500'
            }),
            'detalles_categoria': forms.Textarea(attrs={
                'class': 'block w-full p-2 border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500',
                'rows': 4,
            }),
            'estado_incidencia': forms.Select(attrs={
                'class': 'block w-full p-2 border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500'
            }),
        }

    id_receptor = forms.ModelChoiceField(queryset=Soporte.objects.all(), label="Receptor")
    id_salon = forms.ModelChoiceField(queryset=Salon.objects.all(), label="Salon")
    id_categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(), label="Categoria")
    id_subcategoria = forms.ModelChoiceField(queryset=Subcategoria.objects.all(), label="Subcategoria")
    id_descripcion = forms.ModelChoiceField(queryset=Descripcion.objects.all(), label="Descripcion")
