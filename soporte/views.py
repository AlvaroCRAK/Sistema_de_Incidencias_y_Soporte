from rest_framework import generics
from .models import Incidencia 
from .serializers import IncidenciaSerializer 
from django.shortcuts import render
from django.views import View
from rest_framework.permissions import AllowAny

# Create your views here.
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
