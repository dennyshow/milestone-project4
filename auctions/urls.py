from django.conf.urls import url
from .views import all_auctions, auction_bid

urlpatterns = [
    url(r'^$', all_auctions, name="auctions"),
    url(r'^(?P<product_id>\d+)/', auction_bid, name='auction'),
  ]