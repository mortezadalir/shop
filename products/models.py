from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ProductSort(models.Model):
    products_sort=models.CharField(max_length=256)
    products_image=models.ImageField(upload_to='image')

    def __str__(self):
        return self.products_sort


class Products(models.Model):
    products_name=models.CharField(max_length=256)
    products_sort=models.ForeignKey(ProductSort,related_name="prod_Sort")
    products_price=models.DecimalField(max_digits=6, decimal_places=2)
    prod_image=models.ImageField(upload_to='products')
