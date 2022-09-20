from django.shortcuts import render

from django.http import HttpResponse
from django.core import serializers

from mywatchlist.models import MyWatchList

def mywatchlist(request):
    context = {
        'nama': 'Eugenius Mario Situmorang',
        'npm': '2106750484'
    }
    return render(request, "mywatchlist_homepage.html", context)

def show_html(request):
    # Mengambil data MyWatchList
    data_mywatchlist = MyWatchList.objects.all()

    # Menghitung banyak film ditonton
    watched_total = 0
    for movie in data_mywatchlist:
        if movie.watched:
            watched_total += 1

    # Total film ditonton >= Total film belum ditonton
    watch_a_lot = watched_total > (len(data_mywatchlist) - watched_total) 

    # Menyusun tampilan teks yang akan dikirimkan
    text_display = "Selamat, kamu sudah banyak menonton!" if watch_a_lot else "Wah, kamu masih sedikit menonton!"

    # Merangkum data di context
    context = {
        'list_film': data_mywatchlist,
        'nama': 'Eugenius Mario Situmorang',
        'npm': '2106750484',
        'banyak_menonton': text_display
    }
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")