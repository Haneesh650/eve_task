from django.db import models

# Create your models here.
class Car(models.Model):
    name = models.CharField(max_length=20)
    brand = models.CharField(max_length=20)
    rental_price_per_day = models.PositiveIntegerField()
    availability_status = models.BooleanField(default=True)


    def __str__(self):
        return f"{self.name},{self.brand}"
    

class booking(models.Model):
    name = models.CharField(max_length=20)
    brand = models.CharField(max_length=20)
    rental_price_per_day = models.PositiveIntegerField()
    availability_status = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name},{self.brand}"
