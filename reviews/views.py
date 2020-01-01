from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from auctions.models import Auction
from bids.models import Bid

# Create your views here.

def review(request, auction_id):
    # allows user to leave review on an auction
    
    user = User.objects.filter(request.session['user'])
    auction = Auction.objects.filter(auction_id=auction_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            message = Text()
            message.user.id = user[0]
            message.auction_id = auction[0]
            message.messenger = form.cleaned_data['review']
            message.time_posted = timezone.now()
            message.save()
            return redirect(reverse('bid_page'), {"auction_id": auction_id})
        else:
            return render(request, "home.html")
    return render(request, "home.html")
    