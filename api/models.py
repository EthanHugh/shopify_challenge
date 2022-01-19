from django.db import models

import uuid

from django.db.models.deletion import CASCADE

# Create your models here.

class Inventory(models.Model):
    """Inventory information"""
    inv_primary = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    inventory_id = models.CharField(max_length=50, unique=True)
    inventory_name = models.CharField(max_length=100, unique=True)
    
    class Meta:
        verbose_name = 'Inventory'
        verbose_name_plural = 'Inventories'

    def __str__(self):
        """Return the model as a string"""
        return str(self.inventory_name) + " - " + str(self.inventory_id)
    

class Warehouse(models.Model):
    """Warehouse information"""
    wh_primary = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    warehouse_id = models.CharField(max_length=50, unique=True)
    warehouse_name = models.CharField(max_length=100, unique=True)
    
    class Meta:
        verbose_name = 'Warehouse'
        verbose_name_plural = 'Warehouses'
    
    def __str__(self):
        """Return the warehouse model as a string"""
        return str(self.warehouse_name) + " - " + str(self.warehouse_id)
    

class WarehouseInventoryRelationship(models.Model):
    """a relationship between warehouses and inventory items"""
    warehouse = models.ForeignKey(
        Warehouse,
        on_delete=CASCADE
    )
    inventory = models.ForeignKey(
        Inventory,
        on_delete=CASCADE
    )
    
    class Meta:
        verbose_name = 'Warehouse to Inventory Relationship'
        verbose_name_plural = 'Warehouse to Inventory Relationships'
    
    def __str__(self):
        """Return the warehouse model as a string"""
        return str(self.inventory) + " is held in " + str(self.warehouse)

