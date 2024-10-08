from django.db import models
from django.template.defaultfilters import first
from goods.models import Products


    
class Order(models.Model):

    # информация о пользователе при заказе
    first_name = models.CharField(max_length=150, null=True, blank=False, verbose_name='Имя')
    last_name = models.CharField(max_length=150,  null=True, blank=False, verbose_name='Фамилия')
    company_name = models.CharField(max_length=150, blank=True, verbose_name='Название компании')
    delivery_address = models.TextField(max_length=400, null=True, blank=False, verbose_name="Адресс доставки")
    city = models.CharField(max_length=150, null=True, blank=False, verbose_name='Город')
    index_cod = models.CharField(max_length=150, null=True, blank=False, verbose_name='Индекс')
    phone_number = models.CharField(max_length=20, null=True, blank=False, verbose_name="Номер телефона")
    email = models.CharField(max_length=150, null=True, blank=False, verbose_name='Почта')
    additional_inforation = models.TextField(max_length=1000, blank=True, verbose_name="Дополнительная информация")


    # системная информация о заказе
    #session_key = models.CharField(max_length=32, null=True, blank=True)
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания заказа')
    is_paid = models.BooleanField(default=False, verbose_name="Оплачено")
    status = models.CharField(max_length=50, default="В обработке", verbose_name="Статус заказа")

    # user = models.ForeignKey(to=User, on_delete=models.SET_DEFAULT, verbose_name="Пользователь", default=None)

    

    class Meta:
        db_table = "order"
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def __str__(self):
        return f"Заказ № {self.pk} | Покупатель {self.last_name} {self.first_name}"

class OrderItem(models.Model):
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE, verbose_name="Заказ")
    product = models.ForeignKey(to=Products, on_delete=models.SET_DEFAULT, null=True, verbose_name="Проудкт", default=None)
    name = models.CharField(max_length=150, verbose_name="Название")
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Цена")
    quantity = models.PositiveBigIntegerField(default=0, verbose_name="Количество")
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Дата продажи")

    class Meta:
        db_table = "order_item"
        verbose_name = "Проданный товар"
        verbose_name_plural = "Проданный товар"
    
    def __str__(self):
        return f"Товар {self.name} | Заказ № {self.order.pk}"
    
