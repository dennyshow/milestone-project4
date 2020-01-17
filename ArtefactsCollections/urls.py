"""ArtefactsCollections URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import RedirectView
from django.views import static
from accounts import urls as urls_accounts
from home import urls as urls_home
from products import urls as urls_products
from auctions import urls as urls_auctions
from bids import urls as urls_bids
from search import urls as urls_search
from basket import urls as urls_basket



from home.views import home_view
from products.views import all_products

from bids.views import all_bids
from .settings import MEDIA_ROOT


urlpatterns = [
    
    url(r'^admin/', admin.site.urls),
    url(r'^$', home_view, name="home"),
    url(r'^home/', include('home.urls')),
    url(r'^accounts/', include(urls_accounts)),
    url(r'bid/', include('bids.urls')),
    url(r'basket/', include('basket.urls')),
    url(r'^products/', all_products, name="products"),
    url(r'^search/', include('search.urls')),
    url(r'^auctions/', include('auctions.urls')),
    url(r'^media/(?P<path>.*)$', static.serve, {'document_root': MEDIA_ROOT})
    
]
