from django.db import models
from django.urls import reverse
import uuid


class Usuario(models.Model):
<<<<<<< HEAD
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(null=True, blank=True)
    fechaN = models.DateField(null=True, blank=True)
    telefono = models.IntegerField(null=True, blank=True)
    password = models.CharField(max_length=6)

=======
    Nombre=models.CharField(max_length=50)
    Apellido=models.CharField(max_length=50)
    Email=models.EmailField(null=True, blank=True)
    FechaN=models.DateField(null=True, blank=True)
    Telefono=models.IntegerField(null=True, blank=True)
    password=models.CharField(max_length=6)
    passwordC=models.CharField(max_length=6)
>>>>>>> f0a3373852944327dde91fd3c481cbd19cc5a3a0

    def __str__(self):
        return self.nombre
    
    def get_absolute_url(self):
        return reverse('usuario-detail', args=[str(self.id)])

<<<<<<< HEAD
=======
    def str(self):
        return self.Email
>>>>>>> f0a3373852944327dde91fd3c481cbd19cc5a3a0

   
