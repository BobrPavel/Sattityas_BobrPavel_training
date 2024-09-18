from django.db import models

class Mailing(models.Model):
    email = models.CharField(max_length=200, unique=False, verbose_name='Почта')

    class Meta:
        db_table = 'email_for_mailing'
        verbose_name = 'адресс'
        verbose_name_plural = 'Адресса'
    
    def __str__(self):
        return self.name

class Comment(models.Model):

    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    coment = models.TextField(blank=True, null=True, verbose_name='Коментарий')
    image = models.ImageField(upload_to='goods_images', blank=True, null=True, verbose_name='Фото')
    city = models.TextField(blank=True, null=True, verbose_name='Город')


    class Meta:
        db_table = 'comment'
        verbose_name = 'комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.name


