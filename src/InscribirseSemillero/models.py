from django.db import models


# Create your models here.
class InscribirseASemillero(models.Model):
    correo = models.EmailField(max_length=100, null=False)
    nombre = models.CharField(max_length=50, null=False)
    apellido = models.CharField(max_length=50, null=False)
    codigoSemillero = models.IntegerField()

    def __str__(self):
        return self.correo
