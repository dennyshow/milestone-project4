from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages, auth
from django.contrib.auth.models import User
from .models import Page
from django.utils import timezone
from products.models import Product
from auctions.models import Auction
from bids.models import Bid
from django.db.models import Q

# Create your views here.

def home_view(request):
    home = Page.objects.filter()
    return render(request, "home.html", {"home": home})

    
def bid_from_home(request):
    # view that allows user to bid from home page if authenticated.
        if request.method == "POST":
            if request.user.is_authenticated:
                p_id = request.POST['product_id']
                auction = Auction.objects.get(product_id=p_id)
                if timezone.now() >= auction.start_time and timezone.now() < auction.end_time:
                   
                    product = Product.objects.get(id=p_id)
                    product.auction_price += int(request.POST['bid'])
                    product.save()
                    new_bid = Bid()
                    # auction = get_object_or_404(Auction, pk=pk)
                    new_bid.product_id = product
                    new_bid.auction_id = auction
                    new_bid.user_id = request.user
                    new_bid.bid_time = timezone.now()
                    new_bid.bid_views += 1
                    new_bid.save()
                    messages.error(request, "Bidding is done!")
                else:
                    messages.error(request, "Bidding is closed!")
                
   
            else:
                messages.error(request, "Please register or sign in to bid!")
            
        # else:
        #     return render(request, "home.html")
            
        return redirect(reverse('home'))
        
    
   
        
    
    
            
    
    


            
            
    