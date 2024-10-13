from rest_framework import generics
from .models import Incidencia 
from .serializers import IncidenciaSerializer 
from django.shortcuts import render, redirect
from django.views import View
from rest_framework.permissions import AllowAny
from django.views.generic import ListView
from .models import Incidencia
from django.views.generic import DetailView 
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import SoporteLoginForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

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
        if request.user.is_authenticated:
            return redirect('soporte:incidencias')  # Redirige si ya está autenticado
        form = SoporteLoginForm()
        return render(request, "soporte_login.html", {'form': form})

    def post(self, request, *args, **kwargs):
        form = SoporteLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Bienvenido {username}")
                return redirect('soporte:incidencias')  # Redirige tras el login
            else:
                messages.error(request, "Credenciales incorrectas. Inténtalo de nuevo.")
        else:
            messages.error(request, "Por favor, verifica los campos.")
        return render(request, "soporte_login.html", {'form': form})


@method_decorator(login_required, name='dispatch')
class IncidenciasView(View):
    def get(self, request, *args, **kwargs):
        incidencias = Incidencia.objects.all()  # Traer todas las incidencias
        return render(request, "soporte_incidencias.html", {'incidencias': incidencias})

    def post(self, request, *args, **kwargs):
        incidencia_id = request.POST.get('incidencia_id')
        accion = request.POST.get('accion')

        # Busca la incidencia correspondiente
        incidencia = Incidencia.objects.get(id=incidencia_id)

        # Cambia el estado de la incidencia basado en la acción
        if accion == 'atender':
            incidencia.estado_incidencia = 'Atendida'
        elif accion == 'archivar':
            incidencia.estado_incidencia = 'Archivada'

        # Guarda la incidencia actualizada
        incidencia.save()

        # Redirigir a la vista de incidencias después de actualizar
        return redirect('soporte:incidencias')

class IncidenciaCreateView ( generics.CreateAPIView ):
    queryset = Incidencia.objects.all ()
    serializer_class = IncidenciaSerializer 
    permission_classes = [AllowAny]

class PreguntasView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "soporte_preguntas.html")

