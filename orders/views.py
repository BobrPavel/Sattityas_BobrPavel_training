from django.contrib import messages
from django.db import transaction
from django.forms import ValidationError
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import FormView, ListView


from carts.models import Cart
from orders.forms import CreateOrderForms
from orders.models import Order, OrderItem


class CreateOrderView(FormView):
    template_name = "orders/create_order.html"
    form_class = CreateOrderForms
    success_url = reverse_lazy('main:index')

    def form_valid(self, form):
        try:
            with transaction.atomic():
                cart_items = Cart.objects.filter(
                    session_key=self.request.session.session_key
                )

                if cart_items.exists():
                    order = Order.objects.create(
                        first_name=form.cleaned_data["first_name"],
                        last_name=form.cleaned_data["last_name"],
                        delivery_address=form.cleaned_data["delivery_address"],
                        index_cod=form.cleaned_data["index_cod"],
                        phone_number=form.cleaned_data["phone_number"],
                        email=form.cleaned_data["email"],
                        additional_inforation=form.cleaned_data[
                            "additional_inforation"
                        ],
                    )

                    for cart_item in cart_items:
                        product = cart_item.product
                        name = cart_item.product.name
                        price = cart_item.product.sell_price()
                        quantity = cart_item.quantity

                        if product.quantity < quantity:
                            raise ValidationError(
                                f"Недостаточное количество товара {name} наскладе \
                                                    В наличии - {product.quantity}"
                            )

                        OrderItem.objects.create(
                            order=order,
                            product=product,
                            name=name,
                            price=price,
                            quantity=quantity,
                        )
                        product.quantity -= quantity
                        product.save()

                    cart_items.delete()

                    messages.success(self.request, "Заказ оформлен!")
                    return redirect("main:index")
        except ValidationError as e:
            messages.success(self.request, str(e))
            return redirect("carts:users_cart")

    def form_invalid(self, form):
        messages.success(self.request, "Упс, что-то не так!")
        return redirect("carts:users_cart")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Оформление заказа'
        context['carts'] = Cart.objects.filter(session_key=self.request.session.session_key)
        return context

# def create_order(request):

#     if request.method == "POST":
#         form = CreateOrderForms(data=request.POST)
#         if form.is_valid():
#             try:
#                 with transaction.atomic():

#                     cart_items = Cart.objects.filter(
#                         session_key=request.session.session_key
#                     )

#                     if cart_items.exists():
#                         order = Order.objects.create(
#                             first_name=form.cleaned_data["first_name"],
#                             last_name=form.cleaned_data["last_name"],
#                             delivery_address=form.cleaned_data["delivery_address"],
#                             index_cod=form.cleaned_data["index_cod"],
#                             phone_number=form.cleaned_data["phone_number"],
#                             email=form.cleaned_data["email"],
#                             additional_inforation=form.cleaned_data[
#                                 "additional_inforation"
#                             ],
#                         )

#                         for cart_item in cart_items:
#                             product = cart_item.product
#                             name = cart_item.product.name
#                             price = cart_item.product.sell_price()
#                             quantity = cart_item.quantity

#                             if product.quantity < quantity:
#                                 raise ValidationError(
#                                     f"Недостаточное количество товара {name} наскладе \
#                                                     В наличии - {product.quantity}"
#                                 )

#                             OrderItem.objects.create(
#                                 order=order,
#                                 product=product,
#                                 name=name,
#                                 price=price,
#                                 quantity=quantity,
#                             )
#                             product.quantity -= quantity
#                             product.save()

#                         cart_items.delete()

#                         messages.success(request, "Заказ оформлен!")
#                         return redirect("main:index")
#             except ValidationError as e:
#                 messages.success(request, str(e))
#                 return redirect("carts:users_cart")

#         else:
#             messages.success(request, "Упс, что-то не так!")

#     else:
#         form = CreateOrderForms()

#     carts = Cart.objects.filter(session_key=request.session.session_key)
#     context = {
#         "carts": carts,
#         "form": form,
#         "order": True,
#     }

#     return render(request, "orders/create_order.html", context=context)
