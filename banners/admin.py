from django.contrib import admin
from .models import BannerCategory, BannerItem

# Register your models here.
class BannerCategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug','isActive',]
    prepopulated_fields = {'slug':('name',)}
    list_per_page = 10

admin.site.register(BannerCategory,BannerCategoryAdmin)



class BannerItemAdmin(admin.ModelAdmin):
    list_display = ['name','slug','bannercategory','text1','isActive','image',]
    list_editable = ['bannercategory','text1','isActive',]
    prepopulated_fields = {'slug':('name',)}
    list_per_page = 10
admin.site.register(BannerItem,BannerItemAdmin)
