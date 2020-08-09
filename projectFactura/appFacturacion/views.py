from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator
from appFacturacion.forms import ClienteForm, ProductoForm
from appFacturacion.models import Cliente, Producto, Factura, DetalleFactura
# Create your views here.


def index(request):
    return render(request, 'card-menu.html')


def clientemostrar(request):
    cli = Cliente.objects.all()
    paginas = request.GET.get('page', 1)
    paginacion = Paginator(cli, 2)  # numero de paginas
    cli = paginacion.page(paginas)
    clientes = Cliente.objects.prefetch_related(
        'producto').all().values('id', 'producto__descripcion')
    return render(request, 'clientes-detalle.html', {'clientes': clientes, 'cli': cli})


def clientenuevo(request):
    if request.method == 'POST':
        clienteform = ClienteForm(request.POST)
        if clienteform.is_valid():
            try:
                clienteform.save()
                return redirect('/clientes/')
            except:
                pass
    else:
        clienteform = ClienteForm()
    return render(request, 'clientes-nuevo.html', {'formcliente': clienteform})


def clienteeditar(request, id):
    cliente = Cliente.objects.get(id=id)
    productos = Cliente.objects.prefetch_related('producto').filter(id=cliente.id).values('id','producto__descripcion','producto__id')
    return render(request, 'clientes-editar.html', {'cliente': cliente,'productos':productos})


def clienteactua(request, id):
    cliente = Cliente.objects.get(id=id)
    clienteform = ClienteForm(request.POST, instance=cliente)
    if clienteform.is_valid():
        try:
            clienteform.save()
        except:
            pass
        return redirect('/clientes/')
    return render(request, 'clientes-editar.html', {'cliente': cliente})

def cliente_form_eliminar(request, id):
    cliente = Cliente.objects.get(id=id)
    return render(request, 'clientes-eliminar.html', {'cliente': cliente})

def cliente_eliminar(request,id):
    Cliente.objects.filter(id=id).delete()
    return redirect('/clientes/')

#VISTA EN FUNCIONES DE PRODUCTOS
def productomostrar(request):
    productos = Producto.objects.all()
    paginas = request.GET.get('page', 1)
    paginacion = Paginator(productos, 2)  # numero de paginas
    productos = paginacion.page(paginas)
    return render(request, 'productos-detalle.html', {'productos': productos})

def productonuevo(request):
    if request.method == 'POST':
        productoform = ProductoForm(request.POST)
        if productoform.is_valid():
            try:
                productoform.save()
                redirect('/productos/')
            except:
                pass
    else:
        productoform = ProductoForm()
    return render(request,'productos-nuevo.html',{'productoform':productoform})

def productoeditar(request,id):
    producto = Producto.objects.get(id=id)
    return render(request,'productos-editar.html',{'producto':producto})

def productoactua(request,id):
    producto = Producto.objects.get(id=id)
    productoform = ProductoForm(request.POST, instance=producto)
    if productoform.is_valid():
        try:
            productoform.save()
        except:
            pass
        return redirect('/productos/')
    return render(request, 'productos-editar.html', {'producto': producto})

def producto_form_eliminar(request, id):
    producto = Producto.objects.get(id=id)
    return render(request, 'productos-eliminar.html', {'producto': producto})

def producto_eliminar(request,id):
    Producto.objects.filter(id=id).delete()
    return redirect('/productos/')

def ventamostrar(request):
    ventas =  Factura.objects.select_related('cliente').all().values('id','cliente__nombre','fecha','total') 
    return render(request,'ventas-detalle.html',{'ventas':ventas})