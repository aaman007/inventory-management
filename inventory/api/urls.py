from django.urls import path

from inventory.api.views import InventoryListAPIView

app_name = 'inventory-api'

urlpatterns = [
    path('', InventoryListAPIView.as_view(), name='inventory_list')
]
