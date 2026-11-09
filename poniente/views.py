from django.shortcuts import render, get_object_or_404

from .models import Casa, Personaje, Temporada


def index(request):
    personajes = []
    for casa in Casa.objects.all():
        personaje = casa.personajes.first()
        if personaje:
            personajes.append(personaje)
    return render(request, 'index.html', {'personajes': personajes})


def lista_temporadas(request):
    temporadas = Temporada.objects.all()
    return render(request, 'temporada_list.html', {'temporadas': temporadas})


def detalle_temporada(request, pk):
    temporada = get_object_or_404(Temporada, pk=pk)
    personajes = temporada.personajes.all()
    return render(request, 'temporada_detail.html', {
        'temporada': temporada,
        'personajes': personajes,
    })


def lista_personajes(request):
    casas = Casa.objects.all()
    num_personajes = Personaje.objects.count()
    return render(request, 'personaje_list.html', {
        'casas': casas,
        'num_personajes': num_personajes,
    })


def detalle_personaje(request, pk):
    personaje = get_object_or_404(Personaje, pk=pk)
    temporadas = personaje.temporadas.all()
    companeros = []
    for otro in personaje.casa.personajes.all():
        if otro.pk != personaje.pk:
            companeros.append(otro)
    return render(request, 'personaje_detail.html', {
        'personaje': personaje,
        'temporadas': temporadas,
        'companeros': companeros,
    })


def lista_casas(request):
    casas = Casa.objects.all()
    return render(request, 'casa_list.html', {'casas': casas})


def detalle_casa(request, pk):
    casa = get_object_or_404(Casa, pk=pk)
    personajes = casa.personajes.all()
    return render(request, 'casa_detail.html', {
        'casa': casa,
        'personajes': personajes,
    })