from django.db import models

# Create your models here.

class Persona(models.Model):
    nombre = models.CharField(max_length=50,blank=False,null=False)
    peso = models.PositiveIntegerField(blank=False,null=False)
    talla = models.PositiveSmallIntegerField(blank=False,null=False)
    imc = models.DecimalField(max_digits=4, decimal_places=1,null=True)
    estado = models.CharField(max_length=20,blank=True,null=True)