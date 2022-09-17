from django.shortcuts import render

from django.http import HttpResponse
from django.core import serializers

from mywatchlist.models import MyWatchList

def show_html(request):
    data_mywatchlist = MyWatchList.objects.all()
    context = {
        'list_film': data_mywatchlist,
        'nama': 'Eugenius Mario Situmorang',
        'npm': '2106750484'
    }
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")