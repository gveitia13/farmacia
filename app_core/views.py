from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from app_core.models import Categoria


class CrearCategoria(generic.CreateView):
    model = Categoria
    template_name = 'pages/create-update.html'
    success_url = reverse_lazy('index')
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['text'] = 'Crear Clasificación'
        return context


class ActualizarCategoria(generic.UpdateView):
    model = Categoria
    template_name = 'pages/create-update.html'
    success_url = reverse_lazy('index')
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['text'] = f'Actualizar Clasificación f{self.get_object()}'
        return context
