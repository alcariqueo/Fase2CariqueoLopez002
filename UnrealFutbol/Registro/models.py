from django.db import models

import uuid


class Usuario(models.Model):
    Nombre=models.CharField(max_length=100)
    Apellido=models.CharField(max_length=100)
    Email=models.EmailField( null=True, blank=True)
    FechaN=models.DateField(null=True, blank=True)
    Telefono=models.IntegerField()
    password=models.CharField(max_length=6)
    passwordC=models.CharField(max_length=6)


    def str(self):
        return "usuario creado"
        

   
