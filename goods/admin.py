from django.contrib import admin

from goods.models import Categories, Products, People_categorys

# admin.site.register(Categories)
# admin.site.register(Products)

@admin.register(People_categorys)
class People_categoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}