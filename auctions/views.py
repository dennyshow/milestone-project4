from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime, timedelta
from .models import Auction
from .forms import AuctionForm
from products.models import Product
from bids.models import Bid

# Create your views here.

def all_auctions(request):
    # Create views for all auctions.
    auctions = Auction.objects.filter(end_time__lte=timezone.now()).order_by('end_time')
    return render(request, "auction.html", {"auctions": auctions})
    

def auction(request, product_id):
    #To allow bid during auctions
    
    auction_bid = Auction.objects.filter(Auction, pk=product_id) if product_id else None
    if request.method=="GET":
        auction_bid.views += 1
        auction_bid.save()
        return redirect(reverse('bid'), auction_bid.product_id)
    else: 
        return render(request, 'auction.html', )
        

def remain_time(auction):
    time_left = auction.end_time - timezone.now()
    days, seconds = time_left.days, time_left.seconds
    hours = days * 24 + seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    time_left = str(minutes) + "m " + str(seconds) + "s"
    expired = days
    
    return time_left, expired
    

        
   