from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from app_core.models import Categoria


class CrearCategoria(generic.CreateView):
    model = Categoria
    template_name = 'pages/create-update.html'
    success_url = reverse_lazy('categoria-list')
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['text'] = 'Crear Clasificación'
        context['back_url'] = self.success_url
        return context


class ActualizarCategoria(generic.UpdateView):
    model = Categoria
    template_name = 'pages/create-update.html'
    success_url = reverse_lazy('categoria-list')
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['text'] = f'Actualizar Clasificación {self.get_object()}'
        context['back_url'] = self.success_url
        return context


class ListarCategoria(generic.ListView):
    model = Categoria
    template_name = 'pages/table-list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['text'] = 'Listado de Clasificaciones'
        context['add_url'] = reverse_lazy('categoria-crear')
        return context


class EliminarCategoria(generic.DeleteView):
    model = Categoria
    template_name = 'pages/delete.html'
    success_url = reverse_lazy('categoria-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['model_name'] = 'Categoría'
        context['back_url'] = self.success_url
        return context
