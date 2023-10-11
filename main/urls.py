from django.urls import path

from main.views import (HomeView,
                        SHoppingView,
                        ShoppingCartView,
                        AddProductView
                        )

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('shop', SHoppingView.as_view(), name='shop'),
    path('shopping-cart', ShoppingCartView.as_view(), name='shopping-cart'),
    path('add-product', AddProductView.as_view(), name='add-product')
]