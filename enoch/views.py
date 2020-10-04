from django.shortcuts import render
from django.views.generic import FormView, TemplateView, UpdateView, View
# from django.views import View

import json
from datetime import datetime
from django.conf import settings
from django.contrib import messages
from django.core.mail import EmailMessage
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from enoch.shortcuts import get_cart_list, get_checkout_data, update_cart_list, process_order, send_contact

from .models import Product, Order


class HomeView(TemplateView):
    template_name = 'index.html'

    # def get(self, request, *args, **kwargs):
    #     return render(request, 'index.html')


class ShopView(TemplateView):
    template_name = 'shop.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = self.request.GET.get('category')
        print(category)
        context['products'] = Product.objects.filter(category=category).all()
        print(context['products'])
        return context


class SingleShopView(TemplateView):
    template_name = 'shop-single.html'

    def get_context_data(self, product_id, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'carts' not in self.request.session:
            self.request.session['carts'] = []

        print('product_id ', product_id)
        context['product'] = Product.objects.filter(id=product_id).first()
        print(context['product'])
        return context


class CartView(View):
    template_name = 'cart.html'

    def get(self, request, *args, **kwargs):
        context = get_cart_list(request, Product)
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        print('i am post')
        context = update_cart_list(request, Product)
        # context = {}
        # if request.method == 'POST':
        #     request.session.modified = True
        #     if 'carts' in request.session:
        #         carts = request.session['carts']
        #     else:
        #         request.session['carts'] = []
        #         carts = request.session['carts']
        #     print('old carts ', carts)
        #     temp_cart = {
        #         'product_id': request.POST.get('product_id'),
        #         'product_amount': request.POST.get('product_amount')
        #     }
        #     carts.append(temp_cart)
        #     print('new carts ', carts)
        #
        #     products_ids = []
        #     update_carts = []
        #     if len(carts) > 0:
        #         for cart_data in carts:
        #             if int(cart_data['product_id']) not in products_ids:
        #                 products_ids.append(int(cart_data['product_id']))
        #                 update_carts.append(cart_data)
        #         print('products_ids ', products_ids)
        #
        #         request.session['carts'] = update_carts
        #     context['carts'] = Product.objects.filter(id__in=products_ids).all()
        #     print('updated-carts ', request.session['carts'])
        return render(request, self.template_name, context)


class CheckoutView(View):
    def get(self, request, **kwargs):
        if 'carts' not in request.session or len(request.session['carts']) == 0:
            return redirect('enoch:home')
        context = get_checkout_data(request, Product)

        # else:
        #     request.session['carts'] = []
        #     carts = request.session['carts']
        # if len(carts) == 0:
        #     return redirect('enoch:home')
        # carts_order_list = []
        # total_price = []
        # for cart in carts:
        #     temp = {}
        #     cart_ins = Product.objects.filter(id=int(cart['product_id'])).first()
        #     temp['product_name'] = cart_ins.name
        #     temp['product_price'] = cart_ins.price * int(cart['product_amount'])
        #     temp['amount'] = int(cart['product_amount'])
        #     carts_order_list.append(temp)
        #     total_price.append(cart_ins.price * int(cart['product_amount']))
        #
        # context['carts_order_list'] = carts_order_list
        # context['total_price'] = sum(total_price)
        # print(context['total_price'])
        return render(request, 'checkout.html', context)

    def post(self, request, **kwargs):
        order_data = get_checkout_data(request, Product)
        user_data = {
            'c_fname': request.POST.get('c_fname'),
            'c_companyname': request.POST.get('c_companyname'),  # optional
            'c_address': request.POST.get('c_address'),
            'c_email_address': request.POST.get('c_email_address'),
            'c_phone': request.POST.get('c_phone')
        }
        send_email = process_order(order_data, user_data)
        if send_email is True:
            messages.add_message(request, messages.SUCCESS,
                                 'Thank you for your order!.  We will contact with you shortly.')
            request.session.flush()
            return render(request, 'index.html')
        else:
            messages.add_message(request, messages.WARNING, 'Something went to wrong!. Please try again.')
            request.session.flush()
            return render(request, 'index.html')


class ContactView(View):
    template_name = 'contact.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        user_data = {
            'c_fname': request.POST.get('c_fname'),
            'c_email_address': request.POST.get('c_email_address'),
            'c_message': request.POST.get('c_message'),
            'c_phone': request.POST.get('c_phone')
        }
        send_contact_res = send_contact(user_data)
        if send_contact_res is True:
            messages.add_message(request, messages.SUCCESS,
                                 'Thank you for your contact!.  We will contact with you shortly.')
            return render(request, 'index.html')
        else:
            messages.add_message(request, messages.WARNING, 'Something went to wrong!. Please try again.')
            return render(request, 'index.html')


# @csrf_exempt
def ajax_update_carts(request, product_id):
    print(product_id)
    if 'carts' in request.session:
        carts = request.session['carts']
    else:
        request.session['carts'] = []
        carts = request.session['carts']

    print(carts)
    update_carts = []
    if len(carts) > 0:
        for cart_data in carts:
            print(cart_data['product_id'])
            if int(cart_data['product_id']) != product_id:
                update_carts.append(cart_data)
        request.session['carts'] = update_carts
        print('update_carts ', request.session['carts'])

    return JsonResponse({'valid': True, 'success': True, 'count_carts': len(update_carts)})


class AboutView(TemplateView):
    template_name = 'about.html'
