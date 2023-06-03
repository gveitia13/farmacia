from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from app_core.models import Farmacia, Producto, User


class ProductoForm(ModelForm):
    class Meta:
        fields = '__all__'
        model = Producto

    def clean(self):
        farmacia = Farmacia.objects.first() if Farmacia.objects.exists() else None
        if not farmacia:
            self.add_error('nombre', 'Debe registrar los datos de la farmacia antes de añadir un producto')
            return super().clean()
        cant = 0
        for p in Producto.objects.all():
            cant += p.cantidad

        cant += self.cleaned_data['cantidad']
        if cant > farmacia.capacidad:
            self.add_error('nombre',
                           'Ya la capacidad de la farmacia está llena, debe reducir la cantidad de un producto o aumentar '
                           'la capacidad de la Farmacia antes de añadir')

        return super().clean()


class MyUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'rol', 'email', 'password1', 'password2']
