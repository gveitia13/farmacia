from django.urls import path

from app_core.views.categoria import CrearCategoria, ActualizarCategoria, ListarCategoria, EliminarCategoria
from app_core.views.farmacia import IndexView, CrearFarmacia, EliminarFarmacia, EditarFarmacia
from app_core.views.producto import CrearProducto, ListarProducto, EditarProducto, EliminarProducto

urlpatterns = [
    # path('', lambda request: render(request, 'pages/start_page.html'), name='index'),
    path('', IndexView.as_view(), name='index'),
    # Clasificación
    path('crear-clasificacion/', CrearCategoria.as_view(), name='categoria-crear'),
    path('editar-clasificacion/<int:pk>/', ActualizarCategoria.as_view(), name='categoria-editar'),
    path('eliminar-clasificacion/<int:pk>/', EliminarCategoria.as_view(), name='categoria-eliminar'),
    path('listar-clasificacion/', ListarCategoria.as_view(), name='categoria-list'),
    # Producto
    path('crear-producto/', CrearProducto.as_view(), name='producto-crear'),
    path('listar-producto/', ListarProducto.as_view(), name='producto-list'),
    path('editar-producto/<int:pk>/', EditarProducto.as_view(), name='producto-editar'),
    path('eliminar-producto/<int:pk>/', EliminarProducto.as_view(), name='producto-eliminar'),
    # Farmacia
    path('crear-farmacia/', CrearFarmacia.as_view(), name='farmacia-crear'),
    path('eliminar-farmacia/<int:pk>/', EliminarFarmacia.as_view(), name='farmacia-eliminar'),
    path('editar-farmacia/<int:pk>/', EditarFarmacia.as_view(), name='farmacia-editar'),
]
