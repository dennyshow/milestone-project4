from django.shortcuts import render
from products.models import Product
from auctions.models import Auction
from bids.models import Bid
from home.models import Page
from django.utils import timezone
from datetime import datetime
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib import messages

# Create your views here.

def do_search_on_home(request):
    home = Page.objects.filter(id=1)
    return render(request,  {"home": home})
    
    

def do_search(request):
    query = request.GET.get('q')
    if query is not None:
        lookups= Q(title__icontains=query) | Q(artefact__icontains=query)

        products = Product.objects.filter(lookups).distinct()
        if not products:
            messages.error(request, "No product available!")

    return render(request, "products.html", {"products": products})
    
    
    
def do_search_on_auctions(request, artefact):
    search_auction = []
    if artefact == "Historical":
        search_auction = Auction.objects.filter(product_id_artefact="HIS", name__icontains=request.GET['artefact'])
        
    elif artefact == "Cultural":
        search_auction = Auction.objects.filter(product_id_artefact="CUL", name__icontains=request.GET['artefact'])
        
    elif artefact == "Religious":
        search_auction = Auction.objects.filter(product_id_artefact="REL", name__icontains=request.GET['artefact'])
        
    elif artefact == "Media":
        search_auction = Auction.objects.filter(product_id_artefact="MED", name__icontains=request.GET['artefact'])
        
    return render(request, {"search_auction": search_auction})
    

    
    