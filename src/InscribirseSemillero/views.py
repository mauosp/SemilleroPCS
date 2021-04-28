from django.shortcuts import render
from rest_framework import viewsets
from .models import InscribirseASemillero
from .serializers import InscribirseASemilleroSerializer


# Create your views here.

class InscribirseASemilleroViexSet(viewsets.ModelViewSet):
    serializer_class = InscribirseASemilleroSerializer
    queryset = InscribirseASemillero.objects.all()


def semilleros(request):
    return render(request, "inscribirsemillero.html", {})
