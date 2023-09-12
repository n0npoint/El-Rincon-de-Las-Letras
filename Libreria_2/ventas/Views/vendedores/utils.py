import calendar
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import matplotlib
matplotlib.use('Agg')
from  recursos_humanos.models.empleados import *
from datetime import timedelta
from ventas.models.ventas import *
import datetime 
from django.db.models import Sum , Count



########################################################################
            #Obtener Empleado por cargo

def obtener_empleados_cargo(cargo_id):
    return TbEmpleado.objects.filter(id_cargo=cargo_id)

########################################################################
        # Obtener fecha actual - COMPLETO

def obtener_mes_y_anio_actual():
    ahora = datetime.datetime.now()
    mes_actual = ahora.month
    anio_actual = ahora.year
    return mes_actual, anio_actual

def obtener_anio_actual():
    from datetime import datetime
    return datetime.now().year

########################################################################
    #Obtener las Ventas totales de los empleados del mes - COMPLETO

def obtener_ventas_mes(empleados, today):
    first_day_of_month = today.replace(day=1)
    last_day_of_month = first_day_of_month.replace(month=first_day_of_month.month + 1) - timedelta(days=1)
    
    ventas_queryset = TbFacturaCliente.objects.filter(
        id_empleado__in=empleados,
        fecha_emision__range=(first_day_of_month, last_day_of_month)
    )
    
    ventas_totales = ventas_queryset.aggregate(total_ventas_totales=Sum('total_compra'))['total_ventas_totales'] or 0
    
    ultimas_ventas_mes = ventas_queryset.values('id_empleado').annotate(total_ventas=Sum('total_compra'))
    
    resultados = []
    for venta in ultimas_ventas_mes:
        empleado = TbEmpleado.objects.get(id_empleado=venta['id_empleado'])
        ventas_mes = venta['total_ventas']
        
        porcentaje_ventas = round((ventas_mes / ventas_totales) * 100, 2) if ventas_totales > 0 else 0
        
        resultados.append({
            'empleados': empleado,
            'ventas_mes': ventas_mes,
            'porcentaje_ventas': porcentaje_ventas
        })
    
    return resultados

########################################################################
            #Ventas mensuales del empleado

def obtener_ventas_mensuales_empleado(empleado_id):
    fecha_actual = datetime.datetime.now()
    mes_actual = fecha_actual.month

    ventas_mensuales_empleado = TbFacturaCliente.objects.filter(
        id_empleado_id=empleado_id,
        fecha_emision__year=fecha_actual.year,
        fecha_emision__month__lte=mes_actual
    ).annotate(
        mes=models.functions.ExtractMonth('fecha_emision')
    ).values('mes').annotate(ventas=Sum('total_compra')).order_by('mes')

    ventas_mensuales = [{'mes': mes, 'ventas': 0} for mes in range(1, mes_actual + 1)]
    ventas_mensuales_dict = {venta['mes']: venta for venta in ventas_mensuales_empleado}
    
    ventas_mensuales_actualizadas = [ventas_mensuales_dict.get(venta['mes'], venta) for venta in ventas_mensuales]
    
    return ventas_mensuales_actualizadas


########################################################################
            #obtener ventas diarias totales
def obtener_ventas_diarias_mes_actual():
    mes_actual = datetime.datetime.now().month
    anio_actual = datetime.datetime.now().year
    dias_en_mes = range(1, 32)  # Suponemos 31 días máximos en un mes
    
    ventas_diarias_mes = [
        TbFacturaCliente.objects.filter(
            fecha_emision__day=dia,
            fecha_emision__month=mes_actual,
            fecha_emision__year=anio_actual
        ).aggregate(total=Sum('total_compra'))['total'] or 0
        for dia in dias_en_mes
    ]

    return ventas_diarias_mes

########################################################################
            #Obtener la cantidad de libros vendidos en un mes

def obtener_ventas_libros_mensuales_año_actual():
    ventas_mensuales = TbVentas.objects.annotate(
        mes=models.functions.ExtractMonth('fecha_de_registro'),
        año=models.functions.ExtractYear('fecha_de_registro')
    ).filter(año=obtener_anio_actual()).values('mes').annotate(
        unidades_vendidas=Count('id_venta')
    ).order_by('mes')

    return ventas_mensuales

########################################################################
        #Comparativa de empleados por sus ventas

def obtener_ventas_empleados_anio_actual():
    empleados = TbEmpleado.objects.filter(id_cargo=8)
    ventas_empleados = []

    for empleado in empleados:
        total_ventas = TbFacturaCliente.objects.filter(id_empleado=empleado).filter(
            fecha_emision__year=obtener_anio_actual()
        ).exclude(fecha_emision__month__isnull=True).exclude(fecha_emision__month=0).aggregate(total=Sum('total_compra'))['total']

        if total_ventas is not None:
            ventas_empleados.append({'empleado': empleado.nombre, 'ventas': total_ventas})

    return ventas_empleados

########################################################################
#Calcular el tipo de venta que se realiza (Online o Tienda) y obtener la suma del mes

def obtener_ventas_tipo_anio_actual():
    meses_del_año = list(range(1, 13))  # Lista de meses del año
    ventas_tipo = []

    for mes in meses_del_año:
        ventas_tienda = TbFacturaCliente.objects.filter(
            fecha_emision__year=obtener_anio_actual(),
            fecha_emision__month=mes,
            id_empleado__isnull=False
        ).aggregate(total=Sum('total_compra'))['total'] or 0
        
        ventas_en_linea = TbFacturaCliente.objects.filter(
            fecha_emision__year=obtener_anio_actual(),
            fecha_emision__month=mes,
            id_empleado__isnull=True
        ).aggregate(total=Sum('total_compra'))['total'] or 0
        
        ventas_total = ventas_tienda + ventas_en_linea
        
        mes_nombre = calendar.month_abbr[mes]
        
        ventas_tipo.append({
            'mes': mes_nombre,
            'ventas_en_linea': ventas_en_linea,
            'ventas_tienda': ventas_tienda,
            'venta_total': ventas_total
        })
    
    return ventas_tipo
