from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from back.models import Servicio, Cliente

class ServicioAbm(APIView):
    def get(self, request):
        servicios= Servicio.objects.all()
        data= list(map(lambda x: {'id':x.id,
                                   'nombre': x.nombre,
                                   'descripcion': x.descripcion,
                                    'precio': x.precio,
                                    'imagen': x.imagen.url if x.imagen else None}, servicios))
       
        return Response({"Servicios":data})
    
    def post (self, request):
        data= request.data
        campos= ['nombre', 'descripcion']
                
        for campo in campos:
            if not campo in data:
                return Response({"Error": f"Falta el campo {campo}"}, status=400)
        
        servicio= Servicio.objects.create(
                    nombre= data.get('nombre'),
                    descripcion= data.get('descripcion'),
                    precio= data.get('precio', 0),
                    imagen= data.get('imagen',''),
        )
        return Response({"Mensaje": "Servicio creado con exito",
                          "id": servicio.id}, status=200)
    
    def put(self, request):
        data= request.data
        if not 'id' in data:
            return Response({"Error": "Falta el id"}, status=400)
        
        servicio_id= data.get('id')

        try:
            servicio= Servicio.objects.get(id=servicio_id)
        except Servicio.DoesNotExist:
            return Response({"Error":"el servicio no existe"}, status=404)
        
        for i, value in data.items():
            if i != 'id':
                setattr(servicio, i, value)
        servicio.save()
        return Response({"mensaje": "Servicio actualizada exitosamente"}, status=200)
    
    def delete(self, request):
        data= request.data
        if not 'id' in data:
            return Response({"Error": "Falta el id"}, status=400)
        
        servicio_id= data.get('id')
        try:
            servicio= Servicio.objects.get(id=servicio_id)
        except Servicio.DoesNotExist:
            return Response({"Error":"el servicio no existe"}, status=404)
        servicio.delete()
        return Response({"Mensaje":"Servicio borrado con existo"})
    
class ClienteAbm(APIView):
    def get(self, request):
        clientes= Cliente.objects.all()
        data= list(map(lambda x: {'id':x.id, 
                                  'nombre': x.nombre, 
                                  'descripcion': x.descripcion,
                                  'imagen': x.imagen.url if x.imagen else None}, clientes))

        return Response({"Clientes":data})
    
    def post (self, request):
        data= request.data
        campos= ('nombre', 'descripcion')
                
        for campo in campos:
            if not campo in data:
                return Response({"Error": f"Falta el campo {campo}"}, status=400)
        
        if not Cliente.objects.filter(nombre= data.get('nombre')).exists():
            cliente= Cliente.objects.create(
                        nombre= data.get('nombre'),
                        descripcion= data.get('descripcion'),
                        imagen= data.get('imagen',''),
            )
            return Response({"Mensaje": "Cliente creado con exito",
                          "id": cliente.id}, status=200)
        else:
            return Response({"Error": f"El cliente {data.get('nombre')} ya existe"}, status= 400)

    def put(self, request):
        data= request.data
        if not 'id' in data:
            return Response({"Error": "Falta el id"}, status=400)
        
        cliente_id= data.get('id')

        try:
            cliente= Cliente.objects.get(id=cliente_id)
        except Cliente.DoesNotExist:
            return Response({"Error":"el cliente no existe"}, status=404)
        
        for i, value in data.items():
            if i != 'id':
                setattr(cliente, i, value)
        cliente.save()
        return Response({"mensaje": "Cliente actualizada exitosamente"}, status=200)
    
    def delete(self,request):
        data= request.data
        if not 'id' in data:
            return Response({"Error": "Falta el id"}, status=400)
        
        cliente_id= data.get('id')

        try:
            cliente= Cliente.objects.get(id=cliente_id)
        except Cliente.DoesNotExist:
            return Response({"Error":"el cliente no existe"}, status=404)
        cliente.delete()
        
        return Response({"Mensaje": "Cliente borrado con exito"}, status=200)
        