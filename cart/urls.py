from django.conf.urls import (
  patterns,
  include,
  url,
)


urlpatterns = patterns('cart.views',
  url(r'^$', 'show_cart', name='show_cart'),
)
