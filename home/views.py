from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages, auth
from django.contrib.auth.models import User
from .models import Page
from django.utils import timezone
from auctions.models import Auction
from products.models import Product

# Create your views here.

def home_view(request):
    home = Page.objects.all()
    return render(request, "home.html")
    
    
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
    
    
    
    
    


            
            
    