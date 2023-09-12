from django.shortcuts import get_object_or_404, render , redirect
from django.db import transaction
from bodega.models.libro import TbLibros
from ventas.models.librosxventas import TbLibrosxventas
from ventas.models.ventas import TbVentas
from ventas.models.facturaCliente import *
from carrito.context_processors import *

def realizar_ventas(request):
    try:
        with transaction.atomic():
            # Obtener valores necesarios para la factura
            total_venta, subtotal_compra, impuesto = total_compra(request)
            cliente = obtener_cliente(request)
            empleado = tipo_venta(request)
            metodo_pago = "tarjeta de credito"
            estado_pago = "completo"

            # Obtener el id de ventas necesario para TbVentasxLibros
            id_ventas = obtener_ventas_facturas()

            # Obtener la información sobre los libros y precios
            libros, precios_normales, precios_con_impuesto = obtener_lista_libros(request)
            cantidad = 1

            # Crear una nueva instancia de TbFacturaCliente con los valores adecuados
            realizar_factura = TbFacturaCliente(
                subtotal=subtotal_compra, impuesto=impuesto, descuento=0,
                total_compra=total_venta, metodo_pago=metodo_pago,
                estado_pago=estado_pago, id_cliente=cliente, id_empleado=empleado
            )
            realizar_factura.save()

            # Obtener la factura recién creada
            ultima_factura = TbFacturaCliente.objects.latest('id_factura')
            if ultima_factura:
                id_factura = ultima_factura.id_factura

                if request.user.is_authenticated and 'carro' in request.session:
                    carrito = request.session['carro']

                    for elemento in carrito:
                        # Crea un nuevo registro en la tabla TbVentas para cada elemento del carrito.
                        # Supongamos que elemento contiene la información necesaria para crear un registro en TbVentas.

                        # Por ejemplo, si elemento es un diccionario con información relevante:
                        nueva_venta = TbVentas(
                            forma_pago=metodo_pago,  # Usa el método de pago de la factura
                            estado=estado_pago,  # Usa el estado de pago de la factura
                            id_empleado=empleado,    # Usa el empleado de la factura
                            id_factura=ultima_factura,  # Vincula esta venta con la factura recién creada
                            # Otros campos de TbVentas que necesites llenar
                        )

                        nueva_venta.save()

# Obtener la última factura y las ventas relacionadas con ella
            ultima_factura_id = TbVentas.objects.latest('id_factura').id_factura
            ventas_con_ultima_factura = TbVentas.objects.filter(id_factura=ultima_factura_id)
            print(f" Ventas del querri {ventas_con_ultima_factura}")

    # Iterar sobre las ventas y registrar solo la id en Tbventasporlibros
    # Supongamos que tienes un libro específico al que deseas asociar las ventas
 # Reemplaza 'factura_vista' con la ruta de tu vista de factura
        for venta in range(len(libros)):
            id_venta = ventas_con_ultima_factura[venta]  # Obtener el ID de la venta
            libro_id = libros[venta]
            libro = TbLibros.objects.filter(id_libro=libro_id).first() # Obtener el ID del libro como un valor entero
            valor_individual = precios_normales[venta]  # Obtener el precio individual
            valor_total = precios_con_impuesto[venta]  # Obtener el precio total

            # Crear una instancia de TbLibrosxventas y guárdala en la base de datos
            nuevo_registro = TbLibrosxventas(
                id_venta=id_venta,
                id_libro= libro,
                cantidad=cantidad,
                valor_individual=valor_individual,
                valor_total=valor_total,
                # Mantén los otros campos de TbLibrosxventas aquí
            )
            nuevo_registro.save()

        return redirect('factura_vista') 

    except Exception as e:
        # Si ocurre un error, puedes manejarlo aquí o simplemente mostrar un mensaje de error en la misma vista
        print(f"Error en la transacción: {str(e)}")
        return redirect('carro:carrito')  # Redirige a una página de error

# Resto del código de funciones y definiciones de modelos








##############################################################################################
                    #Funciones de Insert Factura
def total_compra(request):
    subtotal = 0
    if request.user.is_authenticated and 'carro' in request.session:
        for value in request.session["carro"].values():
            subtotal += float(value["precio"])

    impuesto = subtotal * 0.15
    total = subtotal + impuesto

    # Redondear los tres valores
    subtotal, impuesto, total = round(subtotal, 2), round(impuesto, 2), round(total, 2)
    
    return total, subtotal, impuesto

def tipo_venta(request):
    id_empleado = None
    if request.user.is_authenticated and request.user.rol == 'ventas':
        empleado = TbEmpleado.objects.get(username=request.user.username)
        id_empleado = empleado.id_empleado    

    return id_empleado

def obtener_cliente(request):
    cliente = None
    if request.user.is_authenticated and request.user.rol == 'cliente':
        cliente = TbCliente.objects.get(username=request.user.id)

    return cliente


##############################################################################################
                    #Funciones de Insert Venta

def obtener_lista_libros(request):
    libros = []
    precios_normales = []
    precios_con_impuesto = []

    if request.user.is_authenticated and 'carro' in request.session:
        for value in request.session["carro"].values():
            libros.append(value['id_libro'])
            precio = float(value['precio'])
            
            precio = round(precio, 2)
            precios_normales.append(precio)
            precio_con_impuesto = (precio * 0.15) + precio  # Multiplica por 1.15 para aplicar un impuesto del 15%
            precios_con_impuesto.append(precio_con_impuesto)

    print(libros)
    print(precios_normales)
    print(precios_con_impuesto)

    return libros, precios_normales, precios_con_impuesto

def obtener_ventas_facturas():
    id_ventas_ultima_factura = []
    try:
        # Obtén la última factura ingresada
        ultima_factura = TbVentas.objects.latest('id_factura')
        
        # Obtén todas las ventas asociadas a la última factura
        ventas_ultima_factura = TbVentas.objects.filter(id_factura=ultima_factura.id_factura)
        
        # Convierte la QuerySet en una lista de Python
        id_ventas_ultima_factura = list(ventas_ultima_factura.values_list('id_venta', flat=True))

        print(id_ventas_ultima_factura)
        
        return id_ventas_ultima_factura
    except TbVentas.DoesNotExist:
        return []
