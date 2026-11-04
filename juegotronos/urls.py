"""
URL configuration for juegotronos project.

Rutas principales: el admin de Django y las rutas de la app poniente.
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("poniente.urls")),
]
