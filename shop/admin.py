from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe

# Register your models here.
class ProductInline(admin.StackedInline):
    model = models.Product
    extra = 1

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'display_image', 
        'name', 
        'price', 
        'description',
        'category',
        'brand',  
        'status', 
        'date_add', 
        'date_update'
        ]
    list_display_links = [
        'display_image', 
        'name', 
        'price', 
        'description',
        'category',
        'brand', 
        'status', 
        'date_add', 
        'date_update'
        ]
    list_filter = ['category', 'date_add']
    filter_horizontal = ['colors']

    def display_image(self, obj):
        return mark_safe(
            f'<img src={obj.image.url} width=100px height=80px'
        )
    display_image.short_description = 'image'


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'name', 
        'status', 
        'date_add', 
        'date_update'
        ]
    inlines = [ProductInline]


@admin.register(models.Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = [
        'name', 
        'status', 
        'date_add', 
        'date_update'
        ]
    inlines = [ProductInline]


@admin.register(models.Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = [
        'name', 
        'status', 
        'date_add', 
        'date_update'
        ]


@admin.register(models.Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = [
        'value', 
        'status', 
        'date_add', 
        'date_update'
        ]


@admin.register(models.Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = [
        'value', 
        'status', 
        'date_add', 
        'date_update'
        ]