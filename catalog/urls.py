from django.conf.urls import (
  patterns,
  include,
  url,
)

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('catalog.views',
  url(r'^$', 'catalog_home', name='catalog_home'),
  url(r'^category/(?P<category_slug>[-\w]+)/$', 'show_category', name='catalog_category'),
  url(r'^product/(?P<product_slug>[-\w]+)/$', 'show_product', name='catalog_product'),
)

handler404 = 'catalog.views.file_not_found_404'
