# Generated by Django 4.2.1 on 2023-06-03 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_core', '0002_alter_user_rol'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='cantidad',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
