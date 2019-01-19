# Standard django view imports
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings # For file paths

# For api data
from django.db import connections
from django.db.models import Count, Avg
from django.http import JsonResponse
from rental.models import RentalData
from django.core import serializers

# Python & third party imports
import json
import os
import folium
import pandas as pd


def index(request):

    title = {
        'title' : 'Dashboard'
    }

    return render(request,'rental/index.html', {'title': title })

def analytics(request):

    title = {
        'title' : 'Analytics'
    }

    file_path = os.path.join(settings.VISUALS_DIR, 'plots.json')

    with open(file_path) as f:
        data = json.load(f)

    return render(request,'rental/analytics.html', {'title': title, 'data' : data})


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

def pie_data(request):
    """ JSON API """

    # GROUP BY
    data = list(
        RentalData.objects.using('rental_data')
        .values('community')
        .annotate(dcount=Count('community'))
        .order_by('-dcount')
        .filter(dcount__gt=75)
        )

    # SELECT *
    #data = list(RentalData.objects.using('rental_data').values())

    # assuming obj is a model instance (manual serialization)
    #serialized_obj = serializers.serialize('json', count )

    return JsonResponse(data, safe=False)  # or JsonResponse({'data': data})


def scatter_data(request):
    """ JSON API """

    # GROUP BY
    data = list(
        RentalData.objects.using('rental_data')
        .values('community')
        .annotate(Avg('price'))
        .order_by('-price__avg')
        )

    return JsonResponse(data, safe=False) 

def hist_data(request):
    """ JSON API """

    data = list(
        RentalData.objects.using('rental_data')
        .values('price')
        )

    return JsonResponse(data, safe=False)  


def box_data(request):
    """ JSON API """

    data = list(
        RentalData.objects.using('rental_data')
        .values('quadrant','price')
        )

    return JsonResponse(data, safe=False)  

def corr_data(request):
    """ JSON API """

    df = pd.DataFrame(
        list(
            RentalData.objects.using('rental_data')
            # TODO: Convert values to numeric...
            .values('price','_type','sq_feet','location','community','quadrant','bedrooms','den','baths','cats','dogs','utilities_included')
            )
        )

    corr = df.corr()
    z = corr.values.tolist()
    x = corr.columns.tolist()
    y = corr.index.tolist()

    data =  {
            "zValues" : z,
            "xValues" : x,
            "yValues" : y,
    }

    return JsonResponse(data, safe=False) 

def map_data(request):
    """ JSON API """

    data = list(
        RentalData.objects.using('rental_data')
        .values('latitude','longitude')
        )

    return JsonResponse(data, safe=False)  
