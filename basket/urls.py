from django.conf.urls import url
from .views import view_basket, add_to_basket, update_basket, charge

urlpatterns = [
    
    url(r'^$', view_basket.as_view(), name='view_basket'),
    url(r'^add/(?P<id>\d+)', add_to_basket, name='add_to_basket'),
    url(r'^update/(?P<id>\d+)', update_basket, name='update_basket'),
    url(r'charge/', charge, name='charge'),
    
    ]