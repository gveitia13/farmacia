from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic

from app_core.forms import MyUserForm
from app_core.models import User, Farmacia, Categoria


class CrearUsuario(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    model = User
    template_name = 'pages/create-update.html'
    success_url = reverse_lazy('listar-usuario')
    # fields = '__all__'
    form_class = MyUserForm
    permission_required = ['add_user']
    permission_denied_message = 'No posee permisos para entrar a este módulo'

    def handle_no_permission(self):
        messages.error(self.request, self.permission_denied_message)
        return redirect('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['text'] = 'Crear Usuario'
        context['back_url'] = self.success_url
        context['farmacia'] = Farmacia.objects.first() if Farmacia.objects.exists() else None
        context['clasificion_list'] = Categoria.objects.all()
        return context


class EditarUsuario(LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
    model = User
    template_name = 'pages/create-update.html'
    success_url = reverse_lazy('listar-usuario')
    # fields = '__all__'
    form_class = MyUserForm
    permission_required = ['change_user']
    permission_denied_message = 'No posee permisos para entrar a este módulo'

    def handle_no_permission(self):
        messages.error(self.request, self.permission_denied_message)
        return redirect('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['text'] = 'Editar Usuario'
        context['back_url'] = self.success_url
        context['farmacia'] = Farmacia.objects.first() if Farmacia.objects.exists() else None
        context['clasificion_list'] = Categoria.objects.all()
        return context


class EliminarUsuario(LoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):
    model = User
    template_name = 'pages/delete.html'
    success_url = reverse_lazy('listar-usuario')
    permission_required = ['delete_user']
    permission_denied_message = 'No posee permisos para entrar a este módulo'

    def handle_no_permission(self):
        messages.error(self.request, self.permission_denied_message)
        return redirect('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['model_name'] = 'Usuario'
        context['farmacia'] = Farmacia.objects.first() if Farmacia.objects.exists() else None
        context['back_url'] = self.success_url
        context['clasificion_list'] = Categoria.objects.all()
        return context


class ListarUsuario(LoginRequiredMixin, generic.ListView):
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
