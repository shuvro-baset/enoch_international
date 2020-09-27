from django.urls import path
from . import views

app_name = 'enoch'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('shop/', views.ShopView.as_view(), name='shop'),
    path('single-shop/<int:product_id>', views.SingleShopView.as_view(), name='single_shop'),
    path('cart/', views.CartView.as_view(), name='cart'),
    path('checkout/', views.CheckoutView.as_view(), name='checkout'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('ajax-update-carts/<int:product_id>', views.ajax_update_carts, name='ajax_update_carts'),
    path('about', views.AboutView.as_view(), name='about'),
]
