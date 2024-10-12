import requests

from django.shortcuts import render, redirect
from django.views import View
from django.core.cache import cache
from django.http import JsonResponse
from django.contrib import messages

from soporte.serializers import IncidenciaSerializer
from .forms import IncidenciaForm

# Create your views here.
class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "usuario_login.html")

class HistorialView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "usuario_historial.html")

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
                "comentarios": form.cleaned_data['comentarios'],
                "tipo_incidencia": request.POST.get('tipo_incidencia'),  # Debe estar en el formulario
                "dispositivo_afectado": request.POST.get('dispositivo_afectado'),  # Debe estar en el formulario
                "descripcion_estado": request.POST.get('descripcion_estado'),  # Debe estar en el formulario
                "salon": request.POST.get('salon'),  # Debe estar en el formulario
            }

            # Enviar la incidencia a la API
            response = requests.post('http://localhost:8000/soporte/api/incidencias/', json=incidencia_data)

            if response.status_code == 201:  # Si la creación fue exitosa
                messages.success(request, 'Incidencia registrada correctamente!')
                cache.set(f'incidencia_{response.json()["id"]}', incidencia_data)
                return redirect('usuario:historial')  # Redirigir a la página de historial
            else:
                messages.error(request, f"Error al enviar la incidencia: {response.text}")
                return render(request, "usuario_reportar.html", {"form": form})

        messages.error(request, "Datos inválidos.")
        return render(request, "usuario_reportar.html", {"form": form})
