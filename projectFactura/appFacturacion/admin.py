from django.contrib import admin

# Register your models here.
from .models import Producto, Cliente, Factura, DetalleFactura


class ProductoAdmin(admin.ModelAdmin):
    readonly_fields = ['creacion']
    list_display = ('descripcion', 'precio', 'stock', 'iva', 'creacion')
    ordering = ('descripcion',)
    search_fields = ('descripcion',)
    list_filter = ('descripcion',)


class ClienteAdmin(admin.ModelAdmin):
    list_display = ('ruc', 'nombre', 'direccion')
    ordering = ('nombre',)
    search_fields = ('nombre',)
    list_filter = ('ruc', 'nombre')


admin.site.register(Producto, ProductoAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Factura)
admin.site.register(DetalleFactura)
# USUARIO ADMINISTRADOR
#usuario: admin
#password: admin123
