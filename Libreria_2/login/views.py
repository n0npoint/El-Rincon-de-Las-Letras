from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib.auth import login , logout , authenticate
from django.template.loader import render_to_string
from django.contrib import messages
from login.decoradores.decoradores import custom_login_required
from cliente.models.cliente import TbCliente
from login.forms.info_personal_form import ClienteForm
from django.contrib.auth.forms import AuthenticationForm
from login.forms.usuario_form import UsuarioForm
from login.models import TbUsuario
from bodega.models.libro import TbLibros
from django.conf import settings

def inicio(request):
    
    libros = TbLibros.objects.order_by('-id_libro')[:10]

    libro1 = libros[0]
    libro2 = libros[5]

    return render(request , 'general/index.html' , {'libro2': libro1 , 'libro1': libro2 })

def nosotros(request):


    return render(request , 'general/nosotros.html')

@custom_login_required
def contacto(request):
    if request.method == 'POST':
        nombre , apellido , email  , usuario= obtener_informacion_cliente(request)
        asunto = request.POST.get('asunto')
        mensaje = request.POST.get('mensaje')


        
        

        # Cargar y renderizar la plantilla de correo electrónico
        template = 'contacto/correo.html'
        context = {
            'nombre': f"{nombre} {apellido}" ,
            'asunto': asunto,
            'mensaje': mensaje,
            'email': email,
            'username': usuario
        }
        html_content = render_to_string(template, context)

        try:
            email_from = settings.EMAIL_HOST_USER
            recipient_list = ['soport3_rinconletras2023hn@outlook.com']
            send_mail('Asunto del correo', '', email_from, recipient_list, html_message=html_content)
            
            return redirect("/contacto/?valido")
        except Exception as e:
            print("Error al enviar el correo electrónico:", str(e))
            return redirect("/contacto/?email_error")

    return render(request, 'contacto/contacto.html')

def obtener_informacion_cliente(request):
    usuario_actual = request.user

    try:

        cliente = TbCliente.objects.get(username=usuario_actual)

        
        nombre = cliente.nombre
        apellido = cliente.apellido
        email = cliente.email 

        return (nombre,apellido,email , usuario_actual)

    except TbCliente.DoesNotExist:
        return 





def cerrar_sesion(request):
    logout(request)
    messages.success(request, "¡Vuelve Pronto!")

    return redirect('login')




################################################################


def iniciar_sesion(request):
    if request.method == 'POST':
        form = AuthenticationForm(request , data = request.POST)

        if form.is_valid():
            nombre_usuario = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            usuario = authenticate(username=nombre_usuario, password=password)

            if usuario is not None:
                login(request, usuario)
                messages.error(request, f'Bienvenido {nombre_usuario}')
                return redirect('portal')
            else:
                messages.error(request, "usuario no valido")
        else:
            messages.error(request, "Informacion incorrecta")

    form = AuthenticationForm()
    print(form)

    return render(request , 'general/login.html', {"form": form}) 



def registrarse(request):
    if request.method == "POST":
        formulario = UsuarioForm(request.POST)

        if formulario.is_valid():
            formulario.save()

            messages.success(request, "Paso 1 de 2 COMPLETADO. Falta Poco")

            return redirect('registro_info_personal', username=formulario.cleaned_data['username'])
        else:
            for field, errors in formulario.errors.items():
                for error in errors:
                    messages.add_message(request, messages.ERROR, f"{formulario.fields[field].label}: {error}")

    form = UsuarioForm()
    return render(request, 'general/cliente_registro_cuenta.html', {'form': form})

def registro_info_personal(request, username):
    usuario = TbUsuario.objects.filter(username=username).first()

    if request.method == "POST":
        formulario = ClienteForm(request.POST)

        if formulario.is_valid():
            cliente = formulario.save(commit=False)
            cliente.username = usuario
            cliente.save()

            messages.success(request, "Felicidades por unirte a nuestra familia")

            return redirect('login') 
    else:
        formulario = ClienteForm(initial={'username': username})

    return render(request, 'general/cliente_informacion_personal.html', {'form': formulario})




