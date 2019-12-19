from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.models import User
from .models import Page
from django.utils import timezone


# Create your views here.

def home_view(request):
    home = Page.objects.all()
    return render(request, "home.html", {"home": home})
    
    
# def bid_from_home(request, bid_id=None):
#     home_bid = get_object_or_404(Page, bid_id=bid_id) if bid_id else None
#     if request.user.is_authenticated:
        
#         return redirect(reverse('bid'))
#     if request.method == "GET":
#         form = BidForm(request.GET, request.FILES, instance=home_bid)
#         if form.is_valid():
#             home_bid = form.save()
#             return redirect(bid_page, home_bid.bid_id)
#     else:
#         form = BidForm(instance=home_bid)
#     return render(request, "bidform.html", {'form': form})
    
    
    


            
            
    