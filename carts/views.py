from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import ListView

from carts.models import Cart
from goods.models import Products

class UserCartView(ListView):
    template_name = 'carts/cart.html'   
    context_object_name = 'carts'

    def get_queryset(self):
        carts = Cart.objects.filter(session_key=self.request.session.session_key)
        return carts

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Ваша корзина:Sattiyas - Fashion'
        return context


# class CardAdd(View):
#     def post(self, request):
#         product = Products.objects.get(slug=product_slug)

#         carts = Cart.objects.filter(session_key=request.session.session_key, product=product)
#         if carts.exists():
#             cart = carts.first()
#             if cart:
#                 cart.quantity += 1
#                 cart.save()
#             else:
#                 Cart.objects.create(session_key=request.session.session_key, product=product, quantity=1)
        
#         return redirect(request.META['HTTP_REFERER'])

def cart_add(request, product_slug):

    product = Products.objects.get(slug=product_slug)
    
    carts = Cart.objects.filter(session_key=request.session.session_key, product=product)

    if carts.exists():
        cart = carts.first()
        if cart:
            cart.quantity += 1
            cart.save()
    else:
        Cart.objects.create(session_key=request.session.session_key, product=product, quantity=1)


    return redirect(request.META['HTTP_REFERER']) 




def cart_change(request, cart_id):

    quanti = request.GET.get('quantity', None)
    cart = Cart.objects.get(id=cart_id)
    
    quanti = int(quanti)
    x = cart.quantity + quanti
    if x == 0:
        cart.delete()
    else:
        cart.quantity += 1
        cart.save()        

    return redirect(request.META['HTTP_REFERER']) 


def cart_remove(request, cart_id):
    cart = Cart.objects.get(id=cart_id)
    cart.delete()
    return redirect(request.META['HTTP_REFERER']) 
    