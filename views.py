from django.shortcuts import render,redirect
from .models import *
from .forms import *

# Create your views here.

def car_all(request):
    data = Car.objects.all()
    return render (request,'car.html',{'data':data})


def rent_car(request):
    total_cost = None
    if request.method == 'POST':
        form = RentCarForm(request.POST)
    if form.is_valid():
        car = form.cleaned_data['car']
        renter_name = form.cleaned_data['renter_name']
        days = form.cleaned_data['days']            
        total_cost = car.rental_price_per_day * days
        car.availability_status = False
        car.save()

    return render(request, 'rent_car.html', {'form': form, 'total_cost': total_cost, 'success': True,'renter':renter_name,'car':car})





    


