from django.contrib import admin
from .models import ClientType, Client, Product, Order, OrderDetail

admin.site.register(ClientType)
admin.site.register(Client)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderDetail)
