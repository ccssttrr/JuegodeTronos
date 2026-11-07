from django.urls import path
from . import views

# Cada miembro añade aquí solo sus rutas (avisad por el grupo antes de subirlo).
urlpatterns = [
    path('', views.index, name='index'),
    path('temporadas/', views.lista_temporadas, name='temporada_list'),
    path('temporadas/<int:pk>/', views.detalle_temporada, name='temporada_detail'),
    path('personajes/', views.lista_personajes, name='personaje_list'),
    path('personajes/<int:pk>/', views.detalle_personaje, name='personaje_detail'),
        path('casas/', views.lista_casas, name='casa_list'),
    path('casas/<int:pk>/', views.detalle_casa, name='casa_detail'),
]