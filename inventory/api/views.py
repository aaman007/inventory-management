from rest_framework.generics import ListAPIView

from inventory.api.filters import InventoryFilter
from inventory.api.serializers import InventorySerializer
from inventory.models import Inventory


class InventoryListAPIView(ListAPIView):
    serializer_class = InventorySerializer
    filterset_class = InventoryFilter

    def get_queryset(self):
        return Inventory.objects.select_related('supplier')
