from django.contrib import admin

# Register your models here.
from .models import ListadoSemilleros
from .models import Talleres

admin.site.register(ListadoSemilleros)
admin.site.register(Talleres)
