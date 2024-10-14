from django import forms
from soporte.models import Incidencia, Soporte, Salon, TipoDeIncidencia, DispositivoAfectado, DescripcionDelEstado

class IncidenciaForm(forms.ModelForm):
    class Meta:
        model = Incidencia
        fields = [
            'emisor', 'tipo_incidencia', 'dispositivo_afectado', 
            'descripcion_estado', 'salon', 'comentarios', 'observaciones'
        ]
        
        widgets = {
            'emisor': forms.TextInput(attrs={
                'class': 'block w-full p-2 border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500',
                'placeholder': 'Ingrese el nombre del emisor'
            }),
            'tipo_incidencia': forms.Select(attrs={
                'class': 'block w-full p-2 border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500'
            }),
            'dispositivo_afectado': forms.Select(attrs={
                'class': 'block w-full p-2 border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500'
            }),
            'descripcion_estado': forms.Select(attrs={
                'class': 'block w-full p-2 border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500'
            }),
            'salon': forms.Select(attrs={
                'class': 'block w-full p-2 border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500'
            }),
            'comentarios': forms.Textarea(attrs={
                'class': 'block w-full p-2 border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500',
                'placeholder': 'Escriba aquí sus comentarios adicionales...',
                'rows': 4,
            }),
        }

    emisor = forms.CharField( max_length = 100, required = True, label="Usuario emisor")
    tipo_incidencia = forms.ModelChoiceField(queryset=TipoDeIncidencia.objects.all(), label="Tipo de Incidencia")
    dispositivo_afectado = forms.ModelChoiceField(queryset=DispositivoAfectado.objects.all(), label="Dispositivo Afectado")
    descripcion_estado = forms.ModelChoiceField(queryset=DescripcionDelEstado.objects.all(), label="Descripción del Estado")
    salon = forms.ModelChoiceField(queryset=Salon.objects.all(), label="Salón Ocurrencia")

comentarios = forms.CharField(
    label="Comentarios",
    required=True,
    widget=forms.Textarea(attrs={
        'class': 'block w-full p-2 border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500',
        'placeholder': 'Escriba aquí sus comentarios adicionales...',
        'rows': 4
    })
)

