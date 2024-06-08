from django.urls import path
from .views import ServicioAbm, ClienteAbm

urlpatterns = [
    path('servicio/', ServicioAbm.as_view(), name='servicio'),
    path('cliente/', ClienteAbm.as_view(), name='cliente'),
]