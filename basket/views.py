from django.shortcuts import render, reverse, redirect
from django.utils import timezone
import stripe # new
from auctions.models import Auction
from bids.models import Bid

from django.contrib import messages


from django.conf import settings
from django.views.generic.base import TemplateView

        # Stripe payments configuration
        
stripe.api_key = settings.STRIPE_SECRET

            # Checkout Page
            
class view_basket(TemplateView):
    template_name = 'new_basket.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['key'] = settings.STRIPE_PUBLISHABLE
        return context
        
        
# To Charge Page
def charge(request): # new
    if request.method == 'POST':
        product_id = request.POST['bid_product']
        print(product_id)
        auction = Auction.objects.get(product_id=product_id)
        bid = Bid.objects.get(product_id=product_id)
        if timezone.now() >= auction.end_time:
            print(request.user.id, bid.user_id.id)
            if request.user.id == bid.user_id.id:
                if 'bid_price' in request.POST:
                    bid_price = request.POST['bid_price']
                else:
                    bid_price = 500
                charge = stripe.Charge.create(
                    amount=500,
                    currency='usd',
                    description='A Django charge',
                    source=request.POST['stripeToken']
                )
                return render(request, 'charge.html', {'price':bid_price})
            else:
                messages.error(request, "Only winner can purchase!")
        else:
            messages.error(request, "Bidding is going on!")
    return redirect(reverse('bid'))
    
    