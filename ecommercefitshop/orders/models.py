from django.contrib.auth.models import User
from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Departamento(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Municipio(models.Model):
    nombre = models.CharField(max_length=100)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad_disponible = models.IntegerField()
    imagen = models.ImageField(upload_to='product_images/')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, default='None')

    def __str__(self):
        return self.nombre

class Pedido(models.Model):
    ESTADO_PEDIDO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('en_proceso', 'En proceso'),
        ('completado', 'Completado'),
        ('cancelado', 'Cancelado'),
    ]

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    direccion_envio = models.ForeignKey('DireccionEnvio', null=True, on_delete=models.SET_NULL)
    estado_pedido = models.CharField(max_length=20, choices=ESTADO_PEDIDO_CHOICES)

    def __str__(self):
        return f"Pedido {self.id}"

class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

class DireccionEnvio(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=255)
    ciudad = models.ForeignKey(Municipio, on_delete=models.CASCADE)
    estado = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    codigo_postal = models.CharField(max_length=20)

class MetodoPago(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()

class Pago(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    metodo_pago = models.ForeignKey(MetodoPago, on_delete=models.CASCADE)
    fecha_pago = models.DateTimeField()
    monto_total = models.DecimalField(max_digits=10, decimal_places=2)

class ComentarioProducto(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    comentario = models.TextField()
    calificacion = models.IntegerField()
    creado_en = models.DateTimeField(auto_now_add=True)
