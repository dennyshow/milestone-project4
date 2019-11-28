from django.db import models
from django.contrib.auth.models import User
from auctions.models import Auction
from datetime import datetime

# Create your models here.

class Bid(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    auction_id = models.ForeignKey(Auction, on_delete=models.CASCADE)
    bid_time = models.DateTimeField(auto_now_add=True, blank=True)