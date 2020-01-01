from django.conf.urls import url
from .views import do_search_on_home, do_search_on_products, do_search_on_auctions

urlpatterns = [
    url(r'search/(?P<product_id>\d+)', do_search_on_home, name="search"),
    url(r'search/', do_search_on_products, name="search"),
    url(r'artefact/<str:artefact>/', do_search_on_auctions, name="search_auction"),
    
    ]