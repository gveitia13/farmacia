from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from app_core.models import Categoria, Farmacia, Producto


class CrearCategoria(LoginRequiredMixin, generic.CreateView):
    model = Categoria
    template_name = 'pages/create-update.html'
    success_url = reverse_lazy('categoria-list')
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['text'] = 'Crear Clasificación'
        context['back_url'] = self.success_url
        context['farmacia'] = Farmacia.objects.first() if Farmacia.objects.exists() else None
        context['clasificion_list'] = Categoria.objects.all()
        return context


class ActualizarCategoria(LoginRequiredMixin, generic.UpdateView):
    model = Categoria
    template_name = 'pages/create-update.html'
    success_url = reverse_lazy('categoria-list')
    fields = '__all__'

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


class EliminarCategoria(LoginRequiredMixin, generic.DeleteView):
    model = Categoria
    template_name = 'pages/delete.html'
    success_url = reverse_lazy('categoria-list')

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
