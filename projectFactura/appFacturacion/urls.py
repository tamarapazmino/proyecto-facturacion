from django.urls import path
from .views import index, clientemostrar, clientenuevo,clienteeditar,\
clienteactua,cliente_form_eliminar, cliente_eliminar,\
productomostrar,productonuevo,productoeditar,productoactua,producto_form_eliminar, producto_eliminar,\
ventamostrar
urlpatterns = [
    #VISTA DE INDEX
    path('', index, name='Index'),
    #VISTA DE CLIENTES
    path('clientes/',clientemostrar,name='clientes'),
    path('clientes/nuevo/',clientenuevo,name='clientes/nuevo/'),
    path('clientes/editar/<int:id>',clienteeditar),
    path('clientes/actualizar/<int:id>',clienteactua),
    path('clientes/eliminar/<int:id>',cliente_form_eliminar),
    path('clientes/elim/<int:id>',cliente_eliminar),
    #VISTA DE PRODUCTOS
    path('productos/',productomostrar,name='productos'),
    path('productos/nuevo/',productonuevo,name='productos/nuevo/'),
    path('productos/editar/<int:id>',productoeditar),
    path('productos/actualizar/<int:id>',productoactua),
    path('productos/eliminar/<int:id>',producto_form_eliminar),
    path('productos/elim/<int:id>',producto_eliminar),
    #VISTA DE VENTAS
    path('ventas/',ventamostrar, name='ventas')
]
