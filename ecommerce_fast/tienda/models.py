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

class User(models.Model):
    nombreDeUsuario = models.CharField(max_length=40)
    nombreYApellido = models.CharField(max_length=40)
    CURSO_OPCIONES = [
        ("Preceptor", "preceptor"),
        ("Profesor", "profesor"),
        ("Directivo", "directivo"),
        
        ("1-1"),("1-2"),("1-3"),
        ("2-1"),("2-2"),("2-3"),
        ("3-1"),("3-2"),("3-3"),
        ("4-2"),("4-3"),("4-4"),
        ("5-2"),("5-3"),
        ("6-2"),("6-3"),
        ("7-2"),("7-3"),
        
        ("X")
    ]
    curso = models.CharField(
        max_length=3,
        choices=CURSO_OPCIONES,
        default="X"
    )
    contraseña = models.CharField(max_length=64) #Obligatorio sha256
    