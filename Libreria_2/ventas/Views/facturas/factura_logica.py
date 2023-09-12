from datetime import datetime

from ventas.models.facturaCliente import TbFacturaCliente

def obtener_fecha():
    fecha = datetime.today()
    fecha_actual = fecha.strftime("%d/%m/%y")
    

    return(fecha_actual)

def obtener_hora():
    now = datetime.now()

    hora = now.time()

    return(hora)


def obtener_empleado():
    factura = TbFacturaCliente.objects.latest('id_factura')

    try:
        nombre_empleado = factura.id_empleado.nombre
        apellido_empleado = factura.id_empleado.apellido
        id_empleado = factura.id_empleado
    except AttributeError:
        nombre_empleado = None
        apellido_empleado = None
        id_empleado = None

    return(factura , nombre_empleado , apellido_empleado , id_empleado)  


def obtener_cliente():
    factura = TbFacturaCliente.objects.latest('id_factura')

    nombre_cliente = factura.id_cliente.nombre
    apellido_cliente = factura.id_cliente.apellido
    email = factura.id_cliente.email
    id_cliente = factura.id_cliente
    direccion = factura.id_cliente.direccion
    telefono = factura.id_cliente.numero_telefono

    return(nombre_cliente , apellido_cliente , id_cliente , email , direccion , telefono)   

    