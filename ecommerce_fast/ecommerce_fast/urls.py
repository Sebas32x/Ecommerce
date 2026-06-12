"""
URL configuration for ecommerce_fast project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tienda import views

urlpatterns = [
    path('carrito/cantidad/', views.carrito_cantidad, name='carrito_cantidad'),
    path('admin/', admin.site.urls),
    path('', views.pagina1, name="mostrador"),
    path('pagina1/', views.pagina1),
    path('carrito/', views.ver_carrito, name='carrito'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout_cliente, name='logout'),
    path('registro/', views.registro, name='registro'),
    path('finalizar_compra/', views.finalizar_compra, name='finalizar_compra'),
    path('pago/', views.pago, name='pago'),
    path('agregar_carrito/', views.agregar_carrito, name='agregar_carrito')
]
#path(
 #   'descontar_stock/<int:producto_id>/',
  #  views.descontar_stock,
   # name='descontar_stock'
#),