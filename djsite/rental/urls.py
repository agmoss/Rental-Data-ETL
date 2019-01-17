from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('data/', views.data, name = 'data'),
    path('map/', views.map, name = 'map'),
    path('calgary_heat_map/', views.calgary_heat_map, name = 'calgary_heat_map'),
    path('chart/', views.box_chart, name = 'box_chart'), #Testing
    path('api/data',views.box_data, name = 'box_data'), #Testing
]