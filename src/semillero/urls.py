from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
import CrearSemillero.views

from CrearSemillero.views import CrearSemilleroViexSet
from CrearSemillero import views

from InscribirseSemillero.views import InscribirseASemilleroViexSet
from InscribirseSemillero import views

router = DefaultRouter()
router.register(r'CrearSemillero', CrearSemilleroViexSet)
router.register(r'InscribirSemillero', InscribirseASemilleroViexSet)

urlpatterns = router.urls

urlpatterns += [
    path('admin/', admin.site.urls),
    path(r'crear', views.semilleros, name='crear'),
]
