from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings # For file paths

# Testing
from django.db import connections
from django.db.models import Count
from django.http import JsonResponse

import json
import os

import folium


def index(request):

    title = {
        'title' : 'Dashboard'
    }

    file_path = os.path.join(settings.VISUALS_DIR, 'plots.json')

    with open(file_path) as f:
        data = json.load(f)

    return render(request,'rental/index.html', {'title': title, 'data' : data})

def about(request):

    title = {
        'title' : 'About'
    }

    return render(request,'rental/about.html',title)

def data(request):

    title = {
        'title' : 'Data'
    }

    return render(request,'rental/data.html',title)

def map(request):

    title = {
        'title' : 'Data'
    }

    return render(request,'rental/map.html',title)


def calgary_heat_map(request):
    
    title = {
        'title' : 'Data'
    }

    return render(request,'rental/calgary_heat_map.html',title)


# Testing

from rental.models import RentalData

def box_chart(request):
    return render(request, 'graph/graph.html')


def box_data(request):

    from django.core import serializers

    data = list(RentalData.objects.using('rental_data').values())

    return JsonResponse(data, safe=False)  # or JsonResponse({'data': data})


