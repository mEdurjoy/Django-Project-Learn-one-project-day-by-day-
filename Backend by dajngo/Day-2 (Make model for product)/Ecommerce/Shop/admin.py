from django.contrib import admin

# Register your models here.
from . models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'selling_price', 'discounted_price','description', 'brand', 'category', 'product_image']