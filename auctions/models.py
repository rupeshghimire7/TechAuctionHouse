from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    price = models.FloatField()
    description = models.CharField(max_length=1000)
    publish_date = models.DateField()
    bid_ends = models.DateField()
    image = models.ImageField(upload_to='auctions/product_images', default='')

    def __str__(self):
        return  self.product_name

