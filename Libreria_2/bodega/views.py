from django.shortcuts import render , redirect

from django.contrib import messages

from .forms.libro_forms import LibroForm

# Create your views here.


def home(request):

    dato= "prueba"

    return render(request , 'bodega/home_bodega.html' , {'dato': dato})

# Redirecciona a la pagina principal del area
def redirect_to_home(request, undefined_path):
    return redirect('home')


def formulario(request):
    data = {
        "form" : LibroForm()
            }
    
    if request.method == "POST":
        formulario= LibroForm(data=request.POST)

        if formulario.is_valid():
            formulario.save()
            print("1")
        else:
            data["form"] = formulario
            print("2")

    return render(request , 'gestion/formulario.html', data)






#def editar_libro(request):
    # if request.method == 'POST':
    #     nombre = request.POST.get('txtNombre')
    #     isbn = request.POST.get('txtISBN')  # Corregido 'txtISBN' en lugar de 'txtisbn'
    #     id_autor = request.POST.get('selAutor')
    #     sinopsis = request.POST.get('txtSinopsis')
    #     edicion = request.POST.get('txtEdicion')
    #     disponibilidad = request.POST.get('selDisponibilidad')
    #     id_editorial = request.POST.get('selEditorial')
    #     precio = request.POST.get('numPrecio')
    #
    #     libro_id = request.POST.get('libro_id')
    #
    #     libro = TbLibros.objects.get(id=libro_id)
    #     libro.titulo = nombre
    #     libro.isbn = isbn
    #     libro.id_autor = id_autor
    #     libro.sipnosis = sinopsis
    #     libro.edicion = edicion
    #     libro.disponibilidad = disponibilidad
    #     libro.id_editorial = id_editorial
    #     libro.precio_venta = precio
    #     libro.save()
    #
    #     messages.success(request, '¡Libro Modificado!')
    #
    #     return redirect('/')
    #
    # return render()


