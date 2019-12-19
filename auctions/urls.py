from django.conf.urls import url
from .views import all_auctions, auction

urlpatterns = [
    url(r'^$', all_auctions, name="auctions"),
    url(r'^auction/(?P<product_id>\d+)$', auction, name='auction'),
  ]