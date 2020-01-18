from django.contrib import messages
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.models import User
from .models import Bid
from auctions.models import Auction
from django.utils import timezone
from datetime import datetime, timedelta
from django.conf import settings



def all_bids(request):
         # display all ongoing and expired bids
         # Let bid available to only registered user/bidder
         # Else returns the unathorized user back to home
    if request.user.is_authenticated:
        bid = Bid.objects.all()
        endtime_list = []
        # the end of auction to allow user make payment
        for a in bid:
            endtime_list.append(str(a.auction_id.end_time))
        publishable_key = settings.STRIPE_PUBLISHABLE
        return render(request, "bid.html", {"bid": bid, 'key':publishable_key, 'end_time':endtime_list})
    else:
        messages.error(request, "You must be a registered user to view a bid!")
        return redirect(reverse('home'))
    return render(request, "home.html")



    
    


    
        
        
        
    

        
        
    
    
        
        
    