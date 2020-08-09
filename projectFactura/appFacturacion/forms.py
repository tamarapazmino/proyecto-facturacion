from django import forms
from appFacturacion.models import Cliente, Producto


class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = "__all__"
        


class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = "__all__"
