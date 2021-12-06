from django.test import TestCase
from django.urls import reverse, resolve

from inventory.models import Inventory, Supplier
from inventory.views import InventoryListView, InventoryDetailView


class TestUrls(TestCase):
    def setUp(self):
        supplier = Supplier.objects.create(name='Supplier')
        inventory = Inventory.objects.create(
            name='Name',
            description='Description',
            supplier=supplier
        )
        self.list_url = reverse('inventory:inventory_list')
        self.detail_url = reverse('inventory:inventory_detail', kwargs={'pk': inventory.id})

    def test_inventory_list(self):
        self.assertEqual(resolve(self.list_url).func.view_class, InventoryListView)

    def test_inventory_detail(self):
        self.assertEqual(resolve(self.detail_url).func.view_class, InventoryDetailView)

