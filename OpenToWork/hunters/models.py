from django.db import models

# Create your models here.
class Hunter(models.Model):
    name = models.CharField(max_length=50)
    mail = models.EmailField()
    ofertas = models.ForeignKey(Ofertas1, on_delete=models.CASCADE)
    trabaja = models.ManyToManyField(Empresas, on_delete=models.CASCADE)
    perfil_user = models.OneToOneField(Usuarios, on_delete=models.CASCADE)
    publico = models.BooleanField()
class Empresa(models.Model):
    name = models.CharField(max_length=50)
class Sector(models.Models):
    sector = models.ForeignKey(Categoria, on_delete=models.SET_NULL)
class Categoria(models.model):
    categoria = models.CharField(max_length=50)
    sector = models.ManyToOneRel(Sector, on_delete=models.SET_NULL)
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
