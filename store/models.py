from django.db import models
from django.urls import reverse
# Create your models here.

from taggit.managers import TaggableManager

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250,unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='media/category',blank=True)
    icon = models.CharField(max_length=50, blank=True,default='fas fa-tshirt')

    class Meta:
        ordering = ('name',)
        verbose_name = 'cateogry'
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse('store:products_by_category',args=[self.slug])


    def __str__(self):
        return f'{self.name}'





class Product(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250,unique=True)
    description = models.TextField(blank=True)

    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    price = models.DecimalField(max_digits=10,decimal_places=2)
    image = models.ImageField(upload_to='media/product', blank=True)
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    digital = models.BooleanField(default=False)
    tags = TaggableManager()
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ('name',)
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def get_url(self):
        return reverse('store:ProdCatDetail',args=[self.category.slug,self.slug])



    def __str__(self):
        return f'{self.name}'



class SaleCategory(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250,unique=True)
    label = models.CharField(max_length = 250, blank=True)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now=True)



    class Meta:
        ordering = ('name',)
        verbose_name = 'salecategory'
        verbose_name_plural = 'salecategories'


    def __str__(self):
        return f'{self.slug}'



class SaleProduct(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    salecategory = models.ForeignKey(SaleCategory,on_delete=models.CASCADE)

    discount = models.DecimalField(default=None, max_digits=3,decimal_places=2, blank=True,null=True)
    isActive = models.BooleanField(default=True)

    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ('product',)
        verbose_name = 'saleproduct'
        verbose_name_plural = 'saleproducts'





    def __str__(self):
        return f'{self.product},{self.salecategory}'




