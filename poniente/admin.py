from django.contrib import admin

from .models import Casa, Personaje, Temporada

admin.site.register(Casa)
admin.site.register(Temporada)
admin.site.register(Personaje)