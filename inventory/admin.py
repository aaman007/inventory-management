from django.contrib import admin

from inventory.models import Inventory, Supplier


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'stock', 'availability', 'supplier', 'modified_at']
    list_filter = ['availability', 'supplier']
    search_fields = ['name', 'supplier']


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at', 'modified_at']
    search_fields = ['name']
