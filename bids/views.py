from django.contrib import messages
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.models import User
from .models import Bid
from auctions.models import Auction
from django.utils import timezone
from datetime import datetime, timedelta
from django.conf import settings



def all_bids(request):
    
         # display all current and expired bids
    bid = Bid.objects.all()
    endtime_list = []
        # the end of auction to allow user make payment
    for a in bid:
        endtime_list.append(str(a.auction_id.end_time))
    publishable_key = settings.STRIPE_PUBLISHABLE
    return render(request, "bid.html", {"bid": bid, 'key':publishable_key, 'end_time':endtime_list})



    
    


    
        
        
        
    

        
        
    
    
        
        
    