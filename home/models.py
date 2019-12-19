from django.db import models
from django.contrib.auth.models import User
from bids.models import Bid

# Create your models here.

class Page(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    bid_id = models.ForeignKey(Bid, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images")
    
    def __str__(self):
        return "user_id:" + str(self.user_id) + "bid_id:" + str(self.bid_id)