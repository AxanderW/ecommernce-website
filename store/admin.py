from django.contrib import admin

from .models import Category, Product, SaleCategory,SaleProduct

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
    list_per_page = 10

admin.site.register(Category,CategoryAdmin)



class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','slug','category','price','stock','available','created','updated']
    list_editable = ['category','price','stock','available']
    prepopulated_fields = {'slug':('name',)}
    list_per_page = 10
admin.site.register(Product,ProductAdmin)

class SaleCategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug','label',]
    prepopulated_fields = {'slug':('name',)}
    list_per_page = 10

admin.site.register(SaleCategory,SaleCategoryAdmin)


class SaleProductAdmin(admin.ModelAdmin):
    list_display = ['product','salecategory','discount','isActive','created',]
    list_editable = ['salecategory','discount','isActive',]
    list_per_page = 10
admin.site.register(SaleProduct,SaleProductAdmin)

