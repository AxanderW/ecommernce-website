# Import Django libaries
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404,redirect
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.contrib.auth.models import Group,User
from django.contrib.auth import login, authenticate,logout
# Import models
from .models import Category,Product,SaleProduct
from banners.models import BannerItem
from .models import Category,Product
# Import Forms
from .forms import SignUpForm,ContactForm
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def index(request):
    home_hero_banners = BannerItem.objects.filter(bannercategory__slug='home-hero',isActive=True)
    sale_product_list = SaleProduct.objects.filter(isActive=True)
    context = {'home_hero_banners':home_hero_banners,
                'sale_product_list':sale_product_list,
            }
    return render(request,'index.html',context)

def about(request):
    about_banner = BannerItem.objects.filter(bannercategory__slug='about',isActive=True).first()
    about_persons = BannerItem.objects.filter(bannercategory__slug='about-person',isActive=True) 
    context = {
                'about_banner':about_banner,
                'about_persons':about_persons,
            }
    return render(request,'about.html',context)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # send email code goes here
            return render(request,'contact_success.html')
    else:
        form = ContactForm()
    
    context = {'form':form}

    return render(request,'contactus.html',context)



# Category view
# c_slug = slug field of the category model
def allProdCat(request,c_slug=None):
    c_page = None #category page this means all categories
    products_list = None
    if c_slug !=None:
        c_page = get_object_or_404(Category,slug=c_slug)
      
        products_list = Product.objects.filter(category=c_page,available=True)
    else:
        products_list = Product.objects.filter(available=True)



    context = {
        'category': c_page,
        'products': products_list
    }
    #print(c_page,products_list)

    return render(request,'store/category.html',context)


def ProdCatDetail(request, c_slug,product_slug):
    try:
        product = Product.objects.get(category__slug=c_slug,slug=product_slug)
    except Exception as e:
        raise e
        product = None

    context = {
        'product': product
    }
    return render(request,'store/product.html',context)


def signupView(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            signup_user = User.objects.get(username=username)
            customer_group = Group.objects.get(name='Customer')
            customer_group.user_set.add(signup_user)

    else:
        form = SignUpForm()
    
    context = {'form':form}

    return render(request,'accounts/signup.html',context)


def signinView(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect('store:allProdCat')

            else:
                return redirect('signup')
    else:
        form = AuthenticationForm()

    context = {'form':form}
    return render(request, 'accounts/signin.html',context)


def signoutView(request):
    logout(request)
    return redirect('signin')
