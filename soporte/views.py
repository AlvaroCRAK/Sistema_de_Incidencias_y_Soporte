from rest_framework import generics
from .models import Incidencia 
from .serializers import IncidenciaSerializer 
from django.shortcuts import render, redirect
from django.views import View
from rest_framework.permissions import AllowAny
from .models import Incidencia
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SoporteLoginForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.

class IncidenciaListView(View):
    model = Incidencia
    
    def get(self, request, *args, **kwargs):
        
        context = {
            'incidencias': Incidencia.objects.all(),
            'total_incidencias': Incidencia.objects.count(),
            'incidencias_atendidas': Incidencia.objects.filter(estado_incidencia='Atendida').count(),
            'incidencias_por_atender': Incidencia.objects.filter(estado_incidencia='Por atender').count(),
            'incidencias_archivadas': Incidencia.objects.filter(estado_incidencia='Archivada').count(),
        }
        
        # Renderizar la plantilla con el contexto
        return render(request, 'soporte_listar_incidencias.html', context)


class LoginView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('soporte:incidencias')  # Redirige si ya está autenticado
        form = SoporteLoginForm()
        return render(request, "soporte_login.html", {'form': form})

    def post(self, request, *args, **kwargs):
        
        if request.POST.get('logout'):  # Verificar si se envió el formulario de logout
            logout(request)  # Cerrar sesión
            return redirect('soporte:login')  # Redirigir a la vista de login

        form = SoporteLoginForm(request, data=request.POST)
        
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('soporte:incidencias')  # Redirige tras el login
            else:
                messages.error(request, "Credenciales incorrectas. Inténtalo de nuevo.")
        else:
            messages.error(request, "Credenciales incorrectas. Inténtalo de nuevo.")
        
        return render(request, "soporte_login.html", {'form': form})


@method_decorator(login_required, name='dispatch')
class IncidenciasView(View):
    def get(self, request, *args, **kwargs):
        incidencias = Incidencia.objects.filter(estado_incidencia="Por atender") # Traer todas las incidencias
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

