from django.contrib import messages
from django.shortcuts import render
from django.template.defaulttags import comment


from goods.models import Products
from main.form import CreateEmailForms
from main.models import Comment, Mailing

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
        "coments":coments,  
    }
    return render(request, 'main/about.html', context)


def contact(request):
    return render(request, 'main/contact.html')