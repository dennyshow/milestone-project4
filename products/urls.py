from django.conf.urls import url
from .views import all_products

urlpatterns = [
    url('^products/', all_products, name="products")
    
    ]