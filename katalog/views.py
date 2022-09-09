# TODO: Create your views here. (jalan)

from django.shortcuts import render
from django.shortcuts import render
from katalog.models import CatalogItem

# Create your views here.
def show_katalog(request):
    initial_catalog_data = CatalogItem.objects.all()
    context = {
        'list_barang': initial_catalog_data,
        'nama': 'Eugenius Mario Situmorang',
        'npm': '2106750484'
    }
    return render(request, "katalog.html", context)