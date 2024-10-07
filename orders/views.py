from django.shortcuts import render

from carts.models import Cart


def create_order(request):


    carts = Cart.objects.filter(session_key=request.session.session_key)
    context = {
        'carts' : carts,
    }

    return render(request, 'orders/create_order.html', context)
