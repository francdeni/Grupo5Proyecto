from django.db import models

# Create your models here.

class Instrumento(models.Model):
    marca = models.CharField(max_length= 20)
    modelo = models.CharField(max_length = 25)
    tipoInstrumento = models.CharField(max_length = 15)
    color = models.CharField (max_length = 15)

class Pedal(models.Model):
    nombre = models.CharField (max_length = 25)
    efecto = models.CharField (max_length = 15)
    bypass = models.BooleanField ()

class Discos(models.Model):
    artista = models.CharField (max_length = 35)
    album = models.CharField (max_length = 35)
    fechaLanzamiento = models.DateField()
    