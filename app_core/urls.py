from django.urls import path

from app_core.views.categoria import CrearCategoria, ActualizarCategoria, ListarCategoria, EliminarCategoria, \
    FiltrarCategoria
from app_core.views.farmacia import IndexView, CrearFarmacia, EliminarFarmacia, EditarFarmacia
from app_core.views.producto import CrearProducto, ListarProducto, EditarProducto, EliminarProducto
from app_core.views.usuario import CrearUsuario, EditarUsuario, EliminarUsuario, ListarUsuario

urlpatterns = [
    # path('', lambda request: render(request, 'pages/start_page.html'), name='index'),
    path('', IndexView.as_view(), name='index'),
    # Clasificación
    path('crear-clasificacion/', CrearCategoria.as_view(), name='categoria-crear'),
    path('editar-clasificacion/<int:pk>/', ActualizarCategoria.as_view(), name='categoria-editar'),
    path('eliminar-clasificacion/<int:pk>/', EliminarCategoria.as_view(), name='categoria-eliminar'),
    path('listar-clasificacion/', ListarCategoria.as_view(), name='categoria-list'),
    path('filtrar-clasificacion/<int:pk>/', FiltrarCategoria.as_view(), name='categoria-filter'),
    # Producto
    path('crear-producto/', CrearProducto.as_view(), name='producto-crear'),
    path('listar-producto/', ListarProducto.as_view(), name='producto-list'),
    path('editar-producto/<int:pk>/', EditarProducto.as_view(), name='producto-editar'),
    path('eliminar-producto/<int:pk>/', EliminarProducto.as_view(), name='producto-eliminar'),
    # Farmacia
    path('crear-farmacia/', CrearFarmacia.as_view(), name='farmacia-crear'),
    path('eliminar-farmacia/<int:pk>/', EliminarFarmacia.as_view(), name='farmacia-eliminar'),
    path('editar-farmacia/<int:pk>/', EditarFarmacia.as_view(), name='farmacia-editar'),
    # Usuario
    path('crear-usuario/', CrearUsuario.as_view(), name='crear-usuario'),
    path('editar-usuario/<int:pk>/', EditarUsuario.as_view(), name='editar-usuario'),
    path('eliminar-usuario/<int:pk>/', EliminarUsuario.as_view(), name='eliminar-usuario'),
    path('listar-usuario/', ListarUsuario.as_view(), name='listar-usuario'),
]
