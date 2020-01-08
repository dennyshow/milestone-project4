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
    
    

def one_auction(request, id):
    # Allow user to auction a product
    
    try:
        
        if request.method == "GET":
            
                auction_bid = Bid.objects.filter(id=id)
                auction_bid = timezone.now()
                auction_bid.bid_views += 1
                auction_bid.save()
                
                new_bid = auction_bid
                new_bid.append(auction_bid)
                return redirect(reverse('bid'), auction_bid.id, {"auction_bid": auction_bid, "{new_bid": new_bid})
        
        else:
            new_bid.delete(auction_bid)
        return redirect(reverse('bid'))
    
    except ValueError:
        return redirect(reverse('home'))
        
                


 
# def auction_bid(request, product_id):
    
#     #To allow bid a specified product in auctions
    
#     auction = Auction.objects.filter(product_id=product_id)
    
#     if request.user.is_authenticated:
#         return redirect(reverse("auctions"))
        
#         if request.method=="get":
#             auction = auction(Bid)
#             auction.auction_views += 1
#             auction.save()
#             return redirect(reverse('auction'), auction.product_id, {"auction": auction})
            
#         else: 
#             return render(request, 'auction.html', {"id":product_id})
    
#     else:
#         messages.error(request, "Please log in to proceed")
#         return redirect(reverse('auctions'))
        
        
    

        
   