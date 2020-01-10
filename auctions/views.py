from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime, timedelta
from .models import Auction
from products.models import Product
from bids.models import Bid

# Create your views here.

def all_auctions(request):
    # Create views for all auctions.
    auctions = Auction.objects.filter()
    return render(request, "auction.html", {"auctions": auctions})
    
    

def one_auction(request):
    # Allow user to auction a product
    if request.method == "POST":
        if request.user.is_authenticated:
            p_id = request.POST['product_id']
            auction = Auction.objects.get(product_id=p_id)
            if timezone.now() >= auction.start_time and timezone.now() < auction.end_time:
               
                product = Product.objects.get(id=p_id)
                product.auction_price += int(request.POST['Raise'])
                product.save()
                new_bid = Bid()
                
                new_bid.product_id = product
                new_bid.auction_id = auction
                new_bid.user_id = request.user
                new_bid.bid_time = timezone.now()
                new_bid.bid_views += 1
                new_bid.save()
                messages.error(request, "Bidding is Updated!")
            else:
                messages.error(request, "Bidding is closed!")
   
        else:
            messages.error(request, "Please register or sign in to bid!")
            
    return redirect(reverse('auctions'))
        
        
    

        
   