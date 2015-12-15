from django.contrib import admin
from lab3.models import Product, Manufacture, Category, Recall


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'weight', 'price', 'manufacture')
    raw_id_fields = ('category',)


class RecallAdmin(admin.ModelAdmin):
    list_display = ('text', 'user_id')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'floor')


class ManufactureAdmin(admin.ModelAdmin):
    list_display = ('country', 'name')


admin.site.register(Product, ProductAdmin)
admin.site.register(Manufacture, ManufactureAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Recall, RecallAdmin)
