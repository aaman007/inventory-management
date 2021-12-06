import random

import factory
from factory.django import DjangoModelFactory

from inventory.models import Inventory, Supplier

COUNT = Inventory.objects.filter(name__contains='Product').count()


class SupplierFactory(DjangoModelFactory):
    name = factory.Faker('company')

    class Meta:
        model = Supplier


class InventoryFactory(DjangoModelFactory):
    name = factory.Sequence(lambda n: f'Product{n + COUNT}')
    description = factory.Faker('sentence', nb_words=15, variable_nb_words=False)
    notes = factory.Faker('sentence', nb_words=15, variable_nb_words=False)
    stock = factory.LazyFunction(lambda: random.randint(0, 20))
    availability = factory.LazyAttribute(lambda a: True if a.stock else False)
    supplier = factory.SubFactory(SupplierFactory)

    class Meta:
        model = Inventory

