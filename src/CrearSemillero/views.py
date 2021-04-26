from django.shortcuts import render
from rest_framework import viewsets
from .models import CrearSemillero
from .serializers import CrearSemilleroSerializer


# Create your views here.

class CrearSemilleroViexSet(viewsets.ModelViewSet):
    serializer_class = CrearSemilleroSerializer
    queryset = CrearSemillero.objects.all()

def semilleros(request):
    return render(request, "semilleros.html",{})

