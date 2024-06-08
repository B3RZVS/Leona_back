from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from back.models import Servicio, Cliente

class ServicioAbm(APIView):
    def get(self, request):
        servicios= Servicio.objects.all()
        data= list(map(lambda x: {'id':x.id, 'nombre': x.nombre, 'descripcion': x.descripcion, 'precio': x.precio}, servicios))
        
        return Response({"Servicios":data})
    
class ClienteAbm(APIView):
    def get(self, request):
        clientes= Cliente.objects.all()
        data= list(map(lambda x: {'id':x.id, 
                                  'nombre': x.nombre, 
                                  'descripcion': x.descripcion}, clientes))

        return Response({"Clientes":data})