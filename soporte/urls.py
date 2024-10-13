from django.urls import path
from .views import LoginView, IncidenciasView, IncidenciaCreateView, IncidenciaListView, PreguntasView, IncidenciaDetailView

app_name = "soporte"

urlpatterns = [
    path("", LoginView.as_view(), name="login"),  # Ruta de login
    path("incidencias/", IncidenciasView.as_view(), name="incidencias"),
    path('api/incidencias/', IncidenciaCreateView.as_view(), name='incidencia-create'),
    path('listar-incidencias/', IncidenciaListView.as_view(), name='listar_incidencias'),
    path("preguntas/", PreguntasView.as_view(), name="preguntas"),
    path('incidencias/<int:pk>/', IncidenciaDetailView.as_view(), name='detalle_incidencia'),
]

