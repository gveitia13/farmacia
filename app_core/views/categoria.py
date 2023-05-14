from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic

from app_core.models import Categoria, Farmacia, Producto


class CrearCategoria(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    model = Categoria
    template_name = 'pages/create-update.html'
    success_url = reverse_lazy('categoria-list')
    fields = '__all__'
    permission_required = ['add_categoria']
    permission_denied_message = 'No posee permisos para entrar a este módulo'

    def handle_no_permission(self):
        messages.error(self.request, self.permission_denied_message)
        return redirect('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['text'] = 'Crear Clasificación'
        context['back_url'] = self.success_url
        context['farmacia'] = Farmacia.objects.first() if Farmacia.objects.exists() else None
        context['clasificion_list'] = Categoria.objects.all()
        return context


class ActualizarCategoria(LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
    model = Categoria
    template_name = 'pages/create-update.html'
    success_url = reverse_lazy('categoria-list')
    fields = '__all__'
    permission_required = ['change_categoria']
    permission_denied_message = 'No posee permisos para entrar a este módulo'

    def handle_no_permission(self):
        messages.error(self.request, self.permission_denied_message)
        return redirect('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['text'] = f'Actualizar Clasificación {self.get_object()}'
        context['back_url'] = self.success_url
        context['farmacia'] = Farmacia.objects.first() if Farmacia.objects.exists() else None
        context['clasificion_list'] = Categoria.objects.all()
        return context


class ListarCategoria(generic.ListView):
    model = Categoria
    template_name = 'pages/table-list.html'

    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.GET.get('search'):
            return qs.filter(nombre__icontains=self.request.GET.get('search'))
        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['text'] = 'Listado de Clasificaciones'
        context['add_url'] = reverse_lazy('categoria-crear')
        context['farmacia'] = Farmacia.objects.first() if Farmacia.objects.exists() else None
        context['clasificion_list'] = Categoria.objects.all()
        return context


class EliminarCategoria(LoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):
    model = Categoria
    template_name = 'pages/delete.html'
    success_url = reverse_lazy('categoria-list')
    permission_required = ['delete_categoria']
    permission_denied_message = 'No posee permisos para entrar a este módulo'

    def handle_no_permission(self):
        messages.error(self.request, self.permission_denied_message)
        return redirect('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['model_name'] = 'Categoría'
        context['back_url'] = self.success_url
        context['farmacia'] = Farmacia.objects.first() if Farmacia.objects.exists() else None
        context['clasificion_list'] = Categoria.objects.all()
        return context


class FiltrarCategoria(generic.DetailView):
    model = Categoria
    template_name = 'pages/products-cards.html'
    success_url = reverse_lazy('categoria-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['model_name'] = 'Categoría'
        context['back_url'] = self.success_url
        context['farmacia'] = Farmacia.objects.first() if Farmacia.objects.exists() else None
        context['clasificion_list'] = Categoria.objects.all()
        category = self.get_object()
        context['text'] = f'Productos de clasificación "{category}"'
        context['object_list'] = Producto.objects.filter(categoria=category)
        return context
