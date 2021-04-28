from django.db import models


class CrearSemillero(models.Model):
    """ Modelo Base de Datos para crear semilleros """
    codeSemillero = models.IntegerField()
    name = models.CharField(max_length=50, null=False)
    descripcion = models.TextField(max_length=500)
    fechaInicio = models.DateField()
    fechaFin = models.DateField()
    hora = models.TimeField()
    linkReunion = models.CharField(max_length=200)

    def __str__(self):
        return self.codeSemillero
