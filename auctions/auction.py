from django.contrib.auth.models import User
from auctions.models import Auction
from django.utils import timezone
from datetime import datetime, timedelta

def to_auction(request, auction):
    print(to_auction)
    
    auction = Auction.objects.filter()

    time_remaining = auction.end_time - timezone.now()
    no_of_days, seconds = time_remaining.no_days, time_remaining.seconds
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    
    time_left = str("minutes") + "m" + str("seconds") + "s"
    days_left = no_of_days
    
    
    return time_left, days_left