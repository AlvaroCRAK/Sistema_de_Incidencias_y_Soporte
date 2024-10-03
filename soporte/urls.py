from django.urls import path
from .views import LoginView, IncidenciasView

app_name = "soporte"

urlpatterns = [
    path("", LoginView.as_view(), name="login"),
    path("incidencias/", IncidenciasView.as_view(), name="incidencias")
]
