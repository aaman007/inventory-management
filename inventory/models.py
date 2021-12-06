from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import AbstractTimestampModel


class Inventory(AbstractTimestampModel):
    name = models.CharField(verbose_name=_('Name'), max_length=200)
    description = models.CharField(verbose_name=_('Description'), max_length=255)
    notes = models.TextField(verbose_name=_('Notes'), blank=True)
    stock = models.PositiveIntegerField(verbose_name=_('Stock'), default=0)
    availability = models.BooleanField(verbose_name=_('Availability'), default=False)
    supplier = models.ForeignKey(
        verbose_name=_('Supplier'),
        to='Supplier',
        related_name='inventories',
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = _('Inventory')
        verbose_name_plural = _('Inventories')

    def __str__(self):
        return self.name


class Supplier(AbstractTimestampModel):
    name = models.CharField(verbose_name=_('Name'), max_length=200)

    class Meta:
        verbose_name = _('Supplier')
        verbose_name_plural = _('Suppliers')

    def __str__(self):
        return self.name
