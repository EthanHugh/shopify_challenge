from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.models import User

from api import models
# Register your models here.

admin.site.site_header = "Shopify Challenge Admin Page"
admin.site.unregister(Group)
# admin.site.unregister(User)

class InventoryAdmin(admin.ModelAdmin):
    list_display = ('inventory_name', 'inventory_id')
    
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ('warehouse_name', 'warehouse_id')
    
class RelationshipAdmin(admin.ModelAdmin):
    list_display = ('get_warehouse_name', 'get_warehouse_id', 'get_inventory_name', 'get_inventory_id')
    list_filter = ('warehouse', )
    
    def get_warehouse_name(self, obj):
        return obj.warehouse.warehouse_name
    get_warehouse_name.short_description = 'Warehouse Name'
    
    def get_warehouse_id(self, obj):
        return obj.warehouse.warehouse_id
    get_warehouse_id.short_description = 'Warehouse ID'
    
    def get_inventory_name(self, obj):
        return obj.inventory.inventory_name
    get_inventory_name.short_description = 'Inventory Name'
    
    def get_inventory_id(self, obj):
        return obj.inventory.inventory_id
    get_inventory_id.short_description = 'Inventory ID'

admin.site.register(models.Inventory, InventoryAdmin)
admin.site.register(models.Warehouse, WarehouseAdmin)
admin.site.register(models.WarehouseInventoryRelationship, RelationshipAdmin)