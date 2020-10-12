from django.db import models

from apps.adopcion.models import persona

# Create your models here.

class Estado(models.Model):
    estado_mascota = models.CharField(max_length=50)

class mascota(models.Model):
    nombre = models.CharField(max_length=50)
    especie = models.CharField(max_length=50, null= True)
    raza = models.CharField(max_length=50, null= True)
    tamaño = models.CharField(max_length=50, null= True)
    estado = models.CharField(max_length=50, null= True)
    sexo = models.CharField(max_length=10)
    edad_aproximada = models.IntegerField()
    fecha_rescate = models.DateField()
    persona = models.ForeignKey(persona, null = True, blank= True, on_delete= models.CASCADE)
    estado = models.ManyToManyField(Estado)
    
