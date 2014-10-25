from django.conf.urls import (
  patterns,
  include,
  url,
)

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
  url(r'^', include('catalog.urls')),
  url(r'^cart/', include('cart.urls')),
  url(r'^accounts/', include('accounts.urls')),
  url(r'^accounts/', include('django.contrib.auth.urls')),
  url(r'^admin/', include(admin.site.urls)),
)
