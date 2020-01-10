from django.conf.urls import url
from .views import do_search_on_home, do_search, do_search_on_auctions

urlpatterns = [
    url(r'^$', do_search, name="search"),
    
    ]