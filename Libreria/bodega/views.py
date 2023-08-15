from django.shortcuts import render , redirect

# Create your views here.


def home(request):

    dato= "prueba"

    return render(request , 'bodega/home_bodega.html' , {'dato': dato})




#Redirecciona a la pagina principal del area
def redirect_to_home(request, undefined_path):
    return redirect('home')
