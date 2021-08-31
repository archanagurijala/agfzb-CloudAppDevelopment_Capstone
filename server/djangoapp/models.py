from django.db import models
from django.utils.timezone import now


# Create your models here.

# <HINT> Create a Car Make model 
class CarMake(models.Model):
    name = models.CharField(null=False, max_length=30, default='django app')
    description = models.CharField(max_length=1000)
    def __str__(self):
        return "Name: " + self.name + "," + \
               "Description: " + self.description


# <HINT> Create a Car Model model 
class CarModel(models.Model):
    id = models.AutoField(primary_key=True)
    cars = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(null=False, max_length=30)
    dealer_id = models.IntegerField(null=True)
    carType = models.CharField(max_length=1000)
    year = models.DateField()
    def __str__(self):
        return "Name: " + self.name + "," + \
               "Type: " + self.carType + "," + \
               "Year: " + self.year + "," + \
               "Dealer Id: " + self.dealer_id


# <HINT> Create a plain Python class `CarDealer` to hold dealer data


# <HINT> Create a plain Python class `DealerReview` to hold review data
