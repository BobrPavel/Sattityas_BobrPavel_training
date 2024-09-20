from django.shortcuts import render

from goods.models import Products
from main.models import Comment

def index(request):

    coments = Comment.objects.all()
    goods = Products.objects.all()
    
    new_items = Products.objects.filter(new_item=True)
    top_items = Products.objects.filter(top_item=True)

    dresses = Products.objects.filter(featured_item=True) & Products.objects.filter(category__name='Платья')
    jeans = Products.objects.filter(featured_item=True) & Products.objects.filter(category__name='Джинсы')
    t_shirts = Products.objects.filter(featured_item=True) & Products.objects.filter(category__name='Футболки')
    shirts = Products.objects.filter(featured_item=True) & Products.objects.filter(category__name='Рубашки')
    suits = Products.objects.filter(featured_item=True) & Products.objects.filter(category__name='Костюмы')
    accessories = Products.objects.filter(featured_item=True) & Products.objects.filter(category__name='Аксесуары')


    context = {
        "goods":goods,
        "coments":coments,
        "new_items":new_items,
        "top_items":top_items,
        
        "jeans":jeans,
        "t_shirts":t_shirts,
        "shirts":shirts,
        "dresses":dresses,
        "suits":suits,
        "accessories":accessories,


    }



    return render(request, 'main/index.html', context)

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html')