from django.conf.urls import url
from .views import all_bids

urlpatterns = [
    url(r'^bids/', all_bids, name="bids") 
    
    ]