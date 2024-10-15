from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, FormView


from goods.models import Products
from main.form import CreateEmailForms
from main.models import Comment, Mailing


class IndexView(FormView):
    template_name = "main/index.html"
    form_class = CreateEmailForms
    sucsess_url = reverse_lazy("main:index")

    def form_valid(self, form):
        Mailing.objects.create(
            email=form.cleaned_data["email"],
        )
        messages.success(self.request, "Подписка оформлена!")
        return redirect("main:index")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Главная Sattiyas - Fashion"
        context["coments"] = Comment.objects.all()
        context["new_items"] = Products.objects.filter(new_item=True)
        context["top_items"] = Products.objects.filter(top_item=True)
        context["dresses"] = Products.objects.filter(featured_item=True) & Products.objects.filter(category__name="Платья")
        context["jeans"] = Products.objects.filter(featured_item=True) & Products.objects.filter(category__name="Джинсы")
        context["t_shirts"] = Products.objects.filter(featured_item=True) & Products.objects.filter(category__name="Футболки")
        context["shirts"] = Products.objects.filter(featured_item=True) & Products.objects.filter(category__name="Рубашки")
        context["suits"] = Products.objects.filter(featured_item=True) & Products.objects.filter(category__name="Костюмы")
        context["accessories"] = Products.objects.filter(featured_item=True) & Products.objects.filter(category__name="Аксесуары")
        return context


class AboutView(ListView):
    model = Comment
    template_name = "main/about.html"
    context_object_name = "about"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "О нас Sattiyas - Fashion"
        context["coments"] = Comment.objects.all()
        return context


class ContactView(TemplateView):
    template_name = "main/contact.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Контакты Sattiyas - Fashion"
        return context
