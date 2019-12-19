from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.models import User
from .models import Bid
from auctions.models import Auction
from django.utils import timezone


# Create your views here.

def all_bids(request):
    bids = Bid.objects.all()
    return render(request, "bids.html", {"bids": bids})
    
    
def bidding_page(request, auction_id):
    if request.user.is_authenticated:
        auction = Auction.objects.filter(id=auction_id)
        if auction[0].start_time > timezone.now():
            return all_bids(request)
        user = User.objects.filter(username=request.session['user'])
        bid = []
        time_left, expired = remaining_time(auction[0])
        bid.append(time_left)
    
    

# def bid_page(request, product_id):
#     bid = Product.objects.filter()
#     new_bid = get_object_or_404(Bid, pk=product_id)
#     if request.user.is_authenticated:
#         return render(request, "bid.html")
        
            
#     else:
#         messages.error(request, "Please sign in to bid product")
        
        
        
    

        
        
    
    
        
        
    