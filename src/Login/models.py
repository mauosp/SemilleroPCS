from django.db import models


class Login(models.Model):
    """ Modelo Base de Datos para crear semilleros """
    email = models.EmailField(max_length=10)
    password = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.email
