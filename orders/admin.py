from django.contrib import admin

from orders.models import Order
from orders.models import OrderItem

admin.site.register(Order)
admin.site.register(OrderItem)
