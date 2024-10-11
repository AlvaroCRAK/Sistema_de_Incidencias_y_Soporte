from django.shortcuts import render, redirect
from django.views import View
from django.core.cache import cache
from django.http import JsonResponse
import requests
from soporte.models import UsuarioEmisor
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
        context = {
            "form": IncidenciaForm()
        }
        return render(request, "usuario_reportar.html", context)
    def post ( self, request, *args, **kwargs ):
        form = IncidenciaForm ( request.POST )
        if form.is_valid ():
            emisor_nombre = form.cleaned_data['emisor_nombre']
            usuario_emisor, created = UsuarioEmisor.objects.get_or_create ( nombre = emisor_nombre )

            incidencia_data = {
                'emisor': usuario_emisor.id,
                'receptor': form.cleaned_data['receptor_id'],
                'tipo_incidencia': form.cleaned_data['tipo_incidencia'],
                'dispositivo_afectado': form.cleaned_data['dispositivo_afectado'],
                'descripcion_estado': form.cleaned_data['descripcion_estado'],
                'salon': form.cleaned_data['salon'],
            }
            cache_key = f'incidencia_{usuario_emisor.id}'
            cache_data = cache.get ( cache_key, [] )
            cache_data.append ( incidencia_data )
            cache.set ( cache_key, cache_data, timeout = None )

            api_url = 'http://localhost:8000/api/incidencias/'
            serializer = IncidenciaSerializer ( data = incidencia_data )

            if serializer.is_valid ():
                response = requests.post ( api_url, json = serializer.data )
                if response.status_code == 201:
                    return JsonResponse({'message': 'Incidencia reportada correctamente. '}, status = 201 )
                else:
                    return JsonResponse({'message': 'Error al reportar la incidencia en la API. '}, status = response.status_code )
            else: 
                return JsonResponse({'message': 'Error en los datos de la incidencia. '}, status = 400 )
        return render ( request, "usuario_reportar.html", {'form': form})
