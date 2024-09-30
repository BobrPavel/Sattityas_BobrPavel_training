from django.core.paginator import Paginator
from django.shortcuts import render

from goods.models import Products
from goods.utils import q_search

rating_list = []

def catalog(request):

    # переменная страницы для пагинации
    page = request.GET.get('page', 1)

    # переменные фильтров radio (размер и бренд)
    size = request.GET.get('size', None)
    brand =  request.GET.get('brand', None)

    # переменная поиска
    query = request.GET.get('q', None)

# переменные фильтвров chekbox (рейтинг, пол, категория одежды)

        # переменные людей
    x = 3
    people_status = False

    people_list = []
    while x != 0:
        people_list.append(request.GET.get('people' + str(x), None))
        x -= 1
    if 'Женское' in people_list or 'Мужское' in people_list or 'Детское' in people_list:
        people_status = True
    else:
        people_status = False

        # переменные категорий одежды
    x = 7
    clothes_status = False

    clothes_list = []
    while x != 0:
        clothes_list.append(request.GET.get('clothes' + str(x), None))
        x -= 1
    
    if 'Платья' in clothes_list or 'Топы' in clothes_list or 'Джинсы' in clothes_list or 'Футболки' in clothes_list or 'Костюмы' in clothes_list or 'Рубашки' in clothes_list or 'Штаны' in clothes_list:
        clothes_status = True
    else:
        clothes_status = False


        # переменные рейтингов
    x = 5
    rating_status = False

    rating_list = []
    while x != 0:
        rating_list.append(request.GET.get('rating' + str(x), None))
        x -= 1
    if '1' in rating_list or '2' in rating_list or '3' in rating_list or '4' in rating_list or '5' in rating_list:
        rating_status = True
    else:
        rating_status = False

    # переменные фильтров
    order_by = request.GET.get('order_by', None)
    


    if query:
        goods = q_search(query)
    else:
        goods = Products.objects.all()
    
    if size and size != "Default":
        goods = goods.filter(sizе__exact=size)

    if brand and brand != "Default":
        goods = goods.filter(brand__exact=brand)

    if people_status: 
            goods = goods.filter(people_category__name__exact=people_list[2]) | goods.filter(people_category__name__exact=people_list[1]) | goods.filter(people_category__name__exact=people_list[0])
    
    if clothes_status: 
            goods = goods.filter(category__name__exact=clothes_list[6]) | goods.filter(category__name__exact=clothes_list[5]) | goods.filter(category__name__exact=clothes_list[4]) | goods.filter(category__name__exact=clothes_list[3]) | goods.filter(category__name__exact=clothes_list[2]) | goods.filter(category__name__exact=clothes_list[1]) | goods.filter(category__name__exact=clothes_list[0])

    if rating_status: 
        goods = goods.filter(rating__exact=rating_list[4]) | goods.filter(rating__exact=rating_list[3]) | goods.filter(rating__exact=rating_list[2]) | goods.filter(rating__exact=rating_list[1]) | goods.filter(rating__exact=rating_list[0])

    if order_by and order_by != "default":
        goods = goods.order_by(order_by)




    paginator = Paginator(goods, 8)
    current_page = paginator.page(int(page))

    goods_count = len(goods)
    goods_status = True
    goods_all_count = 8
    if goods_count < goods_all_count:
        goods_all_count = goods_count
        goods_status = False

    context = {
        "goods":current_page,
        "goods_count":goods_count,
        "goods_all_count":goods_all_count,
        "goods_status": goods_status,
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