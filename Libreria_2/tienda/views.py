from django.shortcuts import render

from bodega.models.libro import TbLibros
from django.core.paginator import Paginator


def verItem(request, id_libro):
    try:
        item = TbLibros.objects.get(id_libro=id_libro)
    except TbLibros.DoesNotExist:
        item = None  

    return render(request, 'tienda/infoProducto.html', {'item': item})




def catalogo(request):
    listado_libros = TbLibros.objects.all().order_by('id_libro')
    paginator = Paginator(listado_libros, 12)
    pagina = request.GET.get("page") or 1
    libros = paginator.get_page(pagina)
    pagina_actual = int(pagina)
    numero_paginas = range(1, libros.paginator.num_pages + 1)

    datos = {
        'items': libros,
        "paginas": numero_paginas,
        "pagina_actual": pagina_actual
    }

    return render(request, 'tienda/catalogo.html', datos)
