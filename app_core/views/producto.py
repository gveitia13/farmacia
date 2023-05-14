from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic

from app_core.forms import ProductoForm
from app_core.models import Producto, Farmacia, Categoria


class CrearProducto(LoginRequiredMixin, PermissionRequiredMixin,generic.CreateView):
    model = Producto
    template_name = 'pages/create-update.html'
    success_url = reverse_lazy('producto-list')
    form_class = ProductoForm
    permission_required = ['add_producto']
    permission_denied_message = 'No posee permisos para entrar a este módulo'

    def handle_no_permission(self):
        messages.error(self.request, self.permission_denied_message)
        return redirect('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['text'] = 'Crear Producto'
        context['back_url'] = self.success_url
        context['farmacia'] = Farmacia.objects.first() if Farmacia.objects.exists() else None
        context['clasificion_list'] = Categoria.objects.all()
        return context


class EditarProducto(LoginRequiredMixin, PermissionRequiredMixin,generic.UpdateView):
    model = Producto
    template_name = 'pages/create-update.html'
    success_url = reverse_lazy('producto-list')
    fields = '__all__'
    permission_required = ['change_producto']
    permission_denied_message = 'No posee permisos para entrar a este módulo'

    def handle_no_permission(self):
        messages.error(self.request, self.permission_denied_message)
        return redirect('index')

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


class EliminarProducto(LoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):
    model = Producto
    template_name = 'pages/delete.html'
    success_url = reverse_lazy('producto-list')
    permission_required = ['delete_producto']
    permission_denied_message = 'No posee permisos para entrar a este módulo'

    def handle_no_permission(self):
        messages.error(self.request, self.permission_denied_message)
        return redirect('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['model_name'] = 'Producto'
        context['farmacia'] = Farmacia.objects.first() if Farmacia.objects.exists() else None
        context['back_url'] = self.success_url
        context['clasificion_list'] = Categoria.objects.all()
        return context
