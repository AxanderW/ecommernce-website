from django.contrib import admin
from .models import Order, OrderItem

# Register your models here.

class OrderItemAdmin(admin.TabularInline):
    model = OrderItem
    fieldsets = [
        ('Product',{'fields':['product',],}),
        ('Quantity',{'fields':['quantity',],}),
        ('Price',{'fields':['price',],}),
        
    ]
    readonly_fields = ['product','quantity','price']
    # To disable the option of deleting the order on the backend make varable False
    #can_delete = False
    # To allow the option to delete the order on the backend (admin page) make variable True
    can_delete = True   # Make 'False' to disable
    #max_num = 0 # disables the backend (admin page) to add more order items
    

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','billingName','email','created']
    list_display_links = ('id','billingName')
    search_fields = ['id','billingName','email']
    readonly_fields = ['id','token','total','email',
                    'created','billingName','billingAddress1',
                    'billingCity','billingPostcode','billingCountry',
                    'shippingName','shippingAddress1','shippingCity',
                    'shippingPostcode','shippingCountry']




    fieldsets = [
    ('ORDER INFORMATION',{'fields':['id','token','total','created']}),
    ('BILLING INFORMATION',{'fields':['billingName','billingAddress1','billingCity','billingPostcode','billingCountry','email']}),
    ('SHIPPING INFORMATION',{'fields':[ 'shippingName','shippingAddress1','shippingCity','shippingPostcode','shippingCountry']}),
    
]

    inlines = [
        OrderItemAdmin,
    ]

    def has_delete_permission(self,request,obj=None):
        return False


    def has_add_permission(self,request):
        return False