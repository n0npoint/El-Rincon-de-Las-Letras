import matplotlib.pyplot as plt
from io import BytesIO
import base64
import matplotlib
import numpy as np
matplotlib.use('Agg')
from  recursos_humanos.models.empleados import *
from ventas.models.ventas import *
import calendar


########################################################################
            # Grafico para las ventas mensuales de los empleados

def grafico_ventas_mensuales_empleado(meses, ventas, empleado):
    plt.figure(figsize=(10, 6))
    plt.bar(meses, ventas)
    plt.xlabel('Mes')
    plt.ylabel('Ventas')
    plt.title(f'Ventas Mensuales - {empleado.nombre} {empleado.apellido}')

    for i, valor_venta in enumerate(ventas):
        plt.text(i + 0.99, valor_venta + 50, f'{valor_venta:.2f}', ha='center', va='bottom', fontsize=10)

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    plt.close('all') 

    grafico_bytes = buffer.getvalue()
    grafico_base64 = base64.b64encode(grafico_bytes).decode()

    return grafico_base64

########################################################################
        #Comparativa de las ventas por empleado

def generar_ventas_diarias_mes(labels, values):
    plt.figure(figsize=(8, 6))
    plt.plot(labels, values)
    plt.fill_between(labels, values, alpha=0.2)  
    plt.xlabel('Días')
    plt.ylabel('Valores')
    plt.title('Gráfico de Densidad')
    plt.xticks(rotation=45, ha='right')
    
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    plt.close()
    
    grafico_bytes = buffer.getvalue()
    grafico_base64 = base64.b64encode(grafico_bytes).decode()
    
    return grafico_base64

########################################################################
        #Grafico para obtener la cantidad de libros vendidos por mes

def generar_grafico_libros_vendidos_mensual(ventas_mensuales):
    meses = [venta['mes'] for venta in ventas_mensuales]
    unidades_vendidas = [venta['unidades_vendidas'] for venta in ventas_mensuales]

    plt.figure(figsize=(10, 6))
    plt.plot(meses, unidades_vendidas, marker='o')

    plt.xlabel('Mes')
    plt.ylabel('Unidades Vendidas')
    plt.title('Unidades Vendidas Mensuales del Año Actual')

    nombres_meses_pasados = [calendar.month_abbr[mes] for mes in meses]
    plt.xticks(meses, nombres_meses_pasados)

    for mes, unidades in zip(meses, unidades_vendidas):
        plt.annotate(f'{unidades}', (mes, unidades), textcoords="offset points", xytext=(0, 10), ha='center')

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    plt.close()

    grafico_bytes = buffer.getvalue()
    grafico_base64 = base64.b64encode(grafico_bytes).decode()

    return grafico_base64

########################################################################
            # Generar Grafico para la comparativa de empleados

def generar_grafico_comparativa_empleados(ventas_empleados):
    empleados = [venta['empleado'] for venta in ventas_empleados]
    ventas = [venta['ventas'] for venta in ventas_empleados]

    plt.figure(figsize=(8, 8))
    colores = ['#a3d2a1', '#f5a623', '#417505', '#3498db', '#e74c3c','#9b59b6', '#f39c12',
                '#34495e', '#c0392b', '#1abc9c', '#2980b9', '#8e44ad']
    plt.pie(ventas, labels=empleados, colors=colores, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')

    plt.title('Comparativa de Empleados')

    buffer = BytesIO()
    plt.savefig(buffer, format='png', bbox_inches='tight')
    plt.close()

    grafico_bytes = buffer.getvalue()
    grafico_base64 = base64.b64encode(grafico_bytes).decode()

    return grafico_base64

########################################################################
    # Generar Grafico para el tipo de ventas ( Online , Tienda , Total Venta)

def generar_grafico_ventas_tipo(ventas_tipo):
    meses = calendar.month_abbr[1:]

    plt.figure(figsize=(10, 6))
    
    ventas_en_linea = [mes['ventas_en_linea'] for mes in ventas_tipo]
    ventas_tienda = [mes['ventas_tienda'] for mes in ventas_tipo]
    venta_total = [mes['venta_total'] for mes in ventas_tipo]

    num_meses = len(meses)
    ancho_barras = 0.25
    desplazamiento = np.arange(num_meses)
    
    plt.bar(desplazamiento, ventas_en_linea, width=ancho_barras, align='center', label='Ventas en Línea', color='blue')
    plt.bar(desplazamiento + ancho_barras, ventas_tienda, width=ancho_barras, align='center', label='Ventas en Tienda', color='red')
    plt.bar(desplazamiento + 2 * ancho_barras, venta_total, width=ancho_barras, align='center', label='Venta Total', color='purple')
    
    plt.xlabel('Mes')
    plt.ylabel('Ventas')
    plt.title('Comparativa de Ventas en Tienda, en Línea y Total en el Año Actual')
    plt.legend()

    plt.xticks(desplazamiento + ancho_barras, meses, rotation=45, ha='right', fontsize=10)  
    plt.tight_layout()

    buffer = BytesIO()
    plt.savefig(buffer, format='png', bbox_inches='tight')
    plt.close()

    grafico_bytes = buffer.getvalue()
    grafico_base64 = base64.b64encode(grafico_bytes).decode()

    return grafico_base64