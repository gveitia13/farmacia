from django.urls import reverse_lazy
from django.views import generic

from app_core.models import Producto


class CrearProducto(generic.CreateView):
    model = Producto
    template_name = 'pages/create-update.html'
    success_url = reverse_lazy('producto-list')
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['text'] = 'Crear Producto'
        context['back_url'] = self.success_url
        return context


class EditarProducto(generic.UpdateView):
    model = Producto
    template_name = 'pages/create-update.html'
    success_url = reverse_lazy('producto-list')
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['text'] = f'Editar Producto {self.get_object()}'
        context['back_url'] = self.success_url
        return context


class ListarProducto(generic.ListView):
    model = Producto
    template_name = 'pages/products-cards.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['text'] = 'Listado de Productos'
        context['add_url'] = reverse_lazy('producto-crear')
        return context


class EliminarProducto(generic.DeleteView):
    model = Producto
    template_name = 'pages/delete.html'
    success_url = reverse_lazy('producto-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['model_name'] = 'Producto'
        context['back_url'] = self.success_url
        return context
