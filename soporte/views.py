from rest_framework import generics
from .models import Incidencia 
from .serializers import IncidenciaSerializer 
from rest_framework.response import Response 
from rest_framework import status
from django.shortcuts import render
from django.views import View

# Create your views here.
class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "soporte_login.html")
    

class IncidenciasView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "soporte_incidencias.html")

class IncidenciaListCreateView ( generics.ListCreateAPIView ):
    queryset = Incidencia.objects.all () 
    serializer_class = IncidenciaSerializer 

    def create ( self, request, *args, **kwargs ):
        serializer = self.get_serializer ( data = request.data ) 
        if serializer.is_valid ():
            serializer.save () 
            return Response ( serializer.data, status = status.HTTP_201_CREATED )
        return Response ( serializer.errors, status = status.HTTP_400_BAD_REQUEST )
