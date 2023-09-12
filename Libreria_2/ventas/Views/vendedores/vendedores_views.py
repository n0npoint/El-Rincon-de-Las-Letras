
from datetime import datetime
from django.shortcuts import render
from .utils import *
from .graficos import *
import datetime

################################################################################
            #Muestra la Administraion de ventas - COMPLETO

def gestion_ventas(request):
    vendedor = obtener_empleados_cargo(8)
    today = datetime.datetime.today()
    
    ventas_mes = obtener_ventas_mes(vendedor, today)
    
    data = {
        'resultados': ventas_mes,
    }

    return render(request, 'ventas/gestionVentas.html', data)

################################################################################
            #Muestra el grafico de las ventas mensuales del empleado del año actual -COMPLETO

def ventas_mensuales_empleado(request, id_empleado):
    empleado = TbEmpleado.objects.get(id_empleado=id_empleado)
    ventas_mensuales_empleado = obtener_ventas_mensuales_empleado(id_empleado)
    
    meses = [venta['mes'] for venta in ventas_mensuales_empleado]
    ventas = [venta['ventas'] for venta in ventas_mensuales_empleado]
    
    grafico_base64 = grafico_ventas_mensuales_empleado(meses, ventas , empleado)

    data ={'grafico_base64': grafico_base64, 
        'ventas_mensuales_empleado': ventas_mensuales_empleado,
        'empleado': empleado}
    
    return render(request, 'graficos/ventas_empleado_mes.html', data)

################################################################################
            #Ventas diarias del mes - COMPLETO

def ventas_diarias_mes_actual(request):
    mes_actual, anio_actual = obtener_mes_y_anio_actual()
    ventas_diarias_mes = obtener_ventas_diarias_mes_actual()

    dias_del_mes = [f"{dia}" for dia in range(1, len(ventas_diarias_mes) + 1)]

    grafico_base64 = generar_ventas_diarias_mes(dias_del_mes, ventas_diarias_mes)
    datos_ordenados = sorted(zip(dias_del_mes, ventas_diarias_mes), key=lambda x: x[1], reverse=True)
    mejores_ventas = datos_ordenados[:15]

    data = {
        'grafico_base64': grafico_base64,
        'mejores_ventas': mejores_ventas,
        'mes_actual': mes_actual,
        'anio_actual': anio_actual
    }

    return render(request, 'graficos/ventas_diarias_mes.html', data)

################################################################################
        #libros vendidos por unidad por cada mes del año- COMPLETADO


def ventas_libros_mensuales(request):
    ventas_mensuales = obtener_ventas_libros_mensuales_año_actual()
    grafico_base64 = generar_grafico_libros_vendidos_mensual(ventas_mensuales)

    data= {'ventas': ventas_mensuales ,
            'grafico_base64': grafico_base64}

    return render(request, 'graficos/libros_vendidos_anual.html', data)

################################################################################
            #Comparativa de ventas por empleado

def ventas_empleados_anio_actual(request):
    ventas_empleados = obtener_ventas_empleados_anio_actual()
    grafico_base64 = generar_grafico_comparativa_empleados(ventas_empleados)

    data = {"ventas": ventas_empleados,
            'grafico_base64': grafico_base64}

    return render(request, 'graficos/comparativa_ventas.html', data)

################################################################################
            #Tipo de Venta (Online o Tineda) mas la suma de ambas

def comparativa_tipo_ventas(request):
    ventas_tipo = obtener_ventas_tipo_anio_actual()
    grafico_base64 = generar_grafico_ventas_tipo(ventas_tipo)

    data = {'ventas': ventas_tipo, 'grafico_base64': grafico_base64}
    return render(request, 'graficos/comparativa_tipo_venta.html', data)
