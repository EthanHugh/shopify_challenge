from django.urls import path, include

from rest_framework.routers import DefaultRouter

from api import views


router = DefaultRouter()
router.register('inventory', views.InventoryViewSet)
router.register('warehouse', views.WarehouseViewSet)
router.register('relationship', views.RelationshipViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
