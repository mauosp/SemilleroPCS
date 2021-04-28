from django.db import models


# Create your models here.
class ListadoSemilleros(models.Model):
    """ Modelo Base de Datos para crear semilleros """
    codeSemillero = models.IntegerField()
    listadoSemillero = models.TextField()

    def __str__(self):
        return self.codeSemillero


class Talleres(models.Model):
    """ Modelo Base de Datos para crear semilleros """
    codeSemillero = models.IntegerField()
    talleresSemillero = models.TextField()

    def __str__(self):
        return self.codeSemillero
