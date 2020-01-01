from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime, timedelta
from .models import Auction
from auctions.auction import to_auction



def all_auctions(request):
    
    # Create views for all auctions.
    auctions = Auction.objects.filter(end_time__lte=timezone.now()).order_by('end_time')
    return render(request, "auction.html", {"auctions": auctions})


 
def auction_bid(request, product_id):
    
    #To allow bid a specified product in auctions
    
    auction = Auction.objects.filter(product_id=product_id)
    
    if request.user.is_authenticated:
        return redirect(reverse("auctions"))
        
        if request.method=="GET":
            new_auction = to_auction(Product)
            new_auction = timezone.now()
            new_auction = auction_views =+ 1
            new_auction.save()
            
            print(new_auction)
            
       
            return redirect(reverse('new_auction'), new_auction.product_id, {"new_auction": auction})
            
        else: 
            return render(request, 'auction.html', {"id":product_id})
    
    else:
        messages.error(request, "Please Sign In To BID!")
        return redirect(reverse('auctions'))
        
        
    

        
   