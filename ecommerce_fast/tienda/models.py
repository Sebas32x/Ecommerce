from django.db import models

class Producto(models.Model):
    CATEGORIA_OPCIONES = [
        ("bebida", "Bebida"),
        ("golosina", "Golosina"),
        ("snack", "Snack"),
    ]
    
    categoria = models.CharField(
        max_length=20,
        choices=CATEGORIA_OPCIONES,
        default="snack"
    )
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    imagen_url = models.URLField(blank=True) # Para meter un link de imagen rápido

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __str__(self):
        return self.nombre