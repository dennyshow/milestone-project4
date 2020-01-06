from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime, timedelta
from .models import Auction
from django.contrib import messages
from products.models import Product
from bids.views import bid_page
from bids.models import Bid

# Create your views here.

def all_auctions(request):
    
    # Create views for all auctions.
    auctions = Auction.objects.filter(end_time__lte=timezone.now()).order_by('end_time')
    return render(request, "auction.html", {"auctions": auctions})


 
def auction_bid(request, product_id):
    
    #To allow bid a specified product in auctions
    
    auction = Auction.objects.filter(product_id=product_id)
    
    if request.user.is_authenticated:
        return redirect(reverse("auctions"))
        
        if request.method=="get":
            auction = auction(Bid)
            auction.auction_views += 1
            auction.save()
            return redirect(reverse('auction'), auction.product_id, {"auction": auction})
            
        else: 
            return render(request, 'auction.html', {"id":product_id})
    
    else:
        messages.error(request, "Please log in to proceed")
        return redirect(reverse('auctions'))
        
        
    

        
   