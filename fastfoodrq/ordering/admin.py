from django.contrib import admin
from .models import (
    Product,
    Combo,
    Category,
    Ingredient,
    Tag,
    Order,
    OrderItem,
    Tab,
)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'category', 'price', 'price_promo')
admin.site.register(Product, ProductAdmin)


class ComboAdmin(admin.ModelAdmin):
    pass
admin.site.register(Combo, ComboAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'parent')
admin.site.register(Category, CategoryAdmin)


class IngredientAdmin(admin.ModelAdmin):
    pass
admin.site.register(Ingredient, IngredientAdmin)


class TagAdmin(admin.ModelAdmin):
    pass
admin.site.register(Tag, TagAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('table', 'status', 'total')
admin.site.register(Order, OrderAdmin)


class OrderItemAdmin(admin.ModelAdmin):
    pass
admin.site.register(OrderItem, OrderItemAdmin)


class TabAdmin(admin.ModelAdmin):
    pass
admin.site.register(Tab, TabAdmin)
