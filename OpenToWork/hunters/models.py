from django.db import models

class Hunter(models.Model):
    name = models.CharField(max_length=50)
    mail = models.EmailField()
    ofertas = models.ForeignKey('Ofertas1', on_delete=models.CASCADE)  # ForeignKey relaciona con Ofertas
    trabaja = models.ManyToManyField('Empresa')  # No es necesario on_delete en ManyToManyField
    perfil_user = models.OneToOneField('Usuarios', on_delete=models.CASCADE)
    publico = models.BooleanField()

class Empresa(models.Model):
    name = models.CharField(max_length=50)

class Sector(models.Model):  # Cambié models.Models a models.Model
    sector = models.CharField(max_length=50)  # Agregado un campo de nombre para el sector

class Categoria(models.Model):  # Cambié models.model a models.Model
    categoria = models.CharField(max_length=50)
    sector = models.ForeignKey(Sector, null=True, blank=True, on_delete=models.SET_NULL)  # Relación de uno a muchos

class Trabajo(models.Model):
    TIPO_CONTRATO_CHOICES = [
        ('Tiempo Completo', 'Tiempo Completo'),
        ('Medio Tiempo', 'Medio Tiempo'),
        ('Freelance', 'Freelance'),
    ]
    
    JORNADA_CHOICES = [
        ('Diurna', 'Diurna'),
        ('Nocturna', 'Nocturna'),
        ('Mixta', 'Mixta'),
    ]
    
    LOCALIZACION_CHOICES = [
        ('Presencial', 'Presencial'),
        ('Remoto', 'Remoto'),
        ('Híbrido', 'Híbrido'),
    ]
    
    tipoContrato = models.CharField(max_length=30, choices=TIPO_CONTRATO_CHOICES)
    jornada = models.CharField(max_length=30, choices=JORNADA_CHOICES)
    localizacion = models.CharField(max_length=30, choices=LOCALIZACION_CHOICES)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    plazasDisponibles = models.IntegerField()

class Ofertas1(models.Model):
    name = models.CharField(max_length=150)
    descripcion = models.TextField(max_length=500)
    fecha = models.DateTimeField()
    sector = models.ForeignKey(Sector, null=True, blank=True, on_delete=models.SET_NULL)  # Cambié OneToOneField a ForeignKey
    hunter = models.OneToOneField(Hunter, null=True, blank=True, on_delete=models.SET_NULL)  # Para evitar errores, se agregó null y blank
    tipoContrato = models.CharField(max_length=30, choices=Trabajo.TIPO_CONTRATO_CHOICES)
    jornada = models.CharField(max_length=30, choices=Trabajo.JORNADA_CHOICES)
    localizacion = models.CharField(max_length=30, choices=Trabajo.LOCALIZACION_CHOICES)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    plazasDisponibles = models.IntegerField()

# Si Ofertas2 es realmente necesaria, debería ser una variación de Ofertas1.
class Ofertas2(models.Model):
    name = models.CharField(max_length=150)
    descripcion = models.TextField(max_length=500)
    fecha = models.DateTimeField()
    sector = models.ForeignKey(Sector, null=True, blank=True, on_delete=models.SET_NULL)
    tipoContrato = models.CharField(max_length=30, choices=Trabajo.TIPO_CONTRATO_CHOICES)
    jornada = models.CharField(max_length=30, choices=Trabajo.JORNADA_CHOICES)
    localizacion = models.CharField(max_length=30, choices=Trabajo.LOCALIZACION_CHOICES)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    plazasDisponibles = models.IntegerField()
