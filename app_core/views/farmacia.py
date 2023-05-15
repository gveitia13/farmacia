from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
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


class CrearFarmacia(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    template_name = 'pages/create-farmacia.html'
    model = Farmacia
    success_url = reverse_lazy('index')
    fields = '__all__'
    permission_required = ['app_core.add_farmacia']
    permission_denied_message = 'No posee permisos para entrar a este módulo'

    def handle_no_permission(self):
        messages.error(self.request, self.permission_denied_message)
        return redirect('index')

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


class EditarFarmacia(LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
    template_name = 'pages/update-farmacia.html'
    model = Farmacia
    success_url = reverse_lazy('index')
    fields = '__all__'
    permission_required = ['app_core.change_farmacia']
    permission_denied_message = 'No posee permisos para entrar a este módulo'

    def handle_no_permission(self):
        messages.error(self.request, self.permission_denied_message)
        return redirect('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        farmacia = Farmacia.objects.first() if Farmacia.objects.exists() else None
        context['farmacia'] = farmacia
        context['text'] = f'{"Editar"} Farmacia'
        context['back_url'] = self.success_url
        context['clasificion_list'] = Categoria.objects.all()
        return context


class EliminarFarmacia(LoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):
    model = Farmacia
    template_name = 'pages/delete.html'
    success_url = reverse_lazy('index')
    permission_required = ['app_core.delete_farmacia']
    permission_denied_message = 'No posee permisos para entrar a este módulo'

    def handle_no_permission(self):
        messages.error(self.request, self.permission_denied_message)
        return redirect('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['model_name'] = 'Farmacia'
        context['back_url'] = reverse_lazy('farmacia-editar', kwargs={'pk': self.get_object().pk})
        context['clasificion_list'] = Categoria.objects.all()
        return context
