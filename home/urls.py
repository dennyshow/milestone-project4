from django.conf.urls import url
from .views import home_view, bid_from_home

urlpatterns = [
    url(r'^$', home_view, name="home"),
    url(r'^home_bid/(?P<auction_id>)', bid_from_home, name="bid_from_home")
    
    ]