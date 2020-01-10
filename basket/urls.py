from django.conf.urls import url
from .views import view_basket, charge

urlpatterns = [
    
    url(r'^$', view_basket.as_view(), name='view_basket'),
    url(r'charge/', charge, name='charge'),
    
    ]