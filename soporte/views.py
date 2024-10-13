from rest_framework import generics
from .models import Incidencia 
from .serializers import IncidenciaSerializer 
from django.shortcuts import render
from django.views import View
from rest_framework.permissions import AllowAny
from django.views.generic import ListView
from .models import Incidencia
from django.views.generic import DetailView 
from django.http import JsonResponse

# Create your views here.

class IncidenciaListView(ListView):
    model = Incidencia
    template_name = 'soporte_listar_incidencias.html'  # Plantilla que se va a renderizar
    context_object_name = 'incidencias'  # Nombre del contexto para las incidencias

    def get_context_data(self, **kwargs):
        # Llama al método get_context_data de la clase base
        context = super().get_context_data(**kwargs)

        # Añadir variables adicionales al contexto
        context['total_incidencias'] = Incidencia.objects.count()
        context['incidencias_atendidas'] = Incidencia.objects.filter(estado_incidencia='Atendida').count()
        context['incidencias_en_atencion'] = Incidencia.objects.filter(estado_incidencia='En Atención').count()
        context['incidencias_pendientes'] = Incidencia.objects.filter(estado_incidencia='Pendiente').count()

        return context  

class IncidenciaDetailView(DetailView):
    model = Incidencia
    template_name = 'detalle_incidencia.html'  # Esto puede no ser necesario para el JSON

    def get(self, request, *args, **kwargs):
        # Llamar a la implementación base
        self.object = self.get_object()
        
        # Generar un contexto adicional
        context = self.get_context_data(object=self.object)
        
        # Retornar JSON si se solicita
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({
                'hora': self.object.fecha.strftime("%Y-%m-%d %H:%M"),
                'emisor': context['emisor'],
                'aula': context['aula'],
                'categoria': context['categoria'],
                'descripcion': context['descripcion'],
                'asignado': context['asignado'],
            })
        else:
            return super().get(request, *args, **kwargs)

class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "soporte_login.html")
    

class IncidenciasView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "soporte_incidencias.html")

class IncidenciaCreateView ( generics.CreateAPIView ):
    queryset = Incidencia.objects.all ()
    serializer_class = IncidenciaSerializer 
    permission_classes = [AllowAny]

class PreguntasView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "soporte_preguntas.html")

