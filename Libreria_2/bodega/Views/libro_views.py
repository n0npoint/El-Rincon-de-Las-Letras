from django.shortcuts import get_object_or_404, render, redirect
from bodega.forms.libro_forms import LibroForm
from bodega.models.libro import TbLibros
from django.core.paginator import Paginator
from django.contrib import messages

# Comprobar que el ISBN no exista para la creación de un libro

def existe_isbn(request):
    isbn = request.POST.get("isbn")

    if isbn is None or isbn == "":
        messages.success(request, "Inserte un ISBN .")
        return redirect(to="gestionlibro")

    libro = TbLibros.objects.filter(isbn=isbn).first()

    if libro is not None:
        messages.success(request, "El ISBN ya existe")
        return redirect(to="gestionlibro")

    messages.success(request, f"Puedes agregar un libro con el ISBN: {isbn}")
    return redirect('agregarlibro')

# CRUD - listar libros

def gestionlibro(request):
    listado_libros = TbLibros.objects.all()
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
    
    return render(request, 'gestion/gestionLibro.html', datos)

# CRUD - Agregar Nuevo Libro

def agregar_libro(request):
    if request.method == "POST":
        formulario = LibroForm(data=request.POST, files=request.FILES)
        
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "El libro se agregó correctamente")
            return redirect(to="gestionlibro")
    
    form = LibroForm()  # Movido fuera del condicional para mostrar el formulario en el GET
    return render(request, 'gestion/nuevoLibro.html', {'form': form})

# CRUD - Eliminar Libro

def eliminarlibro(request, id_libro):
    libro = get_object_or_404(TbLibros, id_libro=id_libro)
    libro.delete()

    messages.success(request, "El libro se ha eliminado correctamente.")
    return redirect(to="gestionlibro")

# CRUD - Editar Libro

def edicion_libro(request, id_libro):
    libro = get_object_or_404(TbLibros, id_libro=id_libro)

    if request.method == 'POST':
        formulario = LibroForm(data=request.POST, instance=libro, files=request.FILES)

        if formulario.is_valid():
            formulario.save()
            messages.success(request, f"Se actualizó el libro con ID: {id_libro}")
            return redirect(to="gestionlibro")
    
    form = LibroForm(instance=libro)  # Movido fuera del condicional para mostrar el formulario en el GET
    return render(request, 'gestion/edicionLibro.html', {'form': form})
