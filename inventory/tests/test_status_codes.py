from django.test import TestCase
from django.urls import reverse

from inventory.models import Inventory, Supplier


class TestStatusCodes(TestCase):
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
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, 200)

    def test_inventory_detail(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, 200)
