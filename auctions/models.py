from django.db import models
from products.models import Product
from datetime import datetime, timezone

# Create your models here.

class Auction(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    bid_no = models.IntegerField()
    start_time = models.DateTimeField(null=True, blank=True, default='timezone')
    end_time = models.DateTimeField( auto_now_add=True, blank=True, default='timezone')
    
   