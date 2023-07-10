from django.contrib import admin

# Register your models here.
from .models import Good, Category


class GoodAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'article', 'catalog_number', 'description', 'in_stock', 'cat1', 'cat2',
                    'cat3', 'is_good', 'supplier']
    list_display_links = ['name', 'article', 'catalog_number', 'supplier']
    search_fields = ['name', 'article', 'catalog_number', 'supplier']


admin.site.register(Category)
admin.site.register(Good, GoodAdmin)