from django.db import models


# Create your models here.

class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')

    class Meta:
        db_table = 'category'
        verbose_name = 'категорию'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name
    
class People_categorys(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Пол')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')

    class Meta:
        db_table = 'зeople_category'
        verbose_name = 'пол'
        verbose_name_plural = 'Полы'

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    image = models.ImageField(upload_to='goods_images', blank=True, null=True, verbose_name='Изображение')
    price = models.DecimalField(default=0, max_digits=7, decimal_places=0, verbose_name='Цена')
    discount = models.DecimalField(default=0, max_digits=4, decimal_places=0, verbose_name='Скидка в %')
    quantity = models.PositiveBigIntegerField(default=0, verbose_name='Количество')
    people_category = models.CharField(max_length=150, null=True, verbose_name='Пол')
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE, verbose_name='Категория')
    featured_item = models.BooleanField(blank=True, null=True, verbose_name='Рекомендовано')
    new_item = models.BooleanField(blank=True, null=True, verbose_name='Новинка')
    top_item = models.BooleanField(blank=True, null=True, verbose_name='Лучшее')
    

    class Meta:
        db_table = 'product'
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'

    def __str__(self):
        return f'{self.name} количество - {self.quantity} | Рек:{self.featured_item} | Новинка: {self.new_item} | Лучшее: {self.top_item}'
    
    def display_id(self):
        return f'{self.id:05}'
    
    def sell_price(self):
        if self.discount:
            return round(self.price - self.price * self.discount / 100, 2)
        
        return self.price
    
