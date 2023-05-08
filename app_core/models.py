from django.db import models
from solo.models import SingletonModel


class ImagenCarousel(models.Model):
    imagen = models.ImageField('Imagen', upload_to='carousel/')


class Farmacia(SingletonModel):
    nombre = models.CharField('Nombre', max_length=120)
    direccion = models.TextField('Dirección')
    telefono = models.CharField('Teléfono', max_length=15)
    capacidad = models.PositiveIntegerField('Capacidad', )
    carousel = models.ManyToManyField(ImagenCarousel, verbose_name='Banners')

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

    def __str__(self): return self.nombre
