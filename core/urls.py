from django.contrib import admin
from django.urls import path, include
from .views import CoreView


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", CoreView.as_view() ),
    path("usuario/", include("usuario.urls", namespace="usuario") ),
    path("soporte/", include("soporte.urls", namespace="soporte") ),

    # django_browser_reload
    path("__reload__/", include("django_browser_reload.urls")),
]
