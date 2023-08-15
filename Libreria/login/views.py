from django.shortcuts import render

from bodega.models.libro import TbLibros

def login(request):
    
    libro = TbLibros.objects.all()

    libro1 = libro[2]
    libro2 = libro[3]

    return render(request , 'login/index.html' , {'libro': libro1 , 'libro2': libro2 })
