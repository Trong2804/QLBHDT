

# Create your models here.
from django.db import models

class Phone(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

class Warranty(models.Model):
    phone = models.ForeignKey(Phone, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
