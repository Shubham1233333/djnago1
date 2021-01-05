from django.contrib import admin
from products.models import *
# Register your models here.

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display=['name']
@admin.register( catogery)
class  catogeryAdmin(admin.ModelAdmin):
    list_display=['name']
@admin.register(product)
class productAdmin(admin.ModelAdmin):
    list_display=['name','price','list_price','pic','description']
    search_fields = ('price',)
    list_filter=['name','brand']
    list_editable=['price',]
   



