import django_filters

from inventory.models import Inventory


class InventoryFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    supplier__name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Inventory
        fields = {
            'name': ['iexact', 'icontains']
        }
