from django.shortcuts import render
from django.http.response import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated

from api import serializers
from api import models

# Create your views here.
class InventoryViewSet(viewsets.ModelViewSet):
    
    serializer_class = serializers.InventorySerializer
    queryset = models.Inventory.objects.all()
    
    lookup_field = 'inventory_name'
    

class WarehouseViewSet(viewsets.ModelViewSet):
    
    serializer_class = serializers.WarehouseSerializer
    queryset = models.Warehouse.objects.all()
    
    lookup_field = 'warehouse_name'
    

class RelationshipViewSet(viewsets.ModelViewSet):
    
    serializer_class = serializers.RelationshipSerializer
    queryset = models.WarehouseInventoryRelationship.objects.all()
    
    filter_backends = (filters.SearchFilter,)
    search_fields = ('=warehouse__warehouse_name',)