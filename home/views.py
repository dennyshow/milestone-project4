from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages, auth
from django.contrib.auth.models import User
from .models import Page
from django.utils import timezone
from products.models import Product
from auctions.models import Auction

# Create your views here.

def home_view(request):
    home = Page.objects.filter()
    return render(request, "home.html", {"home": home})
    
    

def bid_from_home(request, auction_id):
    if request.user.is_authenticated:
        return redirect(reverse('auctions'))
        
        if request.method == "POST":
            to_bid = get_object_or_404(Auction, pk=auction_id)
            to_bid = timezone.now()
            to_bid.bid_views += 1
            to_bid.save()
            return redirect(reverse('auctions'), to_bid.auction_id, {"to_bid": to_bid})
       
    else:
        messages.error(request, "Please register or sign in to bid!")
    
    return redirect(reverse('auctions'))
            
    
    
# def bid_from_home(request, product_id):
    
#     if request.user.is_authenticated:
#         return redirect(reverse('products'))
        
#         if request.method == "POST":
#             allow_bid = get_object_or_404(Auction, pk=product_id)
#             allow_bid = timezone.now()
#             allow_bid.save()
#             return redirect(reverse("products"), allow_bid.product_id, {"allow_bid": allow_bid})
#     else:
#         messages.error(request, "Please register or sign in to bid")
        
#     return redirect(reverse('home'))
    
    
    
    
    


            
            
    