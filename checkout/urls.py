from django.conf.urls.defaults import *
from config import settings

urlpatterns = patterns('ecomstore.checkout.views',
  url(r'^$', 'show_checkout', {'template_name': 'checkout/checkout.html', 'SSL': settings.ENABLE_SSL}, name='checkout'),
  url(r'^receipt/$', 'receipt', {'template_name': 'checkout/receipt.html', 'SSL': settings.ENABLE_SSL}, name='checkout_receipt'),
)
