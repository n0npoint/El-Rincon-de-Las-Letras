from django.shortcuts import render , redirect
from bodega.models.libro import *
from .carro_logica import Carrito


def agregar_producto(request, id_libro):

    carro = Carrito(request)
    producto = TbLibros.objects.get(id_libro=id_libro)
    carro.agregar_producto(producto=producto)

    return redirect("catalogo")


def eliminar_producto(request, id_libro):

    carro = Carrito(request)
    producto =  TbLibros.objects.get(id_libro=id_libro)

    carro.eliminar_producto(producto=producto)

    return redirect ("catalogo")

def limpiar_carro(request):

    carro = Carrito(request)

    carro.limpiar_carro()

    return redirect ("catalogo")
    




# Create your views here.


def carrito (request):

    return render(request , 'compras/carrito.html')