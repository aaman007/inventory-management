import random

from django.core.management.base import BaseCommand
from django.db import transaction

from inventory.models import Supplier
from core.factories import SupplierFactory, InventoryFactory

NUM_SUPPLIERS = 20
NUM_INVENTORIES = 100


class Command(BaseCommand):
    help = 'Creates dummy data for testing'

    def add_arguments(self, parser):
        parser.add_argument('--num_suppliers', type=int)
        parser.add_argument('--num_inventories', type=int)

    @transaction.atomic
    def handle(self, *args, **options):
        num_suppliers = NUM_SUPPLIERS
        num_inventories = NUM_INVENTORIES

        if options['num_suppliers']:
            num_suppliers = options['num_suppliers']
        if options['num_inventories']:
            num_inventories = options['num_inventories']

        self.stdout.write("Creating new suppliers...")
        suppliers = [
            SupplierFactory() for _ in range(num_suppliers)
        ] + [supplier for supplier in Supplier.objects.all()]

        self.stdout.write("Creating new inventories...")
        for _ in range(num_inventories):
            supplier = random.choice(suppliers)
            InventoryFactory(supplier=supplier)

        self.stdout.write("Created test data successfully...")
