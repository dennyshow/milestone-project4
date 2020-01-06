from django.conf.urls import url
from .views import all_bids, bid_page

urlpatterns = [
    url(r'^(?P<pk>\d+)', all_bids, name="bids"),
    url(r'^bid/(?P<auction_id>\d+)', bid_page, name='bid'),
    
    ]