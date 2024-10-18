from django.db import models

# Create your models here.
class Hunter(models.Model):
    name = models.CharField(max_length=50)
    mail = models.EmailField()
    ofertas = models.ForeignKey(Ofertas, on_delete=models.CASCADE)
    trabaja = models.ManyToManyField(Empresas, on_delete=models.CASCADE)
    perfil_user = models.OneToOneField(Usuarios, on_delete=models.CASCADE)
    publico = models.BooleanField()
class Empresa(models.Model):
    name = models.CharField(max_length=50)
class Sector(models.Models):
    categoria = models.CharField(max_length=50)