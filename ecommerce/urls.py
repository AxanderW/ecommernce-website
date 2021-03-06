"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from store import views as store_views

from django.urls import path, include 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',store_views.index, name='home'),
    path('about/',store_views.about, name='about'),
    path('contact',store_views.contact, name='contact'),
    path('store/',include('store.urls')),
    path('search/',include('search_app.urls')),
    path('cart/',include('cart.urls')),
    path('order/',include('order.urls')),
    path('account/create',store_views.signupView,name='signup'),
    path('account/login',store_views.signinView,name='signin'),
    path('account/logout',store_views.signoutView,name='signout'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)