from django.shortcuts import render
from .models import Bid

# Create your views here.

def all_bids(request):
    bids = Bid.objects.all()
    return render(request, "bids.html", {"bids": bids})