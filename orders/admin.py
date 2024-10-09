from django.contrib import admin

from orders.models import Order
from orders.models import OrderItem


class OrderItemTabulareAdmin(admin.TabularInline):
    model = OrderItem
    fields = ("product", "name", "price", "quantity")
    search_fields = (
        "product",
        "name",
    )
    extra = 0

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("order", "product", "name", "price", "quantity")
    search_fields = (
        "order",
        "product",
        "name",
    )


class OrderTabulareAdmin(admin.TabularInline):
    model = Order
    fields = (
        "status",
        "is_paid",
        "created_timestamp",
    )
    search_fields = (
        "status",
        "is_paid",
        "created_timestamp",
    )
    readonly_fields = ("created_timestamp",)
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'first_name',
        'last_name',
        'created_timestamp',
        'is_paid',
        'status',
    ]
    search_fields = [
        'id',
    ]
    readonly_fields = ("created_timestamp",)
    list_filter = [
        'created_timestamp',
        'is_paid',
        'status',
    ]
    fields = [
        ("first_name", "last_name"),
        ("delivery_address", "index_cod"),
        "phone_number",
        "email",
        "additional_inforation",
        "created_timestamp",
        "is_paid",
        "status",
    ]
    inlines = (OrderItemTabulareAdmin,)