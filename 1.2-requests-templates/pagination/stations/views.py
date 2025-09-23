from django.conf import settings
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
import csv

CONTENT = []
with open (settings.BUS_STATION_CSV, encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        CONTENT.append({
            'Name': row['Name'],
            'Street': row['Street'],
            'District': row['District']
        })



def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    page_number = int(request.GET.get("page", 1))

    paginator = Paginator(CONTENT, 10)

    page = paginator.get_page(page_number)

    bus_stations = page.object_list


    context = {
         'bus_stations': bus_stations,
         'page': page,
    }
    return render(request, 'stations/index.html', context)
