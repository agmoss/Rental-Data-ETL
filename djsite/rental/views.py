from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings # For file paths

import json
import os


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