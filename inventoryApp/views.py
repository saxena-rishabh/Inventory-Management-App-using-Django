from django.shortcuts import render
from inventoryApp.models import item
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from inventoryApp.forms import InventoryForm
from django.shortcuts import redirect, render
import datetime


# Create your views here.
# Create your views here.
'''
class InventoryListView(ListView):
    model = item
'''

def getItems(request):
    items = list(item.objects.all().order_by('expiry_date').values())
    today = datetime.date.today()
    for product in items:
        difference = product['expiry_date'] - today
        product['days_remaining'] = difference.days
    return render(request, 'inventoryApp/item_list.html', {'item_list':items})


class InventoryCreateView(CreateView):
    model = item
    success_url = reverse_lazy('index')
    fields = '__all__'


class InventoryUpdateView(UpdateView):
    model = item
    success_url = reverse_lazy('index')
    fields = '__all__'


class InventoryDeleteView(DeleteView):
    model = item
    success_url = reverse_lazy('index')
