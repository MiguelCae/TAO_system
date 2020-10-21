from django.db import models

# Create your models here.
class usuario(models.Model):
    documento = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    edad = models.IntegerField()
    telefono = models.IntegerField()
    correo = models.EmailField(max_length=80)
    ciudad = models.CharField(max_length=50, null= True)
    direccon = models.CharField(max_length=50, null= True)
    rol = models.CharField(max_length=50)
