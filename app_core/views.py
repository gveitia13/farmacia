from django.shortcuts import render
from django.views import generic

from app_core.models import Categoria


class CrearCategoria(generic.CreateView):
    model = Categoria

