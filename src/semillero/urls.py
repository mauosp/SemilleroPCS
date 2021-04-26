from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
import CrearSemillero.views

from CrearSemillero.views import CrearSemilleroViexSet
from CrearSemillero import views

router = DefaultRouter()
router.register(r'CrearSemillero', CrearSemilleroViexSet)

urlpatterns = router.urls

urlpatterns += [
    path('admin/', admin.site.urls),
    path(r'crear', views.semilleros, name='crear')
]
