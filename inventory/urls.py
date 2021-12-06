from django.urls import path

from inventory.views import InventoryListView, InventoryDetailView

app_name = 'inventory'

urlpatterns = [
    path('', InventoryListView.as_view(), name='inventory_list'),
    path('<int:pk>/', InventoryDetailView.as_view(), name='inventory_detail')
]
