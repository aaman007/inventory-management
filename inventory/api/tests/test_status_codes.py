from django.test import TestCase
from django.urls import reverse


class TestStatusCodes(TestCase):
    def setUp(self):
        self.list_url = reverse('inventory-api:inventory_list')

    def test_inventory_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, 200)
