from .views import *
from django.urls import path

urlpatterns = [

    path('car/',car_all,name='car_details'),
    path('rent/', rent_car, name='rent_car'),
]