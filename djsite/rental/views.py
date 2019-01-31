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
import numpy as np


def home(request):

    content = {
        'title' : 'Home',
    }

    return render(request,'rental/home.html', content)

def dashboard(request):

    content = {
        'title' : 'Dashboard',
    }

    return render(request,'rental/dashboard.html', content)

def analytics(request):

    content = {
        'title' : 'Analytics'
    }

    return render(request,'rental/analytics.html', content)


def about(request):

    content = {
        'title' : 'About'
    }

    return render(request,'rental/about.html',content)

def data(request):

    content = {
        'title' : 'Data'
    }

    return render(request,'rental/data.html',content)

def map(request):

    content = {
        'title' : 'Map'
    }

    return render(request,'rental/map.html',content)

def pie_data(request):
    """ JSON API """

    # GROUP BY
    data = list(
        RentalData.objects.using('rental_data')
        .values('community','_type')
        .annotate(dcount=Count('community'))
        .order_by('-dcount')
        .filter(position = 'active')
        )

    return JsonResponse(data, safe=False)  


def scatter_data(request):
    """ JSON API """

    # GROUP BY
    data = list(
        RentalData.objects.using('rental_data')
        .values('community','_type')
        .annotate(Avg('price'),dcount=Count('community')) # For filtering
        .order_by('-price__avg')
        .filter(position = 'active')             
        )

    return JsonResponse(data, safe=False) 

def hist_data(request):
    """ JSON API """

    data = list(
        RentalData.objects.using('rental_data')
         .values('price','_type')
         .filter(position = 'active')
         )

    return JsonResponse(data, safe=False)  


def box_data(request):
    """ JSON API """

    data = list(
        RentalData.objects.using('rental_data')
        .values('quadrant','price','_type')
        .filter(position = 'active')
        )

    return JsonResponse(data, safe=False)  

def corr_data(request):
    """ JSON API """

    df = pd.DataFrame(
        list(
            RentalData.objects.using('rental_data')
            # TODO: Convert values to numeric...
            .values('price','_type','sq_feet','location','community','quadrant','bedrooms','den','baths','cats','dogs','utilities_included')
            .filter(position = 'active')
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
        .values('latitude','longitude','price','_type')
        .filter(position = 'active')
        )

    from django.core.serializers import serialize

    return JsonResponse(data, safe=False)  