from django.db import models

# Create your models here.
class Products(models.Model):
    name_prod=models.CharField(max_length=256)
    type_prod=models.CharField(max_length=256)
    price_prod=models.FloatField()
    

