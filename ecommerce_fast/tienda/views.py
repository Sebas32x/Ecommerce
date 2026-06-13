import json
from datetime import datetime
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import Producto, Usuario
from .models import CarritoItem
from django.contrib import messages
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

def verificar_sesion(request):
    if 'cliente_id' not in request.session:
        return redirect('login')
    return None


def pagina1(request):

    verificar = verificar_sesion(request)
    if verificar:
        return verificar

    try:
        usuario = Usuario.objects.get(id=request.session['cliente_id'])
    except Usuario.DoesNotExist:
        return redirect('login')

    return render(request, 'tienda/pagina1.html', {
        'golosinas': Producto.objects.filter(categoria="golosina"),
        'bebidas': Producto.objects.filter(categoria="bebida"),
        'snacks': Producto.objects.filter(categoria="snack"),
        'usuario': usuario
    })

def carrito_cantidad(request):

    if 'cliente_id' not in request.session:
        return JsonResponse({"cantidad": 0})

    usuario = Usuario.objects.get(id=request.session['cliente_id'])

    items = CarritoItem.objects.filter(usuario=usuario)

    total = sum(item.cantidad for item in items)

    return JsonResponse({"cantidad": total})

def carrito(request):

    verificar = verificar_sesion(request)
    if verificar:
        return verificar

    return render(request, 'tienda/carrito.html')


def home(request):
    productos = Producto.objects.all()
    return render(request, 'tienda/home.html', {'productos': productos})


@csrf_exempt


def login(request):

    if 'cliente_id' in request.session:
        return redirect('mostrador')

    error_mensaje = None

    if request.method == "POST":

        txt_usuario = request.POST.get("usuario")
        txt_contrasenia = request.POST.get("contrasenia")

        try:
            usuario_encontrado = Usuario.objects.get(nombre_de_usuario=txt_usuario)

            if usuario_encontrado.check_password(txt_contrasenia):
                request.session['cliente_id'] = usuario_encontrado.id
                return redirect('mostrador')
            else:
                error_mensaje = "La contraseña es incorrecta."

        except Usuario.DoesNotExist:
            error_mensaje = "El nombre de usuario no existe."

    return render(request, 'tienda/login.html', {'error': error_mensaje})


def registro(request):

    if request.method == "POST":

        nombre = request.POST.get("nombre")
        apellido = request.POST.get("apellido")
        curso = request.POST.get("curso")
        usuario = request.POST.get("usuario")
        password = request.POST.get("password")

        if Usuario.objects.filter(nombre_de_usuario=usuario).exists():
            return render(request, "tienda/registro.html", {
                "error": "Ese usuario ya existe"
            })

        nuevo_usuario = Usuario(
            nombre_de_usuario=usuario,
            correo=f"{usuario}@local.com",
            nombre_y_apellido=f"{nombre} {apellido}",
            curso=curso
        )

        nuevo_usuario.set_password(password)
        nuevo_usuario.save()

        return redirect('login')

    return render(request, "tienda/registro.html")


def logout_cliente(request):

    if 'cliente_id' in request.session:
        del request.session['cliente_id']

    return redirect('login')


def ver_carrito(request):

    verificar = verificar_sesion(request)
    if verificar:
        return verificar

    usuario = Usuario.objects.get(id=request.session['cliente_id'])

    items = CarritoItem.objects.filter(usuario=usuario)

    total = 0
    for item in items:
        total += item.producto.precio * item.cantidad

    return render(request, "tienda/carrito.html", {
        "items": items,
        "total": total
    })


@csrf_exempt
def agregar_carrito(request):

    if request.method == "POST":

        if 'cliente_id' not in request.session:
            return JsonResponse({"ok": False, "mensaje": "No logueado"})

        data = json.loads(request.body)
        producto_id = data.get("id")

        usuario = Usuario.objects.get(id=request.session['cliente_id'])
        producto = Producto.objects.get(id=producto_id)

        item, created = CarritoItem.objects.get_or_create(
            usuario=usuario,
            producto=producto
        )

        if not created:
            item.cantidad += 1
        else:
            item.cantidad = 1

        item.save()

        return JsonResponse({"ok": True})


def pago(request):

    verificar = verificar_sesion(request)
    if verificar:
        return verificar

    usuario = Usuario.objects.get(id=request.session['cliente_id'])
    items = CarritoItem.objects.filter(usuario=usuario)

    total = sum(i.producto.precio * i.cantidad for i in items)

    return render(request, "tienda/pago.html", {
        "items": items,
        "total": total
    })


def finalizar_compra(request):

    if request.method == "POST":

        if 'cliente_id' not in request.session:
            return redirect("login")

        usuario = Usuario.objects.get(id=request.session['cliente_id'])
        items = CarritoItem.objects.filter(usuario=usuario)

        # Verificar stock
        for item in items:
            producto = item.producto

            if producto.stock < item.cantidad:
                return redirect("carrito")

        # Descontar stock
        total = 0

        for item in items:
            producto = item.producto
            producto.stock -= item.cantidad
            producto.save()

            total += item.producto.precio * item.cantidad

        # Crear PDF
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="factura.pdf"'

        pdf = canvas.Canvas(response)

        pdf.drawString(100, 800, "FACTURA - KIOSCO ESCOLAR")
        pdf.drawString(100, 780, f"Cliente: {usuario.nombre_de_usuario}")
        pdf.drawString(100, 760, f"Curso: {usuario.curso}")
        pdf.drawString( 100, 740, f"Fecha: {datetime.now().strftime('%d/%m/%Y %H:%M')}"
)

        y = 720

        for item in items:
            pdf.drawString(
                100,
                y,
                f"{item.producto.nombre} x{item.cantidad} - ${item.producto.precio}"
            )
            y -= 20

        pdf.drawString(100, y - 20, f"TOTAL: ${total}")

        pdf.save()

        # Vaciar carrito
        items.delete()

        return response

    return redirect("carrito")
def eliminar_del_carrito(request, item_id):

    if 'cliente_id' not in request.session:
        return redirect("login")

    item = get_object_or_404(CarritoItem, id=item_id)

    if item.cantidad > 1:
        item.cantidad -= 1
        item.save()
    else:
        item.delete()

    return redirect("carrito")