from django.shortcuts import render
from .models import Producto

def home(request):
    # Trae todos los productos de la base de datos
    productos = Producto.objects.all()
    # Se los pasa al archivo HTML
    return render(request, 'tienda/home.html', {'productos': productos})
