# Generated by Django 5.0.6 on 2024-09-18 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0003_alter_categories_options_alter_categories_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='featured_item',
            field=models.BooleanField(blank=True, null=True, verbose_name='Рекомендовано'),
        ),
        migrations.AddField(
            model_name='products',
            name='new_item',
            field=models.BooleanField(blank=True, null=True, verbose_name='Новинка'),
        ),
        migrations.AddField(
            model_name='products',
            name='people_category',
            field=models.CharField(max_length=150, null=True, verbose_name='Пол'),
        ),
        migrations.AddField(
            model_name='products',
            name='top_item',
            field=models.BooleanField(blank=True, null=True, verbose_name='Лучшее'),
        ),
        migrations.AlterField(
            model_name='products',
            name='discount',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=4, verbose_name='Скидка в %'),
        ),
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=7, verbose_name='Цена'),
        ),
    ]
