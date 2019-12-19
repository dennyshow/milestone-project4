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
from django.views.static import serve
from accounts import urls as urls_accounts
from home.views import home_view
from products.views import all_products
from auctions.views import auction

from bids.views import all_bids
from .settings import MEDIA_ROOT


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home_view, name="home"),
    url(r'^home/', include('home.urls')),
    url(r'^accounts/', include(urls_accounts)),
    url(r'^bids/', all_bids, name="bids"),
    url(r'^products/', all_products, name="products"),
    url(r'^auctions/', include('auctions.urls')),
    url(r'^auction/(?P<product_id>\d+)$', auction),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT})
    
]
