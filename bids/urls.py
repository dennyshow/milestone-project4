from django.conf.urls import url
from .views import all_bids, bid

urlpatterns = [
    url(r'^$', all_bids, name="bids"),
    url(r'^bids/bid/(<auction_id>d+)/', bid, name='bid'),
    
    ]