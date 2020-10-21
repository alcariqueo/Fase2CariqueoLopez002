from django.db import models
from django.urls import reverse
import uuid


class Usuario(models.Model):
    Nombre=models.CharField(max_length=50)
    Apellido=models.CharField(max_length=50)
    Email=models.EmailField(null=True, blank=True)
    FechaN=models.DateField(null=True, blank=True)
    Telefono=models.IntegerField(null=True, blank=True)
    password=models.CharField(max_length=6)
    passwordC=models.CharField(max_length=6)


    def str(self):
        return self.Email

   
