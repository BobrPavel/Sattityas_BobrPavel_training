from django.urls import path

from carts import views

app_name = 'carts'

urlpatterns = [
    path('users_cart/', views.UserCartView.as_view(), name='users_cart'), 

    # path('cart_add/<slug:product_slug>/', views.CardAdd.as_view(), name='cart_add'), 
    # path('cart_add/', views.CartAdd.as_view(), name='cart_add'), 
    path('cart_add/<slug:product_slug>/', views.cart_add, name='cart_add'), 

    path('cart_change/<int:cart_id>/', views.cart_change, name='cart_change'),
    path('cart_remove/<int:cart_id>/', views.cart_remove, name='cart_remove'),
]
