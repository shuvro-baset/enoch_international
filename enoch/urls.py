from django.urls import path
from . import views

app_name = 'enoch'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('shop/', views.ShopView.as_view(), name='shop'),
    path('single-shop/<int:product_id>', views.SingleShopView.as_view(), name='single_shop'),
    path('cart/', views.CartView.as_view(), name='cart'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('checkout/', views.CheckoutView.as_view(), name='checkout'),
]
