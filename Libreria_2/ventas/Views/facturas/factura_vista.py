
import os
from io import BytesIO
from django.http import FileResponse, HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.conf import settings
from django.shortcuts import render
from carrito.context_processors import *

from carrito.views.carro_logica import Carrito
from .factura_logica import *


def factura_vista(request):
    fecha_actual  = obtener_fecha()
    hora_actual  = obtener_hora()
    id_factura , nombre_empleado , apellido_empleado , id_empleado = obtener_empleado()
    nombre_cliente , apellido_cliente , id_cliente , email , direccion , telefono = obtener_cliente()
    carrito = Carrito(request)

# Obtener el carro (diccionario) de la instancia de Carrito
    carro = carrito.carro
    carro_items = []

    for key, item_data in carro.items():
        carro_items.append({
            'id_libro': item_data['id_libro'],
            'titulo': item_data['titulo'],
            'isbn': item_data['isbn'],
            'precio': item_data['precio'],
    })
    
    data = {"fecha" : fecha_actual,
            "hora" : hora_actual,
            "id_factura" : id_factura,
            "nombre_empleado" : nombre_empleado,
            "apellido_empleado" : apellido_empleado,
            "id_empleado" : str(id_empleado),
            "nombre_cliente" : nombre_cliente,
            "apellido_cliente" : apellido_cliente,
            "id_cliente" : str(id_cliente),
            "email" : email,
            "direccion" : direccion,
            "telefono" : telefono,
            'carro_items': carro_items,
            }   


    return render(request , 'facturas/factura_vista.html' , data)


def factura_imprimir(request):
    fecha_actual  = obtener_fecha()
    hora_actual  = obtener_hora()
    id_factura , nombre_empleado , apellido_empleado , id_empleado = obtener_empleado()
    nombre_cliente , apellido_cliente , id_cliente , email , direccion , telefono = obtener_cliente()
    carrito = Carrito(request)
    context_processor_values = importe_total_carro(request)

# Obtener el carro (diccionario) de la instancia de Carrito
    carro = carrito.carro
    carro_items = []

    for key, item_data in carro.items():
        carro_items.append({
            'id_libro': item_data['id_libro'],
            'titulo': item_data['titulo'],
            'isbn': item_data['isbn'],
            'precio': item_data['precio'],
    })
            
    template = get_template('facturas/factura_impresion.html')
    context = {"fecha" : fecha_actual,
            "hora" : hora_actual,
            "id_factura" : id_factura,
            "nombre_empleado" : nombre_empleado,
            "apellido_empleado" : apellido_empleado,
            "id_empleado" : str(id_empleado),
            "nombre_cliente" : nombre_cliente,
            "apellido_cliente" : apellido_cliente,
            "id_cliente" : str(id_cliente),
            "email" : email,
            "direccion" : direccion,
            "telefono" : telefono,
            'carro_items': carro_items,
            "importe_total_carro": context_processor_values["importe_total_carro"],
            "subtotal_compra": context_processor_values["subtotal_compra"],
            "impuesto": context_processor_values["impuesto"],
            }    

    html = template.render(context)

    pdf_buffer = BytesIO()

    # Convierte el HTML a PDF utilizando xhtml2pdf
    def link_callback(uri, rel):
        print(f'URI: {uri}')

        if uri.startswith('/static/'):
            path = os.path.join(settings.STATICFILES_DIRS[0], uri.replace('/static/', ''))
        else:
            path = os.path.join(settings.MEDIA_ROOT, uri)

        print(f'Ruta completa: {path}')

        return path

    pisa_status = pisa.CreatePDF(
        html, dest=pdf_buffer,
        link_callback=link_callback)

    if pisa_status.err:
        return HttpResponse('Error al generar el PDF: %s' % html, content_type='text/plain')

    pdf_buffer.seek(0)
    response = FileResponse(pdf_buffer, as_attachment=True, filename="factura.pdf")

    return response




    