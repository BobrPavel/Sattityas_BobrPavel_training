from django.shortcuts import render

from goods.models import Products


def catalog(request):

    goods = Products.objects.all()

    context = {
        "goods":goods,
    }

    return render(request, 'goods/catalog.html', context)


def product(request, product_id):

    product = Products.objects.get(id=product_id)
    top_items = Products.objects.filter(top_item=True)

    context = {
        'product':product,
        "top_items":top_items,
    }

    return render(request, 'goods/product.html', context)