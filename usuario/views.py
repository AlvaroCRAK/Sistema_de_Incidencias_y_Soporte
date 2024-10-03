from django.shortcuts import render
from django.views import View

# Create your views here.
class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "usuario_login.html")
    

class ReportarView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "usuario_reportar.html")
    
    
class HistorialView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "usuario_historial.html")
    

class PreguntasView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "usuario_preguntas.html")