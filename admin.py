from django.contrib import admin
from costomer.models import order

# Register your models here.
@admin.register(order)
class orderAdmin(admin.ModelAdmin):
    list_display=['name','product_name','price','quantity']
