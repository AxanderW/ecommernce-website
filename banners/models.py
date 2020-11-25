from django.db import models

# Create your models here.
class BannerCategory(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250,unique=True)
    isActive = models.BooleanField(default=True)


    class Meta:
        ordering = ('name',)
        verbose_name = 'bannercategory'
        verbose_name_plural = 'bannercategories'


    def __str__(self):
        return f'{self.slug}'



class BannerItem(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250,unique=True)
    image = models.ImageField(upload_to='media/banneritem',blank=True)
    bannercategory = models.ForeignKey(BannerCategory,on_delete=models.CASCADE, blank=True, null=True)
    text1 = models.TextField(default='',blank=True, null=True, )
    text2 = models.TextField(default='', blank=True, null=True)
    text3 = models.TextField(default='', blank=True, null=True)
    text4 = models.TextField(default='', blank=True, null=True)
    text5 = models.TextField(default='', blank=True, null=True)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now=True)
    isActive = models.BooleanField(default=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'banneritem'
        verbose_name_plural = 'banneritems'


    def __str__(self):
        return f'{self.slug}'