from django.db import models

# Create your models here.


class Producto(models.Model):
    descripcion = models.CharField(max_length=100, blank=False, null=False)
    precio = models.FloatField(default=0)
    stock = models.FloatField(default=0)
    iva = models.BooleanField(default=True)
    creacion = models.DateTimeField(
        auto_now_add=True, verbose_name='Fecha Creación')

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['-creacion']

    def __str__(self):
        return self.descripcion


class Cliente(models.Model):
    ruc = models.CharField(max_length=13)
    nombre = models.CharField(max_length=300)
    direccion = models.TextField(blank=True, null=True)
    producto = models.ManyToManyField(Producto)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.nombre


class Factura(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateField()
    total = models.FloatField(default=0)

    class Meta:
        verbose_name = 'Factura'
        verbose_name_plural = 'Facturas'

    def __str__(self):
        return self.cliente.nombre


class DetalleFactura(models.Model):
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.FloatField(default=0, blank=False, null=False)
    precio = models.FloatField(default=0, blank=False, null=False)
    subtotal = models.FloatField(default=0, blank=False, null=False)

    def __str__(self):
        return self.factura.cliente.nombre