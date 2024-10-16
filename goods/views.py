from re import S
from typing import Any
from django.db.models.base import Model as Model

from django.db.models.query import QuerySet
from django.views.generic import DetailView, ListView

from goods.models import Products
from goods.utils import q_search

rating_list = []


class CatalogView(ListView):
    model = Products
    template_name = "goods/catalog.html"
    context_object_name = "goods"
    paginate_by = 8

    def get_queryset(self):
        # переменные фильтров radio (размер и бренд)
        size = self.request.GET.get("size")
        brand = self.request.GET.get("brand")
        # переменная поиска
        query = self.request.GET.get("q")
        # переменные фильтвров chekbox (рейтинг, пол, категория одежды)
            # переменные людей
        x = 3
        people_status = False
        people_list = []
        while x != 0:
            people_list.append(self.request.GET.get("people" + str(x)))
            x -= 1
        if (
            "Женское" in people_list
            or "Мужское" in people_list
            or "Детское" in people_list
        ):
            people_status = True
        else:
            people_status = False
            # конец переменной людей
            # переменные категорий одежды
        x = 7
        clothes_status = False
        clothes_list = []
        while x != 0:
            clothes_list.append(self.request.GET.get("clothes" + str(x)))
            x -= 1
        if (
            "Платья" in clothes_list
            or "Топы" in clothes_list
            or "Джинсы" in clothes_list
            or "Футболки" in clothes_list
            or "Костюмы" in clothes_list
            or "Рубашки" in clothes_list
            or "Штаны" in clothes_list
        ):
            clothes_status = True
        else:
            clothes_status = False
            # конец переменной категорий одежды
            # переменные рейтингов
        x = 5
        rating_status = False
        rating_list = []
        while x != 0:
            rating_list.append(self.request.GET.get("rating" + str(x)))
            x -= 1
        if (
            "1" in rating_list
            or "2" in rating_list
            or "3" in rating_list
            or "4" in rating_list
            or "5" in rating_list
        ):
            rating_status = True
        else:
            rating_status = False
            # конец перемееной рейтингов
            # переменные фильтров
        order_by = self.request.GET.get("order_by")
            # конец переменных фильтров

            # формирование запроса в БД
        if query:
            goods = q_search(query)
        else:
            goods = super().get_queryset()
        if size and size != "Default":
            goods = super().get_queryset().filter(sizе__exact=size)

        if brand and brand != "Default":
            goods = super().get_queryset().filter(brand__exact=brand)

        if people_status:
            goods = (
                super().get_queryset().filter(people_category__name__exact=people_list[2])
                | super().get_queryset().filter(people_category__name__exact=people_list[1])
                | super().get_queryset().filter(people_category__name__exact=people_list[0])
            )

        if clothes_status:
            goods = (
                super().get_queryset().filter(category__name__exact=clothes_list[6])
                | super().get_queryset().filter(category__name__exact=clothes_list[5])
                | super().get_queryset().filter(category__name__exact=clothes_list[4])
                | super().get_queryset().filter(category__name__exact=clothes_list[3])
                | super().get_queryset().filter(category__name__exact=clothes_list[2])
                | super().get_queryset().filter(category__name__exact=clothes_list[1])
                | super().get_queryset().filter(category__name__exact=clothes_list[0])
            )

        if rating_status:
            goods = (
                super().get_queryset().filter(rating__exact=rating_list[4])
                | super().get_queryset().filter(rating__exact=rating_list[3])
                | super().get_queryset().filter(rating__exact=rating_list[2])
                | super().get_queryset().filter(rating__exact=rating_list[1])
                | super().get_queryset().filter(rating__exact=rating_list[0])
            )

        if order_by and order_by != "default":
            goods = goods.order_by(order_by)
            # запрос сформирован, возврат результата
        
        return goods

    def get_context_data(self, **kwargs):

        goods = self.get_queryset()
        goods_count = len(goods)
        goods_status = True
        goods_all_count = 8
        if goods_count < goods_all_count:
            goods_all_count = goods_count
            goods_status = False

        context = super().get_context_data(**kwargs)
        context["title"] = "Каталог - Sattiyas - Fashion"
        context["goods_count"] = goods_count
        context["goods_all_count"] = goods_all_count
        context["goods_status"] = goods_status

        return context


class ProductView(DetailView):

    template_name = "goods/product.html"
    slug_url_kwarg = "product_slug"
    context_object_name = "product"

    def get_object(self, queryset=None):
        product = Products.objects.get(slug=self.kwargs.get(self.slug_url_kwarg))
        return product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.object.name 
        context["top_items"] = Products.objects.filter(top_item=True)
        return context
