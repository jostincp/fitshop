from django.contrib import admin
from .models import Category, Departamento, Municipio, Product, Order, OrderItem, ShippingAddress, ProductComment

# Registra tus modelos aquí.
admin.site.register(Category)
admin.site.register(Departamento)
admin.site.register(Municipio)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
admin.site.register(ProductComment)