from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic

from app_core.models import Farmacia, Producto, Categoria


class IndexView(generic.ListView):
    template_name = 'pages/start_page.html'
    queryset = Producto.objects.all().order_by('-pk')

    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.GET.get('search'):
            return qs.filter(nombre__icontains=self.request.GET.get('search'))
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['farmacia'] = Farmacia.objects.first() if Farmacia.objects.exists() else None
        context['text'] = 'Últimos productos'
        context['add_url'] = reverse_lazy('producto-crear')
        context['clasificion_list'] = Categoria.objects.all()
        print(context['object_list'])
        return context


class CrearFarmacia(LoginRequiredMixin, generic.CreateView):
    template_name = 'pages/create-farmacia.html'
    model = Farmacia
    success_url = reverse_lazy('index')
    fields = '__all__'

    def get(self, request, *args, **kwargs):
        farmacia = Farmacia.objects.first() if Farmacia.objects.exists() else None
        if farmacia:
            return redirect(reverse_lazy('farmacia-editar', kwargs={'pk': farmacia.pk}))
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        farmacia = Farmacia.objects.first() if Farmacia.objects.exists() else None
        context['farmacia'] = farmacia
        context['text'] = f'{"Crear"} Farmacia'
        context['back_url'] = self.success_url
        context['clasificion_list'] = Categoria.objects.all()
        return context


class EditarFarmacia(LoginRequiredMixin, generic.UpdateView):
    template_name = 'pages/update-farmacia.html'
    model = Farmacia
    success_url = reverse_lazy('index')
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        farmacia = Farmacia.objects.first() if Farmacia.objects.exists() else None
        context['farmacia'] = farmacia
        context['text'] = f'{"Editar"} Farmacia'
        context['back_url'] = self.success_url
        context['clasificion_list'] = Categoria.objects.all()
        return context


class EliminarFarmacia(LoginRequiredMixin, generic.DeleteView):
    model = Farmacia
    template_name = 'pages/delete.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['model_name'] = 'Farmacia'
        context['back_url'] = reverse_lazy('farmacia-editar', kwargs={'pk': self.get_object().pk})
        context['clasificion_list'] = Categoria.objects.all()
        return context
