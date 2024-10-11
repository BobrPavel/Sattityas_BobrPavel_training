from typing import Any
from django.contrib import messages
from django.shortcuts import render
from django.views.generic import TemplateView


from goods.models import Products
from main.form import CreateEmailForms
from main.models import Comment, Mailing


class ContactView(TemplateView):
    template_name = 'main/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Контакты Sattiyas - Fashion"
        return context


    # 'title':"О нас Sattiyas - Fashion",


#def contact(request):
#    
#    return render(request, 'main/contact.html')



def index(request):

    if request.method == "POST":
        form = CreateEmailForms(data=request.POST)
        if form.is_valid():
            maill = Mailing.objects.create(
                email=form.cleaned_data['email'],
            )
            
            messages.success(request, 'Сообщение отправлено!')


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
        'title':"Главная Sattiyas - Fashion",
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
    coments = Comment.objects.all()

    context = {
        'title':"О нас Sattiyas - Fashion",
        "coments":coments,  
    }
    return render(request, 'main/about.html', context)


