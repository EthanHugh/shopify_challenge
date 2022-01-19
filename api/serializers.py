from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse

from api import models

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Inventory
        fields = ('inventory_id', 'inventory_name')
        

class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Warehouse
        fields = ('warehouse_id', 'warehouse_name')
        

class RelationshipSerializer(serializers.ModelSerializer):
    warehouse_id = serializers.CharField(source='warehouse.warehouse_id', read_only=True)
    warehouse_name = serializers.CharField(source='warehouse.warehouse_name', read_only=True)
    inventory_id = serializers.CharField(source='inventory.inventory_id', read_only=True)
    inventory_name = serializers.CharField(source='inventory.inventory_id', read_only=True)

    
    class Meta:
        model = models.WarehouseInventoryRelationship
        fields = (
            'id',
            'warehouse',
            'warehouse_id',
            'warehouse_name',
            'inventory',
            'inventory_id',
            'inventory_name'
        )