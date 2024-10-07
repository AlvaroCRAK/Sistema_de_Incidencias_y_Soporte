from django.shortcuts import render
from django.views import View

# Create your views here.
class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "soporte_login.html")
    

class IncidenciasView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "soporte_incidencias.html")