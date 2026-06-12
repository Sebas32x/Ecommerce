from django.contrib import admin

# Register your models here.

from .models import Producto

admin.site.register(Producto)

# 1. Importamos tu modelo Usuario desde el archivo models.py
from .models import Usuario  

# 2. Registramos el modelo en el admin de Django
admin.site.register(Usuario)