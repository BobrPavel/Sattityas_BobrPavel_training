from django.shortcuts import redirect, render

from carts.models import Cart
from carts.utils import get_user_carts
from goods.models import Products


def users_carts(request):
    carts = Cart.objects.filter(session_key=request.session.session_key)

    context = {
        'carts' : carts,
    }

    return render(request, 'carts/cart.html', context)


def cart_add(request, product_slug):

    #product_id = request.POST.get("product_id")
    user_cart = get_user_carts(request)

    product = product = Products.objects.get(slug=product_slug)
    
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
    