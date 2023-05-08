# Generated by Django 4.2.1 on 2023-05-08 04:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=120, verbose_name='Nombre')),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name='Descripción')),
            ],
            options={
                'verbose_name': 'Clasificación',
                'verbose_name_plural': 'Clasificaciones',
            },
        ),
        migrations.CreateModel(
            name='ImagenCarousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='carousel/', verbose_name='Imagen')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=120, verbose_name='Nombre')),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name='Descripción')),
                ('foto', models.ImageField(upload_to='producto/', verbose_name='Foto')),
                ('tipo', models.CharField(max_length=130, verbose_name='Tipo')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_core.categoria', verbose_name='Clasificación')),
            ],
        ),
        migrations.CreateModel(
            name='Farmacia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=120, verbose_name='Nombre')),
                ('direccion', models.TextField(verbose_name='Dirección')),
                ('telefono', models.CharField(max_length=15, verbose_name='Teléfono')),
                ('capacidad', models.PositiveIntegerField(verbose_name='Capacidad')),
                ('carousel', models.ManyToManyField(to='app_core.imagencarousel', verbose_name='Banners')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]