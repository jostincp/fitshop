from django.contrib import admin
from .models import Categoria, Departamento, Municipio, Producto, Pedido, ItemPedido, DireccionEnvio, MetodoPago, Pago, ComentarioProducto

admin.site.register(Categoria)
admin.site.register(Departamento)
admin.site.register(Municipio)
admin.site.register(Producto)
admin.site.register(Pedido)
admin.site.register(ItemPedido)
admin.site.register(DireccionEnvio)
admin.site.register(MetodoPago)
admin.site.register(Pago)
admin.site.register(ComentarioProducto)
