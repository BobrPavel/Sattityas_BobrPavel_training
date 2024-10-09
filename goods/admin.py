from django.contrib import admin

from goods.models import Categories, Products, People_categorys

# admin.site.register(Categories)
# admin.site.register(Products)

@admin.register(People_categorys)
class People_categoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name',]

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name',]

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'quantity', 'price', 'discount', 'rating', 'featured_item', 'new_item', 'top_item',]
    list_editable = ['price', 'discount', 'rating', 'featured_item', 'new_item', 'top_item',]
    search_fields = ['name', 'description',]
    list_filter = ['discount', 'quantity', 'category',]
    fields = [
        "name",
        "category",
        "slug",
        "description",
        "image",
        ("price", "discount"),
        "quantity",
        "people_category",
        ("sizе", "brand", "rating"),
        ("featured_item", "new_item", "top_item"),

    ]