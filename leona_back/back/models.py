from django.db import models

class Servicio(models.Model):
    nombre= models.CharField(max_length=50)
    descripcion= models.TextField(null=True, blank=True)
    precio= models.FloatField(default=0, null=True, blank=True)
    imagen=  models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__ (self): #To_string
        return self.nombre

class Cliente(models.Model):
    nombre= models.CharField(max_length=50)
    descripcion= models.TextField(null=True, blank=True)
    imagen=  models.ImageField(upload_to='images/', null=True, blank=True)
    def __str__ (self): #To_string
        return self.nombre