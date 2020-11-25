from django.urls import path
from . import views

urlpatterns = [
    #Leave as empty for base url
    path('',views.store, name='store-home'),
    path('cart/',views.cart, name='store-cart'),
    path('checkout/',views.checout,name='store-checkout'),
]