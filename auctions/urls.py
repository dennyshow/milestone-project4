from django.conf.urls import url
from .views import all_auction

urlpatterns = [
    url('^auctions/', all_auction, name="auctions")
    ]