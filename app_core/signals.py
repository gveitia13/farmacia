from django.contrib.auth.models import Permission
from django.db.models.signals import post_save
from django.dispatch import receiver

from app_core.models import User


@receiver(post_save, sender=User)
def add_permissions_user(sender, instance: User, created, **kwargs):
    if instance.rol == '1':
        instance.user_permissions.clear()
        for p in Permission.objects.all():
            print(p.codename)
            instance.user_permissions.add(p)
        print(instance.get_user_permissions())

    if instance.rol == '2':
        instance.user_permissions.clear()
        instance.user_permissions.add(Permission.objects.get(codename='add_categoria'))
        instance.user_permissions.add(Permission.objects.get(codename='change_categoria'))
        instance.user_permissions.add(Permission.objects.get(codename='delete_categoria'))
        instance.user_permissions.add(Permission.objects.get(codename='view_categoria'))
        instance.user_permissions.add(Permission.objects.get(codename='view_farmacia'))
        instance.user_permissions.add(Permission.objects.get(codename='add_producto'))
        instance.user_permissions.add(Permission.objects.get(codename='change_producto'))
        instance.user_permissions.add(Permission.objects.get(codename='delete_producto'))
        instance.user_permissions.add(Permission.objects.get(codename='view_producto'))
        instance.user_permissions.add(Permission.objects.get(codename='view_user'))
        print(instance.get_user_permissions())

    if instance.rol == '3':
        instance.user_permissions.clear()
        instance.user_permissions.add(Permission.objects.get(codename='add_user'))
        instance.user_permissions.add(Permission.objects.get(codename='change_user'))
        instance.user_permissions.add(Permission.objects.get(codename='delete_user'))
        instance.user_permissions.add(Permission.objects.get(codename='view_user'))
