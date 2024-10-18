from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class FuenteOfertas2(models.Model):
    name = models.CharField(max_length=50)
class Sector(models.Models):
    sector = models.CharField(max_length=100)
class CategoriaSector(models.Model):
    name_categoria = models.CharField(max_length=100)
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
class Trabajo(models.Model):
    TIPO_CONTRATO_CHOICES = [
        ('Tiempo Completo', 'Tiempo Completo'),
        ('Medio Tiempo', 'Medio Tiempo'),
        ('Freelance', 'Freelance'),
        # Agrega más opciones según sea necesario
    ]
    
    JORNADA_CHOICES = [
        ('Diurna', 'Diurna'),
        ('Nocturna', 'Nocturna'),
        ('Mixta', 'Mixta'),
        # Agrega más opciones según sea necesario
    ]
    
    LOCALIZACION_CHOICES = [
        ('Presencial', 'Presencial'),
        ('Remoto', 'Remoto'),
        ('Híbrido', 'Híbrido'),
        # Agrega más opciones según sea necesario
    ]

class Ofertas1(models.Model):
    name = models.CharField(max_length=150)
    descripcion = models.TextField(max_length=500)
    fecha = models.DateTimeField()
    sector = models.OneToOneField(Sector, on_delete=models.SET_NULL)
    hunter = models.OneToOneField(Hunter, on_delete=models.SET_NULL)
    tipoContrato = models.CharField(max_length=30, choices=Trabajo.TIPO_CONTRATO_CHOICES)
    jornada = models.CharField(max_length=30, choices=Trabajo.JORNADA_CHOICES)
    localizacion = models.CharField(max_length=30, choices=Trabajo.LOCALIZACION_CHOICES)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    plazasDisponibles = models.IntegerField()
class Ofertas2(models.Model):
    name = models.CharField(max_length=150)
    descripcion = models.TextField(max_length=500)
    fecha = models.DateTimeField()
    sector = models.OneToOneField(Sector, on_delete=models.SET_NULL)
    tipoContrato = models.CharField(max_length=30, choices=Trabajo.TIPO_CONTRATO_CHOICES)
    jornada = models.CharField(max_length=30, choices=Trabajo.JORNADA_CHOICES)
    localizacion = models.CharField(max_length=30, choices=Trabajo.LOCALIZACION_CHOICES)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    plazasDisponibles = models.IntegerField()
    fentes = models.ForeignKey(FuenteOfertas2, on_delete=models.CASCADE)
class Hunter(models.Model):
    name = models.CharField(max_length=50)
    mail = models.EmailField()
    ofertas = models.ForeignKey(Ofertas1, on_delete=models.CASCADE)
    trabaja = models.CharField(max_length=50)
    perfil_user = models.OneToOneField(User, on_delete=models.CASCADE)
    publico = models.BooleanField()

# scraping, secotr, web, fechas de scraping, hora de automatico, fecha maxima