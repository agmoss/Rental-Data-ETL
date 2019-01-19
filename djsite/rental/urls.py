from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.index, name='index'),
    path('analytics/', views.analytics, name='analytics'),
    path('about/', views.about, name='about'),
    path('data/', views.data, name = 'data'),
    path('map/', views.map, name = 'map'),
    path('calgary_heat_map/', views.calgary_heat_map, name = 'calgary_heat_map'),
    path('api/pie_data',views.pie_data, name = 'pie_data'), 
    path('api/scatter_data',views.scatter_data, name = 'scatter_data'), 
    path('api/hist_data',views.hist_data, name = 'hist_data'), 
    path('api/box_data',views.box_data, name = 'box_data'), 
    path('api/corr_data',views.corr_data, name = 'corr_data'), 
]