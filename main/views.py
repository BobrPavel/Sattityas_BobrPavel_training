from django.contrib import messages
from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, TemplateView, CreateView


from goods.models import Products
from main.form import CreateEmailForms
from main.models import Comment, Mailing

class IndexView(ListView):
    model = Comment
    template_name = 'main/index.html'
    context_object_name = 'index'


    def get_context_data(self, **kwargs):

    #     if self.request.method == "POST":
    #         form = CreateEmailForms(data=self.request.POST)
    #         if form.is_valid():
    #             maill = Mailing.objects.create(
    #                 email=form.cleaned_data['email'],
    #             )

    #             messages.success('Сообщение отправлено!')



        context = super().get_context_data(**kwargs)
        context['title'] = "Главная Sattiyas - Fashion"
        context['coments'] = Comment.objects.all()
        context['new_items'] = Products.objects.filter(new_item=True)
        context['top_items'] = Products.objects.filter(top_item=True)
        context['dresses'] = Products.objects.filter(featured_item=True) & Products.objects.filter(category__name='Платья')
        context['jeans'] = Products.objects.filter(featured_item=True) & Products.objects.filter(category__name='Джинсы')
        context['t_shirts'] = Products.objects.filter(featured_item=True) & Products.objects.filter(category__name='Футболки')
        context['shirts'] = Products.objects.filter(featured_item=True) & Products.objects.filter(category__name='Рубашки')
        context['suits'] = Products.objects.filter(featured_item=True) & Products.objects.filter(category__name='Костюмы')
        context['accessories'] = Products.objects.filter(featured_item=True) & Products.objects.filter(category__name='Аксесуары')
        
        return context

    # if request.method == "POST":
    #     form = CreateEmailForms(data=request.POST)
    #     if form.is_valid():
    #         maill = Mailing.objects.create(
    #             email=form.cleaned_data['email'],
    #         )
            
    #         messages.success(request, 'Сообщение отправлено!')

        



class AboutView(ListView):
    model = Comment
    template_name = 'main/about.html'
    context_object_name = 'about'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "О нас Sattiyas - Fashion"
        context['coments'] = Comment.objects.all()
        return context

class ContactView(TemplateView):
    template_name = 'main/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Контакты Sattiyas - Fashion"
        return context
