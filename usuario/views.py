from django.shortcuts import render, redirect
from django.views import View
from .forms import IncidenciaForm


# Create your views here.
class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "usuario_login.html")


class ReportarView(View):
    def get(self, request, *args, **kwargs):
        
        context = {
            "form": IncidenciaForm()
        }
        
        return render(request, "usuario_reportar.html", context)
    
    def post(self, request, *args, **kwargs):
        form = IncidenciaForm
        
        if form.is_valid():
            form.save()
            
            return redirect("usuario:historial")
        else:
            self.get()


class HistorialView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "usuario_historial.html")
    

class PreguntasView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "usuario_preguntas.html")