from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from app_core.forms import MyUserForm
from app_core.models import User, Farmacia, Categoria


class CrearUsuario(LoginRequiredMixin, generic.CreateView):
    model = User
    template_name = 'pages/create-update.html'
    success_url = reverse_lazy('listar-usuario')
    # fields = '__all__'
    form_class = MyUserForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['text'] = 'Crear Usuario'
        context['back_url'] = self.success_url
        context['farmacia'] = Farmacia.objects.first() if Farmacia.objects.exists() else None
        context['clasificion_list'] = Categoria.objects.all()
        return context


class EditarUsuario(LoginRequiredMixin, generic.UpdateView):
    model = User
    template_name = 'pages/create-update.html'
    success_url = reverse_lazy('listar-usuario')
    # fields = '__all__'
    form_class = MyUserForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['text'] = 'Editar Usuario'
        context['back_url'] = self.success_url
        context['farmacia'] = Farmacia.objects.first() if Farmacia.objects.exists() else None
        context['clasificion_list'] = Categoria.objects.all()
        return context


class EliminarUsuario(LoginRequiredMixin, generic.DeleteView):
    model = User
    template_name = 'pages/delete.html'
    success_url = reverse_lazy('listar-usuario')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['model_name'] = 'Usuario'
        context['farmacia'] = Farmacia.objects.first() if Farmacia.objects.exists() else None
        context['back_url'] = self.success_url
        context['clasificion_list'] = Categoria.objects.all()
        return context


class ListarUsuario(generic.ListView):
    model = User
    template_name = 'pages/user-list.html'

    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.GET.get('search'):
            return qs.filter(username__icontains=self.request.GET.get('search'))
        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['text'] = 'Listado de Usuarios'
        context['add_url'] = reverse_lazy('crear-usuario')
        context['farmacia'] = Farmacia.objects.first() if Farmacia.objects.exists() else None
        context['clasificion_list'] = Categoria.objects.all()
        return context
