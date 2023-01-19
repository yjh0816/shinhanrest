from django.contrib import admin
from .models import Product, Comment

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    list_filter = ['product_type']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass