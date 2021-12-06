from django.views.generic import ListView, DetailView

from inventory.models import Inventory


class InventoryListView(ListView):
    queryset = Inventory.objects.all()
    context_object_name = 'inventories'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context.update({
            'home_nav': 'active'
        })
        return context


class InventoryDetailView(DetailView):
    model = Inventory
    context_object_name = 'inventory'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'home_nav': 'active'
        })
        return context
