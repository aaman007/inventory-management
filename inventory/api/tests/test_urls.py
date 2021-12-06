from django.test.testcases import SimpleTestCase
from django.urls import reverse, resolve

from inventory.api.views import InventoryListAPIView


class TestUrls(SimpleTestCase):
    def setUp(self):
        self.list_url = reverse('inventory-api:inventory_list')

    def test_inventory_list(self):
        self.assertEqual(resolve(self.list_url).func.view_class, InventoryListAPIView)
