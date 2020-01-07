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
    
    
    

def bid_from_home(request, pk):
    # view that allows user to bid from home page if authenticated.
    
    try:
        
        if request.method == "POST":
            if request.user.is_authenticated:
                to_bid = get_object_or_404(Auction, pk=pk)
                to_bid = timezone.now()
                to_bid.bid_no += 1
                to_bid.save()
                return redirect(reverse('bids'), to_bid.pk, {"to_bid": to_bid})
            else:
                messages.error(request, "Please register or sign in to bid!")
            
        else:
            messages.error(request, "Please Log in")
    
        return redirect(reverse('home'))
        
    except ValueError:
        return redirect(reverse('auctions'))
        
    
   
        
    
    
            
    
    


            
            
    