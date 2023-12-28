from django.contrib import admin
from django.utils.html import format_html

from main.models import NetworkUnit, Product, Contact


def clear_field(modeladmin, request, queryset):
    queryset.update(debt=None)

clear_field.short_description = "Очистить поле 'задолженность'"

@admin.register(NetworkUnit)
class NetworkUnitAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'supplier_link', 'debt', 'created_at', 'level')
    list_filter = ('contact__city',)
    actions = [clear_field]

    def supplier_link(self, obj):
        if obj.supplier:
            return format_html('<a href="/admin/main/networkunit/{}/">{}</a>', obj.id, obj.supplier)

    supplier_link.short_description = 'ссылка на поставщика'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'model', 'release')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('email', 'country', 'city', 'street', 'house', 'unit')
