from django.shortcuts import render
from django.urls import path

from app_core.views import CrearCategoria, ActualizarCategoria

urlpatterns = [
    path('', lambda request: render(request, 'pages/start_page.html'), name='index'),
    path('crear-clasificacion/', CrearCategoria.as_view(), name='categoria-crear'),
    path('editar-clasificacion/<int:pk>/', ActualizarCategoria.as_view(), name='categoria-editar'),
]
