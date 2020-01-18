from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Bidder(models.Model):
        # creating model to store bidder/user info 
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=30)
    street_address1 = models.CharField(max_length=100)
    street_address2 = models.CharField(max_length=100)
    county = models.CharField(max_length=20)
    eircode = models.CharField(max_length=10)
    country = models.CharField(max_length=20)
    
    
@receiver(post_save, sender=User)
        # updating into profile when a new user/bidder has been created
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Bidder.objects.create(user=instance)
    instance.bidder.save()