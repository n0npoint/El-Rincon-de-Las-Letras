from django.shortcuts import get_object_or_404, redirect, render
from ventas.Views.facturas.factura_logica import obtener_fecha , obtener_hora
from django.core.paginator import Paginator 
from ventas.models.librosxventas import TbLibrosxventas
from ventas.models.ventas import TbVentas
from ventas.models.facturaCliente import *
from django.db.models import Sum
from django.http import Http404

########################################################################
#-------------------------PAGINADOR-------------------------------------#
def paginar_facturas(items, page):
    try:
        paginator = Paginator(items, 10)
        items = paginator.page(page)
    except:
        raise Http404
    
    return items, paginator

###########################################################################

def miperfil(request):
    usuario_actual = request.user
    
    try:
        cliente = TbCliente.objects.get(username=usuario_actual)
        total = total_compras(cliente.id_cliente)
        facturas = obtener_facturas_por_cliente(cliente.id_cliente)

        pagina = request.GET.get('page') or 1
        facturas, paginator = paginar_facturas(facturas, pagina)

        data = {
            "username": usuario_actual,
            "nombre": cliente.nombre,
            "apellido": cliente.apellido,
            "dni": cliente.dni,
            "telefono": cliente.numero_telefono,
            "direccion": cliente.direccion,
            "total_compra": total,
            'items': facturas,
            'paginator': paginator,
        }

        return render(request, 'perfil/miperfil.html', data)

    except TbCliente.DoesNotExist:
        return render(request, 'error/404.html')

    
def mifactura(request, id_factura):
    # Obtener la factura correcta usando get_object_or_404
    factura = get_object_or_404(TbFacturaCliente, id_factura=id_factura)
    id_factura = factura.id_factura
    cliente_id = factura.id_cliente_id
    empleado_id = factura.id_empleado_id
    cliente = TbCliente.objects.get(id_cliente=cliente_id)
    id_libros_por_venta = []
    fecha_actual = obtener_fecha()
    hora_actual = obtener_hora()

    ventas_asociadas = TbVentas.objects.filter(id_factura=id_factura)

    id_libros_por_venta = []

    for venta in ventas_asociadas:
                try:
                    libro_venta = TbLibrosxventas.objects.get(id_venta=venta.id_venta)
                    id_libro = libro_venta.id_libro 
                    id_libros_por_venta.append(id_libro)
                except TbLibrosxventas.DoesNotExist:
                    return redirect("miperfil")

    try:
        empleado = TbEmpleado.objects.get(id_empleado=empleado_id)
        id_empelado = empleado.id_empleado
        nombre_empleado = empleado.nombre
        apellido_empleado = empleado.apellido

    except TbEmpleado.DoesNotExist:
        id_empelado = None
        nombre_empleado = None
        apellido_empleado = None

    data = {
        "factura": factura.id_factura,
        "id_cliente": factura.id_cliente,
        "nombre_cliente": cliente.nombre,
        "apellido_cliente": cliente.apellido,
        "direccion": cliente.direccion,
        "telefono": cliente.numero_telefono ,
        "email": cliente.email, 
        "id_empleado": id_empelado ,
        "nombre_empleado": nombre_empleado ,
        "apellido_empleado":apellido_empleado,
        "fecha_emision": factura.fecha_emision,
        "subtotal": factura.subtotal,
        "impuesto": factura.impuesto,
        "total_compra": factura.total_compra,
        "fecha_actual": fecha_actual,
        "hora_actual": hora_actual,
        "ventas": id_libros_por_venta,
    }
    
    return render(request, 'perfil/mifactura.html' , data)

 
def total_compras(cliente_id):
    try:
        
        facturas_cliente = TbFacturaCliente.objects.filter(id_cliente=cliente_id)
        
        total_compra_resultado = facturas_cliente.aggregate(total_compra=Sum('total_compra'))
        total_compra_valor = total_compra_resultado['total_compra']

        if total_compra_valor is  None:
            total_compra = float(0)
        else:
            total_compra = float(total_compra_valor)
            

        return (total_compra)
    except TbCliente.DoesNotExist:
        return 0
    
def obtener_facturas_por_cliente(id_cliente):
    try:
        facturas = TbFacturaCliente.objects.filter(id_cliente=id_cliente).order_by('-id_factura')

        return facturas
    except TbFacturaCliente.DoesNotExist:
        return []
    





