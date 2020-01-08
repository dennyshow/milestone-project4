from django.conf.urls import url
from home.views import home_view, bid_from_home

urlpatterns = [
    url(r'^$', home_view, name="home"),
    url(r'(?P<id>)', bid_from_home, name="bid_from_home" )
    ]