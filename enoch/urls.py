from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('home-test', views.home, name='home_test'),
    path('contact', views.contact, name='contact'),
    path('cart', views.cart, name='cart'),
    path('checkout', views.checkout, name='checkout'),
    path('shop', views.shop, name='shop'),
    path('shop-single', views.shopsingle, name='shop-single'),
]
