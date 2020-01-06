from django.conf.urls import url
from .views import home_view

urlpatterns = [
    url(r'(?P<product_id>\d+)', home_view, name="home"),
    
    
    ]