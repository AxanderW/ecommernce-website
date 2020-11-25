from django.shortcuts import render, get_object_or_404
from .models import Order, OrderItem
from django.contrib.auth.decorators import login_required

# Create your views here.
def thanks(request,order_id):
    if order_id:
        customer_order = get_object_or_404(Order,id=order_id)
    else:
        customer_order = {}


    context = {'customer_order':customer_order}

    return render(request,'thanks.html',context)


@login_required()
def orderHistory(request):
    if request.user.is_authenticated:
        email = str(request.user.email)
        order_details = Order.objects.filter(email=email)
        #print(f"################### USER EMAIL {email} ########################")
        #print(order_details)
    else:
        order_details = None


    
    context = {'order_details': order_details}


    return render(request,'order_list.html',context)


@login_required()
def viewOrder(request, order_id):
    if request.user.is_authenticated:
        email = str(request.user.email)
        order = Order.objects.get(id=order_id,email=email)
        order_items = OrderItem.objects.filter(order=order)
    else:
        order_items = None

    context = {'order': order,
                'order_items':order_items}
    return render(request,'order_details.html',context)







