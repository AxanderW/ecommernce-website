from django.shortcuts import render, redirect, get_object_or_404
from store.models import Product
from .models import Cart, CartItem
from django.core.exceptions import ObjectDoesNotExist
import stripe
from django.conf import settings
from order.models import Order,OrderItem


# Create your views here.
def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()

    return cart 


def add_cart(request,product_id):
    product = Product.objects.get(id=product_id)
    print(product)
    try:
        cart = Cart.objects.get(cart_id = _cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id = _cart_id(request)
        )
        cart.save()

    try:
        cart_item = CartItem.objects.get(product = product, cart=cart)
        if cart_item.quantity <= cart_item.product.stock:
            cart_item.quantity +=1
        cart_item.save()

    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product = product,
            quantity = 1,
            cart = cart
        )
        cart_item.save()

    return redirect('cart:cart_detail')


def cart_detail(request,total=0,counter=0,cart_items=None):
    try:
        cart = Cart.objects.get(cart_id = _cart_id(request))
        #print(f'Cart id: {cart.cart_id}')
        cart_items = CartItem.objects.filter(cart=cart,active=True)
        #print(f'\n{cart_items}')
        for cart_item in cart_items:
            total +=(cart_item.product.price * cart_item.quantity)
            counter += cart_item.quantity
        
    except ObjectDoesNotExist:
        pass
    stripe.api_key = settings.STRIPE_SECRET_KEY
    stripe_total = int(total * 100)
    description = 'A Cool Fashion Store by AW Technologies'
    data_key = settings.STRIPE_PUBLISHABLE_KEY
    if request.method == 'POST':
        #print(request.POST)
        try:
            token = request.POST['stripeToken']
            email = request.POST['stripeEmail']
            billingName = request.POST['stripeBillingName']
            billingAddress1 = request.POST['stripeBillingAddressLine1']
            billingCity = request.POST['stripeBillingAddressCity']
            billingPostcode = request.POST['stripeBillingAddressZip']
            billingCountry = request.POST['stripeBillingAddressCountryCode']
            
            shippingName = request.POST.get('stripeShippingName',False)
            shippingAddress1 = request.POST.get('stripeShippingAddressLine1',False)
            shippingCity = request.POST.get('stripeShippingAddressCity',False)
            shippingPostcode = request.POST.get('stripeShippingAddressZip',False)
            shippingCountry = request.POST.get('stripeShippingAddressCountryCode',False)


            customer = stripe.Customer.create(
                email = email,
                source = token,
            )
            charge = stripe.Charge.create(
                amount = stripe_total,
                currency = "usd",
                description = description,
                customer = customer.id 
            )

            ''' Creating the order'''
            try:
                order_details = Order.objects.create(
                    token = token,
                    total =total,
                    email = email,
                    billingName = billingName,
                    billingAddress1 = billingAddress1,
                    billingCity = billingCity,
                    billingPostcode = billingPostcode,
                    billingCountry = billingCountry,

                    shippingName = shippingName,
                    shippingAddress1 = shippingAddress1,
                    shippingCity = shippingCity,
                    shippingPostcode = shippingPostcode,
                    shippingCountry = shippingCountry

                )
                order_details.save()
                for order_item in cart_items:
                    oi = OrderItem.objects.create(
                        product = order_item.product.name,
                        quantity = order_item.quantity,
                        price = order_item.product.price,
                        order = order_details
                    )
                    oi.save()
                    ''' Reduce the stock when order is placed or saved'''
                    products = Product.objects.get(id=order_item.product.id)
                    products.stock = int(order_item.product.stock - order_item.quantity)
                    products.save()
                    ''' remove item from cart now '''
                    order_item.delete()
                    '''' This will print a test script to terminal upon successful completetion'''
                    print('#################### THE ORDER HAS BEEN CREATED ##########################################')
                return redirect('order:thanks',order_details.id)
            except ObjectDoesNotExist:
                pass      
        except stripe.error.CardError as e:
            return False,e

    context = {
        'cart_items':cart_items,
        'total':total,
        'counter':counter,
        'data_key':data_key,
        'stripe_total': stripe_total,
        'description':description,
    }
    return render(request,'cart.html',context)


def cart_remove(request,product_id):
    cart = Cart.objects.get(cart_id = _cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    if cart_item.quantity >1:
        cart_item.quantity -=1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart:cart_detail')



def full_remove(request,product_id):
    cart = Cart.objects.get(cart_id = _cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    cart_item.delete()

    return redirect('cart:cart_detail')


    