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
        form = IncidenciaForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect("usuario:historial")
        else:
            # Imprime los errores en consola para depuración
            print(form.errors)
            context = {
                "form": form  # Pasa el formulario con errores al contexto
            }
            return render(request, "usuario_reportar.html", context)


class HistorialView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "usuario_historial.html")
    

class PreguntasView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "usuario_preguntas.html")