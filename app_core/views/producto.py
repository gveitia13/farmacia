from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from app_core.models import Producto, Farmacia, Categoria


class CrearProducto(LoginRequiredMixin, generic.CreateView):
    model = Producto
    template_name = 'pages/create-update.html'
    success_url = reverse_lazy('producto-list')
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['text'] = 'Crear Producto'
        context['back_url'] = self.success_url
        context['farmacia'] = Farmacia.objects.first() if Farmacia.objects.exists() else None
        context['clasificion_list'] = Categoria.objects.all()
        return context


class EditarProducto(LoginRequiredMixin, generic.UpdateView):
    model = Producto
    template_name = 'pages/create-update.html'
    success_url = reverse_lazy('producto-list')
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['text'] = f'Editar Producto {self.get_object()}'
        context['back_url'] = self.success_url
        context['farmacia'] = Farmacia.objects.first() if Farmacia.objects.exists() else None
        context['clasificion_list'] = Categoria.objects.all()
        return context


class ListarProducto(generic.ListView):
    model = Producto
    template_name = 'pages/products-cards.html'

    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.GET.get('search'):
            return qs.filter(nombre__icontains=self.request.GET.get('search'))
        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['text'] = 'Listado de Productos'
        context['add_url'] = reverse_lazy('producto-crear')
        context['farmacia'] = Farmacia.objects.first() if Farmacia.objects.exists() else None
        context['clasificion_list'] = Categoria.objects.all()
        return context


class EliminarProducto(LoginRequiredMixin, generic.DeleteView):
    model = Producto
    template_name = 'pages/delete.html'
    success_url = reverse_lazy('producto-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['model_name'] = 'Producto'
        context['farmacia'] = Farmacia.objects.first() if Farmacia.objects.exists() else None
        context['back_url'] = self.success_url
        context['clasificion_list'] = Categoria.objects.all()
        return context
