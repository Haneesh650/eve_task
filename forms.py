from django import forms
from .models import *

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = "__all__"

class RentCarForm(forms.ModelForm):
    class Meta:
        model = booking
        fields = "__all__"