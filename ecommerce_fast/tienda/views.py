from django.shortcuts import render, redirect
from .models import Producto 
from .models import Usuario  # Importamos tu tabla personalizada de usuarios
def home(request):
    # Trae todos los productos de la base de datos
    productos = Producto.objects.all()
    # Se los pasa al archivo HTML
    return render(request, 'tienda/home.html', {'productos': productos})
def pagina1(request):
    
    golosinas = Producto.objects.filter(categoria = "golosina")
    bebidas = Producto.objects.filter(categoria = "bebida")
    snacks = Producto.objects.filter(categoria = "snack")
    
    return render(request, 'tienda/pagina1.html', {'golosinas'  : golosinas,
                                                   'bebidas'    : bebidas,
                                                   'snacks'     : snacks    })
    
def carrito(request):
    
    return render(request, 'tienda/carrito.html')


def login(request):
    # Si el usuario ya está logueado, lo mandamos directo al mostrador
    if 'cliente_id' in request.session:
        return redirect('mostrador')
    
    error_mensaje = None

    # ¿El usuario apretó el botón de "Ingresar"? (Petición POST)
    if request.method == "POST":
        # Capturamos lo que el usuario escribió en los inputs usando sus 'name'
        txt_usuario = request.POST.get("usuario")
        txt_contrasenia = request.POST.get("contrasenia")

        try:
            # 1. Buscamos al usuario en TU tabla por su nombre_de_usuario
            usuario_encontrado = Usuario.objects.get(nombre_de_usuario=txt_usuario)

            # 2. Usamos el método check_password() que definiste en tu modelo
            if usuario_encontrado.check_password(txt_contrasenia):
                # ¡Golazo! Guardamos su ID único en la sesión del servidor
                request.session['cliente_id'] = usuario_encontrado.id
                
                # Lo redireccionamos a la página de inicio/mostrador
                return redirect('mostrador')
            else:
                error_mensaje = "La contraseña es incorrecta."
                
        except Usuario.DoesNotExist:
            error_mensaje = "El nombre de usuario no existe."

    # Si la petición es GET (solo entra a ver la página) o si hubo un error,
    # renderizamos el formulario y le pasamos el mensaje de error si existe.
    return render(request, 'tienda/login.html', {'error': error_mensaje})
    
def logout_cliente(request):
    # Si el ID del cliente está en la sesión, lo borramos
    if 'cliente_id' in request.session:
        del request.session['cliente_id']
    return redirect('login')