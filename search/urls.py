from django.conf.urls import url
from .views import do_search_on_home, do_search, do_search_on_auctions

urlpatterns = [
    # url(r'search/(?P<product_id>\d+)', do_search_on_home, name="search"),
    url(r'^$', do_search, name="search"),
    # url(r'artefact/<str:artefact>/', do_search_on_auctions, name="search_auction"),
    
    ]