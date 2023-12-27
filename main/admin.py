from django.contrib import admin

from main.models import NetworkUnit, Product, Contact


def clear_field(modeladmin, request, queryset):
    queryset.update(debt=None)

clear_field.short_description = "Очистить поле"

@admin.register(NetworkUnit)
class NetworkUnitAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'supplier', 'debt', 'created_at', 'level')
    actions = [clear_field]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'model', 'release')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('email', 'country', 'city', 'street', 'house', 'unit')