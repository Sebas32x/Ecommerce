from django.shortcuts import render
from .models import Producto

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
                                                   'snacks'      : snacks    })
    
def carrito(request):
    
    return render(request, 'tienda/carrito.html')
