from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.index, name='index'),
    path('analytics/', views.analytics, name='analytics'),
    path('about/', views.about, name='about'),
    path('data/', views.data, name = 'data'),
    path('map/', views.map, name = 'map'),
    path('calgary_heat_map/', views.calgary_heat_map, name = 'calgary_heat_map'),
    path('api/pie_data',views.pie_data, name = 'pie_data'), #JSON API f
    path('api/scatter_data',views.scatter_data, name = 'scatter_data'), #JSON API for SVG
]