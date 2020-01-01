from django.db import models
from django.contrib.auth.models import User
from products.models import Product
from django.utils import timezone

# Create your models here.

class Auction(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    bid_no = models.IntegerField(default=1)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(blank=True, null=True, default=timezone.now)
    auction_views = models.IntegerField(default=0)
    
    
    def __str__(self):
        return "id=" + str(self.pk) + "product_id:" + str(self.product_id)
        

class AuctionLineItem(models.Model):
    auction = models.ForeignKey(Auction, null=False)
    bid_winner = models.ForeignKey(User, null=False)
    product = models.ForeignKey(Product, null=False)
    price = models.IntegerField(blank=False)
    
    def __str__(self):
        return "{0} {1} @ {2}".format(self.bid_winner, self.product.artefact, self.product.price)
    
    
    
   