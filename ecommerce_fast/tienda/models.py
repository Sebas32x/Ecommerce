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


from django.contrib.auth.hashers import make_password, check_password
class Usuario(models.Model):
    nombre_de_usuario = models.CharField(max_length=40, unique=True)
    correo = models.EmailField(max_length=320, unique=True)
    nombre_y_apellido = models.CharField(max_length=100)

    CURSO_OPCIONES = [
    ("Preceptor", "Preceptor"),
    ("Profesor", "Profesor"),
    ("Directivo", "Directivo"),

    ("1-1", "1-1"),
    ("1-2", "1-2"),
    ("1-3", "1-3"),

    ("2-1", "2-1"),
    ("2-2", "2-2"),
    ("2-3", "2-3"),

    ("3-1", "3-1"),
    ("3-2", "3-2"),
    ("3-3", "3-3"),

    ("4-2", "4-2"),
    ("4-3", "4-3"),
    ("4-4", "4-4"),

    ("5-2", "5-2"),
    ("5-3", "5-3"),

    ("6-2", "6-2"),
    ("6-3", "6-3"),

    ("7-2", "7-2"),
    ("7-3", "7-3"),

    ("X", "X"),
]
    curso = models.CharField(max_length=20, choices=CURSO_OPCIONES, default="X")

    contraseña = models.CharField(max_length=128)  # se guarda en hash

    def set_password(self, raw_password):
        """Guarda la contraseña en formato seguro (hash)."""
        self.contraseña = make_password(raw_password)

    def check_password(self, raw_password):
        """Verifica la contraseña ingresada contra el hash guardado."""
        return check_password(raw_password, self.contraseña)

    def __str__(self):
        return self.nombre_de_usuario

class CarritoItem(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.usuario.nombre_de_usuario} - {self.producto.nombre} x{self.cantidad}"