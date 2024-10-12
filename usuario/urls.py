from django.urls import path, include
from .views import LoginView, ReportarIncidenciasView, HistorialView, PreguntasView

app_name = "usuario"

urlpatterns = [
    path("", LoginView.as_view(), name="login"),
    path("reportar/", ReportarIncidenciasView.as_view(), name="reportar"),
    path("historial/", HistorialView.as_view(), name="historial"),
    path("preguntas/", PreguntasView.as_view(), name="preguntas"),
]
