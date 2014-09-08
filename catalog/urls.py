from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

from config import settings

from django.conf.urls import (
  patterns,
  include,
  url,
)

from django.contrib import admin
admin.autodiscover()

# Main patterns
urlpatterns = patterns('catalog.views',
  url(r'^$', 'catalog_home', name='catalog_home'),
  url(r'^category/(?P<category_slug>[-\w]+)/$', 'show_category', name='catalog_category'),
  url(r'^product/(?P<product_slug>[-\w]+)/$', 'show_product', name='catalog_product'),
)

# Handling media files like images
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Error handlers
handler404 = 'catalog.views.file_not_found_404'
