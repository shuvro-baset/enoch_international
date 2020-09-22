import os

from django.shortcuts import redirect


def product_image_upload_path(instance, file_name):
    return os.path.join("product_images", str(instance.id) + '_' + file_name)


def update_cart_list(request, model_name):
    context = {}
    request.session.modified = True
    if 'carts' in request.session:
        carts = request.session['carts']
    else:
        request.session['carts'] = []
        carts = request.session['carts']
    print('old carts ', carts)
    temp_cart = {
        'product_id': request.POST.get('product_id'),
        'product_amount': request.POST.get('product_amount')
    }
    carts.append(temp_cart)
    print('new carts ', carts)

    products_ids = []
    update_carts = []
    if len(carts) > 0:
        for cart_data in carts:
            if int(cart_data['product_id']) not in products_ids:
                products_ids.append(int(cart_data['product_id']))
                update_carts.append(cart_data)
        print('products_ids ', products_ids)

    request.session['carts'] = update_carts
    # context['carts'] = model_name.objects.filter(id__in=products_ids).all()
    carts_data = []
    for cart in update_carts:
        temp = {}
        products_ins = model_name.objects.filter(id=int(cart['product_id'])).first()
        temp['products_ins'] = products_ins
        temp['product_amount'] = cart['product_amount']
        carts_data.append(temp)
    context['carts'] = carts_data

    print('updated-carts ', request.session['carts'])
    return context


def get_cart_list(request, model_name):
    context = {}
    request.session.modified = True
    if 'carts' in request.session:
        carts = request.session['carts']
    else:
        request.session['carts'] = []
        carts = request.session['carts']
    print('old carts ', carts)
    # temp_cart = {
    #     'product_id': request.POST.get('product_id'),
    #     'product_amount': request.POST.get('product_amount')
    # }
    # carts.append(temp_cart)
    # print('new carts ', carts)

    products_ids = []
    update_carts = []
    if len(carts) > 0:
        for cart_data in carts:
            if int(cart_data['product_id']) not in products_ids:
                products_ids.append(int(cart_data['product_id']))
                update_carts.append(cart_data)
        print('products_ids ', products_ids)

    request.session['carts'] = update_carts
    # context['carts'] = model_name.objects.filter(id__in=products_ids).all()
    carts_data = []
    for cart in update_carts:
        temp = {}
        products_ins = model_name.objects.filter(id=int(cart['product_id'])).first()
        temp['products_ins'] = products_ins
        temp['product_amount'] = cart['product_amount']
        carts_data.append(temp)
    context['carts'] = carts_data

    print('updated-carts ', request.session['carts'])
    return context


def get_checkout_data(request, model_name):
    context = {}
    if 'carts' in request.session:
        carts = request.session['carts']
    else:
        request.session['carts'] = []
        carts = request.session['carts']

    carts_order_list = []
    total_price = []
    for cart in carts:
        temp = {}
        cart_ins = model_name.objects.filter(id=int(cart['product_id'])).first()
        temp['product_name'] = cart_ins.name
        temp['product_price'] = cart_ins.price * int(cart['product_amount'])
        temp['amount'] = int(cart['product_amount'])
        carts_order_list.append(temp)
        total_price.append(cart_ins.price * int(cart['product_amount']))

    context['carts_order_list'] = carts_order_list
    context['total_price'] = sum(total_price)
    print(context['total_price'])
    return context
