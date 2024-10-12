import requests

from django.shortcuts import render, redirect
from django.views import View
from django.core.cache import cache
from django.http import JsonResponse
from django.contrib import messages

from soporte.models import DescripcionDelEstado, DispositivoAfectado, Salon, TipoDeIncidencia
from soporte.serializers import IncidenciaSerializer
from .forms import IncidenciaForm

# Create your views here.
class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "usuario_login.html")


class HistorialView(View):
    def get(self, request, *args, **kwargs):
        claves = cache.get('claves_incidencias', [])  # Obtener la lista de claves de incidencias
        incidencias = []
        
        for clave in claves:
            incidencia = cache.get(clave)  # Recuperar cada incidencia
            if incidencia:
                # Obtener los nombres correspondientes a los IDs
                salon_nombre = Salon.objects.get(id=incidencia['salon']).salon
                tipo_incidencia_nombre = TipoDeIncidencia.objects.get(id=incidencia['tipo_incidencia']).tipo
                dispositivo_afectado_nombre = DispositivoAfectado.objects.get(id=incidencia['dispositivo_afectado']).dispositivo
                descripcion_estado_nombre = DescripcionDelEstado.objects.get(id=incidencia['descripcion_estado']).descripcion
                
                # Agregar los nombres al diccionario
                incidencia['salon'] = salon_nombre
                incidencia['tipo_incidencia'] = tipo_incidencia_nombre
                incidencia['dispositivo_afectado'] = dispositivo_afectado_nombre
                incidencia['descripcion_estado'] = descripcion_estado_nombre
                
                incidencias.append(incidencia)
        
        return render(request, "usuario_historial.html", {"incidencias": incidencias})


class PreguntasView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "usuario_preguntas.html")


class ReportarIncidenciasView(View):
    def get(self, request, *args, **kwargs):
        form = IncidenciaForm()
        return render(request, "usuario_reportar.html", {"form": form})
    
    def post(self, request, *args, **kwargs):
        form = IncidenciaForm(request.POST)
        
        if form.is_valid():
            # Obtén datos del formulario
            incidencia_data = {
                "emisor": form.cleaned_data['emisor'],
                "salon": request.POST.get('salon'),  # Debe estar en el formulario
                "tipo_incidencia": request.POST.get('tipo_incidencia'),  # Debe estar en el formulario
                "dispositivo_afectado": request.POST.get('dispositivo_afectado'),  # Debe estar en el formulario
                "descripcion_estado": request.POST.get('descripcion_estado'),  # Debe estar en el formulario
                "comentarios": form.cleaned_data['comentarios'],
                "estado_incidencia" : "Por atender"
            }

            # Enviar la incidencia a la API
            response = requests.post('http://localhost:8000/soporte/api/incidencias/', json=incidencia_data)

            if response.status_code == 201:  # Si la creación fue exitosa
                messages.success(request, 'Incidencia registrada correctamente!')
                
                # Guardar la incidencia en la caché
                cache.set(f'incidencia_{response.json()["id"]}', incidencia_data)
                
                # Obtener la lista de claves de incidencias en caché
                claves = cache.get('claves_incidencias', [])
                claves.append(f'incidencia_{response.json()["id"]}')  # Agregar la nueva clave
                cache.set('claves_incidencias', claves)  # Actualizar la lista de claves                
                
            else:
                messages.error(request, f"Hubo un error al enviar la incidencia: {response.text}")
        
        else:
            messages.error(request, "Datos inválidos.")

        return render(request, "usuario_reportar.html", {"form": form})