from django.shortcuts import render
from .models import Auction

# Create your views here.

def all_auction(request):
    auctions = Auction.objects.all()
    return render(request, "auction.html", {"auctions": auctions})