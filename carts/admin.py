from django.contrib import admin

from carts.models import Cart

# admin.site.register(Cart)

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ["product", "quantity", "created_timestamp",]
    list_filter = [ "product__name", "created_timestamp",]

    def display(self, obj):
        return f"Анонимный польховательь | {str(obj.product.name)}"