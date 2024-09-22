from django.core.paginator import Paginator
from django.shortcuts import render

from goods.models import Products, Categories, People_categorys


def catalog(request):

    page = request.GET.get('page', 1)

    goods = Products.objects.all()

    paginator = Paginator(goods, 8)
    current_page = paginator.page(int(page))


    context = {
        "goods":current_page,
    }

    return render(request, 'goods/catalog.html', context)


def product(request, product_slug):



    product = Products.objects.get(slug=product_slug)
    top_items = Products.objects.filter(top_item=True)

    context = {
        'product':product,
        "top_items":top_items,
    }

    return render(request, 'goods/product.html', context)