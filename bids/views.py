from django.contrib import messages
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.models import User
from .models import Bid
from auctions.models import Auction
from django.utils import timezone
from datetime import datetime, timedelta
from auctions.auction import to_auction



# Create your views here.

def all_bids(request):
    print(all_bids)
    # display all current and expired bids
    bids = Bid.objects.all()
    return render(request, "bids.html", {"bids": bids})

    

def bid(request, auction_id):
    # return a bid page when auctionn is won
   
    
    let_bid = Auction.objects.filter(auction_id=auction_id)
    if let_bid[0].start_time > timezone.now():
        return redirect(reverse('bid'), let_bid.auction_id, {"let_bid": let_bid[0] })
    
    
    collect_bid = []
    
    
    time_left, expired = remaining_time(let_bid[0])
    collect_bid.append(time_left) #First collect of auction
    
    current_price = 10.00 + (let_bid[0].bid_no * 10)
    current_price = "%0.10f" % current_price
    collect_bid.append(current_price)
    
    if expired < 0:
        collect_bid.append(False)
    else:
        collect_bid.append(True)
        
    last_bid = Bid.objects.all().order_by('-bid_time')
    
    if last_bid:
        win = User.objects.filter(id=last_bid[0].user.id.id)
        collect_bid.append(win)
    else:
        collect_bid.append(None)
    
    return render(request, "bid.html", {"collect_bid": collect_bid})
    
    

    
    


    
        
        
        
    

        
        
    
    
        
        
    