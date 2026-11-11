from django.db import models


class Casa(models.Model):
    nombre = models.CharField(max_length=50)
    lema = models.CharField(max_length=100)
    sede = models.CharField(max_length=50)
    descripcion = models.TextField()
    # null=True, blank=True -> la imagen es opcional
    imagen = models.ImageField(upload_to="imgs/casas/", null=True, blank=True)

    class Meta:
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre


class Temporada(models.Model):
    numero = models.IntegerField()
    anio = models.IntegerField()
    resumen = models.TextField()
    imagen = models.ImageField(upload_to="imgs/temporadas/", null=True, blank=True)

    class Meta:
        ordering = ["numero"]

    def __str__(self):
        return f"Temporada {self.numero}"


class Personaje(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    # 1:N -> cada personaje pertenece a una casa
    casa = models.ForeignKey(Casa, on_delete=models.CASCADE, related_name="personajes")
    # N:M -> un personaje aparece en varias temporadas
    temporadas = models.ManyToManyField(Temporada, related_name="personajes")
    imagen = models.ImageField(upload_to="imgs/personajes/", null=True, blank=True)

    class Meta:
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre