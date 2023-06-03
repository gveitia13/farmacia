from django.contrib.auth.models import AbstractUser, Permission
from django.db import models
from solo.models import SingletonModel


class Farmacia(SingletonModel):
    nombre = models.CharField('Nombre', max_length=120)
    direccion = models.TextField('Dirección')
    telefono = models.CharField('Teléfono', max_length=15)
    capacidad = models.PositiveIntegerField('Capacidad', )

    def __str__(self): return self.nombre


class Categoria(models.Model):
    nombre = models.CharField("Nombre", max_length=120)
    descripcion = models.TextField('Descripción', null=True, blank=True)

    def __str__(self): return self.nombre

    class Meta:
        verbose_name = 'Clasificación'
        verbose_name_plural = 'Clasificaciones'


class Producto(models.Model):
    categoria = models.ForeignKey(Categoria, verbose_name='Clasificación', on_delete=models.CASCADE)
    nombre = models.CharField("Nombre", max_length=120)
    descripcion = models.TextField('Descripción', null=True, blank=True)
    foto = models.ImageField('Foto', upload_to='producto/')
    tipo = models.CharField('Tipo', max_length=130)
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self): return self.nombre


class User(AbstractUser):
    rol = models.CharField('Rol', choices=(
        ('1', 'Administrador'),
        ('2', 'Empleado'),
        ('3', 'Recursos Humanos'),
    ), max_length=2, default='2')

    REQUIRED_FIELDS = ['rol']
