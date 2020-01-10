from django.conf.urls import url
from .views import all_auctions, one_auction

urlpatterns = [
    url(r'^$', all_auctions, name="auctions"),
    url(r'one_auction', one_auction, name="one_auction")
  ]